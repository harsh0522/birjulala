import ssl
import base64
import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab
g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-ywfB-i6JNpzwCNYkdE85',ssl_verify = False ,timeout = 30,api_version = 4)
g1.auth()

project_id = 32104786
project = g1.projects.get(project_id)
#branch = project.branches.get('main')

#List the commits for a project:
# commits = project.commits.list()
# print(commits)
# 
# You can use the ref_name, since and until filters to limit the results:
#to limit the use we can use this
# commits = project.commits.list(ref_name='main')
# print(commits)
# commits = project.commits.list(since='2016-01-01T00:00:00Z')

# The available all listing argument conflicts with the python-gitlab argument. Use query_parameters to avoid the conflict:
# commits = project.commits.list(all=True,
#                                query_parameters={'ref_name': 'main'})
# print(commits)


# Create a commit:
data = {
    'branch': 'main',
    'commit_message': 'blah blah blah',
    'actions': [
        {
            'action': 'create',
            'file_path': 'pranjal.txt',
            'content': open('C:/Users/Harsh.agarwal/Desktop/pranjal.txt').read(),
        }

    ]
}
commit = project.commits.create(data)

# print(branch)
# Get a commit detail:
#004a2721 this is branch short id
# commit = project.commits.get('004a2721')

# Get the diff for a commit:
# diff = commit.diff()
# print(diff)

# Cherry-pick a commit into another branch:
# commit.revert(branch='target_branch')


# Revert a commit on a given branch:
# commit.revert(branch='main')

# Get the references the commit has been pushed to (branches and tags):
# commit.refs()  # all references
# commit.refs('tag')  # only tags
# commit.refs('branch')  # only branches



# List the merge requests related to a commit:
# commit.merge_requests()












