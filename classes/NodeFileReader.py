"""This class will read in nodes from our special node file 
and store. It will also provide easy access to the nodes
for later.
"""

from classes import Node

class NodeFileReader():
    """This class will hold the graphs/filename and when called will 
    read the entire file to create a dictionary of nodes that we can use.
    """

    def __init__(self, nodeFilename):
        """Takes in a filename of a node file from the graphs/ folder.
        
        :param self: This.
        :param nodeFilename: Filename of our special node file
        """   
        self.filename = nodeFilename
        self.nodes = dict()

    def read(self):
        """Reads the file and creates a dictionary of nodes, adding one
        every 4 lines. Pretty simple loop through every 4 lines of node
        data.
        """   
        file = open('graphs/' + self.filename, 'r')
        # Setting up variables to store things while we iterate
        i = 0
        nodeId = 0
        lat = 0
        lon = 0
        nodes = []

        for line in file:
            # Node ID #
            if i % 4 == 0:
                nodeId = line
            
            # Node GPS Coordinates
            elif i % 4 == 1:
                lat = line.split()[0]
                lon = line.split()[1]

            # List of adjacent nodes
            elif i % 4 == 2:
                nodes = line.split()

            # Last line of the node = create node
            else:
                self.nodes[nodeId] = Node.Node(nodeId, lat, lon)
                self.nodes[nodeId].setAdjacent(nodes)
                # Streets aren't in a variable
                streets = line.split('\"')
                streets.pop(0)
                streets.pop(len(streets) - 1)
                self.nodes[nodeId].setStreets(streets)

            # Increment the line counter
            i += 1

    def getNodes(self):
        """Will return the entire dictionary of nodes."""   
        return self.nodes

    def getNode(self, nodeID):
        """Will get a node reference by it's ID #.

        :param self: This.
        :param nodeID: The node ID that we want to retrieve the node of.
        """   
        return self.nodes[nodeID]