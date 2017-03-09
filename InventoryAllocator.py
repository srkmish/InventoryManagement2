# This class is responsible for the logic of allocating orders
import collections

class Allocator(object):
    def __init__(self,datasource,inventory):
        self.datasource = datasource
        # print(self.orderStream)# Get Total List of Orders from datasource
        self.inventory = inventory # Total amount of inventory
        self.orderStream = []
        self.inventoryOver = False # To check whether inventory is empty
        self.orders = [] # List of orders generated per line
        self.ordersAllocated = [] # List of orders Allocated per line
        self.ordersBackOrdered = [] # List of orders Backordered per line
        self.headers = [] # Header of the order
        self.counter = 0

    def allocateOrders(self):

        self.orderStream = self.datasource.returnData()
        if(self.orderStream):

            for stream in self.orderStream[self.counter:]:  # Process every line in order Stream
                if(not(self.inventory.isInventoryOver())):
                    line = stream["Lines"]
                    self.tempheader = stream["Header"]
                    print("Header:",self.tempheader)
                    self.tempDictOrder = collections.OrderedDict() # Create temporary dictionaries to store order requested, allocated and backordered
                    self.tempDictOrder['A'] = 0
                    self.tempDictOrder['B'] = 0
                    self.tempDictOrder['C'] = 0
                    self.tempDictOrder['D'] = 0
                    self.tempDictOrder['E'] = 0
                    self.tempDictAllocated = self.tempDictOrder.copy()
                    self.tempDictBackOrdered = self.tempDictOrder.copy()
                    for order in line: # Check for every order in a line

                        orderproduct = order["Product"]
                        orderquantity = order["Quantity"]
                        self.tempDictOrder[orderproduct] += orderquantity
                        if orderquantity>0 and orderquantity<6: # If order quantity is invalid, dont allocate it or backorder it

                            if self.inventory.items[orderproduct]<orderquantity: # If inventory  is less than quantity ordered, put it in backordered queue
                                self.tempDictBackOrdered[orderproduct] = orderquantity
                            else: # If inventory is greater than quantity ordered, allocate it and subtract quantity from inventory
                                self.tempDictAllocated[orderproduct] = orderquantity
                                self.inventory.items[orderproduct] -=  orderquantity

                    self.headers.append(self.tempheader)
                    self.orders.append(self.tempDictOrder)
                    self.ordersAllocated.append(self.tempDictAllocated)
                    self.ordersBackOrdered.append(self.tempDictBackOrdered)
                    self.counter += 1



                # If inventory got over, return the total list of orders processed and the headers
        return [self.headers,self.orders,self.ordersAllocated,self.ordersBackOrdered]







