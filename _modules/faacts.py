import requests
from requests.auth import HTTPBasicAuth
import logging
import json

#log = logging.getLogger(__name__)

__virtual_name__ = 'faacts'

def __virtual__():
  return __virtual_name__

def rest(**kwargs):
  '''
  Makes a RESTful request
  
  CLI Example::

      salt minion faacts.rest something
  '''
  #restargs = {}
  #for name in ['path', 'method', 'username', 'password']:
  #  restargs[name] = _config(name, **kwargs)
    
  with open('/tmp/data.txt','rb') as payload:
    r = requests.post('http://%s/cxf/slc/NCRServices?ncr_service=wfs' % __pillar__['ipport'], 
        auth=HTTPBasicAuth('ncr_test_ext2', '4Sk1K8s3q9h7uJr'), 
        data=payload, verify=False, headers=__pillar__['headers'])

  return "headers: " + str(r.headers)
