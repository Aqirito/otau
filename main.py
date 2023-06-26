import requests
from git_log import get_commit_sha

def is_remote_ahead(repo_owner, repo_name, branch_name, local_commit_sha):
    # GitHub API endpoint to get the latest commit SHA of the remote branch
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/branches/{branch_name}"
    
    # Send GET request to the GitHub API
    response = requests.get(url)
    
    if response.status_code == 200:
        remote_commit_sha = response.json()["commit"]["sha"]
        
        # Compare the commit SHAs
        return remote_commit_sha != local_commit_sha
    else:
        print(f"Error: Unable to fetch remote branch information. Status code: {response.status_code}")
        return False

# Example usage
repo_owner = "Aqirito"
repo_name = "otau"
branch_name = "main"
local_commit_sha = get_commit_sha  # Replace with your local commit SHA

result = is_remote_ahead(repo_owner, repo_name, branch_name, local_commit_sha)
print(f"Is remote branch ahead of local branch? {result}")