import argparse
import sys
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["pass", "fail"])
    args = parser.parse_args(sys.argv[1:])
    os.environ['github_link'] = 'http://github.com/runs/1234'
    os.environ['environment'] = 'development'
    
    if args.action == "pass":
        print("Sample App Pass")
        os.environ['message_content'] = 'Orchestor Passed Successfully'
    else:
        os.environ['message_content'] = 'Orchestor Failed'
        with open("./build_file.txt", "w") as fh:
            fh.write("Sample App Log")
        print("Sample App FAIL")
        x = 1/0
