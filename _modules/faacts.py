import query from salt.utils.http
import logging
import salt
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
  restargs = {}
  for name in ['path', 'method', 'username', 'password']:
    restargs[name] = _config(name, **kwargs)
    
  query( "http://155.178.172.254:8188/cxf/slc/NCRServices?ncr_service=wfs",
          method="POST",
	  status=True,
	  headers=False,
	  text=False,
	  username="ncr_test_ext2",
	  password="4Sk1K8s3q9h7uJr",
          header_file="/tmp/headers.txt",
	  data_file="/tmp/data.txt",
	  text_out="/tmp/data_response.txt",
	  headers_out="/tmp/headers_response.txt",
  )
  
  
