import os
import t5paths
from huggingface_hub import HfApi, Repository
from pathlib import Path


api = HfApi()
paths = t5paths.t5paths()
model_local_dir = "/home/perk/models/"


#Debug
#paths = paths[1:2]



for m in paths:
    local_dir = model_local_dir+m['name']
    repo = Repository(local_dir=local_dir)
    repo.git_pull()

    #Read the README template
    txt = Path('templates/README.md').read_text()
    priv_desc = Path('templates/PRIV-DESC.md').read_text()
    
    #Modify the README
    txt = txt.replace("##MODELS##",t5paths.create_index_table(m['name']))
    if m['private'] == True:
        txt = txt.replace("##PRIV-DESC##",priv_desc)
    else:
        txt = txt.replace("##PRIV-DESC##","")
    
    #Save the REAME
    with open(local_dir+"/README.md", 'w+') as f: 
        f.write(txt)
    

    #Push the changes
    print(f"***Pushing the README in {local_dir} to the hub")
    repo.push_to_hub(commit_message="Updated README")

