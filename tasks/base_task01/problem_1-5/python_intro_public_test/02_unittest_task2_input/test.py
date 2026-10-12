from task15 import int_to_roman
import pytest


@pytest.mark.parametrize(
    "num,ans",
    [
        [1, 'I'],
        [2, 'II'],
        [3, 'III'],
        [4, 'IV'],
        [5, 'V'],
        [6, 'VI'],
        [7, 'VII'],
        [9, "IX"],
        [10, 'X'],
        [20, 'XX'],
        [50, 'L'],
        [54, 'LIV'],
        [90, "XC"],
        [100, 'C'],
        [199, "CXCIX"],
        [328, "CCCXXVIII"],
        [400, "CD"],
        [500, 'D'],
        [754, "DCCLIV"],
        [888, "DCCCLXXXVIII"],
        [973, "CMLXXIII"],
        [1000, 'M'],
        [1996, 'MCMXCVI'],
        [2143, "MMCXLIII"]
    ]
)
def test_int_to_roman(num, ans):
    assert int_to_roman(num) == ans

