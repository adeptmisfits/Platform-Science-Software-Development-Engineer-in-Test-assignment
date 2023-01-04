"""This script gets the info from a json file to give instructions to an imaginary hoover to get patches
of dirt and move across a restricted room"""

import os
import json


# Function to open json file
with open(f'{os.getcwd()}/Instructions.json', 'r') as f:
    data = json.load(f)

hooverEndInfo = {"coords": data.get("coords"),
                 "patches": 0}

"""Method to update coordinates to final position of hoover"""
def getCoordinates(coordinateX, coordinateY):
    if 0 < data.get("coords")[0] < data.get("roomSize")[0]:
        hooverEndInfo.get("coords")[0] += coordinateX
    if 0 < data.get("coords")[1] < data.get("roomSize")[1]:
        hooverEndInfo.get("coords")[1] += coordinateY


"""Method to verify if a patch of dirt need to be removed"""
def checkToRemovePatchOfDirt():
    for coords in range(1, len(data.get("patches")), 1):
        if hooverEndInfo.get("coords") == data.get("patches")[coords]:
            data.get("patches").remove(data.get("coords"))
            hooverEndInfo["patches"] += 1
            print("Hoover pick a patch")


"""Method to update X Y coordinate based on sent instructions"""
def hooverInstructions(instruction):
    if instruction == "N":
        getCoordinates(0, 1)
    if instruction == "S":
        getCoordinates(0, -1)
    if instruction == "E":
        getCoordinates(1, 0)
    if instruction == "W":
        getCoordinates(-1, 0)


# Getting each instruction to update final coordinates
for character in data.get("instructions"):
    hooverInstructions(character)
    checkToRemovePatchOfDirt()
    print(f"Hoover instruction was {character}, current coordinates are {hooverEndInfo.get('coords')}")

# Function to create json file containing the output
with open('hooverOutput.json', 'w') as json_file:
    json.dump(hooverEndInfo, json_file)
