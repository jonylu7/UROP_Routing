from tools import loadFile
from VectorModel import Vector
from WaypointGraphModel import WaypointGraph
from GenerateWaypointGraph import generateRectangleGraph,convertFromWaypointGraphToJSON
from ModifyWaypointGraph import mergeWaypointGraphs
from enum import Enum
filelocation="commands_to_generate.txt"
class InputMode(Enum):
    Nothing=-1
    Quit = 0
    GenerateRectangle=1
    Merge=2

def loadInputMode(line):
    if (line == "GenerateRectangle"):
        return InputMode.GenerateRectangle
    elif(line=="Merge"):
        return InputMode.Merge
    elif(line=="Quit"):
        return InputMode.Quit
    else:
        return InputMode.Nothing

def loadVector(line):
    location=list(line.split(" "))[1]
    x=float(list(location.split(","))[0])
    y=float(list(location.split(","))[1])
    return Vector(x,y)

def generateRectangle(lines,lineIndex):
    print(lines[lineIndex])
    fileLocation=list(lines[lineIndex].split(" "))[1]
    lineIndex += 1
    bottomLeft=loadVector(lines[lineIndex])

    lineIndex += 1
    bottomRight=loadVector(lines[lineIndex])

    lineIndex += 1
    topRight=loadVector(lines[lineIndex])

    lineIndex += 1
    topLeft=loadVector(lines[lineIndex])

    rectangleGraph=generateRectangleGraph(bottomLeft,bottomRight,topRight,topLeft,0)
    convertFromWaypointGraphToJSON(rectangleGraph,fileLocation)


def merge(lines,lineIndex):
    ##path
    lineIndex += 1
    fromfileLocation = list(lines[lineIndex].split(" "))[1]

    ##path
    lineIndex += 1
    intofileLocation = list(lines[lineIndex].split(" "))[1]

    ##path
    lineIndex += 1
    savefileLocation = list(lines[lineIndex].split(" "))[1]

    fromFile=loadFileJSON(fromfileLocation)
    intoFile=loadFileJSON(intofileLocation)


    filedata=mergeWaypointGraphs(fromFile,intoFile)
    saveFile(filedata, "", savefileLocation)

def main():
    lines=[]
    with open(filelocation, "r") as filedata:
        lines = [line.rstrip() for line in filedata]

    currentMode=InputMode.Nothing
    lineIndex=0
    while(lineIndex<len(lines)):
        if (currentMode == InputMode.GenerateRectangle):
            generateRectangle(lines,lineIndex)
            lineIndex+=7
        elif(currentMode==InputMode.Merge):
            merge(lines,lineIndex)
        elif(currentMode==InputMode.Quit):
            exit()
        if(currentMode==InputMode.Nothing):
            currentMode=loadInputMode(lines[lineIndex])
            lineIndex+=1



main()