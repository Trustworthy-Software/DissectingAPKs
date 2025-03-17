import os
import argparse


# ---------------------------------------------------------------------- #

# Checks if the provided file exists
def file(path):
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"{path} doesn't exist")


# ---------------------------------------------------------------------- #

def parse():
    parser = argparse.ArgumentParser(description="AndroZoo Analyzer")
    parser.add_argument("-k", "--key", type=str, help="API key to access the AndroZoo collection",
                        nargs=1, default="")
    parser.add_argument("-i", "--input", type=str, help="row from the AndroZoo collection information (latest.csv)",
                        nargs=1, default="")
    parser.add_argument("-o", "--output", type=file, help="path to the CSV file where we wish to store the results",
                        nargs="?")
    return parser.parse_args()


# ---------------------------------------------------------------------- #

ARGS = parse()

# ---------------------------------------------------------------------- #
