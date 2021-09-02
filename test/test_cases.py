import sys
sys.path.append('/../code/')
from fibonacci import fibonacci
def test_answer():
    print("testing")
    assert len(fibonacci.fibo(5))==5
