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

def generateCostMatrix(offsets,edges,weights):
    graph=FindPath.convertFromCSRToDijGraph(offsets,edges,weights)

    costmatrix=FindPath.findAllShortestPath(graph)
    return costmatrix


def calculateDistance(location1,location2):
    return((location1[0]-location2[0])**2+(location1[1]-location2[1])**2+(location1[2]-location2[2])**2)**0.5

def calculateGraphWeight(graphfile):
    weights=[]
    for startnode in graphfile["graph"]:
        for endnode in graphfile["graph"][startnode]:
            startlocation=graphfile["node_locations"]][int(startnode)]
            endlocation=graphfile["node_locations"]][int(endnode)]
            weights.append(calculateDistance(startlocation,endlocation))
    return weights


def convertOrdersData(ordersdata):
    return ordersdata["task_locations"]


def convertGraphData(graphfile):
    offsets, edges = convertGraphFileToCSR(graphfile)
    weights=calculateGraphWeight(graphfile)
    return offsets, edges, weights


def preprocess(graphfilelocation,ordersfilelocation):
    graphFile = loadFile(graphfilelocation)
    offsets, edges, weights=convertGraphData(graphFile)


    ordersLocation = loadFile(ordersfilelocation)
    ##orders = convertOrdersData(ordersLocation,)

    return offsets, edges, weights




