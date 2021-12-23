import ssl

import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab
g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-ywfB-i6JNpzwCNYkdE85',ssl_verify = False ,timeout = 30,api_version = 4)
g1.auth()

project_id = 32104786
project = g1.projects.get(project_id)

#Get the list of branches for a repository:
# branches = project.branches.list()
# print(branches)

#Get a single repository branch:
# branch = project.branches.get('main')
# print(branch)

#Create a repository branch:
# branch = project.branches.create({'branch': 'feature2','ref':'main'})
# print(branch)

#Delete a repository branch:
# project.branches.delete('feature2')

# Protect/unprotect a repository branch:
# branch = project.branches.get('feature1')
# branch.protect()
# branch.unprotect()
# By default, developers are not authorized to push or merge into protected branches. This can be changed by passing developers_can_push or developers_can_merge:
# branch.protect(developers_can_push=True, developers_can_merge=True)

# Delete the merged branches for a project:
# project.delete_merged_branches()


































































