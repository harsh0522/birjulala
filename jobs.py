import time
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


# project.trigger_build('master', trigger_token,
                    #   {'extra_var1': 'foo', 'extra_var2': 'bar'})

# List jobs for the project:
# jobs = project.jobs.list()
# print(jobs)


# Get a single job:
job_id = 1900772694
c = project.jobs.get(job_id)
# print(c)

# List the jobs of a pipeline:
# pipeline_id = 430958748
# project = g1.projects.get(project_id)
# pipeline = project.pipelines.get(pipeline_id)
# jobs = pipeline.jobs.list()[1]
# pipeline_job = pipeline.jobs.list()[0]
# build_or_jobs = project.jobs.get(pipeline_job.id, lazy=True)
# # print(job)
# xml = build_or_jobs.trace()
# print(xml)
print(c.trace().decode())

# Get the test report for a pipeline:
# test_report = pipeline.test_report.get()
# print(test_report)




















