import argparse
import sys
import os
import logging

def write_to_github_output(name: str, value: str):
    # is_action = os.getenv('GITHUB_ACTION')
    # output_path = os.getenv('GITHUB_OUTPUT')
    # if is_action and output_path:
    #     with open(output_path, 'a') as fh:
    #         fh.write(f"{name}={value}\n")
    # else:
    #     logging.info("Skipping write to GithHub outputs. (Not running via GitHub Actions)")
    if os.getenv('GITHUB_ACTION'):
        try:
            with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
                fh.write(f"{name}={value}\n")
        except KeyError as key_error:
            logging.exception(f"Unable to to write to GitHub actions")
            raise key_error
        except IOError as io_error:
            logging.exception(f"Unable to to write to GitHub actions")
            raise io_error
    else:
        logging.info("Skipping write to GithHub outputs. (Not running via GitHub Actions)")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s,", stream=sys.stdout)
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["pass", "fail"])
    args = parser.parse_args(sys.argv[1:])
    # write_to_github_output("info", "http://github.com/1234")
    # write_to_github_output("info", "http://github.com/1234")
    # write_to_github_output("info", "http://github.com/1234")
    if args.action == "pass":
        print("Sample App Pass")
        write_to_github_output("status", "0")
        write_to_github_output("info", "success in deployment")
    else:
        print("Sample App FAIL")
        try:
            x = 1/0
        except Exception as e:
            logging.error("error: %s" % str(e))
            write_to_github_output("status", "error")
            write_to_github_output("info", "error failed to deploy")
            write_to_github_output("error", str(e))
            write_to_github_output("link", "http://github.com/1234")
            raise e
