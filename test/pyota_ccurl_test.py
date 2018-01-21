# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from unittest import TestCase

from pyota_ccurl import is_installed


class IsInstalledTestCase(TestCase):
  def test_is_installed(self):
    """
    Verify that the C extension is installed correctly.
    """
    self.assertTrue(is_installed())

  def test_pow(self):
    """
    Verify that the C extension is installed correctly.
    """
    from ccurl import Curl
    print(dir(Curl))
    #print(dir(ccurl))
    Curl.local_pow()
    print('XX')
