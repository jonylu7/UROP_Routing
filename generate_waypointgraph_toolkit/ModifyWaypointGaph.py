
filelocation="waypoint_graph.json"
import json
from VectorModel import Vector
from tools import loadJSONFile,saveFile

def modifyNodeLocation(filedata,whichnode:int,newlocations:Vector):
    filedata["node_locations"][whichnode]=newlocations.toListWithZ()
    return filedata


def connectNode(filedata,nodeA:int,nodeB:int):
    if nodeB not in filedata["graph"][str(nodeA)]["edges"]:
        filedata["graph"][str(nodeA)]["edges"].append(nodeB)
    if nodeA not in filedata["graph"][str(nodeB)]["edges"]:
        filedata["graph"][str(nodeB)]["edges"].append(nodeA)
    return filedata


def addNewNodeAndConnectToPrevNode(filedata,newnodelocation:Vector,prevnode:int):
    filedata["node_locations"].append(newnodelocation.toListWithZ())

    newNodeIndex=len(filedata["node_locations"])-1
    filedata["graph"][str(newNodeIndex)]={"edges":[prevnode]}
    filedata=connectNode(filedata,prevnode,newNodeIndex)
    return filedata

def mergeWaypointGraphs(mergetofile,mergefromfile):

    return

def duplicateWaypointGraphs(filedata,relocatebottomleft):


def main():
    filedata=loadJSONFile(filelocation)
    ##connect to source
    filedata=connectNode(filedata,16,0)
    ##connect intermid right
    filedata=addNewNodeAndConnectToPrevNode(filedata,Vector(216,-248.5),10)
    filedata=connectNode(filedata,len(filedata["node_locations"])-1,3)
    ##connect intermid left
    filedata = addNewNodeAndConnectToPrevNode(filedata, Vector(212, -248.5), 11)
    filedata = connectNode(filedata, len(filedata["node_locations"]) - 1, 2)
    ##connect intermid right left
    filedata = connectNode(filedata, 17, 18)
    filedata = connectNode(filedata, 10, 18)
    filedata = connectNode(filedata, 11, 17)
    filedata = connectNode(filedata, 2, 17)
    filedata = connectNode(filedata, 18, 3)

    filedata=modifyNodeLocation(filedata,15,Vector(204, -248.5))
    filedata = modifyNodeLocation(filedata, 7, Vector(224, -248.5))

    saveFile(filelocation,"_modify_1",filedata)







main()