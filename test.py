from argparse import ArgumentParser
from time import sleep

import subprocess


parser = ArgumentParser()
parser.add_argument("time", type=int)
args = parser.parse_args()
print(f"Starting timer of {args.time} seconds")

for _ in range(args.time):
    print(".", end="", flush=True)
    sleep(1)
print("Done")


if __name__ == '__main__':
    subprocess.run(["python", __file__, "5"])