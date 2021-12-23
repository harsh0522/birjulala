############################Project pipelines############################
import ssl

import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab
g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-ywfB-i6JNpzwCNYkdE85',ssl_verify = True ,timeout = 30,api_version = 4)
g1.auth()

# List pipelines for a project:

# project_id = 32104786
# project = g1.projects.get(project_id)
# pipelines = project.pipelines.list(owened = True)
# # print(pipelines)

# Get a pipeline for a project:

# pipeline_id_1 = pipelines[0].id
# print(pipeline_id_1)
# print("__" * 40 )
# pipeline = project.pipelines.get(pipeline_id_1)
# print(pipeline)
# print("__" * 40 )
# print(pipeline.detailed_status['group'])

# Get variables of a pipeline:
# project_id = 32104786
# project = g1.projects.get(project_id)
# pipelines = project.pipelines.list(owened = True)
# pipeline_id_1 = pipelines[3].id
# p=433950270
# pipeline = project.pipelines.get(p)
# variables = pipeline.variables.list()
# print(variables)


# Create a pipeline for a particular reference with custom variables:
project_id = 32104786
project = g1.projects.get(project_id)
pipeline = project.pipelines.create({'ref': 'feature1', 'variables': [{'key': 'harsh', 'value': 'done docker'}]})
print(pipeline)
print("__"*40)
































