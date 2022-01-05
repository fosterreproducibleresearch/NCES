from typing import Final

class F1():
    __slots__ = ()

    name: Final = 'F1'

    def score(self, pos_instances:set = {}, instances:set = {}):
        if len(instances) == 0:
            0.

        tp = len(pos_instances.intersection(instances))
        # tn = len(self.lp.kb_neg.difference(instances))

        fp = len(instances.difference(pos_instances))
        fn = len(pos_instances.difference(instances))

        try:
            recall = float(tp) / (tp + fn)
        except ZeroDivisionError:
            return 0.

        try:
            precision = float(tp) / (tp + fp)
        except ZeroDivisionError:
            return 0.

        if precision == 0. or recall == 0.:
            return 0.

        f_1 = 2 * ((precision * recall) / (precision + recall))
        return round(f_1, 5)