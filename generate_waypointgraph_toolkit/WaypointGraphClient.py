from tools import loadFile,loadJSONFile,saveFile
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
    fromfileLocation = list(lines[lineIndex].split(" "))[1]
    lineIndex += 1

    ##path
    intofileLocation = list(lines[lineIndex].split(" "))[1]
    lineIndex += 1

    ##path
    savefileLocation = list(lines[lineIndex].split(" "))[1]
    lineIndex += 1
    fromFile=loadJSONFile(fromfileLocation)
    intoFile=loadJSONFile(intofileLocation)


    filedata=mergeWaypointGraphs(intoFile,fromFile)
    saveFile(filedata, "", savefileLocation)

def main():
    lines=[]
    with open(filelocation, "r") as filedata:
        lines = [line.rstrip() for line in filedata]

    currentMode=InputMode.Nothing
    lineIndex=0
    while(lineIndex<len(lines)):
        if (currentMode == InputMode.Nothing):
            currentMode = loadInputMode(lines[lineIndex])
            print(lines[lineIndex])
            lineIndex += 1

        if (currentMode == InputMode.GenerateRectangle):
            generateRectangle(lines,lineIndex)
            lineIndex+=6
        elif(currentMode==InputMode.Merge):
            merge(lines,lineIndex)
            lineIndex+=3
        elif(currentMode==InputMode.Quit):
            exit()

        #reset every round
        currentMode = InputMode.Nothing



main()