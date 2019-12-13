'''
Created on 12 dic 2019

@author: Andrea
'''
import unittest

import os

import sys

from docs import auto_build


def python_path():
  return os.path.dirname(sys.executable)


class Test(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass
  
  def test_linux(self):
    os.name = 'posix'

    self.assertEqual(':', auto_build.path_separator())

    self.assertEqual(
      auto_build.normalize_path(f'{python_path()}'),
      auto_build.normalize_path(auto_build.get_python_script_path())
    )

  def test_windows(self):
    os.name = 'nt'

    self.assertEqual(';', auto_build.path_separator())

    self.assertEqual(
      auto_build.normalize_path(f'{python_path()}/Scripts'),
      auto_build.normalize_path(auto_build.get_python_script_path())
    )


if __name__ == "__main__":
  #import sys;sys.argv = ['', 'Test.testName']
  unittest.main()