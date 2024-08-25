# test_remove_element.py
import pytest
from myfile import removeElement  # add the test function

def test_remove_element_success(): # this one will pass
    nums = [1, 2, 3, 4, 5, 6]
    result = removeElement(nums, 3)
    assert result == 5  
    assert nums == [1, 2, 4, 5, 6]  

def test_remove_element_failure():# fails
    nums = [3, 4, 5, 6]
    result = removeElement(nums, 3)
    assert result == 3  
    assert nums == [4, 5, 6]  
