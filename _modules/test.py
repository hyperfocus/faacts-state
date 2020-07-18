import salt

__virtual_name__ = 'test'

def __virtual__():
  return __virtual_name__


def hello():
    return "hello " + __pillar__['ipport']
