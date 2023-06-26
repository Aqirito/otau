import requests

def detect_changes_on_branch(repo_owner, repo_name, branch_name):
    # GitHub API endpoint for comparing branches
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/compare/{branch_name}"

    # Send GET request to the GitHub API
    response = requests.get(url)

    if response.status_code == 200:
        comparison = response.json()
        total_commits = comparison['total_commits']
        files_changed = len(comparison['files'])

        print(f"Total commits on branch '{branch_name}': {total_commits}")
        print(f"Total files changed on branch '{branch_name}': {files_changed}")
    else:
        print("Error: Unable to fetch branch comparison.")

# Example usage
repo_owner = "your_username"
repo_name = "your_repository"
branch_name = "main"

detect_changes_on_branch(repo_owner, repo_name, branch_name)
