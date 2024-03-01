import json

with open("ethereum.json", "r") as file:
    data = json.load(file)


poly_project = [project for project in data["Projects"] if project["Chain"] == "Polygon"]

poly_data = {"Project": poly_project}

with open("polygon.json", "w") as file2:
    json.dump(poly_data, file2, indent=3)

