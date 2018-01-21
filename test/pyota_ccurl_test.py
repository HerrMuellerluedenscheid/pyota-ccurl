# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from unittest import TestCase

from pyota_ccurl import is_installed
from ccurl import Curl


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
    print(dir(Curl))
    #print(dir(ccurl))
    # Curl.local_pow()
    print('XX')

  def test_pearl_diver(self):
    """
    Verify that the C extension is installed correctly.
    """
    from ccurl import Curl
    from iota import TryteString

    # "trits", "length", "min_weight_manitudes", "number_of_threads
    # Curl().pearl_diver(trits=[111], length=1, min_weight_manitude=1, number_of_threads=1)
    c = Curl()
    trits = TryteString.from_string('TEST')
    c.pearl_diver([trits], 1, 1, 1)
