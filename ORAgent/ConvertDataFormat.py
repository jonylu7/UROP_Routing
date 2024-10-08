import json
import numpy as np
import FindPath

def loadFile(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def convertGraphFileToCSR(graphfile):

    num_nodes = len(graphfile["graph"])

    offsets = []
    edges = []

    cur_offset = 0
    for node in range(num_nodes):
        offsets.append(cur_offset)
        cur_offset += len(graphfile["graph"][str(node)]["edges"])
        edges = edges + graphfile["graph"][str(node)]["edges"]

    offsets.append(cur_offset)
    return np.array(offsets), np.array(edges)

def generateMatrix(offsets,edges,weights):
    graph=FindPath.convertFromCSRToDijGraph(offsets,edges,weights)

    costmatrix,pathmatrix=FindPath.findAllShortestPath(graph)
    return costmatrix,pathmatrix


def calculateDistance(location1,location2):
    return((location1[0]-location2[0])**2+(location1[1]-location2[1])**2+(location1[2]-location2[2])**2)**0.5

def calculateGraphWeight(graphfile):
    weights=[]
    for startnode in graphfile["graph"]:
        for endnode in graphfile["graph"][startnode]["edges"]:
            startlocation=graphfile["node_locations"][int(startnode)]
            endlocation=graphfile["node_locations"][int(endnode)]
            weights.append(calculateDistance(startlocation,endlocation))
    return weights

def findOrderRelativeToNodeIndex(orderlocation,graphFile):
    for index,nodeLocation in enumerate(graphFile["node_locations"]):
        if(abs(nodeLocation[0]-orderlocation[0])<1 and abs(nodeLocation[1]-orderlocation[1])<1 and abs(nodeLocation[2]-orderlocation[2])<1):
            return index


def convertOrdersData(ordersdata,graphFile):
    orders=[]
    for orderlocation in ordersdata["task_locations"]:
        index=findOrderRelativeToNodeIndex(orderlocation,graphFile)
        orders.append(index)
    return orders


def convertGraphData(graphfile):
    offsets, edges = convertGraphFileToCSR(graphfile)
    weights=calculateGraphWeight(graphfile)
    return offsets, edges, weights


def preprocess(graphfilelocation,ordersfilelocation):
    graphFile = loadFile(graphfilelocation)
    offsets, edges, weights=convertGraphData(graphFile)


    ordersLocation = loadFile(ordersfilelocation)
    orders = convertOrdersData(ordersLocation,graphFile)
    ## start from zero
    orders.insert(0,0)

    return offsets, edges, weights,orders




