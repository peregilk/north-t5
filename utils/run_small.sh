T5X_CHECKPOINT_PATH="gs://north-t5x/pretrained_models/small/norwegian_NCC_plus_English_t5x_small/checkpoint_1500000"
FLAX_DUMP_FOLDER_PATH="/home/perk/conv/north-t5-small/"
CONFIG_NAME="small.json"

python convert_t5x_checkpoint_to_flax.py --t5x_checkpoint_path ${T5X_CHECKPOINT_PATH} --config_name ${CONFIG_NAME} --flax_dump_folder_path ${FLAX_DUMP_FOLDER_PATH}
python create_pytorch_and_vocab.py --flax_dump_folder_path ${FLAX_DUMP_FOLDER_PATH}

