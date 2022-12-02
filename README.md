# Feedback Prize - English Language Learning - 1st Place Solution (Yevhenii Part)

It's 1st place solution to Kaggle competition: https://www.kaggle.com/competitions/feedback-prize-english-language-learning

This repo contains the code I used to train the models, while the solution writeup is available here: https://www.kaggle.com/competitions/feedback-prize-english-language-learning/discussion/369457

### HARDWARE: (The following specs were used to create the original solution)

Almost all models were trained using Paperspace Free A6000 Machine.

* OS: Ubuntu 20.04.4 LTS
* CPU: Intel Xeon Gold 5315Y @3.2 GHz, 8 cores
* RAM: 44Gi 
* GPU: 1 x NVIDIA RTX A6000 (49140MiB)


### SOFTWARE (python packages are detailed separately in `requirements.txt`):

* Python 3.9.13
* CUDA 11.6
* nvidia drivers v510.73.05

### Training

During training phase I iteratively re-labeled previous competition data. Also, I trained most of the models in two steps:
* Pretraining on pseudo labels, `./config/model21_pretraining_training_config.yaml` is an example of config for this step. 
* Fine-tuning from checkpoint from previous step on this competition true labels. `model21_training_config.yaml` is an example of config for this step.


To train:
* Download additional training data from https://www.kaggle.com/datasets/evgeniimaslov2/feedback3-additional-data and training data from https://www.kaggle.com/competitions/feedback-prize-english-language-learning, and extract it to `./data` directory. Pseudolabels and oofs also can be generated by running scripts below
* To train models: 
  * train_first_step.sh - this will train models from model2 to model50, make their OOFs, generate pseudo labels for previous competition data, and make an ensemble of pseudo labels (model-wise weighted sum)
  * rohit_pseudo.sh - download or train Rohit's solution models, run this script to make pseudo labels (or just use pseudo labels from the data link above)
  * train_second_step.sh - this script will make a column-wise ensemble of model2-model50 and Rohit's models and train the remaining models

Note: train_first_step.sh and train_second_step.sh scripts will rewrite existing oofs and pseudo labels files, and rename existing models

You also can train a model by running `python train.py` with arguments:
* `config_name` - name of config from `CONFIGS_DIR_PATH` directory specified in SETTING.json
* `run_id` - model_id, should be the same across folds. For example, I used modelN_pretrain for pretraining step and modelN for finetuning step
* `debug` - if True, script will select only 50 samples for training and validation dataframes
* `use_wandb` - if True, script will log metrics to Weights and Biases
* `fold` - fold to train

To find models weights in the ensemble I used `./notebooks/find_ensemble_weights.ipynb` notebook.
* All weight used is stored in `ensemble_weights` dictionary in `./src/make_pseudolabels_ensemble.py`
* `./src/make_pseudolabels_ensemble.py` will load pseudolabels from `PREVIOUS_DATA_PSEUDOLABELS_DIR_PATH` directory (or `CURRENT_DATA_PSEUDOLABELS_DIR_PATH` in case if `ensemble_id` = `current_train_ensemble_4434`) and save ensembled pseudolabels in the same directory, in `ensemble_id` subfolder


### Inference

Final inference kernel is available here: https://www.kaggle.com/code/rohitsingh9990/merged-submission-01?scriptVersionId=111953356

You also can run `python inference.py` with arguments:
* `model_dir_path` - path to model directory, `../models/model2` for example
* `mode`:
  * `oofs` - script will load dataframe from `TRAIN_CSV_PATH` (specified in SETTINGS.json) and save oof to `OOFS_DIR_PATH` 
  * `prev_pseudolabels` - script will load dataframe `PREVIOUS_DATA_PSEUDOLABELS_DIR_PATH` and save pseudolabels for previous competition data to `f'{PREVIOUS_DATA_PSEUDOLABELS_DIR_PATH}/{model_id}_pseudolabels'` dir
  * `curr_pseudolabels` - script will load dataframe `CURRENT_DATA_PSEUDOLABELS_DIR_PATH` and make pseudolabels for this competition data to `f'{CURRENT_DATA_PSEUDOLABELS_DIR_PATH}/{model_id}_pseudolabels'` dir
  * `submission` - script will load dataframe `TEST_CSV_PATH` and make save submission to `SUBMISSIONS_DIR_PATH`
* `debug` - if True, script will select only 50 samples for training and validation dataframes

To get pseudo labels from Rohit's models I used `python make_rohit_pseudolabels.py` specifiying model_id in arguments.