'''
Created on 6 dic 2019

@author: Andrea
'''
import sphinx_autobuild

import sys
import os


def path_separator():
  if os.name == "nt":
    separator = ";"
  elif os.name == "posix":
    separator = ":"
  return separator

def normalize_path(paths:str) -> str:
  return paths.lower().replace('\\', '/')

def ensure_in_environ_PATH(path:str):
  env_path = os.environ.get('PATH')
  if normalize_path(path) not in normalize_path(env_path):
    print(f"Adding {path} in environ PATH")
    os.environ['PATH'] = env_path + f"{path_separator()}{path}"
    
def get_python_script_path():
  python_path = os.path.dirname(sys.executable)
  if os.name == 'nt':
    python_script_path = os.path.join(python_path, r'Scripts')
  elif os.name == 'posix':
    python_script_path = python_path
  return python_script_path


def main():
  ensure_in_environ_PATH(get_python_script_path())
  
  sys.argv = [
    'sphinx-autobuild', './source', './build/html_live',
    '--port', '8000',
    '--watch', '..',
  ]
  sphinx_autobuild.main()

if __name__ == '__main__':
  main()
