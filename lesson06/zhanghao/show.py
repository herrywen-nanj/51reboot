from prettytable import PrettyTable

FILEDS = ['id', 'username', 'age', 'tel', 'email']


class Output(object):
    def table(self, data):
        xtb = PrettyTable()
        xtb.field_names = FILEDS
        if data:
            for i in data:
                xtb.add_row(i)
            print(xtb)
        else:
            print(xtb)
