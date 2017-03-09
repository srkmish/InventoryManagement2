from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import pandas as pd
import numpy as np

class SimpleTableModel(QtCore.QAbstractTableModel):
 def __init__(self, orderList):
    QtCore.QAbstractTableModel.__init__(self)

  # Cache the passed data list as a class member.


    columns = ['Header', 'Qty A', 'Qty B', 'Qty C', 'Qty D', 'Qty E', 'Alloc A', 'Alloc B', 'Alloc C', 'Alloc D', 'Alloc E',
                 'BO-A', 'BO-B', 'BO-C', 'BO-D', 'BO-E']
    self.df = pd.DataFrame(columns = columns)
    self.headerData = columns






    if (orderList):
          self.headers, self.orders, self.ordersAllocated, self.ordersBackOrdered = orderList
          for i in range(len(self.headers)):

              self.df.loc[i,['Header']] = self.headers[i]
              self.df.loc[i,['Qty A']],self.df.loc[i,['Qty B']],self.df.loc[i,['Qty C']],self.df.loc[i,['Qty D']],self.df.loc[i,['Qty E']] = self.orders[i].values()
              self.df.loc[i, ['Alloc A']], self.df.loc[i, ['Alloc B']], self.df.loc[i, ['Alloc C']], self.df.loc[i, ['Alloc D']], self.df.loc[i, ['Alloc E']] = \
              self.ordersAllocated[i].values()
              self.df.loc[i, ['BO-A']], self.df.loc[i, ['BO-B']], self.df.loc[i, ['BO-C']], self.df.loc[i, ['BO-D']], self.df.loc[i, ['BO-E']] = \
              self.ordersBackOrdered[i].values()

    #print(self.df)







 def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.df) # Returns the nunmber of headers

 def columnCount(self, parent=QtCore.QModelIndex()):
        return 16


 def data(self, index, role = QtCore.Qt.DisplayRole):
       if role == QtCore.Qt.DisplayRole:
       # The view is asking for the actual data, so, just return the item it's asking for.
        return self.df.iloc[index.row(),index.column()]
 def headerData(self, col, Qt_Orientation, role=None):
     if Qt_Orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
         return self.headerData[col]

 # def headerData(self, p_int, Qt_Orientation, role=None):
 #     if(Qt_Orientation=='Horizontal' and role == QtCore.Qt.DisplayRole):
 #


