from transformers import T5ForConditionalGeneration, T5Config, AutoTokenizer
import shutil
import argparse


def convert_pytorch_and_vocab(flax_dump_folder_path):

    shutil.copyfile('spiece.model',flax_dump_folder_path+'spiece.model')
    shutil.copyfile('special_tokens_map.json',flax_dump_folder_path+'special_tokens_map.json')
    shutil.copyfile('tokenizer_config.json',flax_dump_folder_path+'tokenizer_config.json')

    print("Copied tokenizer files")

    config= T5Config.from_pretrained(flax_dump_folder_path+'config.json')
    model = T5ForConditionalGeneration(config=config)
    model.save_pretrained(flax_dump_folder_path)

    print("Saved PyTorch-model")

    tokenizer = AutoTokenizer.from_pretrained(flax_dump_folder_path)
    tokenizer.save_pretrained(flax_dump_folder_path)

    print("Saved tokenizer")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument(
        "--flax_dump_folder_path", default=None, type=str, required=True, help="Path to the output FLAX model."
    )
    args = parser.parse_args()
    convert_pytorch_and_vocab(args.flax_dump_folder_path)
