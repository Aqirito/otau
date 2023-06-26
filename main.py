import requests
from git import Repo
import os
current_directory = os.getcwd()
print("Current Directory:", current_directory)

repo_owner = "Aqirito"
repo_name = "otau"
branch_name = "main"
repo = Repo(current_directory)

def is_remote_ahead(repo_owner, repo_name, branch_name):
    # GitHub API endpoint to get the latest commit SHA of the remote branch
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/branches/{branch_name}"

    local_commit_sha = get_commit_sha(branch_name)  # Replace with your local commit SHA
    
    # Send GET request to the GitHub API
    response = requests.get(url)
    
    if response.status_code == 200:
        remote_commit_sha = response.json()["commit"]["sha"]
        remote_commit_branch = response.json()["name"]
        print(f"Commit SHA of REMOTE:'{remote_commit_branch}': {remote_commit_sha}")
        
        # Compare the commit SHAs
        return remote_commit_sha != local_commit_sha
    else:
        print(f"Error: Unable to fetch remote branch information. Status code: {response.status_code}")
        return False

def get_commit_sha(branch_name):
    branch = repo.heads[branch_name]
    commit = branch.commit
    commit_sha = commit.hexsha
    print(f"Commit SHA of LOCAL: '{branch_name}': {commit_sha}")
    return commit_sha

def git_pull():

    result = is_remote_ahead(repo_owner, repo_name, branch_name)
    print(f"Is remote branch ahead of local branch? {result}")

    if result == True:
        repo.git.pull()
    else:
        print("Already up to date")


git_pull()
