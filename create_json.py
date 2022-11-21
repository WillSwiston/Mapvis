import pandas as pd
import json as json
import sys
from unidecode import unidecode

def imp(csv, year):
    file = pd.read_csv(csv)

    new_json = {}
    for elem in file.iterrows():
        element = elem[1]
        if element.year != year: continue
        name = element.county_name + str(element.year)
        new_arr = {}

        if name not in new_json:
            new_json[name] = []

        new_arr['county_name'] = unidecode(element.county_name)
        new_arr['state'] = element.state
        new_arr['candidate'] = unidecode(element.candidate)
        new_arr['party'] = element.party
        new_arr['candidatevotes'] = element.candidatevotes

        new_json[name].append(new_arr)
    return new_json


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("<year> <filename>")
        exit(1)
    
    year = sys.argv[1]
    filename = sys.argv[2]

    print(f"Creating JSON file \"json/{filename}\" for year {year}.")
    new_json = imp("elect_results.csv", int(year))

    with open(f"json/{filename}.json", "w") as f:
        f.write(json.dumps(new_json))

