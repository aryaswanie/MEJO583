import glob
import json

# thanks to Elisabeth for sharing the code written by Jonas Kölker!!

def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:

        first = True

        for infile_name in input_filenames:
            with open(infile_name) as infile:
                if first:
                    outfile.write('[')
                    first = False
                else:
                    outfile.write(',')
                outfile.write(infile.read())
        outfile.write(']')

cat_json('data.json', ['ChapelHill.json', 'Durham.json', 'Raleigh.json'])
