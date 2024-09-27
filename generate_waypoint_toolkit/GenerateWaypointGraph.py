import json
import logging
from WaypointGraphModel import WaypointGraph
from VectorModel import Vector
defaultSpacing=4
fileLocation="waypoint_graph.json"
startIndex=0

def calculatedDistanceAndRemaingSpacingDistanceBetweenNodes(x1:float,x2:float,defaultSpacing:float):
    distance=abs(x1-x2)
    remains=(distance%defaultSpacing)/2
    return distance,remains



def addEdgeBetweenNodes(nodeA:int,nodeB:int,graph):
    if(nodeA not in graph):
        graph[nodeA]=[]
    if (nodeB not in graph):
        graph[nodeB] = []

    if(nodeB not in graph[nodeA]):
        graph[nodeA].append(nodeB)

    if (nodeA not in graph[nodeB]):
        graph[nodeB].append(nodeA)
    return graph


def generateStraightLineGraph(startVector:Vector,endVector:Vector,defaultSpacing:float,side:str,incremantal:str,startingKey:int,edges):
    ##always start from small
    nodeLocations=[]
    incremants=1
    if(incremantal=="-"):
        incremants=-1

    if (side == "y"):
        distance,remains=calculatedDistanceAndRemaingSpacingDistanceBetweenNodes(startVector.y,endVector.y,defaultSpacing)

        itermediateNodeCount=int(distance//defaultSpacing)


        tempVector=startVector

        tempVector.y +=remains*incremants
        nodeLocations.append(tempVector.toListWithZ())
        tempKey=startingKey


        for i in range(1,itermediateNodeCount+1,1):
            tempVector.y+=defaultSpacing*incremants
            nodeLocations.append(tempVector.toListWithZ())
            edges=addEdgeBetweenNodes(tempKey,tempKey+1,edges)
            tempKey+=1

        tempVector.y +=remains*incremants
        nodeLocations.append(tempVector.toListWithZ())
        edges=addEdgeBetweenNodes(tempKey, tempKey+1,edges)
        tempKey += 1
        print(nodeLocations)
    elif(side=="x"):
        distance,remains=calculatedDistanceAndRemaingSpacingDistanceBetweenNodes(startVector.x,endVector.x,defaultSpacing)

        itermediateNodeCount=int(distance//defaultSpacing)


        tempVector=startVector

        tempVector.x +=remains*incremants
        nodeLocations.append(tempVector.toListWithZ())
        tempKey=startingKey


        for i in range(1,itermediateNodeCount+1,1):
            tempVector.x+=defaultSpacing*incremants
            nodeLocations.append(tempVector.toListWithZ())
            edges=addEdgeBetweenNodes(tempKey,tempKey+1,edges)
            tempKey+=1

        tempVector.x +=remains*incremants
        nodeLocations.append(tempVector.toListWithZ())
        edges=addEdgeBetweenNodes(tempKey, tempKey+1,edges)
        tempKey += 1

    else:
        logging.error("You have something wrong in your brain, isnt it? cause you keyin wrong infos")

    return nodeLocations,edges

def generateRectangleGraph(lowerLeft:Vector,lowerRight:Vector,topRight:Vector,topLeft:Vector,startIndex:int)->WaypointGraph:
    edges={}
    #1
    nodeLocations,edges=generateStraightLineGraph(lowerLeft, lowerRight,defaultSpacing,"x","+",startIndex,edges)
    #2
    newNodeLocations, edges = generateStraightLineGraph(lowerRight, topRight, defaultSpacing, "y", "+", len(edges.keys())-1+startIndex,edges)
    nodeLocations+=newNodeLocations[1:]

    #3
    newNodeLocations, edges = generateStraightLineGraph(topRight, topLeft, defaultSpacing, "x", "-",
                                                        len(edges.keys()) - 1+startIndex, edges)
    nodeLocations+=newNodeLocations[1:]

    #4
    newNodeLocations, edges = generateStraightLineGraph(topLeft, lowerLeft, defaultSpacing, "y", "-",
                                                        len(edges.keys()) - 1+startIndex, edges)
    nodeLocations+=newNodeLocations[1:]
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
    return lowerLeft,lowerRight,topRight,topLeft


def main():
    lowerLeft=Vector(204,-252)
    lowerRight=Vector(224,-252)
    topRight=Vector(224,-245)
    topLeft=Vector(204,-245)
    rectangleGraph=generateRectangleGraph(lowerLeft,lowerRight,topRight,topLeft,startIndex)
    convertFromWaypointGraphToJSON(rectangleGraph,fileLocation)


main()