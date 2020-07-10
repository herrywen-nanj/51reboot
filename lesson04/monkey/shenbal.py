

RESULT = {}


def loadFile():
    with open('/etc/passwd', 'r') as fd:
        data = fd.read()
        return data


def opLogic():
    RESULT = loadFile()
    print(RESULT)

def main():
    opLogic()



main()