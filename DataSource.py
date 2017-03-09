# This class is responsible for creating a datasource object
from random import randint

class DataSource(object):

    def __init__(self):
        # The order stream is a list of unique order streams with each stream containing
        # header and lines as key. Line is a list of orders represented as dictionary
        # The quantity generated for each product in the line could be any integer randomly from 0 - 7 where 1 -5 is valid order and 0,6,7 are invalid
        self.orderStreams = []


    def returnData(self):
        return self.orderStreams

    def generateRandomData(self,length):

        for i in range(length,200):  # Dummy number which ensures that datasource gets allocated completely and results are printed
            self.orderStreams.append({"Header": i + 1, "Lines": [{"Product": "A", "Quantity": randint(0, 7)},
                                                                 {"Product": "B", "Quantity": randint(0, 7)},
                                                                 {"Product": "C", "Quantity": randint(0, 7)},
                                                                 {"Product": "D", "Quantity": randint(0, 7)},
                                                                 {"Product": "E", "Quantity": randint(0, 7)}]})


    def resetData(self):
        self.orderStreams = []
