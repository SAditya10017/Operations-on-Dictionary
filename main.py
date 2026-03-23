trains = {"southern":"green","northern":"black","southwestern":"red"}
print(trains)
trains["southeastern"] = "Blue/yellow"
print(trains)
trains["southeastern"] = "Dark blue"
print(trains)
trains.pop("southern")
print(trains)