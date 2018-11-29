import cv2
import uuid
import os
import numpy as np

from iv.model.vehicle import VehicleModel


def get_lincese_plate(vehicle_img, debug=False):
    nparr = np.frombuffer(vehicle_img, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    output_path = ''
    if debug:
        output_path = str(uuid.uuid4()) + '.jpg'
        output_path = os.path.join(os.getcwd(), '.saved', output_path)

    model = VehicleModel(img, output_path)
    model.predict()

    return model
