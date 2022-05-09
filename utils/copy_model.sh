SIZE="xxl"

SOURCE_BUCKET="t5x-backup"
TARGET_BUCKET="north-t5x"
TARGET_DIRECTORY="pretrained_models/${SIZE}"

MODEL="norwegian_NCC_plus_English_pluss200k_scandinavian_t5x_${SIZE}"
CHECKPOINT="1700000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
eval $CMD

MODEL="norwegian_NCC_plus_English_pluss200k_balanced_bokmaal_nynorsk_t5x_${SIZE}"
CHECKPOINT="1700000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
eval $CMD

MODEL="norwegian_NCC_plus_English_pluss200k_balanced_bokmaal_nynorsk_pluss100k_lm_t5x_${SIZE}"
CHECKPOINT="1800000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
eval $CMD

MODEL="norwegian_NCC_plus_English_t5x_${SIZE}"
CHECKPOINT="1500000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
eval $CMD

MODEL="scandinavian_t5x_${SIZE}"
CHECKPOINT="1500000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
eval $CMD



