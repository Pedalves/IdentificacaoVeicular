import darknet.darknet as dn
import os


net = dn.load_net("/home/pedalv/Workspace/darknet/cfg/yolov3-iv-test.cfg".encode('utf-8'),
                  "/home/pedalv/Workspace/darknet/yolov3-iv_7100.weights".encode('utf-8'), 0)


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
