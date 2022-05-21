import os
import t5paths
from huggingface_hub import HfApi, Repository

api = HfApi()
paths = t5paths.t5paths()
model_local_dir = "/home/perk/models/"

#For debugging - working on the first one
#paths = paths[0:1]


for m in paths:
    #Create the repo if it does not exist
    try:
        repo_url = api.create_repo(
                "north/"+m['name'],
                private = m['private'],
                )
    except:
        print("Repo already exists")

    #Clone the repo
    repo = Repository(local_dir = model_local_dir+m['name'], clone_from = "north/"+m['name'])
    repo.git_pull()

    cmd = "huggingface-cli lfs-enable-largefiles "+model_local_dir+m['name']
    os.system(cmd)

    repo.push_to_hub(commit_message="Just verifying that everything works")

    
