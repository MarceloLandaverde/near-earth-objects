"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

"""
import csv
import json
from helpers import datetime_to_str

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    rows = [list(fieldnames)]
    
    for a in results:
        r = [datetime_to_str(a.time),a.distance, a.velocity, a.neo.designation, a.neo.name, a.neo.diameter, a.neo.hazardous]
        
        # Be sure that the name attribute is not None
        if r[4] == None:
            r[4] = ""
        # Be sure that the Hazardous values are strings
        r[6] = str(r[6]).capitalize()
    
        rows.append(r)
    
    # Generate csv output file    
    with open(filename,"w") as outfile:
        writer = csv.writer(outfile,lineterminator="\n")
        for r in rows:
            writer.writerow(r)
    

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    top_level = []
    for a in results:
        d = {}
        d["datetime_utc"] = datetime_to_str(a.time)
        d["distance_au"] = a.distance
        d["velocity_km_s"] = a.velocity
        d["neo"] = {"designation":a.neo.designation ,
                    "name": a.neo.name,
                    "diameter_km":a.neo.diameter,
                    "potentially_hazardous": a.neo.hazardous}

        top_level.append(d)
    
    # Be sure that the name attribute is not None
    for e in top_level:
        if e["neo"]["name"] == None:
            e["neo"]["name"] = ""
    
    with open(filename,"w") as outfile:
        json.dump(top_level,outfile,indent=2)
