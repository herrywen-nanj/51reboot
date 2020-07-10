# coding: utf-8
import os
import csv
import xlrd

Org = 15
startNumber = 100


# file_dir = '/Users/superlk/Desktop/供电设备履历/巴海区间/一杆一档'
# file_dir = '/Users/superlk/Desktop/供电设备履历/海南站/机走线/一杆一档/机走线一杆一档'


def file_name(file_dir):
    l = list()
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if not file.startswith('.~') and not file.startswith('~$') and not file.startswith('.'):
                file_name = file_dir + '/' + file
                source = read_excel(file_name)
                l.append(source)
    return l, file_dir


def read_excel(file):
    # print(">>>>",file)
    ex = xlrd.open_workbook(file)
    sheet1 = ex.sheet_by_name('主设备信息')
    row = sheet1.nrows
    col = sheet1.ncols
    data = {}
    data['value'] = []
    for i in range(row):
        if i > 0:
            if i == 1:
                data['key'] = list(sheet1.row_values(i, 0, col))
            else:

                data['value'].append(list(sheet1.row_values(i, 0, col)))

    Data = []
    for v in data['value']:
        Data.append(dict(zip(data['key'], v)))

    # 处理 一级设备
    sheet2 = ex.sheet_by_name('一级')
    row2 = sheet2.nrows
    col2 = sheet2.ncols
    # print(row2, col2)
    data2 = {}
    Data2 = []
    data2['value'] = []
    for x in range(row2):
        if x == 0:
            data2['key'] = sheet2.row_values(x, 0, col2)
        else:
            l = sheet2.row_values(x, 0, col2)
            data2['value'].append(l)
    for s in data2['value']:
        Data2.append(dict(zip(data2['key'], s)))

    # print(Data,Data2)
    source = dict()
    source['main'] = Data
    source['first'] = Data2
    # print(source)
    return source


def write_csv(l, file_dir):
    file = '/Users/superlk/Desktop/MainDeviceYGBHQJ.csv'
    file1 = '/Users/superlk/Desktop/mainYG.csv'
    file2 = '/Users/superlk/Desktop/FirstDeviceYGYD.csv'
    file3 = '/Users/superlk/Desktop/firstYG.csv'
    with open(file, encoding='gbk') as f:
        # with open(file) as f:
        f_csv = csv.reader(f)
        f_csv_list = list(f_csv)

        num = len(f_csv_list)
    # datalist = formatData(data, f_csv_list[1], startNumber)

    with open(file2, encoding='gbk') as f2:
        # with open(file) as f2:
        f_csv2 = csv.reader(f2)
        f_csv_list2 = list(f_csv2)

        num = len(f_csv_list2)
    dataList, dataList2 = formatData(l, f_csv_list[1], f_csv_list2[1], file_dir)

    with open(file1, 'a+', encoding='utf-8', newline='') as f1:
        writer = csv.DictWriter(f1, f_csv_list[1])
        writer.writeheader()
        writer.writerows(dataList)

    with open(file3, 'a+', encoding='utf-8', newline='') as f3:
        writer = csv.DictWriter(f3, f_csv_list2[1])
        writer.writeheader()
        writer.writerows(dataList2)

    print('write is success  :', file_dir)


def formatData(l, csv_list, csv_list2, file_dir):
    global startNumber
    # num = startNumber
    DataList = []
    DataList2 = []
    for i in l:
        data = i['main']
        data2 = i['first']
        for d in data:
            DataDict = {}
            for k, v in d.items():
                # for row in csv_list:
                if k in csv_list:
                    DataDict[k] = str(v)
                    if k == '设备编码':
                        DataDict[k] = startNumber
                    if k == '拉线安装图号':
                        DataDict[k] = ' %s' % v
                    if k == '附加悬挂安装图号':
                        DataDict[k] = ' %s' % v
                    if k == '避雷器安装图号':
                        DataDict[k] = ' %s' % v

                elif k == '''跨号
（关联作业单查询）''':
                    DataDict['跨号 （关联作业单查询） '] = str(v)
                elif k == '''软横跨号/硬横梁
（关联作业单查询）''':
                    DataDict['软横跨号/硬横梁 （关联作业单查询）'] = str(v)
                elif k == '''相邻股道号
（关联作业单查询）''':
                    DataDict['相邻股道号 （关联作业单查询）'] = str(v)
                elif k == ' 标识标志':
                    DataDict['标识标志'] = str(v)
                elif k == '先岔安装图号':
                    DataDict['线岔安装图号'] = str(v)
                # elif k == '工区名称':
                    # print(">>>", file_dir)
                else:
                    # print('主设备匹配错误keyK>>>', k, file_dir)
                    pass
                DataDict['组织 '] = Org

            DataList.append(DataDict)
            num2 = 1
            type_ = ''
            for d2 in data2:
                DataDict2 = {}
                for m, n in d2.items():
                    if m in csv_list2:
                        DataDict2[m] = str(n)
                        if m == '一级从分类':
                            if n:
                                type_ = str(n)
                                DataDict2[m] = str(n)
                            else:
                                DataDict2[m] = type_

                    elif m == "投运时间":
                        DataDict2['投运日期'] = str(n)
                    elif m == '一级从设备编码':
                        DataDict2['设备编号'] = startNumber * 1000 + num2
                        # print( ">>>>>",num2)
                    elif m == '设备编码':
                        DataDict2['设备编号'] = startNumber * 1000 + num2
                    else:
                        # print('一级匹配错误key>>>>>>', m, csv_list2)
                        pass
                    DataDict2['主设备编号'] = startNumber
                    DataDict2['组织'] = Org
                num2 += 1
                DataList2.append(DataDict2)

        startNumber += 1

    # startNumber = num

    return DataList, DataList2


