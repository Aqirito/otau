from git import Repo
import os

current_directory = os.getcwd()
print("Current Directory:", current_directory)

def get_commit_sha(repo_path, branch_name):
    repo = Repo(repo_path)
    branch = repo.heads[branch_name]
    commit = branch.commit
    commit_sha = commit.hexsha
    return commit_sha

# Example usage
repo_path = current_directory
branch_name = "main"  # Replace with your branch name

commit_sha = get_commit_sha(repo_path, branch_name)
print(f"Commit SHA of branch '{branch_name}': {commit_sha}")