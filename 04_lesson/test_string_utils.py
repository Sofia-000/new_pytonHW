import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("sofia", "Sofia"),
]
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123qwerty", "123qwerty"),
    ("", ""),
    ("   ", "   "),
]
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("", ""),
    ("   ", ""),
]
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   123abc", "123abc"),
    ("   04 april 2023", "04 april 2023"),
    ("  SkyPro", "SkyPro"),
]
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, Symbol ", [
    ("SkyPro", "y"),
    ("qwerty", "w"),
    ("asd3", "3"),
    ("12.12.25", "."),
    ("@@@", "@"),
]
)
def test_contains_positive(input_str, Symbol):
    assert string_utils.contains(input_str, Symbol) == True


@pytest.mark.positive
@pytest.mark.parametrize("input_str, Symbol ", [
    ("SkyPro", "t"),
    ("Abcd", "Ae"),  # Баг-репорт в файле "Defects.txt", баг №1
    (" sd4", "3"),
    ("12/12/25", "3"),
    ("@@@", "a"),
    ("S", "s")  # Баг-репорт в файле "Defects.txt", баг №2
]
)
def test_contains_positive(input_str, Symbol):
    assert string_utils.contains(input_str, Symbol) == False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, Symbol ,expected", [
    ("SkyPro", "P", "Skyro"),
    (" Qwerty", " ", "Qwerty"),
    ("aosjdl3", "3", "osjdl3"),
    ("12/12/25", "12/12/25", ""),
]
)
def test_delete_symbol_positive(input_str, Symbol, expected):
    assert string_utils.delete_symbol(input_str, Symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, Symbol ,expected", [
    ("", "", ""),
    ("A_bcd", "_", "Abcd"),
    ("   ", "   ", ""),
    ("Вика", "л", "Вика"),  # Баг-репорт в файле "Defects.txt", баг №3
    ("@@@   ", "   ", "@@@"),
]
)
def test_delete_symbol_positive(input_str, Symbol, expected):
    assert string_utils.delete_symbol(input_str, Symbol) == expected
    print(expected)
