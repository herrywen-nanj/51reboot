import json


def loadUser(filename):
    with open(filename, 'r') as f:
        result = f.read()
        if not result:
            print("\033[0;31;1m{} is none.\033[0m".format(filename))
            result = {}
        else:
            result = json.loads(result)
    return result
