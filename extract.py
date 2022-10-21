"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Load NEO data from the given CSV file.
    filas = []
    with open(neo_csv_path,"r") as inputfile:
        reader = csv.reader(inputfile)
        for r in reader:
            filas.append(r)
    
    # Filter inputs
    indices = []
    labels = ["pdes","name","diameter","pha"]
    for label in labels:
        indices.append(filas[0].index(label))
    
    # Return filtered data
    all_rows = []
    
    for x in range(len(filas)):
        all_rows.append([filas[x][i] for i in indices])
        
    neos = []
    for neo in all_rows[1:]:
        neos.append(NearEarthObject(neo[0],neo[1],neo[2],neo[3],approaches=[]))
    
    return neos


def load_approaches(cad_json_path):
    
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    with open(cad_json_path,"r") as infile:
        data = json.load(infile)
    
    # Filter inputs
    fields = ["des","cd","dist","v_rel"]
    field_index = [data["fields"].index(e) for e in fields]
    
    # Return filtered data
    all_rows = [fields]
    for r in data["data"]:
        each_row = []
        for i in field_index:
            each_row.append(r[i])
        all_rows.append(each_row)
    
    cas = []
    for ca in all_rows[1:]:
        cas.append(CloseApproach(ca[0],ca[1],ca[2],ca[3]))
    
    return cas
