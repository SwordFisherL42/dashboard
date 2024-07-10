import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("status")
    parser.add_argument("info")
    args = parser.parse_args(sys.argv[1:])
    # info_data = args.info.split(",")
    github_link = None
    environment = None
    commit_sha = None
    error = None
    # for data in info_data:
    #     if "Github Link:" in data:
    #         github_link = data.split("Github Link:")[1].strip(" ,")
    #     elif "environment:" in data:
    #         environment = data.split("environment:")[1].strip(" ,")
    #     elif "commit:" in data:
    #         commit_sha = data.split("commit:")[1].strip(" ,")
    #     elif "error:" in data:
    #         error = data.split("error:")[1].strip(" ,")
    if args.status == "0":
        print(f"Success message: {args.status} {args.info}")
        # print(f"Sucessfully Deployed on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}")
        # Success Message
    else:
        print(f"Fail message: {args.status} {args.info}")
        # print(f"Failed to deploy on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}\nError: {error}")
        # Failure Message