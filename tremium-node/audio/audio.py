'''
This script is the entry point to launch the audio event detection.
It should be lauched by the container entry point script
'''

import argparse
from tremium.audio import AudioEventDetector

# parsing script arguments
parser = argparse.ArgumentParser()
parser.add_argument("config_path", help="path to the .json config file")
args = parser.parse_args()

if __name__ == "__main__":
    data_generator = AudioEventDetector(args.config_path)