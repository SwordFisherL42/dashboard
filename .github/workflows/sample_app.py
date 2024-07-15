import argparse
import sys
import os
import logging

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
    write_to_github_output("status", "dev")
    write_to_github_output("environment", "development")
    write_to_github_output("github_link", "http://github.com/1234")
    write_to_github_output("commit", "abcde12345")
    if args.action == "pass":
        print("Sample App Pass")
        write_to_github_output("status", "success")
    else:
        print("Sample App FAIL")
        try:
            x = 1/0
        except Exception as e:
            logging.error("error: %s" % str(e))
            write_to_github_output("status", "error")
            write_to_github_output("error", str(e))
            raise e
