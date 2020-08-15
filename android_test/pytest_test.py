import pytest
def fun(a):
    return a+1

def test_answer():
    assert fun(2)==3
