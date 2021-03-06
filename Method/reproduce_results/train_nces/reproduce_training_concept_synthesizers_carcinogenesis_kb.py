import matplotlib.pyplot as plt
import torch, pandas as pd, numpy as np
import sys, os, json

base_path = os.path.dirname(os.path.realpath(__file__)).split('reproduce_results')[0]
sys.path.append(base_path)

from helper_classes.experiment import Experiment
from sklearn.model_selection import train_test_split
from util.data import Data
import json

data_path = base_path+"Datasets/carcinogenesis/Train_data/Data.json"
with open(data_path, "r") as file:
    data = json.load(file)
data = list(data.items())
path_to_triples = base_path+"Datasets/carcinogenesis/Triples/"
triples = Data({"path_to_triples":path_to_triples})

max_num_atom_repeat = 10
kwargs = {"learner_name":"GRU", "emb_model_name":"", 'knowledge_graph_path': base_path+"Datasets/carcinogenesis/carcinogenesis.owl",
          "pretrained_embedding_path":base_path+"Datasets/carcinogenesis/Model_weights/ConEx_GRU.pt",
          "pretrained_concept_synthesizer":base_path+"Datasets/carcinogenesis/Model_weights/GRU.pt", 
          "path_to_csv_embeddings":base_path+"Embeddings/carcinogenesis/ConEx_entity_embeddings.csv",
          "learning_rate":0.001, "decay_rate":0, 'grad_clip_value':5., "path_to_triples":path_to_triples, 'max_num_atom_repeat': max_num_atom_repeat,
          'index_score_upper_bound':10., 'index_score_lower_bound_rate': 0.8, 'max_num_tokens':30,
          "random_seed":1, "embedding_dim":20, "num_entities":len(triples.entities),
          "num_relations":len(triples.relations), "num_examples":1000, "input_dropout":0.0, 'drop_prob':0.1,
          "kernel_size":4, "num_of_output_channels":8, "feature_map_dropout":0.1,
          "hidden_dropout":0.1, "rnn_n_layers":2, 'input_size':40,
          'rnn_n_hidden':100,'seed':10, 'kernel_w':5, 'kernel_h':11, 'stride_w':1, 'stride_h':7, 'conv_out':960}

Models = ["GRU", "LSTM", "CNN"]

experiment = Experiment(kwargs)

data_train, data_test = train_test_split(data, test_size=0.2, random_state=123)

final = False
test = True
cross_validate = False
record_runtime = True
save_model = True
if final:
    data_train = data
    test = False
    cross_validate = False
experiment.train_all_nets(Models, data_train, data_test, epochs=1000, cs_batch_size=512, tc_batch_size=1024, kf_n_splits=10, cross_validate=cross_validate, test=test, save_model = save_model, include_embedding_loss=True, optimizer = 'Adam', tc_label_smoothing=0.9, record_runtime=record_runtime, final=final)
