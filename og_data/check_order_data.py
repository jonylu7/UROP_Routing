
import json
def main():
    with open("orders_data.json", "r") as f:
        data=json.load(f)
    with open("waypoint_graph.json","r") as f:
        w=json.load(f)
    print(w["node_locations"][24])
    print(data["task_locations"][3])

main()