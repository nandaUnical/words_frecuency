import pytest
import app_code.code as cd

def test_nothing ():
    assert cd.sum(3,5) == 8
