import os
from dotenv import load_dotenv
from git import Repo
from directory import Directory


load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


class Gitinit:
    def __init__(self, repo_path, remote, commit_message, branch, username, token):
        self.repo_path = repo_path
        self.remote = remote
        self.commit_message = commit_message
        self.branch = branch
        self.username = username
        self.token = token
        self.origin = None
        self.repo = Repo.init(self.repo_path)

    def add_all_files_to_repo(self):
        self.repo.git.add(all=True)

    def perform_git_commit(self):
        self.repo.git.commit("-m", self.commit_message)

    def add_github_remote(self):
        
        self.origin = self.repo.create_remote('origin', self.remote)
        
        self.repo.git.remote("set-url", "origin", self.remote.replace("https://", f"https://{self.username}:{self.token}@"))

    def push_to_github(self):
        self.origin.push(refspec="master:origin")

    def compute(self):
        self.add_all_files_to_repo()
        self.perform_git_commit()
        self.add_github_remote()
        self.push_to_github()

    
    


if __name__ == '__main__':

    dir_root = '../output' 


    folders = Directory(dir_root)


    folders.tree()


    # for repository, url in myDict.items():
    repo_path = dir_root
    remote = 'https://github.com/uribalb/versioning_dev_output.git'
    commit_message = "Output of versioning_dev script"
    branch = "master"
    username = 'uribalb'
    token = GITHUB_TOKEN

    myGit = Gitinit(repo_path, remote, commit_message, branch, username, token)
    myGit.compute()
    

    
 