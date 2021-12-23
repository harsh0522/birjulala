import ssl

import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab
g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-ywfB-i6JNpzwCNYkdE85',ssl_verify = False ,timeout = 30,api_version = 4)
g1.auth()



# Get a project by ID
# project_id = 32104786
# project = g1.projects.get(project_id)
# print(project.attributes)



# Get a project by name with namespace
# project_name_with_namespace = "Harsh Agarwal / Basic_project"
# project = g1.projects.get(project_name_with_namespace)
# print(project)

#g1.projects.delete(project_id)
# # or
# project.delete()

# project = g1.projects.create({'name': 'project3'})
# alice = g1.users.list(username='alice')[0]
# user_project = alice.projects.create({'name': 'project2'})
# user_projects = alice.projects.list()



### MEMBERS
project_id = 32104786
project = g1.projects.get(project_id)
# print(project.attributes)
# project = g1.projects.get("Basic_project")
# members = project.members.list()
# print(members)
# member = project.members.create({'user_id': 9563385, 'access_level':
#                                  gitlab.DEVELOPER_ACCESS})

# members = project.members.list()
# print(members)
# project.members.delete(9563385)
project.upload("brij.txt", filepath="C:/Users/Harsh.agarwal/Desktop/terra/brij/brij.txt")





















