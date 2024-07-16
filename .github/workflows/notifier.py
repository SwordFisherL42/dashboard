import argparse
import sys
import json


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--data")
    # parser.add_argument("--environment")
    # parser.add_argument("--commit")
    # parser.add_argument("--link")
    # parser.add_argument("--error")
    args = parser.parse_args()

    if args.data:
        try:
            runtime_data = json.loads(args.data)
            status = runtime_data.get("status")
            environment = runtime_data.get("environment")
            link = runtime_data.get("github_link")
            commit = runtime_data.get("commit")
            action = runtime_data.get("action")
            error = runtime_data.get("error")
            print(f'Status: "{status}", Environment: "{environment}",  Commit: "{commit}", github_link: "{link}" error: "{error}"')
                # elif args.status == "failure":
                #     print(f'Fail message: "{args.status}" "{args.environment}" "{args.commit}" "{args.link}" "{args.error}"') 
                #     # print(f"Failed to deploy on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}\nError: {error}")
                #     # Failure Message
        except json.decoder.JSONDecodeErro as e:
            print("Unable to de-serialize runtime data")
            

    # if args.status == "success":
    #     print(f'Success message: "{args.status}" "{args.environment}" "{args.commit}" "{args.link}" "{args.error}"')
    #     # print(f"Sucessfully Deployed on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}")
    #     # Success Message
    # elif args.status == "failure":
    #     print(f'Fail message: "{args.status}" "{args.environment}" "{args.commit}" "{args.link}" "{args.error}"') 
    #     # print(f"Failed to deploy on Commit {commit_sha} for environment {environment}\nGithub Link: {github_link}\nError: {error}")
    #     # Failure Message
    # else:
    #     print(f'Unexpected status: "{args.status}" "{args.environment}" "{args.commit}" "{args.link}" "{args.error}"') 