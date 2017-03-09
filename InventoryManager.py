
from PyQt5 import QtWidgets


import sys
from Inventory import Inventory
from InventoryAllocator import Allocator
from DataSource import DataSource
from InventoryInput import InventoryInputDialog
from MainWindow import MyMainWindow


# set things up, and run it. :)
if __name__ == '__main__':
    inventoryList = {'A': 150, 'B': 150, 'C': 100, 'D': 100, 'E': 200}  # Dummy inventory List
    inventory = Inventory(inventoryList)
    # Get Datasource object which initially creates blank data
    datasource = DataSource()
    allocator = Allocator(datasource,inventory)
    # The order list will be initially empty and will get filled up as the user enters the order
    # quantities in the GUI Screen
    orderList = allocator.allocateOrders()
    app = QtWidgets.QApplication(sys.argv)
    # This invokes the input for initial Inventory which upon success invokes main window as below
    dialog = InventoryInputDialog(inventory)
    dialog.exec_()

    # Invoke the main window
    w = MyMainWindow(orderList,datasource,allocator,inventory)
    w.show()
    app.exec_()
    sys.exit()