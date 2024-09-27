def loadFile(filelocation):
    with open(filelocation, "r") as f:
        return f

def loadJSONFile(filelocation):
    with open(filelocation,"r") as f:
        return json.load(f)

def saveFile(filelocation,postfix,filedata):
    nameAndLocation=filelocation[:-4]
    jsondata=json.dumps(filedata,indent=2)
    with open(nameAndLocation+postfix+".json", "w") as outfile:
        outfile.write(jsondata)