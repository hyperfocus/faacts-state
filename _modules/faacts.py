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
    headers = {'Content-Type': 'application/xml', 'Expect': '100-continue', 'NWC_Request_Sent_Time': 'today'}
    r = requests.post('http://155.178.172.254:8188/cxf/slc/NCRServices?ncr_service=wfs', 
        auth=HTTPBasicAuth('ncr_test_ext2', '4Sk1K8s3q9h7uJr'), 
        data=payload, verify=False, headers=headers)

  return "headers: " + str(r.headers)
