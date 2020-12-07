import argparse
import pandas as pd
from itertools import chain

def get_terms():
    df = pd.read_csv('color_semantics_ratings.tsv', sep='\t')
    colors = ['white', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'black']
    dimensions = list(df['dimension'].unique())
    dimensions = [pair.split('-') for pair in dimensions]
    dimensions = list(chain(*dimensions))
    return colors, dimensions

def filter_cooccurrences(fname, colors, dimensions):
    colors = set(colors)
    dimensions = set(dimensions)
    with open(fname, 'r') as infile, open(fname.replace('.txt', '.filtered.txt'), 'w') as outfile, open(fname.replace('.txt', '.filtered_out.txt'), 'w') as filterfile:
        for line in infile:
            words = set(line.strip('\n').split(' '))
            if (colors & words) and (dimensions & words):
                filterfile.write(line)
            else:
                outfile.write(line)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('fname')
    args = argparser.parse_args()

    colors, dimensions = get_terms()
    filter_cooccurrences(args.fname, colors, dimensions)
