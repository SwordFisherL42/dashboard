import argparse
import sys

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--status", choices=['success', 'failure', 'dev'], required=True)
    parser.add_argument("--environment", required=True)
    parser.add_argument("--commit")
    parser.add_argument("--link")
    parser.add_argument("--error")
    args = parser.parse_args()

    if args.status == "success":
        print(f'Success message: "{args.status}" "{args.environment}" "{args.commit}" "{args.link}" "{args.error}"')
        # print(f"Sucessfully Deployed on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}")
        # Success Message
    elif args.status == "failure":
        print(f'Fail message: "{args.status}" "{args.environment}" "{args.commit}" "{args.link}" "{args.error}"') 
        # print(f"Failed to deploy on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}\nError: {error}")
        # Failure Message