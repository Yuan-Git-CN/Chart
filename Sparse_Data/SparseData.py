'''
    数据分析，清理
'''
def DataFromFile(fname):#从文本中提取数据
    record = []
    file_iter = open(fname, "rU")
    for line in file_iter.readlines():
        lines = line.strip('\n')#按行读取且处理掉换行符，效果:"\'\n'变为了''
        lists = lines.split(' ')
        lists=list(map(int, lists))
        if list:
            record.append(lists)
    return record

def Clean_Data(file_data):#清洗数据
    f = []
    for item in file_data:
        if item[0] == item[1]:
            continue
        if [item[0], item[1]] in f:
            continue
        if [item[1], item[0]] in f:
            continue
        f.append([item[0], item[1]])
    f.sort()  # 排序，无所谓关键，可删除
    return f



def Item_Characteristic(File_name):#初始点属性值{‘数值’：‘属性’}
    link_dict = dict(File_name)
    dict_link = {}
    for i in set(link_dict.values()):
        for j in link_dict.keys():
            if i in dict_link.keys():
                if link_dict[j] == i:
                    dict_link[i].append(j)
            else:
                if link_dict[j] == i:
                    dict_link[i]=[]
                    dict_link[i].append(j)

    return dict_link







