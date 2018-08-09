import sys
sys.path.append("/home/pedro/Workspace/IdentificacaoVeicular/IV-Flask")

import darknet.darknet as dn
import os

from iv.neural_network.license_plate import LicensePlateNetwork

dn.set_gpu(1)
LICENSE_PLATE_NN = LicensePlateNetwork()


def config(variable, namespace="IV_"):
    # make case insensitive
    variable = variable.upper()
    variable_name = '{}{}'.format(namespace, variable)

    value = os.getenv(variable_name)

    # evaluate string as boolean
    if isinstance(value, str) and value.lower() in ["true", "yes"]:
        return True
    elif isinstance(value, str) and value.lower() in ["false", "no"]:
        return False

    try:
        value = int(str(value))
    except (ValueError, TypeError):
        try:
            value = float(value)
        except (ValueError, TypeError):
            pass
        pass

    return value


if __name__ == '__main__':
    import time
    s = time.time()
    print(LICENSE_PLATE_NN.detect('/home/pedro/Workspace/IdentificacaoVeicular/IV-Flask/.saved/temp.jpg'))
    print(time.time() - s)
