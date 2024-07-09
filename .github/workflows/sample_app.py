import argparse
import sys
import os
import logging

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="[%(levelname)s] %(message)s,")
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["pass", "fail"])
    args = parser.parse_args(sys.argv[1:])
    if args.action == "pass":
        print("Sample App Pass")
        logging.info("Github Link: %s" % "http://github.com/1234")
        logging.info("environment: %s" % "development")
    else:
        print("Sample App FAIL")
        try:
            x = 1/0
        except Exception as e:
            logging.error("Error in runtime: %s" % str(e))
            raise e
