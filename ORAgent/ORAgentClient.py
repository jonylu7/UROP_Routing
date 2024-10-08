import json
import ConvertDataFormat
import OR
import ORExport
import Init
graph_file_location= "./og_data/waypoint_graph.json"
orders_file_location= "./og_data/orders_data.json"
vehicle_file_location="./og_data/vehicle_data.json"
export_file_location="./og_data/OR_response.json"

def runORAgent(graph_file_location,orders_file_location,vehicle_file_location,export_file_location):
    Init.initClient()
    ##preprocess
    offsets,edges,weights,orders=ConvertDataFormat.preprocess(graph_file_location,orders_file_location)

    costmatrix,pathmatrix=ConvertDataFormat.generateMatrix(offsets,edges,weights)


    solution,totalCost=OR.solveTSP(costmatrix,orders)
    solutionPath=OR.generateSolution(pathmatrix, solution)
    ORExport.exportFormat(solutionPath,totalCost,export_file_location)
    ##costmatrix as argument

if __name__=="__main__":
    runORAgent(graph_file_location,orders_file_location,vehicle_file_location,export_file_location)