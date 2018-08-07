from . import Model
import cv2


class VehicleModel(Model):

    def __init__(self, vehicle_img):
        super().__init__()

        self._vehicle_img = vehicle_img
        self.license_plate = 'ABC-1234'

    def save_img(self):
        cv2.imwrite('.saved/abc.jpg', self._vehicle_img)

    def show_img(self):
        cv2.imshow('image', self._vehicle_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
