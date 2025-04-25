import requests
import os

# URLs for the datasets
dataset_links = {
    "SEMEVAL-21-T6": "https://raw.githubusercontent.com/di-dimitrov/SEMEVAL-2021-task6-corpus/main/data/training_set_task2.txt",

    "COCOLOFA":
    {
    "DEV": "https://github.com/Crowd-AI-Lab/cocolofa/blob/main/dev.json?raw=true",
    "TRAIN": "https://github.com/Crowd-AI-Lab/cocolofa/blob/main/train.json?raw=true",
    "TEST": "https://github.com/Crowd-AI-Lab/cocolofa/blob/main/test.json?raw=true"
    },

    "LOGICAL_FALLACY":
    {
    "TRAIN": "https://huggingface.co/datasets/MidhunKanadan/logical-fallacy-classification/resolve/main/data/train-00000-of-00001.parquet?download=true",
    "TEST": "https://huggingface.co/datasets/MidhunKanadan/logical-fallacy-classification/resolve/main/data/test-00000-of-00001.parquet?download=true",
    "DEV": "https://huggingface.co/datasets/MidhunKanadan/logical-fallacy-classification/resolve/main/data/dev-00000-of-00001.parquet?download=true"
    },

    "MAFALDA": "https://raw.githubusercontent.com/ChadiHelwe/MAFALDA/refs/heads/main/datasets/gold_standard_dataset.jsonl"

}

os.makedirs("./data", exist_ok=True)

for name, link in dataset_links.items():
    if isinstance(link, dict):
        os.makedirs(f"./data/{name}", exist_ok=True)
        for sub_name, sub_link in link.items():
            response = requests.get(sub_link)
            filename = sub_name + ".json" if isinstance(sub_link, str) else sub_name + ".txt"
            with open(f"data/{name}/{filename}", "wb") as file:
                file.write(response.content)
    else:
        response = requests.get(link)
        filename = name + ".json" if isinstance(link, str) else name + ".txt"
        with open(f"data/{filename}", "wb") as file:
            file.write(response.content)



