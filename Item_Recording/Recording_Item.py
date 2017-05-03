'''
    更新划分数据
'''
class Recording:
    def __init__(self,item,sum_item):
        self.item = item
        self.sum_item = sum_item

    def Item_Record(self):
        for i in self.item.keys():
            j = 0
            if not i in self.sum_item.keys():
                s_item = list(set(self.item[i]))
                self.sum_item[i] = {}
                self.sum_item[i][j] = s_item
            else:
                a = max(self.sum_item[i].keys()) + 1
                s_item = list(set(self.item[i]))
                self.sum_item[i][a] = s_item
        return self.sum_item#返回为以划分好数据，并记录是第几跳

