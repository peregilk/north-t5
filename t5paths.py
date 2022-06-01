import sys

def t5paths(size="all"):
    sizes = ["small", "base", "large", "xl", "xxl"] 
    if size not in sizes and size != "all":
        print("Not a valid model size. Valid sizes are:"+sizes)
        sys.exit()

    paths = []
    for s in sizes:
        if s==size or size=="all":
            #if size == "base":
            #    private = False
            #else:
            private = True

            n = "byt5_"+s+"_NCC"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_byt5x_"+s+"/"
            c = p+"checkpoint_1500000"
            if s!="xl" and s!="xxl":
                paths.append({"name":n,"path":p,"checkpoint":c,"private":private,"size":s})
            
            n = "t5_"+s+"_scand"
            p = "gs://north-t5x/pretrained_models/"+s+"/scandinavian_t5x_"+s+"/"
            c = p+"checkpoint_1700000"
            if s!="xl" and s!="xxl":
                paths.append({"name":n,"path":p,"checkpoint":c,"private":private,"size":s})
            
            n = "t5_"+s+"_NCC_lm"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_pluss100k_lm_t5x_"+s+"/"
            c = p+"checkpoint_1600000"
            paths.append({"name":n,"path":p,"checkpoint":c,"private":False,"size":s})
            
            n = "t5_"+s+"_NCC_modern_lm"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_pluss200k_balanced_bokmaal_nynorsk_pluss100k_lm_t5x_"+s+"/"
            c = p+"checkpoint_1800000"
            if s!="xxl":
                paths.append({"name":n,"path":p,"checkpoint":c,"private":private,"size":s})
            
            n = "t5_"+s+"_NCC_modern"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_pluss200k_balanced_bokmaal_nynorsk_t5x_"+s+"/"
            c = p+"checkpoint_1700000"
            if s!="xxl":
                paths.append({"name":n,"path":p,"checkpoint":c,"private":private,"size":s})
            
            n = "t5_"+s+"_NCC_scand"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_pluss200k_scandinavian_t5x_"+s+"/"
            c = p+"checkpoint_1700000"
            if s!="xxl":
                paths.append({"name":n,"path":p,"checkpoint":c,"private":private,"size":s})
            
            n = "t5_"+s+"_NCC"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_t5x_"+s+"/"
            c = p+"checkpoint_1500000"
            paths.append({"name":n,"path":p,"checkpoint":c,"private":False,"size":s})

    return paths

def create_index_table(target):
    mdict = dict()
    model = dict()
    
    for m in t5paths():
        mdict[m['name']] ={"size":m['size'], 'path': m['path'], 'private': m['private']}

    show_private = mdict[target]['private']

    sizes=['small','base','large','xl','xxl']
    types=['t5_##_NCC','t5_##_NCC_lm','t5_##_NCC_modern','t5_##_NCC_modern_lm','t5_##_NCC_scand','t5_##_scand','byt5_##_NCC']
    table="| |**Small** <br />_60M_|**Base** <br />_220M_|**Large** <br />_770M_|**XL** <br />_3B_|**XXL** <br />_11B_|\n|:-----------|:------------:|:------------:|:------------:|:------------:|:------------:|\n"

    for t in types:
        row = "|"
        for s in sizes:
            model = mdict.get(t.replace('##',s))
            if model:
                if model['private'] == False or show_private == True:

                    if t.replace('##',s) == target:
                        row += "✔|"
                    else:
                        row+='[🤗](https://huggingface.co/north/'+t.replace('##',s)+')|'
            else:
                row+" ❌|"

        if row.replace("|","").replace("-","") != "":
            table+="|"+t.replace("_##","").replace("byt5","North-byT5").replace("t5","North-T5").replace("_","&#8209;")+row+"|\n"
   
    bucket = "\n## T5X Checkpoint\nThe original T5X checkpoint is also available for this model in the [Google Cloud Bucket]("+mdict[target]['path']+").\n"

    return table + bucket


