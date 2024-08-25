# test_remove_element.py
import pytest
from your_code_file import removeElement  # 替换为实际的代码文件名

def test_remove_element_success():
    nums = [1, 2, 3, 4, 5, 6]
    result = removeElement(nums, 3)
    assert result == 5  # 期望的长度是 5，因为 3 应该被移除
    assert nums == [1, 2, 4, 5, 6]  # 期望的列表是 [1, 2, 4, 5, 6]

def test_remove_element_failure():
    nums = [1, 2, 3, 4, 5, 6]
    result = removeElement(nums, 3)
    assert result == 4  # 故意设置错误的期望值
    assert nums == [1, 2, 4, 5, 6]  # 期望的列表是 [1, 2, 4, 5, 6]
