import ssl

import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ssl._create_default_https_context = ssl._create_unverified_context

import gitlab

g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-ywfB-i6JNpzwCNYkdE85',ssl_verify = False ,timeout = 30,api_version = 4)



g1.auth()

# projects = g1.projects.list()
# print(projects)

# List all projects (default 20)
# projects = g1.projects.list(all=True)
# print(projects)

# Archived projects
#projects = g1.projects.list(archived=1)
# # Limit to projects with a defined visibility
# projects = g1.projects.list(visibility='public')

# # List owned projects
# projects = g1.projects.list(owned=True)
# print(projects)

# # List starred projects
#projects = g1.projects.list(starred=True)


# # Search projects
# projects = g1.projects.list(search='main')
# print(projects)


# Get a project by ID
project_id = 32247814
project = g1.projects.get(project_id)

# Get a project by name with namespace
project_name_with_namespace = "Harsh Agarwal / Basic_project"
project = g1.projects.get(project_name_with_namespace)
print(project)
