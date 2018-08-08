import os
import cv2

import darknet.darknet as dn


class LicenseBoxNetwork:
    def __init__(self):
        curr_path = os.getcwd()

        self._net = dn.load_net(os.path.join(curr_path, 'iv', 'neural_network', 'net',
                                             'yolov3-iv-test.cfg').encode('utf-8'),
                                os.path.join(curr_path, 'iv', 'neural_network', 'net',
                                             'yolov3-iv_23600.weights').encode('utf-8'), 0)
        self._meta = dn.load_meta(os.path.join(curr_path, 'iv', 'neural_network',
                                               'meta', 'bb', 'obj.data').encode('utf-8'))

    def detect(self, img):
        return dn.detect(self._net, self._meta, img.encode('utf-8'))

    def get_plate_img(self, img):

        prediction = self._select_plate(self._convert_to_conners(self.detect(img)), 0.7)

        if prediction is None:
            print('ERROR')
            return None

        if self._validate_plate_shape(prediction):
            return self._crop_image(img, prediction)
        return None

    def _convert_to_conners(self, prediction):
        for index, pred in enumerate(prediction):
            x = pred[2][0]
            y = pred[2][1]
            w = pred[2][2]
            h = pred[2][3]

            x1 = x - (w / 2)
            y1 = y - (h / 2)
            x2 = x + (w / 2)
            y2 = y + (h / 2)

            prediction[index] = (pred[0], pred[1], (x1, y1, x2, y2))

        return prediction

    def _select_plate(self, predictions, limiar):

        for data in predictions:
            if data[0] == 'placa'.encode() and data[1] >= limiar:
                return data[2]

        return None

    def _validate_plate_shape(self, box):

        w = (box[2] - box[0])
        h = (box[3] - box[1])

        prop = w / h

        if prop >= 2.5 and prop <= 3.4:
            return True
        else:
            return False

    def _crop_image(self, file_path, box):
        output_folder = os.path.join(os.getcwd(), '.saved')

        x = int(box[0])
        y = int(box[1])
        w = int(box[2])
        h = int(box[3])

        img = cv2.imread(file_path)
        crop_img = img[y:h, x:w]

        file_path = os.path.join(output_folder, 'placa.jpg')

        if os.path.isfile(file_path):
            os.remove(file_path)

        cv2.imwrite(file_path, crop_img)
        return file_path


class LicensePlateNetwork:
    def __init__(self):
        curr_path = os.getcwd()

        self._net = dn.load_net(os.path.join(curr_path, 'iv', 'neural_network', 'net',
                                             'yolov3-tiny-test.cfg').encode('utf-8'),
                                os.path.join(curr_path, 'iv', 'neural_network', 'net',
                                             'yolov3-tiny_43000.weights').encode('utf-8'), 0)
        self._meta = dn.load_meta(os.path.join(curr_path, 'iv', 'neural_network', 'meta',
                                               'plate', 'obj.data').encode('utf-8'))

        self.bb_network = LicenseBoxNetwork()

    def detect(self, car_img):
        img = self.bb_network.get_plate_img(car_img)

        if not img:
            return ''

        reverse = False
        if img.find("_aug") != -1:
            reverse = True

        r = dn.detect(self._net, self._meta, img.encode('utf-8'))
        _, pred_plate = self._convert_to_conners(r, reverse)

        return pred_plate

    def _char_to_int(self, char):
        if char == 'I':
            return '1'
        elif char == 'Z':
            return '2'
        elif char == 'E':
            return '3'
        elif char == 'A':
            return '4'
        elif char == 'S':
            return '5'
        elif char == 'G':
            return '6'
        elif char == 'T':
            return '7'
        elif char == 'B':
            return '8'
        elif char == 'P':
            return '9'
        elif char == 'O':
            return '0'
        else:
            return char

    def _convert_to_conners(self, prediction, reverse):

        if len(prediction) > 7:
            prediction = sorted(prediction, key=lambda pre: pre[1], reverse=True)[:7]

        prediction = sorted(prediction, key=lambda pre: pre[2][0], reverse=reverse)

        if len(prediction) == 6:
            prediction = self._bigger_distance(prediction)

        str_plate = ''

        for index, pred in enumerate(prediction):

            x = pred[2][0]
            y = pred[2][1]
            w = pred[2][2]
            h = pred[2][3]

            x1 = x - (w / 2)
            y1 = y - (h / 2)
            x2 = x + (w / 2)
            y2 = y + (h / 2)

            prediction[index] = (pred[0], pred[1], (x1, y1, x2, y2))

            if index > 2:
                str_plate += self._char_to_int(pred[0].decode("utf-8"))
            else:
                str_plate += pred[0].decode("utf-8")

        return prediction, str_plate

    def _bigger_distance(self, prediction):

        bigger = 0
        pos_bigger = len(prediction)

        for index, pred in enumerate(prediction):

            if index == len(prediction) - 1:
                break

            dist = pred[2][0] - prediction[index + 1][2][0]

            if dist < 0:
                dist = dist * -1

            if dist > bigger and dist > ((pred[2][2]) + (pred[2][2] * 0.8)):
                bigger = dist
                pos_bigger = index + 1

        prediction.insert(pos_bigger, ('?', 0, (-1, -1, -1, -1)))

        return prediction
