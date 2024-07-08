import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["pass", "fail"])
    args = parser.parse_args(sys.argv[1:])
    if args.action == "pass":
        pass
    else:
        x = 1/0
