import os
import t5paths
from huggingface_hub import HfApi, Repository
from pathlib import Path


api = HfApi()
paths = t5paths.t5paths()
model_local_dir = "/home/perk/models/"
mdict = dict()
model = dict()

def create_index_table(target):
    for m in paths:
        mdict[m['name']] ={"size":m['size'], 'path': m['path'], 'private': m['private']}

    
    show_private = mdict[target]['private']

    sizes=['small','base','large','xl','xxl']
    types=['t5_##_NCC','t5_##_NCC_lm','t5_##_NCC_modern','t5_##_NCC_modern_lm','t5_##_NCC_scand','t5_##_scand','byt5_##_NCC']
    table="| |**Small**|**Base**|**Large**|**XL**|**XXL**|\n|:-----------|:------------|:------------|:------------|:------------|:------------|\n"

    for t in types:
        row = "|"
        for s in sizes:
            model = mdict.get(t.replace('##',s))
            if model:
                if model['private'] == False or show_private == True:
                    if mdict.get(t.replace('##',s)) == target:
                        row += "this|"
                    else:
                        row+='[🤗](https://huggingface.co/north/'+t+')|'
            else:
                row+="-"

        if row.replace("|","").replace("-","") != "":
            table+="|"+t.replace("_##","")+row+"|\n"
   
    bucket = "\n### T5X Checkpoint\nThe original T5X checkpoint is also available for this model in the [Google Cloud Bucket]{"+mdict[target]['path']+")\n"

    return table + bucket

print(create_index_table("t5_small_NCC"))

