import argparse
import sys
import os
import logging
import json


def write_to_github_output(name: str, value: str):
    is_action = os.getenv('GITHUB_ACTION')
    output_path = os.getenv('GITHUB_OUTPUT')
    if is_action and output_path:
        with open(output_path, 'a') as fh:
            fh.write(f"{name}={value}\n")
    else:
        print("Skipping write to GithHub outputs. (Not running via GitHub Actions)")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s,", stream=sys.stdout)
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["pass", "fail", "dev"])
    args = parser.parse_args(sys.argv[1:])
    runtime_data  = {}
    runtime_data["environment"] = "development"
    runtime_data["github_link"] = "http://github.com/1234"
    runtime_data["commit"] = "abcde12345"
    runtime_data["status"] = ""
    if args.action == "pass":
        print("Sample App Pass")
        runtime_data["status"] = "Sample App Pass"
        write_to_github_output("runtime-data", json.dumps(runtime_data))
    elif args.action == "fail":
        print("Sample App FAIL")
        try:
            x = 1/0
        except Exception as e:
            logging.error("error: %s" % str(e))
            runtime_data["status"] = "Sample App FAIL"
            runtime_data["error"] = str(e)
            write_to_github_output("runtime-data", json.dumps(runtime_data))
            raise e
