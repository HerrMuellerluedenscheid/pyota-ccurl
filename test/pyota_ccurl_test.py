# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

from unittest import TestCase

from pyota_ccurl import is_installed
from ccurl import Curl
from iota import TryteString


class IsInstalledTestCase(TestCase):
  def test_is_installed(self):
    """
    Verify that the C extension is installed correctly.
    """
    self.assertTrue(is_installed())

  def test_pow(self):
    """
    test pearl diver

    #define TRYTE_LENGTH 2673
    #define TRANSACTION_LENGTH TRYTE_LENGTH * 3

    Values from test_pearl_diver_search in c tests
    """
    tryte_length = 2673
    transaction_length = tryte_length * 3
    nonce_size = 13

    s = TryteString.from_string('Test')
    trits = s.as_trits()
    Curl().pearl_diver(trits, transaction_length, nonce_size, 8)