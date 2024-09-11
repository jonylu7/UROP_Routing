import json
import ConvertDataFormat
import OR
graph_file_location="preprocess_data/weighted_graph.json"
orders_file_location="preprocess_data/orders_dataset.json"

def main():
    graphData=ConvertDataFormat.loadFile(graph_file_location)
    offsets,edges,weights=ConvertDataFormat.convertGraphToCSR(graphData)

    ordersData=ConvertDataFormat.loadFile(orders_file_location)
    orders=ConvertDataFormat.convertOrdersData(ordersData)

    costmatrix=ConvertDataFormat.generateCostMatrix(offsets,edges,weights)


    solution=OR.solveTSP(costmatrix,orders)
    print(solution)
    ##costmatrix as argument


if __name__=="__main__":
    main()