from prettytable import PrettyTable

def serialize_data(data):
    """
    格式化数据
    :param data: 要格式化的数据
    :return:
    """
    xtb = PrettyTable()
    xtb.field_names = ['username', 'age', 'tel', 'email']
    for i in data:
        xtb.add_row(i)
    return xtb