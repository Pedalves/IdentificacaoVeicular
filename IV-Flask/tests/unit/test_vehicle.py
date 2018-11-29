# pylint: disable=missing-docstring
import pytest

import cv2

from iv.controller import vehicle


def test_get_license_plate():
    print()
    img = cv2.imread('KXT8495.jpg')

    _, img_encoded = cv2.imencode('.jpg', img)

    plate = vehicle.get_lincese_plate(img_encoded)

    assert plate.license_plate == "KXT8495"
