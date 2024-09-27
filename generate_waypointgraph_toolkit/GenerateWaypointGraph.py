import json
import logging
from WaypointGraphModel import WaypointGraph
from VectorModel import Vector
from tools import loadFile
defaultSpacing=4
fileLocation="waypoint_graph.json"
startIndex=0

def calculatedDistanceAndRemaingSpacingDistanceBetweenNodes(x1:float,x2:float,defaultSpacing:float):
    distance=abs(x1-x2)
    remains=(distance%defaultSpacing)/2
    return distance,remains



def addEdgeBetweenNodes(nodeA:int, nodeB:int, edges):
    if(nodeA not in edges):
        edges[nodeA]=[]
    if (nodeB not in edges):
        edges[nodeB] = []

    if(nodeB not in edges[nodeA]):
        edges[nodeA].append(nodeB)

    if (nodeA not in edges[nodeB]):
        edges[nodeB].append(nodeA)
    return edges


def addIntermediateNodes():


def generateStraightLineGraph(startVector:Vector,endVector:Vector,defaultSpacing:float,side:str,incremantal:str,startingKey:int,edges):
    ##always start from small
    nodeLocations=[]
    incremants=1

    tempVector = startVector
    tempKey = startingKey
    if(incremantal=="-"):
        incremants=-1

    if (side == "y"):
        distance,remains=calculatedDistanceAndRemaingSpacingDistanceBetweenNodes(startVector.y,endVector.y,defaultSpacing)

        intermediateNodeCount=int(distance//defaultSpacing)
        if(intermediateNodeCount>1):
            tempVector.y +=remains*incremants
            nodeLocations.append(tempVector.toListWithZ())


            for i in range(1,intermediateNodeCount+1,1):
                tempVector.y+=defaultSpacing*incremants
                nodeLocations.append(tempVector.toListWithZ())
                edges=addEdgeBetweenNodes(tempKey,tempKey+1,edges)
                tempKey+=1

            tempVector.y +=remains*incremants
            nodeLocations.append(tempVector.toListWithZ())
            edges=addEdgeBetweenNodes(tempKey, tempKey+1,edges)
            tempKey += 1

        elif(intermediateNodeCount==1):
            incremants=distance/2
            tempVector.y+=remains*incremants
            nodeLocations.append(tempVector.toListWithZ())

            edges = addEdgeBetweenNodes(tempKey, tempKey + 1, edges)
            tempKey += 1
            edges = addEdgeBetweenNodes(tempKey, tempKey+1, edges)

        print(nodeLocations)
    elif(side=="x"):
        distance,remains=calculatedDistanceAndRemaingSpacingDistanceBetweenNodes(startVector.x,endVector.x,defaultSpacing)

        intermediateNodeCount=int(distance//defaultSpacing)
        if(intermediateNodeCount>1):

            tempVector.x +=remains*incremants
            nodeLocations.append(tempVector.toListWithZ())



            for i in range(1,intermediateNodeCount+1,1):
                tempVector.x+=defaultSpacing*incremants
                nodeLocations.append(tempVector.toListWithZ())
                edges=addEdgeBetweenNodes(tempKey,tempKey+1,edges)
                tempKey+=1

            tempVector.x +=remains*incremants
            nodeLocations.append(tempVector.toListWithZ())
            edges=addEdgeBetweenNodes(tempKey, tempKey+1,edges)
            tempKey += 1
        elif(intermediateNodeCount==1):
            incremants = distance / 2
            tempVector.y += remains * incremants
            nodeLocations.append(tempVector.toListWithZ())
            tempKey = startingKey
            edges = addEdgeBetweenNodes(tempKey, tempKey + 1, edges)
            tempKey += 1
            edges = addEdgeBetweenNodes(tempKey, tempKey + 1, edges)


    else:
        logging.error("You have something wrong in your brain, isnt it? cause you keyin wrong infos")

    return nodeLocations,edges

def generateRectangleGraph(bottomLeft:Vector,bottomRight:Vector,topRight:Vector,topLeft:Vector,startIndex:int)->WaypointGraph:
    edges={}
    #1
    nodeLocations,edges=generateStraightLineGraph(bottomLeft, bottomRight,defaultSpacing,"x","+",startIndex,edges)
    #2
    newNodeLocations, edges = generateStraightLineGraph(bottomRight, topRight, defaultSpacing, "y", "+", len(edges.keys())-1+startIndex,edges)
    nodeLocations+=newNodeLocations[1:]

    #3
    newNodeLocations, edges = generateStraightLineGraph(topRight, topLeft, defaultSpacing, "x", "-",
                                                        len(edges.keys()) - 1+startIndex, edges)
    nodeLocations+=newNodeLocations[1:]

    #4
    newNodeLocations, edges = generateStraightLineGraph(topLeft, bottomLeft, defaultSpacing, "y", "-",
                                                        len(edges.keys()) - 1+startIndex, edges)
    nodeLocations+=newNodeLocations[1:]
    #connect the last one to og
    edges=addEdgeBetweenNodes(0,len(nodeLocations)-1,edges)

    rectangleGraph = WaypointGraph(edges, nodeLocations)

    return rectangleGraph



def convertFromWaypointGraphToJSON(waypoint:WaypointGraph,exportlocation:str):
    graphJSON={}
    for key,value in waypoint.graph.items():
        graphJSON[str(key)]={"edges":value}
    data={"node_locations":waypoint.nodeLocations,"graph":graphJSON}
    json_object = json.dumps(data, indent=2)

    # Writing to sample.json
    with open(exportlocation, "w") as outfile:
        outfile.write(json_object)


def loadCoord():
    commandlocation="R1C1.txt"
    filedata=loadFile(commandlocation).readlines()

    #for line in filedata:
        #line.split(" ")

    return bottomLeft,bottomRight,topRight,topLeft


def main():
    bottomLeft=Vector(195,-86)
    bottomRight=Vector(216,-86)
    topRight=Vector(216,-80)
    topLeft=Vector(195,-80)
    rectangleGraph=generateRectangleGraph(bottomLeft,bottomRight,topRight,topLeft,startIndex)
    convertFromWaypointGraphToJSON(rectangleGraph,fileLocation)


main()