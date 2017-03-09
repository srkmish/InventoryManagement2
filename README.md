# InventoryManagement2

In order to run this software, you must have Pandas and Pyqt5 installed.

This software is built for managing inventory. Upon initial loading, you will be prompted with a screen to enter inventory values for each
product type. Once done, you will get to the main screen of the application where there is a table view for displaying each order line in 
a separate row with details containing the orders Processed, the order Allocated and the order backordered for each line. Any order quantity
which does not fall in range of 1-5 will be ignored and not processed. The user gets to enter the order quantities for each product type and presses on the enter button to display it in the table view. The inventory quantites displayed get updated automatically. The software can also simulate the orders by clicking on the Generate Random orders button. This randomly generates a quantity for each order type from range 0-7 (where 0,6,7 are invalid and 1-5 is valid). The orders get processed until the inventory gets exhausted. At this point, the text boxes get disabled so that the user cannot enter more orders.

If the user wishes to reset the application, he can do so by clicking on reset button. This again promps the user to enter new inventory 
quantities. The user is further prompted with a dialog asking whether he/she wishes to process the orders in backordered queue. If the user
presses yes, the backlog is processed and displayed and then the user can enter new order values.

Initial Inventory Input Screen:

![Image](https://github.com/srkmish/InventoryManagement2/blob/master/1.png)

Main Screen to enter values for orders:

![Image](https://github.com/srkmish/InventoryManagement2/blob/master/2.png)

Orders updated after pressing generate random button:

![Image](https://github.com/srkmish/InventoryManagement2/blob/master/3.png)

After pressing reset button:

![Image](https://github.com/srkmish/InventoryManagement2/blob/master/4.png)

After pressing option for processing backordered queues:

![Image](https://github.com/srkmish/InventoryManagement2/blob/master/5.png)





