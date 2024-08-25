def removeElement(nums, val) -> int:
        p_num = 0
        while(p_num <= len(nums)):
            if nums[p_num] == val:
                nums.remove(val)
            else:
                p_num += 1
        count_nonval = len(nums)
        return count_nonval
removeElement([1,2,3,4,5,6], 3)