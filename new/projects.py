import ssl

import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab
g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-ywfB-i6JNpzwCNYkdE85',ssl_verify = True ,timeout = 30,api_version = 4)
g1.auth()

# projects
# pipelines 
# triggers
# commits
# branches
# jobs

# List projects:
# projects = g1.projects.list()[1]
# print(projects)

# List all projects (default 20)
# projects = g1.projects.list(all=True)
# print(projects)
# print("__"*20)

# # Archived projects
# projects = g1.projects.list(archived=1)
# print(projects)
# print("__"*40)

# # Limit to projects with a defined visibility
# projects = g1.projects.list(visibility='public')
# print(projects)
# print("__"*40)

# List owned projects
#these are the projects that is owen by us or someone give us membership
# projects = g1.projects.list(owned=True)
# print(projects)
# print("__"*40)

# # List starred projects
# projects = g1.projects.list(starred=True)
# print(projects)
# print("__"*40)

# # Search projects
# projects = g1.projects.list(search='Basic_project',owned=True)
# print(projects)
# print("__"*40)

# Get a project by ID
# project_id = 32104786
# project = g1.projects.get(project_id)
# print(project)
# print(project.web_url)
# print("__"*40)
# print(project.name_with_namespace)
# print("__"*40)

# Get a project by name with namespace
# project_name_with_namespace = "Harsh"
# project = g1.projects.get(project_name_with_namespace)
# print(project)
# print("__"*40)


# Create a project:
# project = g1.projects.create({'name': 'basic2'})
# print(project)
# print("__"*40)

###################GROUP#########################
# Create a project in a group:
# You need to get the id of the group, then use the namespace_id attribute

# group_id = g1.groups.list(owened=True)
# print(group_id)
# print("_"*40)


# Create a project in a group:
# group_id = g1.groups.list()[0].id
# project = g1.projects.create({'name': 'myrepo', 'namespace_id': group_id})
# print(group_id)
# print("_"*40)
# print(project)
# print("_"*40)

# Update a project:
# project_id = 32104786
# project = g1.projects.get(project_id)
# project.snippets_enabled = 1
# project.save()
# print("__"*40)

# the avatar image can be passed as data (content of the file) or as a file
# object opened in binary mode
# project_id = 32104786
# project = g1.projects.get(project_id)
# project.avatar = open('C:/Users/Harsh.agarwal/Desktop/BijjuLala/children13.png', 'rb')
# project.save()
# print("__"*40)

# Delete a project:
# project_id = 32281870
# project = g1.projects.get(project_id)
# g1.projects.delete(project_id)
# or
# project.delete()
# print("__"*40)

# Fork a project:
#pankaj's project
# project_id = 29226305
# project = g1.projects.get(project_id)
# fork = project.forks.create({})

# fork to a specific namespace
# fork = project.forks.create({'namespace': 'myteam'})

# Get a list of forks for the project:
# project_id = 32104786
# project = g1.projects.get(project_id)
# forks = project.forks.list()
# print(forks)

# Get languages used in the project with percentage value:
# project_id = 32104786
# project = g1.projects.get(project_id)
# languages = project.languages()
# print(languages)

# Star/unstar a project:
# project_id = 32104786
# project = g1.projects.get(project_id)
# project.star()
# project.unstar()

# Archive/unarchive a project:
# project_id = 32104786
# project = g1.projects.get(project_id)
# project.archive()
# project.unarchive()

# Start the housekeeping job:
# project_id = 32104786
# project = g1.projects.get(project_id)
# project.housekeeping()

# List the repository tree:
# list the content of the root directory for the default branch
# project_id = 32104786
# project = g1.projects.get(project_id)
# print(project)
# items = project.repository_tree()
# print(items)

# list the content of a subdirectory on a specific branch
# items = project.repository_tree(path='basic_project', ref='feature1')
# print(items)

# Get a snapshot of the repository:
# project_id = 32104786
# project = g1.projects.get(project_id)
# tar_file = project.snapshot()
# print(tar_file)


# Compare two branches, tags or commits:
# project_id = 32104786
# project = g1.projects.get(project_id)
# result = project.repository_compare('main', 'feature1')

# get the commits
# for commit in result['commits']:
#     print(commit)

# get the diffs
# for file_diff in result['diffs']:
#     print(file_diff)





# Get a list of contributors for the repository:
# project_id = 31752457
# project = g1.projects.get(project_id)
# contributors = project.repository_contributors()
# print(contributors)


# Get a list of users for the repository:
# project_id = 32104786
# project = g1.projects.get(project_id)
# users = project.users.list()
# print(users)
# search for users
# users = project.users.list(search='pran')
# users = project.users.list(search='hars')
# print(users)

# Start the pull mirroring process (EE edition):
# project_id = 32104786
# project = g1.projects.get(project_id)
# project.mirror_pull()


####################IMPORT/EXPORT################################
# import time

# project_id = 32104786
# project = g1.projects.get(project_id)
# # Create the export

# p = g1.projects.get(project)
# export = p.exports.create()

# # Wait for the 'finished' status
# export.refresh()
# while export.export_status != 'finished':
#     time.sleep(1)
#     export.refresh()

# Download the result
# with open('C:/Users/Harsh.agarwal/Desktop/BijjuLala/new/export.tgz', 'wb') as f:
#     export.download(streamed=True, action=f.write)


####################Project files###########################################

# Get a file:

# project_id = 32104786
# project = g1.projects.get(project_id)
# f = project.files.get(file_path='pranjal.txt', ref='main')

# # get the base64 encoded content
# print(f.content)

# # get the decoded content
# print(f.decode())



# Get a raw file:
#this will read file from a file in repo and paste the contents of that file to new file in a given location "C:/Users/Harsh.agarwal/Desktop/BijjuLala/questions.txt"
# project_id = 32104786
# project = g1.projects.get(project_id)
# raw_content = project.files.raw(file_path='pranjal.txt', ref='main')
# print(raw_content)
# with open('C:/Users/Harsh.agarwal/Desktop/BijjuLala/questions.txt', 'wb') as f:
#     project.files.raw(file_path='pranjal.txt', ref='main', streamed=True, action=f.write)


# Create a new file:
# project_id = 32104786
# project = g1.projects.get(project_id)
# file_content = "my name is harsh agarwal"
# f = project.files.create({'file_path': 'testfile.txt',
#                           'branch': 'main',
#                           'content': file_content,
#                           'author_email': 'agarwalharsh0522@gmail.com',
#                           'author_name': 'harsh0522',
#                         #   'encoding': 'text',
#                           'commit_message': 'Create testfile'})

##############################Additional project statistics#############################
# Get all additional statistics of a project:

# project_id = 32104786
# project = g1.projects.get(project_id)
# # statistics = project.additionalstatistics.get()
# # print(statistics)

# # Get total fetches in last 30 days of a project:
# total_fetches = project.additionalstatistics.get().fetches['total']
# print(total_fetches)




































































