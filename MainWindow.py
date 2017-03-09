from PyQt5 import QtWidgets

from Model import SimpleTableModel
from InventoryAllocator import Allocator
from InventoryInput import InventoryInputDialog


class MyMainWindow(QtWidgets.QWidget):
    def __init__(self, orderList, datasource, allocator, inventory):
        QtWidgets.QWidget.__init__(self, None)

        # create a grid layout to arrange items
        self.gridLayout = QtWidgets.QGridLayout()

        # Create a pandas dataframe to be displayed in table view. Initially it is empty
        self.m = SimpleTableModel(orderList)

        self.allocator = allocator
        self.datasource = datasource
        self.inventory = inventory
        self.counter = 0
        # Create the view and attach model to it
        self.v = QtWidgets.QTableView()
        self.v.setModel(self.m)
        self.v.verticalHeader().hide()
        self.gridLayout.addWidget(self.v, 1, 0, 1, 16)

        self.labelQtyA = QtWidgets.QLabel("Quantity A")
        self.labelQtyB = QtWidgets.QLabel("Quantity B")
        self.labelQtyC = QtWidgets.QLabel("Quantity C")
        self.labelQtyD = QtWidgets.QLabel("Quantity D")
        self.labelQtyE = QtWidgets.QLabel("Quantity E")

        self.labelInvA = QtWidgets.QLabel("Inventory A: " + str(self.getInventory('A')))
        self.labelInvB = QtWidgets.QLabel("Inventory B: " + str(self.getInventory('B')))
        self.labelInvC = QtWidgets.QLabel("Inventory C: " + str(self.getInventory('C')))
        self.labelInvD = QtWidgets.QLabel("Inventory D: " + str(self.getInventory('D')))
        self.labelInvE = QtWidgets.QLabel("Inventory E: " + str(self.getInventory('E')))

        self.editA = QtWidgets.QLineEdit()
        self.editB = QtWidgets.QLineEdit()
        self.editC = QtWidgets.QLineEdit()
        self.editD = QtWidgets.QLineEdit()
        self.editE = QtWidgets.QLineEdit()

        self.labels = [self.labelQtyA, self.labelQtyB, self.labelQtyC, self.labelQtyD, self.labelQtyE]
        self.labelsInv = [self.labelInvA, self.labelInvB, self.labelInvC, self.labelInvD, self.labelInvE]
        self.editBoxes = [self.editA, self.editB, self.editC, self.editD, self.editE]

        for i in range(5):
            self.gridLayout.addWidget(self.labelsInv[i], 2, i)
            self.gridLayout.addWidget(self.labels[i], 3, i)
            self.gridLayout.addWidget(self.editBoxes[i], 4, i)

        self.enterBtn = QtWidgets.QPushButton("Enter")
        self.randomBtn = QtWidgets.QPushButton("Generate Random")
        self.resetBtn = QtWidgets.QPushButton("Reset")
        # add bottom to main window layout

        self.gridLayout.addWidget(self.enterBtn, 5, 0)
        self.gridLayout.addWidget(self.randomBtn, 5, 1)
        self.gridLayout.addWidget(self.resetBtn, 5, 2)

        # set layout on the window
        self.setLayout(self.gridLayout)

        self.enterBtn.clicked.connect(self.enterValues)
        self.randomBtn.clicked.connect(self.generateRandom)
        self.resetBtn.clicked.connect(self.reset)

        # dialog = MyDialog(inventory)
        # dialog.exec_()

    def getInventory(self, type):
        return self.inventory.items[type]

    def enterValues(self):
        # Gets called when user enters input values for an order line
        # If values are valid append the order to datasource object
        if self.editA.text().isdigit() and self.editB.text().isdigit() and self.editC.text().isdigit() and self.editD.text().isdigit() and self.editE.text().isdigit():
            self.datasource.orderStreams.append(
                {"Header": self.counter + 1, "Lines": [{"Product": "A", "Quantity": int(self.editA.text())},
                                                       {"Product": "B", "Quantity": int(self.editB.text())},
                                                       {"Product": "C", "Quantity": int(self.editC.text())},
                                                       {"Product": "D", "Quantity": int(self.editD.text())},
                                                       {"Product": "E", "Quantity": int(self.editE.text())}]})
            self.counter += 1
            self.processData()

        else:
            # If order is not valid, display popup box saying the same
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please enter integer values in all the fields")
            msg.setWindowTitle("Alert")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def generateRandom(self):
        self.datasource.generateRandomData(len(self.m.df))
        self.processData()

    def setInventoryLabels(self):
        self.labelInvA.setText("Inventory A: " + str(self.getInventory('A')))
        self.labelInvB.setText("Inventory B: " + str(self.getInventory('B')))
        self.labelInvC.setText("Inventory C: " + str(self.getInventory('C')))
        self.labelInvD.setText("Inventory D: " + str(self.getInventory('D')))
        self.labelInvE.setText("Inventory E: " + str(self.getInventory('E')))

    def processData(self):
        # Get the processed data from Allocator object
        orderList = self.allocator.allocateOrders()
        # Build a new Model based on the processed data and attach it to view
        self.m = SimpleTableModel(orderList)
        self.v.setModel(self.m)
        # IF inventory is over , disable the input textboxes
        if (self.inventory.isInventoryOver()):
            for editBox in self.editBoxes:
                editBox.setDisabled(True)
        self.setInventoryLabels()

    # This method gets called when user presses reset button
    def reset(self):
        # Reset the data in datasource object
        self.datasource.resetData()

        for editBox in self.editBoxes:
            editBox.setEnabled(True)
            editBox.clear()
        self.counter = 0

        # Ask again for initial inventory
        dialog = InventoryInputDialog(self.inventory)
        dialog.exec_()
        # Ask whether user wants the backordered items processed
        result = QtWidgets.QMessageBox.question(self, 'Question',
                                                "Would you like to process orders in Backordered Queue?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            # Check for the items in backordered queue and process those lines
            # which have atleast one order by adding it to datasource object
            for backorderedDict in self.allocator.ordersBackOrdered:
                if sum(backorderedDict.values()) > 0:
                    print(backorderedDict)
                    self.datasource.orderStreams.append(
                        {"Header": self.counter + 1, "Lines": [{"Product": "A", "Quantity": backorderedDict['A']},
                                                               {"Product": "B", "Quantity": backorderedDict['B']},
                                                               {"Product": "C", "Quantity": backorderedDict['C']},
                                                               {"Product": "D", "Quantity": backorderedDict['D']},
                                                               {"Product": "E", "Quantity": backorderedDict['E']}]})
                    self.counter += 1

        self.allocator = Allocator(self.datasource, self.inventory)
        # Create orderlist from allocator object and create model from it
        # Attach the model to view
        orderList = self.allocator.allocateOrders()
        print(orderList)
        self.m = SimpleTableModel(orderList)
        self.v.setModel(self.m)
        self.setInventoryLabels()
