import argparse
import os

import kagglehub


def main():
    parser = argparse.ArgumentParser(description="script for making kaggle dataset")

    parser.add_argument("dataset_name", type=str, help="dataset name")
    parser.add_argument("folder_path", type=str, help="folder path")

    args = parser.parse_args()

    kagglehub.dataset_upload(
        os.environ["KAGGLE_USERNAME"] + "/" + args.dataset_name, args.folder_path
    )
