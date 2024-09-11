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


def calculateGraphWeight(graphfile):
    return


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
    orders = convertOrdersData(ordersLocation,)

    return offsets, edges, weights




