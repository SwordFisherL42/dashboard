import argparse
import sys
import os
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s,")
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["pass", "fail"])
    args = parser.parse_args(sys.argv[1:])
    logging.info("environment: %s" % "development")
    logging.info("commit: %s" % "5678abcd")
    if args.action == "pass":
        print("Sample App Pass")
        logging.info("Github Link: %s" % "http://github.com/1234")
    else:
        print("Sample App FAIL")
        try:
            x = 1/0
        except Exception as e:
            logging.error("error: %s" % str(e))
            raise e
