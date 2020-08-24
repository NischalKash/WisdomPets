from git import Repo
import os
os.system('ruby bug_fix_ruby.rb')
repo_dir = "Ruby"
print("fefde")
repo = Repo(repo_dir,search_parent_directories=True)
print("GEKEKEKE")
file_list = ['/Users/nischalkashyap/Downloads/Fall 2020/SE2020/HW2/Repository/HW2_SoftwareEngineering/log.txt']
commit_message = "Testing Scenarios Logs"
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()