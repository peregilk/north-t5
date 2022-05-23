import os
import t5paths
from convert_t5x_checkpoint_to_flax import convert_t5x_checkpoint_to_flax as convert_t5x
from create_pytorch_tf_and_vocab import create_pytorch_tf_and_vocab as create_transformers
from copy_additional_files_from_bucket import copy_additional_files_from_bucket as copy_adf
from huggingface_hub import HfApi, Repository

api = HfApi()
temp_paths = t5paths.t5paths()
model_local_dir = "/home/perk/models/"
forceConvert=False
forceTFPT=True
forceFiles=False

#For debugging - working on the first one
#temp_paths = temp_paths[1:2]
#print(temp_paths)

paths = []
for m in temp_paths:
    #if ("small" in m['name'] or "base" in m['name']) and "byt5" not in m['name']:
    if "_xl_" in m['name'] and "byt5" not in m['name'] and "modern_lm" not in m['name']:
        paths.append(m)
        print(m['name'])


for m in paths:
    repo = Repository(local_dir=model_local_dir+m['name'])
    repo.git_pull()
    if forceConvert or not os.path.exists(model_local_dir+m['name']+"/flax_model.msgpack"):
        print(f"***Starting to convert {m['name']}")
        convert_t5x(m['checkpoint'],m['size']+'.json',model_local_dir+m['name'])
    else:
        print("***Dropping conversion")


    if forceTFPT or not os.path.exists(model_local_dir+m['name']+"/pytorch_model.bin"):
        print(f"***Starting to convert to pyTorch and tensorflow")
        create_transformers(model_local_dir+m['name'],m['size'])
   
    else:
        print("***Dropping PyTorch and Tensorflow")


    if forceFiles or not os.path.exists(model_local_dir+m['name']+"/config.gin"):
        print("***Starting to copy additional files from the bucket")
        copy_adf(m['path'],model_local_dir+m['name'])
    else:
        print("***Dropping to copy files")

    print("***Starting to push  all the files to the hub")
    repo.push_to_hub(commit_message="Commit from model create scripts")


print("Finished")
