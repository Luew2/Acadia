import os
import argparse
import openai
from generators.dalle.dalle import generate_dalle

#############################################################################
#
# Args
#
#############################################################################

# What generator are you running? What image size is desired?

# Parser
parser = argparse.ArgumentParser()

# Parser Arguements
parser.add_argument(
    "-generator", "--generator", help="Generator must be dalle (for now)", type=str
)
parser.add_argument("-size", "--size", help="Size must be 256, 512, 1024", type=str)
parser.add_argument("-n", "--n", help="Number of stickers to generate", type=int)
args = parser.parse_args()

#############################################################################
#
# PATHS
#
#############################################################################

# What is the base directory of the project?

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#############################################################################
#
# ENVIRONMENT VARIABLES
#
#############################################################################

# What are the environment variables?

openai.organization = os.environ.get("ENV_OPENAI_ORG")
openai.api_key = os.environ.get("ENV_OPENAI_KEY")

#############################################################################
#
# Runtime
#
#############################################################################

if __name__ == "__main__":
    # What is the generator?
    if args.generator == "dalle":
        generate_dalle(args.size, args.n)
    else:
        print("Please specify a generator with -generator, defaulting to dalle")
        generate_dalle(args.size, args.n)
