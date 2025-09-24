class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            new_target = 0
            new_target += target - nums[i]
            if new_target in nums[i+1:]:
                ans.append(i)
                ans.append(nums.index(new_target, i+1))
                return (ans)
                break
            else:
                i += 1
