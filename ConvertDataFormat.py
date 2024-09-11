import json
import numpy as np
import FindPath

def loadFile(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def convertGraphToCSR(graphdata):

    num_nodes = len(graphdata)

    offsets = []
    edges = []
    weights = []

    cur_offset = 0
    for node in range(num_nodes):
        offsets.append(cur_offset)
        cur_offset += len(graphdata[str(node)]["edges"])

        edges = edges + graphdata[str(node)]["edges"]
        weights = weights + graphdata[str(node)]["weights"]

    offsets.append(cur_offset)
    return np.array(offsets), np.array(edges), np.array(weights)

def generateCostMatrix(offsets,edges,weights):
    graph=FindPath.convertFromCSRToDijGraph(offsets,edges,weights)

    costmatrix=FindPath.findAllShortestPath(graph)
    print(costmatrix)
    return costmatrix


def convertOrdersData(ordersdata):
    return ordersdata["task_locations"]




