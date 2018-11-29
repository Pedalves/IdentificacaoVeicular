import os

from iv import LICENSE_PLATE_NN
from . import Model
import cv2
import time


class VehicleModel(Model):

    def __init__(self, vehicle_img, output_path=''):
        super().__init__()

        self._vehicle_img = vehicle_img
        self.license_plate = ''
        self.score = {}
        self.output_path = output_path

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
        start = time.time()
        file_path = self.save_img()
        self.license_plate, self.score = LICENSE_PLATE_NN.detect(file_path, self.output_path)
        os.remove(file_path)
        self.time = time.time() - start
