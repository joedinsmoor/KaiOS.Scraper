import pytest 

def f():
    raise SystemExit(1)

def test():
    with pytest.raises(SystemExit):
        f()