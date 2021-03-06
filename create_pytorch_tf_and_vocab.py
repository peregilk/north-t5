from transformers import FlaxT5ForConditionalGeneration,TFT5ForConditionalGeneration, T5ForConditionalGeneration, T5Config, AutoTokenizer
import shutil
import argparse
import os

def create_pytorch_tf_and_vocab(flax_dump_folder_path, model_size):
    shutil.copyfile('spiece.model',flax_dump_folder_path+'/spiece.model')
    shutil.copyfile('special_tokens_map.json',flax_dump_folder_path+'/special_tokens_map.json')
    shutil.copyfile('tokenizer_config.json',flax_dump_folder_path+'/tokenizer_config.json')
    shutil.copyfile('.gitattributes',flax_dump_folder_path+'/.gitattributes')

    print("Copied tokenizer files and a gitattributes file")
    config= T5Config.from_pretrained(flax_dump_folder_path+'/config.json')
   
    #For the huge models, we will also open and save the Flax file
    #if model_size == "xl" or model_size=="xxl":
    #    model = FlaxT5ForConditionalGeneration.from_pretrained(flax_dump_folder_path,config=config)
    #    model.save_pretrained(flax_dump_folder_path)
        

    print(f"Starting pyTorch conversion from Flax with the parameters: flax_dump_folder_path={flax_dump_folder_path}, config={config}")

    model = T5ForConditionalGeneration.from_pretrained(flax_dump_folder_path,config=config,from_flax=True)
    model.save_pretrained(flax_dump_folder_path)
    print("Saved PyTorch-model")
    
    #Remove this wile because it is too big
    if model_size=="xxl":
        os.remove(flax_dump_folder_path+"/flax_model.msgpack")

    # Disable the conversion to Tensorflow
    #print(f"Starting TensorFlow conversion from PyTorch with the parameters: flax_dump_folder_path={flax_dump_folder_path}, config={config}")
    #model = TFT5ForConditionalGeneration.from_pretrained(flax_dump_folder_path,config=config, from_pt=True)
    #model.save_pretrained(flax_dump_folder_path)
    #print("Saved Tensorflow-model")

    try:    
        tokenizer = AutoTokenizer.from_pretrained(flax_dump_folder_path)
        tokenizer.save_pretrained(flax_dump_folder_path)

        print("Saved tokenizer")
    except:
        print("No tokenizer generated. If this is a byT5 model, this is expected")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument(
        "--flax_dump_folder_path", default=None, type=str, required=True, help="Path to the output FLAX model."
    )
    parser.add_argument(
        "--model_size", default="base", type=str, required=True, help="Model size. Used for finding the correct config file."
    )
    args = parser.parse_args()
    create_pytorch_tf_and_vocab(args.flax_dump_folder_path)
