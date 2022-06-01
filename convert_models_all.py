import os
import t5paths
import shutil
from convert_t5x_checkpoint_to_flax import convert_t5x_checkpoint_to_flax as convert_t5x
from create_pytorch_tf_and_vocab import create_pytorch_tf_and_vocab as create_transformers
from copy_additional_files_from_bucket import copy_additional_files_from_bucket as copy_adf
from huggingface_hub import HfApi, Repository

api = HfApi()
temp_paths = t5paths.t5paths()
model_local_dir = "/home/perk/models/"
forceConvert=True
forceTFPT=True
forceFiles=True

#For debugging - working on the first one
#temp_paths = temp_paths[1:2]
#print(temp_paths)

paths = []
for m in temp_paths:
    #if "xxl" in m['name']:
    if "large_NCC_modern_lm" in m['name']:
        paths.append(m)
        print(m['name'])

for m in paths:
    repo = Repository(local_dir=model_local_dir+m['name'])
    repo.git_pull()
    
    if forceConvert or not os.path.exists(model_local_dir+m['name']+"/flax_model.msgpack"):
        print(f"***Starting to convert {m['name']}")
        if "byt5" not in m['name']:
            shutil.copyfile(m['size']+'.json',model_local_dir+m['name']+'/config.json')
            convert_t5x(m['checkpoint'],m['size']+'.json',model_local_dir+m['name'])
        else:
            shutil.copyfile("byt5_"+m['size']+'.json',model_local_dir+m['name']+'/config.json')
            convert_t5x(m['checkpoint'],"byt5_"+m['size']+'.json',model_local_dir+m['name'])
    else:
        print("***Dropping conversion")

    if forceFiles or not os.path.exists(model_local_dir+m['name']+"/config.gin"):
        print(f"***Starting to copy additional files to {m['name']} from the bucket")
        copy_adf(m['path'],model_local_dir+m['name'])
    else:
        print("***Dropping to copy files")

    if forceTFPT or not os.path.exists(model_local_dir+m['name']+"/pytorch_model.bin"):
        print(f"***Starting to convert {m['name']} to pyTorch and tensorflow")
        create_transformers(model_local_dir+m['name'],m['size'])
   
    else:
        print("***Dropping conversion to PyTorch and Tensorflow")

    print(f"***Starting to push  all the files for {m['name']} to the hub")
    repo.push_to_hub(commit_message="Commit from model create scripts")


print(f"Finished pushing {m['name']}.")
