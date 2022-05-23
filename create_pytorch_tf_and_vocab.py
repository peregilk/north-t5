from transformers import FlaxT5ForConditionalGeneration,TFT5ForConditionalGeneration, T5ForConditionalGeneration, T5Config, AutoTokenizer
import shutil
import argparse


def create_pytorch_tf_and_vocab(flax_dump_folder_path, model_size):

    shutil.copyfile('spiece.model',flax_dump_folder_path+'/spiece.model')
    shutil.copyfile('special_tokens_map.json',flax_dump_folder_path+'/special_tokens_map.json')
    shutil.copyfile('tokenizer_config.json',flax_dump_folder_path+'/tokenizer_config.json')
    shutil.copyfile('.gitattributes',flax_dump_folder_path+'/.gitattributes')

    print("Copied tokenizer files and a gitattributes file")
    config= T5Config.from_pretrained(model_size+'.json')
    
    #For the huge models, we will also open and save the Flax file
    #if model_size = "xl" or model_size="xxl":
    model = T5ForConditionalGeneration.from_pretrained(flax_dump_folder_path,config=config,from_flax=True)
    model.save_pretrained(flax_dump_folder_path)


    model = T5ForConditionalGeneration.from_pretrained(flax_dump_folder_path,config=config,from_flax=True)
    model.save_pretrained(flax_dump_folder_path)
    print("Saved PyTorch-model")

    model = TFT5ForConditionalGeneration.from_pretrained(flax_dump_folder_path,config=config, from_pt=True)
    model.save_pretrained(flax_dump_folder_path)
    print("Saved Tensorflow-model")

    tokenizer = AutoTokenizer.from_pretrained(flax_dump_folder_path)
    tokenizer.save_pretrained(flax_dump_folder_path)

    print("Saved tokenizer")


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
