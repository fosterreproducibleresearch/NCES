# NCES
Implementation of neural class expression synthesizers (NCES)


## Installation

Clone this repository:
```
https://github.com/ConceptLengthLearner/NCES.git
```
First install Anaconda3, then all required librairies by running the following:
```
conda env create -f environment.yml
```
A conda environment (cel) will be created. Next activate the environment:
``` conda activate cel```

Dowload DL-Learner-1.4.0 from [github](https://github.com/SmartDataAnalytics/DL-Learner/releases) and extract it into the directory containing NCES (cloned above), not inside NCES!

Download Datasets from [drive](https://drive.google.com/file/d/1rfCujY256RE8OMexLAbNpNOXc8BW2kPC/view?usp=sharing), extract it into NCES/Method and rename the folder as Datasets

## Reproducing the reported results

### NCES (Ours)

*Open a terminal and navigate into Method/reproduce_results/* ``` cd NCES/Method/reproduce_results/```
- Reproduce training NCES: ``` python reproduce_training_concept_synthesizers_[name_of_knowledge_graph].py```

- Reproduce training NCES on all KGs: ``` sh reproduce_training_nces_on_all_kgs.sh```

- To reproduce evaluation results, please open the jupyter notebook/lab file ReproduceNCES.ipynb

### DL-Learner

*Open a terminal and navigate into Method/dllearner/* ``` cd NCES/Method/dllearner/```
- Reproduce CELOE, OCEL, and ELTL concept learning results: ``` python reproduce_dllearner_experiment_[name_of_knowledge_graph].py```

- Reproduce CELOE, OCEL, and ELTL results for all KGs: ``` sh reproduce_dllearner_experiment_all_kgs.sh```

*Remark* ```name_of_knowledge_graph``` is one of ```carcinogenesis_kg, semantic_bible_kg, mutagenesis_kg or family_benchmark_kg```

## Acknowledgement 
We based our implementation on the open source implementation of [ontolearn](https://docs--ontolearn-docs-dice-group.netlify.app/). We would like to thank the Ontolearn team for the readable codebase.