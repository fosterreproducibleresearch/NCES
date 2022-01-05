import json, time
import numpy as np
from collections import defaultdict
from tqdm import tqdm
import os, sys, random
from sklearn.model_selection import train_test_split

currentpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentpath.split("dllearner")[0])

from ontolearn.binders import DLLearnerBinder
from concept_length_metric import concept_length
from ontolearn import KnowledgeBase

lp_path = currentpath.split("dllearner")[0]+"Datasets/vicodi/Train_data/Data.json"
with open(lp_path,"r") as lp_file:
    data = json.load(lp_file)
data = list(data.items())
_, data_test = train_test_split(data, test_size=0.2, random_state=123)

random.seed(142)
data_test = random.sample(data_test, 200)

kg_path = currentpath.split("dllearner")[0]+'Datasets/vicodi/vicodi.owl'
# To download DL-learner,  https://github.com/SmartDataAnalytics/DL-Learner/releases.
dl_learner_binary_path = currentpath.split("dllearner")[0]+'dllearner-1.4.0/'
knowledge_base = KnowledgeBase(path=kg_path)
all_inds = set([ind.get_iri().as_str() for ind in knowledge_base.individuals()])
kb_namespace = list(knowledge_base.individuals())[0].get_iri().get_namespace()
kb_prefix = kb_namespace[:kb_namespace.rfind("/")+1]

for model in ['ocel', 'eltl', 'celoe']:
    algo = DLLearnerBinder(binary_path=dl_learner_binary_path, kb_path=kg_path, model=model)
    #{'F-measure': [], 'Prediction': [], 'Learned Concept': [], 'Runtime': []} 
    Result_dict = {'F-measure': [], 'Accuracy': [], 'Runtime': [], 'Prediction': [], 'Length': [], 'Learned Concept': []}
    Avg_result = defaultdict(lambda: defaultdict(float))
    print("#"*60)
    print(f"{model.upper()} on "+kg_path.split("/")[-2]+" knowledge graph")
    print("#"*60)
    for str_target_concept, examples in tqdm(data_test, desc=f'Learning {len(data_test)} problems'):
        print('TARGET CONCEPT:', str_target_concept)
        p = [kb_prefix+ind for ind in examples['positive examples']]
        n = list(all_inds-set(p))
        t0 = time.time()
        best_pred_algo = algo.fit(pos=p, neg=n, max_runtime=120).best_hypotheses() # Start learning
        t1 = time.time()
        duration = t1-t0
        print('Best prediction: ', best_pred_algo)
        print()
        if model == 'ocel': # No F-measure for OCEL
            Result_dict['F-measure'].append(-1.)
        else:
            Result_dict['F-measure'].append(best_pred_algo['F-measure']/100)
        Result_dict['Accuracy'].append(best_pred_algo['Accuracy']/100)
        if not 'Runtime' in best_pred_algo or best_pred_algo['Runtime'] is None:
            Result_dict['Runtime'].append(duration)
        else:
            Result_dict['Runtime'].append(best_pred_algo['Runtime'])
        if best_pred_algo['Prediction'] is None:
            Result_dict['Prediction'].append('None')
            Result_dict['Length'].append(10)
        else:
            Result_dict['Prediction'].append(best_pred_algo['Prediction'])
            Result_dict['Length'].append(concept_length(best_pred_algo['Prediction']))
        Result_dict['Learned Concept'].append(str_target_concept)

    for key in Result_dict:
        if key in ['Prediction', 'Learned Concept']: continue
        Avg_result[key]['mean'] = np.mean(Result_dict[key])
        Avg_result[key]['std'] = np.std(Result_dict[key])

    with open(currentpath.split("dllearner")[0]+'Datasets/vicodi/Results/concept_learning_results_'+model+'.json', 'w') as file_descriptor1:
                json.dump(Result_dict, file_descriptor1, ensure_ascii=False, indent=3)

    with open(currentpath.split("dllearner")[0]+'Datasets/vicodi/Results/concept_learning_avg_results__'+model+'.json', 'w') as file_descriptor2:
                json.dump(Avg_result, file_descriptor2, indent=3)

    print("Avg results: ", Avg_result)
    print()