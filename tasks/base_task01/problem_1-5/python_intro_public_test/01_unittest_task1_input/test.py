from task15 import hello
import pytest

# task 1
@pytest.mark.parametrize(
    "arg,res",
    [
        ('', 'Hello!'),
        ('Masha', 'Hello, Masha!'),
        (' ', 'Hello,  !'),
        ('r', 'Hello, r!'),
        ('123', 'Hello, 123!'),
        ('I love machine learning', 'Hello, I love machine learning!')
    ]
)
def test_one_argument(arg, res):
    assert hello(arg) == res


def test_no_arguments():
    assert hello() == 'Hello!'
