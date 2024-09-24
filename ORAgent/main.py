import json
import ConvertDataFormat
import OR
import ORExport
graph_file_location= "./og_data/waypoint_graph.json"
orders_file_location= "./og_data/orders_data.json"
vehicle_file_location="./og_data/vehicle_data.json"
export_file_location="./og_data/OR_response.json"

def runORAgent():
    ##preprocess
    offsets,edges,weights,orders=ConvertDataFormat.preprocess(graph_file_location,orders_file_location)

    costmatrix,pathmatrix=ConvertDataFormat.generateMatrix(offsets,edges,weights)


    solution,totalCost=OR.solveTSP(costmatrix,orders)
    solutionPath=OR.generateSolutionPath(pathmatrix,solution)
    ORExport.exportFormat(solutionPath,totalCost,export_file_location)
    ##costmatrix as argument


if __name__=="__main__":
    runORAgent()