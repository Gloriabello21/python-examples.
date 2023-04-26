# estos ejemplo se corren pytest test_name.py
#ejemplo1
from hello import hello

def test_hello():
    hello("gloria") == "hello, gloria"

#ejemplo2
from hello import hello

def test_hello():
    assert hello("gloria") == "hello, gloria"

#ejemplo3
from hello import hello

def test_hello():
    assert hello("gloria") == "hello, gloria"
    assert hello("gloria") == "hello, world"

#ejemplo4
from hello import hello

def test_hello():
    assert hello("gloria") == "hello, world"

def test_argument():
    assert hello("gloria") == "hello, gloria"    



