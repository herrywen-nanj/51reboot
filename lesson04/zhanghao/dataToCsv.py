import csv
import json
import os

USERFILE = os.path.abspath(os.path.dirname(__file__) + '/51reboot.txt')
CSVFILE = os.path.abspath(os.path.dirname(__file__) + '/51reboot.csv')


def dataToCsv(filename):
    with open(USERFILE, 'r') as f:
        result = f.read()
        if not result:
            print("\033[0;31;1m{} is none.\033[0m".format(FILENAME))
        else:
            result = json.loads(result)
            RESULT = []
            for k, v in result.items():
                RESULT.append(v.values())
    csvFile = open(filename, 'w', newline='')
    try:
        writer = csv.writer(csvFile)
        writer.writerow(("name", "age", "tel", 'email'))
        for info in RESULT:
            writer.writerow(info)
    except Exception as e:
        print(e)
    finally:
        csvFile.close()


dataToCsv(CSVFILE)
