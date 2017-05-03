'''
    结点划分
'''

import collections

from Sparse_Data.Flatten_Data import *


class Attribution:
    def __init__(self,a_item,item,sum_item):#a_item为下一跳单个点集合，item为当前属性表集合
        self.a_item=a_item
        self.sum_item=sum_item
        self.item=item
        self.item_recording={}
        self.item_count={}

    def Judge_Nodes_Eauql(self):  # item测试使用值

        for i in self.a_item.keys():
            if len(self.a_item[i].keys()) == 1:

                x_node=list(self.a_item[i].keys())[0]
                if not x_node in self.item_recording.keys():
                    self.item_recording[x_node]=[]
                    self.item_recording[x_node].append(i)
                else:
                    self.item_recording[x_node].append(i)
                continue

            #字典，keys与values互换位置
            d = collections.defaultdict(list)
            for k, v in self.a_item[i].items():
                d[v].append(k)

            max_node = max(d.keys())
            max_length = len(d[max_node])
            if max_length == 1:#判断最大值中是否含有唯一值
                node=d[max_node]
                if not node[0] in self.item_recording.keys():
                    self.item_recording[node[0]]=[]
                    self.item_recording[node[0]].append(i)
                else:
                    self.item_recording[node[0]].append(i)

            else:

                for j in d[max_node]:
                    if not j in self.item_count.keys():
                        self.item_count[j] = 0

                for k in self.item_count.keys():
                    if not k in self.item_recording.keys():
                        self.item_recording[k]=[]

                    past_sum=len(flatten(list(self.sum_item[k].values())))
                    now_sum=len(flatten(list(self.item_recording[k])))

                    self.item_count[k] = now_sum+past_sum

                items_count={}
                for past_count in self.item_count.keys():
                    if past_count in d[max_node]:
                        items_count[past_count]=self.item_count[past_count]

                dk = collections.defaultdict(list)
                for k, v in items_count.items():
                    dk[v].append(k)

                min_node = min(dk.keys())
                min_sum_length = len(dk[min_node])
                if min_sum_length == 1:
                    o_node = dk[min_node][0]

                    if not o_node in self.item_recording.keys():
                        self.item_recording[o_node] = []
                        self.item_recording[o_node].append(i)
                    else:
                        self.item_recording[o_node].append(i)
                else:
                    if not dk[min_node][0] in self.item_recording.keys():
                        self.item_recording[min_node] = []
                        self.item_recording[min_node].append(i)
                    else:
                        #print("test",self.item_recording,dk[min_node][0])
                        end_node=dk[min_node][0]
                        self.item_recording[end_node].append(i)
            # print('点i{}被添加到那个属性内item_recording{}'.format(i,self.item_recording))
        return self.item_recording