def start(path):
    l, file_dir = file_name(path)
    write_csv(l, file_dir)


def SearchPath(dir, Patch):
    # D = dir
    for root, dirs, files in os.walk(dir):
        for d in dirs:
            if d == '一杆一档':
                p = dir + '/' + '一杆一档'
                Patch.append(p)
            elif d == '一跨一档':
                pass
            else:
                SearchPath(dir + '/' + d, Patch)
        break
    return Patch


if __name__ == '__main__':
    Patch = SearchPath('/Users/superlk/Desktop/供电设备履历', [])
    for d in Patch:
        startNumber=100
        # print('-----', startNumber)
        print('>>>',d)
        if '巴海区间' in d:
            Org = 15
        elif '机走线' in d:
            Org = 16
        elif '联络线' in d:
            Org = 17
        elif '零散支柱' in d:
            Org = 18
        elif '牵出线' in d:
            Org = 19
        elif '正线/I场I道' in d:
            Org = 20
        elif 'II场I道' in d:
            Org = 21
        elif '敖包沟隧道上行' in d:
            # print('----' * 10)
            Org = 22
        elif '海四上行/海四上行' in d:
            Org = 23
        elif '海四区间下行' in d:
            Org = 24
        elif '敖包沟隧道下行' in d:
            Org = 25
        elif '机务折返所' in d:
            Org = 26
        elif '纳点区间上行' in d:
            Org = 27
        elif '保海圪堵1号隧道上行' in d:
            Org = 28
        elif '保海圪堵2号隧道上行' in d:
            Org = 29
        elif '刘家渠隧道上行' in d:
            Org = 30
        elif '尔林兔隧道上行' in d:
            Org = 31
        elif '马石梁隧道上行' in d:
            Org = 32
        elif '海子塔隧道上行' in d:
            Org = 33
        elif '保佬兔沟隧道上行' in d:
            Org = 34
        elif '后碾房梁隧道上行' in d:
            Org = 35
        elif '潘家疙楞隧道上行' in d:
            Org = 36
        elif '纳点区间下行' in d:
            Org = 37
        elif '保海圪堵1号隧道下行' in d:
            Org = 38
        elif '保海圪堵2号隧道下行' in d:
            Org = 39
        elif '刘家渠隧道下行' in d:
            Org = 40
        elif '尔林兔隧道下行' in d:
            Org = 41
        elif '马石梁隧道下行' in d:
            Org = 42
        elif '海子塔隧道下行' in d:
            Org = 43
        elif '保佬兔沟隧道下行' in d:
            Org = 44
        elif '后碾房梁隧道下行' in d:
            Org = 45
        elif '潘家疙楞隧道下行' in d:
            Org = 46
        elif '纳林川站/I道' in d:
            Org = 47
        elif '纳林川站/II道' in d:
            Org = 48
        elif '纳林川站/3道' in d:
            Org = 49
        elif '纳林川站/4道' in d:
            Org = 50
        elif '纳林川上行' in d:
            Org = 51
        elif '纳林川下行' in d:
            Org = 52
        elif '四道柳站/I道' in d:
            Org = 53
        elif '四道柳站/II道' in d:
            Org = 54
        elif '四道柳站/3道' in d:
            Org = 55
        elif '四道柳站/4道' in d:
            Org = 56
        elif '四道柳上行' in d:
            Org = 57
        elif '四道柳下行' in d:
            Org = 58
        elif '四纳区间上行' in d:
            Org = 59
        elif '王家梁隧道上行' in d:
            Org = 60
        elif '忽吉图沟隧道上行' in d:
            Org = 61
        elif '李家圪卜1号隧道上行' in d:
            Org = 62
        elif '李家圪卜2号隧道上行' in d:
            Org = 63
        elif '王连圪堵1号隧道上行' in d:
            Org = 64
        elif '王连圪堵2号隧道上行' in d:
            Org = 65
        elif '哈拉沟隧道上行' in d:
            Org = 66
        elif '四纳区间下行' in d:
            Org = 67
        elif '王家梁隧道下行' in d:
            Org = 68
        elif '忽吉图沟隧道下行' in d:
            Org = 69
        elif '李家圪卜1号隧道下行' in d:
            Org = 70
        elif '李家圪卜2号隧道下行' in d:
            Org = 71
        elif '王连圪堵1号隧道下行' in d:
            Org = 72
        elif '王连圪堵2号隧道下行' in d:
            Org = 73
        elif '哈拉沟隧道下行' in d:
            Org = 74
        else:
            print('****', d)
            pass

        start(d)
        # break

    # start(dir)
    # write_csv(file_dir)
