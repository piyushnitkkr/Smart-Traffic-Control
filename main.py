import os
import pandas as pd
import matplotlib.pyplot as plt

from detect import load_model, count_vehicles
from traffic_logic import calculate_duration
from utils import load_image


# CONFIG
IMAGE_PATHS = [
    "data/images/lane1.jpg",
    "data/images/lane2.jpg",
    "data/images/lane3.jpg",
    "data/images/lane4.jpg"
]

WEIGHTS_PATH = "yolov5/runs/train/yolov5x_idd_finetune/weights/best.pt"


def main():
    # Load model
    model = load_model(weights_path=WEIGHTS_PATH, device='cuda')

    lane_durations = []

    for i, img_path in enumerate(IMAGE_PATHS):
        try:
            img = load_image(img_path)
        except ValueError as e:
            print(e)
            continue

        cars, bigs, results = count_vehicles(model, img)
        duration = calculate_duration(cars, bigs)

        lane_durations.append({
            'Lane': i + 1,
            'Cars': cars,
            'Bigs': bigs,
            'Duration': duration
        })

        # Visualization
        annotated = results.render()[0]
        plt.imshow(annotated)
        plt.title(f"Lane {i+1}: Cars={cars}, Bigs={bigs}, Duration={duration}s")
        plt.axis('off')
        plt.show()

    # Save CSV
    df = pd.DataFrame(lane_durations)
    df.to_csv("signal_output.csv", index=False)

    print(df)


if __name__ == "__main__":
    main()
