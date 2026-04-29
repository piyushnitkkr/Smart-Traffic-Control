import cv2

def load_image(path):
    img = cv2.imread(path)

    if img is None:
        raise ValueError(f"Image not found: {path}")

    img = cv2.resize(img, (1280, 720))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img
