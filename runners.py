import time
import ssl
import base64
import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects, runners
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab
g1 = gitlab.Gitlab('https://gitlab.com',private_token ='glpat-ywfB-i6JNpzwCNYkdE85',ssl_verify = False ,timeout = 30,api_version = 4)
g1.auth()

project_id = 32104786
project = g1.projects.get(project_id)
branch = project.branches.get('main')

# List owned runners
# runners = g1.runners.list()
# print(runners)
# With a filter
# runners = g1.runners.list(scope='active')
# print(runners)
# List all runners, using a filter
# runners = g1.runners.all(scope='paused')
# print(runners)

# Register a new runner:
# secret_token = 9H3hJpTfp6J3FBcxSSsg
runner = g1 .runners.create({'token': '9H3hJpTfp6J3FBcxSSsg'})
print(runner)