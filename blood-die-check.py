#!/opt/local/bin/python3.4
# Simon de Wit, maart 2015

import json
from collections import namedtuple


def main():

    # Open .json file
    with open("blood-die.json", "r") as in_f:
        # Create namedtuple for languages
        Language = namedtuple("Language", "lang_name, classification, w_blood, w_die")
        json_f = json.load(in_f)

        with open("result.json", "w") as output:
            # Walk through file and check if languages has matching words, if so, write to result.json
            for line in json_f:
                lang = Language(line[0], line[1], line[2].split(), line[3].split())
                [json.dump(lang, output) for i in lang.w_blood if i in lang.w_die]

if __name__ == '__main__':
    main()