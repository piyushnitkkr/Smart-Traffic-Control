import os
import subprocess

def train_model():
    os.chdir("yolov5")

    command = [
        "python", "train.py",
        "--img", "640",
        "--batch", "16",
        "--epochs", "50",
        "--data", "../IDK20K_Vehicles-1/data.yaml",
        "--weights", "yolov5x.pt",
        "--name", "yolov5x_idd_finetune"
    ]

    subprocess.run(command)

if __name__ == "__main__":
    train_model()
