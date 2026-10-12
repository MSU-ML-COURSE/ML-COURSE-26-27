from task15 import longest_common_prefix
import pytest


@pytest.mark.parametrize(
    "arg,res",
    [
        [["flower","flow","flight"], "fl"],
        [["      flower","  flow"," flight", "flight    "], "fl"],
        [["dog","racecar","car"], ""],
        [["c","cc","ccc"], "c"],
        [["","  ","   "], ""],
        [[" ","  ","   "], ""],
        [["123"," 1 23","12 3"], "1"],
        [["1" for _ in range(100)], "1"],
        [["23" + str(i) for i in range(100)], "23"],
        [[" ML;", "\t\t\tML", "\n \tML"], "ML"],
        [[], ""]
    ]
)
def test_prefix(arg, res):
    assert longest_common_prefix(arg) == res
