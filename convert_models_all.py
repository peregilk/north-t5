import os
import t5paths
from convert_t5x_checkpoint_to_flax import convert_t5x_checkpoint_to_flax as convert_t5x
from create_pytorch_tf_and_vocab import create_pytorch_tf_and_vocab as create_transformers
from copy_additional_files_from_bucket import copy_additional_files_from_bucket as copy_adf
from huggingface_hub import HfApi, Repository

api = HfApi()
paths = t5paths.t5paths()
model_local_dir = "/home/perk/models/"

#For debugging - working on the first one
paths = paths[1:2]

for m in paths:
    repo = Repository(local_dir=model_local_dir+m['name'])
    repo.git_pull()
	# print(f"***Starting to convert {m['name']}")
	# convert_t5x(m['checkpoint'],m['size']+'.json',model_local_dir+m['name'])
	# print(f"***Starting to convert to pyTorch")
	#create_transformers(model_local_dir+m['name'],m['size'])
    copy_adf(m['path'],model_local_dir+m['name'])
    print("***Copied additional files from the bucket")
    repo.push_to_hub(commit_message="Commit from model create scripts")
    print("***Successfully pushed all files to the hub")

