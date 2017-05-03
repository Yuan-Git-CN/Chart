'''
    关系边以及关系度
'''

import copy

from Sparse_Data.Flatten_Data import flatten


class Side_Link:
    def __init__(self, item, sum_item, data):

        self.data = data
        self.item = item
        self.sum_item = sum_item
        self.next_node = {}
        self.item_sum = []


    #寻找下一跳next_node
    def Find_Link_Item(self):#item结点{0:[1,2]}，sum_item为全部属性总集合，data为关系集合
        # print("\033[0;31m____________________关联边归属__________________\033[0m")

        items = flatten(list(self.item.values()))

        sum_items = []
        for m in self.sum_item.keys():
            sum_items.append(list(self.sum_item[m].values()))
        sum_items = flatten(sum_items)


        for i in self.item.keys():
            for j in self.item[i]:
                for k in self.data:
                    if j in k:
                        if len(set(k).intersection(set(items))) == 2:
                            continue
                        self.item_sum.append(k)#结点与下一节点有关系的边


        test_item = copy.deepcopy(self.item_sum)#深拷贝

        for n in test_item:
            if len(set(n).intersection(set(sum_items))) == 2:
                self.item_sum.remove(n)

        a_item = flatten(self.item_sum)
        self.next_node = set(a_item).difference(set(items))#下一跳数值
        return self.item_sum

        
    def Find_Link(self):#item为属性的SUM
        a_item = {}

        for i in self.next_node:
            # print("_____________________%d______________________________"%i)
            # print("i:{} 为下一节点数,item_sum:{} 为下一节点所有的边,item:{} 为结点属性".format(i,self.item_sum,self.item))
            if not i in a_item.keys():
                a_item[i]={}
            for j in self.item_sum:
                # print("i:{}为下一节点数,j:{}关系边,是否存在关系:{}".format(i,j,i in j))
                if i in j:
                    element = list(set(j).intersection(set(flatten(list(self.item.values())))))
                    # print("关系点为{}".format(element))

                    if element:#寻找节点属性
                        # print("{}结点是否存当前属性结点表{}中：{}".format(element, self.item, element[0] in flatten(list(self.item.values()))))
                        for m in self.item.keys():

                            if element[0] in self.item[m]:
                                if not m in a_item[i].keys():
                                    a_item[i][m] = 1
                                else:
                                    a_item[i][m] =a_item[i][m]+1

            # print("记录下节点与结点{}关系度{}".format(i,a_item))
        return a_item#下结点与结点关系度{8: {0: 1, 1: 2}, 4: {0: 2, 1: 1}, 5: {0: 1, 1: 1}, 6: {0: 1, 1: 1}, 7: {0: 1, 1: 1}}
