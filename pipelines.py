import ssl
import base64
import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab
g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-ywfB-i6JNpzwCNYkdE85',ssl_verify = True ,timeout = 30,api_version = 4)
g1.auth()

project_id = 32104786
project = g1.projects.get(project_id)
branch = project.branches.get('main')

# List pipelines for a project:
# pipelines = project.pipelines.list()
# print(pipelines)

# Get a pipeline for a project
# pipeline_id = 430958748
# pipeline = project.pipelines.get(pipeline_id)
# print(pipeline)

# Get variables of a pipeline:
# variables = pipeline.variables.list()
# print(variables)

# Retry the failed builds for a pipeline:
# pipeline.retry()

# Cancel builds in a pipeline:
# pipeline.cancel()

# Delete a pipeline:
# pipeline_id = 430958748
# pipeline = project.pipelines.get(pipeline_id)
# pipeline.delete()

# Create a pipeline for a particular reference with custom variables:
# pipeline = project.pipelines.create({'ref': 'main', 'variables': [{'key': '', 'value': 'hello'}]})
# print(pipeline)
# a = []
# for i in pipelines:
#     a.append(i.id)

# c = a[1:]
# print(c)
pipelines = project.pipelines.list()
for i in pipelines:
    if i.id == 430899158:
        pipeline_id = i.id
        pipeline = project.pipelines.get(pipeline_id)
        pipeline.delete()

print(type(i))


    







