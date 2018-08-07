import cv2
import numpy as np

from iv import net
from iv.model.vehicle import VehicleModel


def get_lincese_plate(vehicle_img):
    nparr = np.fromstring(vehicle_img, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    model = VehicleModel(img)
    # model.save_img()

    return model
