import requests

def compare_commits(repo_owner, repo_name, base_commit, head_commit):
    # GitHub API endpoint for comparing commits
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/compare/{base_commit}...{head_commit}"

    # Send GET request to the GitHub API
    response = requests.get(url)

    if response.status_code == 200:
        comparison = response.json()
        total_commits = comparison['total_commits']
        files_changed = len(comparison['files'])

        print(f"Total commits between {base_commit} and {head_commit}: {total_commits}")
        print(f"Total files changed between {base_commit} and {head_commit}: {files_changed}")
    else:
        print("Error: Unable to compare commits.")

# Example usage
repo_owner = "Aqirito"
repo_name = "sbx-voice-cloning-booth"
base_commit = "main"  # Replace with the base commit SHA
head_commit = "resample-audio"  # Replace with the head commit SHA

compare_commits(repo_owner, repo_name, base_commit, head_commit)
