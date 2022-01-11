# Neural Class Expression Synthesis (NCES)
Implementation of neural class expression synthesizers (NCES)

![ncel-dlo](ncel-dlo.png)

## Installation

Clone this repository:
```
https://github.com/ConceptLengthLearner/NCES.git
```
First install Anaconda3, Java 8+, Maven 3.6.3+, then all required librairies (for NCES) by running the following:
```
conda env create -f environment.yml
```
A conda environment (cl) will be created. Next activate the environment:
``` conda activate cl```

Dowload DL-Learner-1.4.0 from [github](https://github.com/SmartDataAnalytics/DL-Learner/releases) and extract it into the directory Method

Clone DL-Foil from [bitbucket](https://bitbucket.org/grizzo001/dl-foil.git) into Method

Download Datasets from [drive](https://drive.google.com/file/d/1rfCujY256RE8OMexLAbNpNOXc8BW2kPC/view?usp=sharing), extract it into NCES/Method and rename the folder as Datasets

## Reproducing the reported results

### NCES (Ours)


*Open a terminal and navigate into Method/reproduce_results/* ``` cd NCES/Method/reproduce_results/```
- Reproduce training NCES: ``` python reproduce_training_concept_synthesizers_[name_of_knowledge_base]_kb.py```

- Reproduce training NCES on all KBs: ``` sh reproduce_training_nces_on_all_kbs.sh```

- To reproduce evaluation results on concept learning, please open the jupyter notebook file ReproduceNCES.ipynb

*Remark: name_of_knowledge_base is one of carcinogenesis, mutagenesis, family-benchmark, semantic_bible, vicodi*

### DL-Learner

*Open a terminal and navigate into Method/dllearner/* ``` cd NCES/Method/dllearner/```
- Reproduce CELOE, OCEL, and ELTL concept learning results: ``` python reproduce_dllearner_experiment.py --algo --kb --max_runtime --num_probs```

### DL-Foil

*Open a terminal and navigate into Method/dl-foil/* ``` cd NCES/Method/dl-foil/```

- Run mvn package

- Copy `generate_dlfoil_config_all_kbs.py` into dl-foil and run `python generate_dlfoil_config_all_kbs.py` to prepare configuration files for all knowledge bases

- Reproduce concept learning results: ` mvn -e exec:java -Dexec.mainClass=it.uniba.di.lacam.ml.DLFoilTest -Dexec.args=DL-Foil2/kb_config.xml `

### ECII

*Open a terminal and navigate into Method/dl-foil/* ``` cd NCES/Method/ecii/```

- Run `python generate_config_ecii.py --kb "knowledge base name(s)" ` to prepare configuration files

- To start concept learning, run `java -Xms2g -Xmx8g -Xss1g -jar ecii_v1.0.0.jar -b kb/`

- Run `python parse_ecii_output.py --kb "knowledge base name(s)" ` to parse the output and save the results such as f_measure and runtime



## Acknowledgement 
We based our implementation on the open source implementation of [ontolearn](https://docs--ontolearn-docs-dice-group.netlify.app/). We would like to thank the Ontolearn team for the readable codebase.
