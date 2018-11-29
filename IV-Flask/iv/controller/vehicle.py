import cv2
import numpy as np

from iv.model.vehicle import VehicleModel


def get_lincese_plate(vehicle_img):
    nparr = np.frombuffer(vehicle_img, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    model = VehicleModel(img)
    model.predict()

    return model
