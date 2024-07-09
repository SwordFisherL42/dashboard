import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("status")
    parser.add_argument("info")
    args = parser.parse_args(sys.argv[1:])
    info_data = args.info.split(",")
    github_link = None
    environment = None
    commit_sha = None
    for data in info_data:
        if "github_link:" in data:
            github_link = data.split("github_link:").strip(" ,")
        elif "environment:" in data:
            environment = data.split("environment:").strip(" ,")
        elif "commit:" in data:
            commit_sha = data.split("commit:").strip(" ,")
    if args.status == "0":
        print(f"Sucessfully Deployed on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}")
        # Success Message
    else:
        print(f"Failed to deploy on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}")
        # Failure Message
    print(args.info)