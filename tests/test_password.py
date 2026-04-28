"""
    Validates a password based on:
    - Minimum length of 8
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one special character
    Returns True if valid, otherwise raises ValueError.
    Unit tests for passwordcheck.py
"""
import pytest
from password import *

def test_valid_password():
    assert check_password("12345Nl!") == True

def test_password__too_short():
    with pytest.raises(ValueError):
        check_password("aarond")

def test_no_uppercase():
    with pytest.raises(ValueError):
        check_password("aarondunne!")

def test_no_lowercase():
    with pytest.raises(ValueError):
        check_password("AARONDUNNE!")

def test_no_schar():
    with pytest.raises(ValueError):
        check_password("Aarondunn")

def test_password_length():
    with pytest.raises(ValueError):
        check_password("Aarondun")

