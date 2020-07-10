import json


def saveUser(result, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(result))
