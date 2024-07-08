import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("result")
    parser.add_argument("info")
    args = parser.parse_args(sys.argv[1:])
    if not args.action:
        print("Notify of Pass")
    else:
        print("Notify of Failure")
    print(args.info)