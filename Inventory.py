# This class is responsible for creating Inventory object which contains
# total amount of inventory for each product type
class Inventory(object):

    def __init__(self,inventoryList):

        self.items = inventoryList
        self.orderType =  ['A', 'B', 'C', 'D', 'E']

    def returnItems(self):
        return self.items

    def isInventoryOver(self):
        sum = 0
        flag = False
        for order in self.orderType:
            sum += self.items[order]
        if sum == 0:
            flag = True
        return flag

    def reset(self,inventoryList):
        self.items = inventoryList






