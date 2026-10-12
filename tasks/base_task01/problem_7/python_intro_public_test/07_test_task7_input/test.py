from task7 import find_modified_max_argmax
import pytest

class A(int):
    def __init__(self):
        pass

@pytest.mark.parametrize(
    "arg1,arg2,res",
    [
        [[1, 3, 4, 4.5], lambda x: x ** 2, (16, 2)],
        [["str", "1", 23, 4, 65], lambda x: -x + 2, (-2, 1)],
        [["str", 4, 4.5, 2, '-2', '3', -8], lambda x: abs(x) - 10, (-2, 2)],
        [["str", '-2', '3'], lambda x: abs(x) - 10, ()],
        [[A(), 1, 2], lambda x: x, (2, 1)],
        [[], lambda x: abs(x) - 10, ()]
    ]
)
def test_find_shortest(arg1, arg2, res):
    assert find_modified_max_argmax(arg1, arg2) == res