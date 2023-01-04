import os
import json


with open(f'{os.getcwd()}/Instructions.json', 'r') as f:
    data = json.load(f)

hooverEndInfo = {"coords": 0,
                 "patches": 0}
print(data)


def hooverInstructions(coordinateX, coordinateY, instruction):
    if 0 < data.get("coords")[0] < data.get("roomSize")[0]:
        data.get("coords")[0] = data.get("coords")[0] + coordinateX
    if 0 < data.get("coords")[1] < data.get("roomSize")[1]:
        data.get("coords")[1] = data.get("coords")[1] + coordinateY
    print(f"Hoover instruction was {instruction}, current coordinates are {data.get('coords')[0]},{data.get('coords')[1]}")

    for coords in range(1,len(data.get("patches")),1):
        if data.get("coords") == data.get("patches")[coords]:
            data.get("patches").remove(data.get("coords"))
            hooverEndInfo["patches"] += 1
            print("Hoover pick a patch")


for character in data.get("instructions"):
    if character == "N":
        hooverInstructions(0, 1, character)
    if character == "S":
        hooverInstructions(0, -1, character)
    if character == "E":
        hooverInstructions(1, 0, character)
    if character == "W":
        hooverInstructions(-1, 0, character)

hooverEndInfo["coords"] = [data.get("coords")[0], data.get("coords")[1]]
print(hooverEndInfo)

