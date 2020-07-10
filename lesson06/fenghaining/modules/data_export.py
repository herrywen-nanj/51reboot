import csv

def data_export(users, info_list):
    """
    数据导出到csv文件
    :param users: 存储于文件中的用户信息字典
    :return:
    """

    msg = ''
    flag = True
    if len(info_list) < 2:
        msg = '数据长度不等于2，请重新输入'
        flag = False
        return msg, flag
    filename = info_list[1]
    with open('%s.csv' % filename, 'w', newline='') as datacsv:
        csvwriter = csv.writer(datacsv, dialect=('excel'))
        csvwriter.writerow(['姓名', '年龄', '电话', '邮箱'])
        for k, v in users.items():
            csvwriter.writerow(list(v.values()))
    msg = '文件导出成功，文件名为%s.csv' % filename
    return msg, flag