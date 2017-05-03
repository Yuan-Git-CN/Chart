import os
import sys
from optparse import OptionParser

from Attribution_Node.Node_Attribution import Attribution
from Item_Recording.Recording_Item import Recording
from Side_Link.Link_Side import Side_Link
from Sparse_Data.Flatten_Data import *
from Sparse_Data.SparseData import DataFromFile,Clean_Data,Item_Characteristic


def main():
    a = True
    sum_item = {}
    f = Clean_Data(inFile)
    item= Item_Characteristic(LinkFile)
    memory = Recording(item, sum_item)
    record = memory.Item_Record()
    while a:
        c = {}
        for i in record.keys():
            j = max(record[i].keys())
            if record[i][j] != []:
                c[i] = record[i][j]
        link = Side_Link(c, record, f)
        item_sum=link.Find_Link_Item()#下一节点数值
        if item_sum ==[]:#终止命令
            break
        a_item = link.Find_Link()
        node_attribution = Attribution(a_item, c,record)
        c=node_attribution.Judge_Nodes_Eauql()
        memory = Recording(c, record)  # 记录结点库
        record = memory.Item_Record()

        for k in item_sum:
            f.remove(k)

    for h in record.keys():#创建文件txt

        full_path = file_name+'/' + str(h) + '.txt'
        file = open(full_path,'w')
        file.write(str(flatten(list(record[h].values()))))
        file.close()




if __name__ == "__main__":
    #创建输出文本地址路径
    base = '/Users/yyf-C/Desktop/Chart/'
    file_name = base + str('DataBase')
    try:
        os.mkdir(file_name)
    except Exception as error:
        print(error)

    # 设置输入文本
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing txt',
                         default='picture.txt')
    optparser.add_option('-s', '--linkSupport',
                         dest='link',
                         help='link support value',
                         default='link.txt')

    (options, args) = optparser.parse_args()
    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = DataFromFile(options.input)
    else:
        print('No dataset filename specified, system with exit\n')
        sys.exit('System will exit')
    LinkFile=None
    if options.link is None:
        LinkFile = sys.stdin
    elif options.input is not None:
        LinkFile = DataFromFile(options.link)
    else:
        print('No dataset filename specified, system with exit\n')
        sys.exit('System will exit')
    #调用主函数
    print("开始执行任务")
    main()
    print("任务执行结束")







