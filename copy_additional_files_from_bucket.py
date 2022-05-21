import shutil
import argparse
import os

def copy_additional_files_from_bucket(bucket_model_path, local_path):
    cmd = "gsutil -m cp -r "+bucket_model_path+"train"+" "+local_path
    os.system(cmd)
    cmd = "gsutil -m cp -r "+bucket_model_path+"training_eval"+" "+local_path
    os.system(cmd)
    cmd = "gsutil cp "+bucket_model_path+"config.gin"+" "+local_path
    os.system(cmd)
    cmd = "gsutil cp "+bucket_model_path+"model-info.txt"+" "+local_path
    os.system(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument(
        "--bucket_model_path", default=None, type=str, required=True, help="Path to model in the bucket."
    )
    parser.add_argument(
        "--local_path", default=None, type=str, required=True, help="Path to local directory."
    )
    args = parser.parse_args()
    copy_additional_files_from_bucket(args.bucket_model_path, args.local_path)
