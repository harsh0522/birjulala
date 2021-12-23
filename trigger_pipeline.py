import time
import ssl
import base64
import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab
g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-XqMXYQUqYJWToaBN_xpf',ssl_verify = False ,timeout = 30,api_version = 4)
g1.auth()
# glpat-XqMXYQUqYJWToaBN_xpf
p_project_id = 31752457
p_project = g1.projects.get(p_project_id)
branch = p_project.branches.get('main')

# Create a trigger:
# trigger = p_project.triggers.create({'description': 'pranjal_pipeline3'})
# print(trigger)

pranjal_trigger_id = p_project.triggers.list()[0].id
pranjal_trigger_token = p_project.triggers.list()[0].token
# print(pranjal_trigger_token)
# print(pranjal_trigger_token)


def get_or_create_trigger(p_project):
    trigger_decription = 'pranjal_pipeline1'
    for t in p_project.triggers.list():
        if t.description == trigger_decription:
            return t
    return p_project.triggers.create({'description': trigger_decription})

trigger = get_or_create_trigger(p_project)
pipeline = p_project.trigger_pipeline('main', trigger.token, variables={"DEPLOY_ZONE": "us-west1"})
while pipeline.finished_at is None:
    pipeline.refresh()
    time.sleep(1)
