import os
import git
import config as c


REPO_URL = "https://github.com/dreapadoir/data-representation-coursework.git"
FILE_PATH = "assignments/assignment4-file.txt"
MY_NAME = "David"
TOKEN = c.config["apiKey"]  #calls the personal access token from the dict object in config.py

#gives the location of a temporary folder to hold the cloned repository
repo_dir = "C:/Users/dhiggins/Desktop/Data Representation/temp"

#creates the temporary folder if it doesn't already exist
if not os.path.exists(repo_dir):
    os.makedirs(repo_dir)

#clones repo to temp folder and adds personal access token to URL for use in later HTTP method
git_url_with_token = REPO_URL.replace("https://", f"https://{TOKEN}@")
repo = git.Repo.clone_from(git_url_with_token, repo_dir, branch='main', depth=1)

#reads the contents of assignment4-file.txt
with open(os.path.join(repo_dir, FILE_PATH), 'r') as file:
    file_contents = file.read()

#replaces Andrew with David
file_contents = file_contents.replace("Andrew", MY_NAME)

#saves the updated content to the assignment4-file.txt file
with open(os.path.join(repo_dir, FILE_PATH), 'w') as file:
    file.write(file_contents)

#carries out the git add, commit, push workflow
repo.git.add(FILE_PATH)

commit_message = "Replace 'Andrew' with my name"
repo.git.commit('-m', commit_message)

#the first line of this block sets origin to be the original remote repo that the local repo was cloned from, the existing data-representation-coursework repo on GitHub in this case.
#refspec defines the branches in the local and remote repos respectively (local:remote). Both are main in this program.
origin = repo.remote(name='origin')
origin.push(refspec='main:main')


print(f"Replaced 'Andrew' with '{MY_NAME}' in {FILE_PATH} and pushed to repository.")

#This block of code will delete the temp cloned repo from my machine after running the program. I had issues running the code a second time while this repo still existed on my machine (fatal errors).

import shutil
shutil.rmtree(repo_dir)
