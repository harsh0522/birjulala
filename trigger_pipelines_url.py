import time
import ssl
import base64
import sys,os,urllib3,pdb,argparse
from gitlab.v4.objects import projects
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
import gitlab

gl = gitlab.Gitlab('https://gitlab.com',ssl_verify = False)  # no authentication
project = gl.projects.get(31752457, lazy=True)  # no API call
project.trigger_pipeline('main', 'af1c1bbbb9b5c443979b31d6efc69c')