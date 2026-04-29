import torch

def load_model(weights_path=None, device='cpu'):
    if weights_path:
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path)
    else:
        model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

    model.conf = 0.4
    model.to(device)
    return model


def count_vehicles(model, frame):
    results = model(frame)
    detections = results.xyxy[0]

    car_count = 0
    big_vehicle_count = 0

    for det in detections:
        class_id = int(det[5])
        class_name = model.names[class_id]

        if class_name == 'car':
            car_count += 1
        elif class_name in ['bus', 'truck']:
            big_vehicle_count += 1

    return car_count, big_vehicle_count, results
