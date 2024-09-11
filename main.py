import json
import ConvertDataFormat
import OR
graph_file_location= "og_data/waypoint_graph.json"
orders_file_location= "og_data/orders_data.json"
vehicle_file_location="og_data/vehicle_data.json"

def main():
    ##preprocess
    offsets,edges,weights=ConvertDataFormat.preprocess(graph_file_location,orders_file_location)

    ##
    costmatrix=ConvertDataFormat.generateCostMatrix(offsets,edges,weights)


    solution=OR.solveTSP(costmatrix,orders)
    print(solution)
    ##costmatrix as argument


if __name__=="__main__":
    main()