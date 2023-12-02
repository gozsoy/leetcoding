import pytest
from sorting import merge_sort, bubble_sort, \
                    selection_sort, insertion_sort, \
                    quick_sort

test_pairs = [([-100, 5, 0, 2, 9, -1010], [-1010, -100, 0, 2, 5, 9]),
              ([10, 11, 12, 13, 14, 15], [10, 11, 12, 13, 14, 15]),
              ([], []),
              ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7,]),
              ([6, 6, 6, 6, 6, 6, 6], [6, 6, 6, 6, 6, 6, 6]),
              ([4, 5, 2, 2, 3, 3, 1, 4], [1, 2, 2, 3, 3, 4, 4, 5])]    
            

@pytest.mark.parametrize("test_input, expected", test_pairs)
def test_merge_sort(test_input, expected):
    assert merge_sort(test_input) == expected


@pytest.mark.parametrize("test_input, expected", test_pairs)
def test_bubble_sort(test_input, expected):
    assert bubble_sort(test_input) == expected


@pytest.mark.parametrize("test_input, expected", test_pairs)
def test_selection_sort(test_input, expected):
    assert selection_sort(test_input) == expected


@pytest.mark.parametrize("test_input, expected", test_pairs)
def test_insertion_sort(test_input, expected):
    assert insertion_sort(test_input) == expected


@pytest.mark.parametrize("test_input, expected", test_pairs)
def test_quick_sort(test_input, expected):
    assert quick_sort(test_input) == expected