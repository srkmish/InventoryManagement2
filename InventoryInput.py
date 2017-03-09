from PyQt5 import QtWidgets


class InventoryInputDialog(QtWidgets.QDialog):
    def __init__(self, inventory):

        QtWidgets.QWidget.__init__(self, None)
        self.inventory = inventory
        self.gridLayout = QtWidgets.QGridLayout()
        self.labelQtyA = QtWidgets.QLabel("Quantity A")
        self.labelQtyB = QtWidgets.QLabel("Quantity B")
        self.labelQtyC = QtWidgets.QLabel("Quantity C")
        self.labelQtyD = QtWidgets.QLabel("Quantity D")
        self.labelQtyE = QtWidgets.QLabel("Quantity E")
        self.editA = QtWidgets.QLineEdit()
        self.editB = QtWidgets.QLineEdit()
        self.editC = QtWidgets.QLineEdit()
        self.editD = QtWidgets.QLineEdit()
        self.editE = QtWidgets.QLineEdit()
        self.enterBtn = QtWidgets.QPushButton("Enter")
        self.gridLayout.addWidget(self.labelQtyA, 1, 0)
        self.gridLayout.addWidget(self.editA, 1, 1)
        self.gridLayout.addWidget(self.labelQtyB, 2, 0)
        self.gridLayout.addWidget(self.editB, 2, 1)
        self.gridLayout.addWidget(self.labelQtyC, 3, 0)
        self.gridLayout.addWidget(self.editC, 3, 1)
        self.gridLayout.addWidget(self.labelQtyD, 4, 0)
        self.gridLayout.addWidget(self.editD, 4, 1)
        self.gridLayout.addWidget(self.labelQtyE, 5, 0)
        self.gridLayout.addWidget(self.editE, 5, 1)
        self.gridLayout.addWidget(self.enterBtn, 6, 1)
        self.setLayout(self.gridLayout)
        self.setWindowTitle("Enter Initial Inventory Quantities")
        self.enterBtn.clicked.connect(self.setInventory)

    def setInventory(self):
        if self.editA.text().isdigit() and self.editB.text().isdigit() and self.editC.text().isdigit() and self.editD.text().isdigit() and self.editE.text().isdigit():
            self.inventory.items = {'A': int(self.editA.text()), 'B': int(self.editB.text()),
                                    'C': int(self.editC.text()), 'D': int(self.editD.text()),
                                    'E': int(self.editE.text())}
            self.close()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please enter integer values in all the fields")
            msg.setWindowTitle("Alert")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
