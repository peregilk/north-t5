<<<<<<< HEAD
SIZE="large"
=======
SIZE="small"
>>>>>>> ddedc35fe4413dabc6c77ba8ffb5691f45d1b695

SOURCE_BUCKET="t5x-backup"
TARGET_BUCKET="north-t5x"
TARGET_DIRECTORY="pretrained_models/${SIZE}"

#1.5M - mT5 + 500k NCC
MODEL="norwegian_NCC_plus_English_t5x_${SIZE}"
CHECKPOINT="1500000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
#eval $CMD

#1.6M - mT5 + 500k NCC + 100k LM
MODEL="norwegian_NCC_plus_English_pluss100k_lm_t5x_${SIZE}"
CHECKPOINT="1600000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
#eval $CMD

#1.7M - mT5+ 500k NCC + 200k Scandinavian
MODEL="norwegian_NCC_plus_English_pluss200k_scandinavian_t5x_${SIZE}"
CHECKPOINT="1700000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
#eval $CMD

#1.7M - mT5 + 500k NCC + 200k Nynorsk/Bokmål
MODEL="norwegian_NCC_plus_English_pluss200k_balanced_bokmaal_nynorsk_t5x_${SIZE}"
CHECKPOINT="1700000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
#eval $CMD

#1.8M - mT5 + 500k NCC + 200k Nynorsk/Bokmål + 100k LM
MODEL="norwegian_NCC_plus_English_pluss200k_balanced_bokmaal_nynorsk_pluss100k_lm_t5x_${SIZE}"
CHECKPOINT="1800000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
#eval $CMD

#1.5M - byT5 + 500k NCC
MODEL="norwegian_NCC_plus_English_byt5x_${SIZE}"
CHECKPOINT="1500000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
#eval $CMD

#1.7M - mT5 + 700k Scandinavian
MODEL="scandinavian_t5x_${SIZE}"
CHECKPOINT="1700000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
#eval $CMD

#1.7M - mT5 + 700k Scandinavian
MODEL="scandinavian_t5x_${SIZE}"
CHECKPOINT="1500000"
CMD="gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/config.gin gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ &&gsutil -m cp -n gs://${SOURCE_BUCKET}/${MODEL}/model-info.txt gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/train/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -n -r gs://${SOURCE_BUCKET}/${MODEL}/training_eval/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/ && gsutil -m cp -r -n gs://${SOURCE_BUCKET}/${MODEL}/checkpoint_${CHECKPOINT}/ gs://${TARGET_BUCKET}/${TARGET_DIRECTORY}/${MODEL}/"
eval $CMD



