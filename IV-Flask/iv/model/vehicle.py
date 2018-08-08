import os

from iv import LICENSE_PLATE_NN
from . import Model
import cv2


class VehicleModel(Model):

    def __init__(self, vehicle_img):
        super().__init__()

        self._vehicle_img = vehicle_img
        self.license_plate = ''

    def save_img(self, name='temp'):
        file_path = os.path.join(os.getcwd(), '.saved/{}.jpg'.format(name))

        if os.path.isfile(file_path):
            os.remove(file_path)

        cv2.imwrite(file_path, self._vehicle_img)

        return file_path

    def show_img(self):
        cv2.imshow('image', self._vehicle_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def predict(self):
        self.license_plate = LICENSE_PLATE_NN.detect(self.save_img())
