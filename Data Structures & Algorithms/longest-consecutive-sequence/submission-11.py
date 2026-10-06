class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(set(nums))
        if len(sorted_nums) == 1:
            return 1

        groups = []
        sub_group = []
        for i in range(len(sorted_nums)-1):
            if i == 0:
                sub_group.append(sorted_nums[i])

            if sorted_nums[i+1] == sorted_nums[i] + 1:
                sub_group.append(sorted_nums[i+1])
            else:
                groups.append(sub_group)
                sub_group = []
                sub_group.append(sorted_nums[i+1])
            
        groups.append(sub_group)
        print(groups)

        counter = 0
        for group in groups:
            if len(group) > counter:
                counter = len(group)
        
        return counter