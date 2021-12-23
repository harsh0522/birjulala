import time
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
branch = project.branches.get('main')

# List triggers:
triggers = project.triggers.list()[0]
# print(triggers)


# Create a trigger:
# trigger = project.triggers.create({'description': 'pranjal_pipeline'})
# print(trigger)

# Get a trigger:
# c = trigger.id 
# pranjal_trigger = triggers
pranjal_token = triggers.id
print(pranjal_token)
# trigger_token = 319326
# trigger = project.triggers.get(trigger_token)
# print(trigger)

#Full example with wait for finish:


# def get_or_create_trigger(project):
#     trigger_decription = 'mytrigger1'
#     for t in project.triggers.list():
#         if t.description == trigger_decription:
#             return t
#     return project.triggers.create({'description': trigger_decription})

# trigger = get_or_create_trigger(project)
# pipeline = project.trigger_pipeline('main', trigger.token, variables={"DEPLOY_ZONE": "us-west1"})
# while pipeline.finished_at is None:
#     pipeline.refresh()
#     time.sleep(1)














