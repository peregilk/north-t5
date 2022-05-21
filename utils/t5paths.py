import sys

def t5paths(size="all"):
    sizes = ["small", "base", "large", "xl", "xxl"] 
    if size not in sizes and size != "all":
        print("Not a valid model size. Valid sizes are:"+sizes)
        sys.exit()

    paths = []
    for s in sizes:
        if s==size or size=="all":
            n = "mt5_"+s+"_NCC"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_byt5x_"+s+"/"
            c = p+"checkpoint_15000000"
            if s!="xl" and s!="xxl":
                paths.append([n,p,c])
            
            n = "t5_"+s+"_scand"
            p = "gs://north-t5x/pretrained_models/"+s+"/scandinavian_t5x_"+s+"/"
            c = p+"checkpoint_15000000"
            if s!="xl" and s!="xxl":
                paths.append([n,p,c])
            
            n = "t5_"+s+"_NCC_lm"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_pluss100k_lm_t5x_"+s+"/"
            c = p+"checkpoint_16000000"
            paths.append([n,p,c])
            
            n = "t5_"+s+"_NCC_modern_lm"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_pluss200k_balanced_bokmaal_nynorsk_pluss100k_lm_t5x_"+s+"/"
            c = p+"checkpoint_18000000"
            if s!="xxl":
                paths.append([n,p,c])
            
            n = "t5_"+s+"_NCC_modern"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_pluss200k_balanced_bokmaal_nynorsk_t5x_"+s+"/"
            c = p+"checkpoint_16000000"
            if s!="xxl":
                paths.append([n,p,c])
            
            n = "t5_"+s+"_NCC_scand"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_pluss200k_scandinavian_t5x_"+s+"/"
            c = p+"checkpoint_17000000"
            if s!="xxl":
                paths.append([n,p,c])

            n = "t5_"+s+"_NCC"
            p = "gs://north-t5x/pretrained_models/"+s+"/norwegian_NCC_plus_English_t5x_"+s+"/"
            c = p+"checkpoint_15000000"
            paths.append([n,p,c])

    return paths


