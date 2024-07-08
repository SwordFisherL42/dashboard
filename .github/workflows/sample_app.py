import argparse
import sys
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["pass", "fail"])
    args = parser.parse_args(sys.argv[1:])
    if args.action == "pass":
        print("Sample App Pass")
    else:
        with open("./build_file.txt", "w") as fh:
            fh.write("Sample App Log")
        
        x = 1/0
