#!/bin/bash

set -ex

## Rohit pseudolabels here

python make_pseudolabels_ensemble.py --ensemble_id ensemble_4419


for model_id in model52
do
  python train.py --config_name "${model_id}_pretraining_training_config.yaml" --run_id "${model_id}_pretrain" --debug True --use_wand False --fold 0
  python train.py --config_name "${model_id}_pretraining_training_config.yaml" --run_id "${model_id}_pretrain" --debug True --use_wand False --fold 1
  python train.py --config_name "${model_id}_pretraining_training_config.yaml" --run_id "${model_id}_pretrain" --debug True --use_wand False --fold 2
  python train.py --config_name "${model_id}_pretraining_training_config.yaml" --run_id "${model_id}_pretrain" --debug True --use_wand False --fold 3
  python train.py --config_name "${model_id}_pretraining_training_config.yaml" --run_id "${model_id}_pretrain" --debug True --use_wand False --fold 4

  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 0 
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 1 
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 2 
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 3 
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 4 
  
  python inference.py --model_dir_path "../models/${model_id}" --mode oofs --debug True
  python inference.py --model_dir_path "../models/${model_id}" --mode prev_pseudolabels --debug True
done


for model_id in model67 model68 model69 model70 model71 model75 model81 model84
do
  
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 0
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 1
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 2
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 3
  python train.py --config_name "${model_id}_training_config.yaml" --run_id $model_id --debug True --use_wand False --fold 4
  
  python inference.py --model_dir_path "../models/${model_id}" --mode oofs --debug True
  python inference.py --model_dir_path "../models/${model_id}" --mode prev_pseudolabels --debug True
done
