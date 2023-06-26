import requests

def detect_changes_on_branch(repo_owner, repo_name, branch_name):
    # GitHub API endpoint for comparing branches
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/compare/{branch_name}"
    print(url)

    # Send GET request to the GitHub API
    response = requests.get(url)

    print("response", response)

    if response.status_code == 200:
        comparison = response.json()
        total_commits = comparison['total_commits']
        files_changed = len(comparison['files'])

        print(f"Total commits on branch '{branch_name}': {total_commits}")
        print(f"Total files changed on branch '{branch_name}': {files_changed}")
    else:
        print("Error: Unable to fetch branch comparison.")

# Example usage
repo_owner = "Aqirito"
repo_name = "sbx-voice-cloning-booth"
branch_name = "setup-frontend"

detect_changes_on_branch(repo_owner, repo_name, branch_name)
