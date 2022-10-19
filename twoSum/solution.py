class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    hash = {}
    
    for i, n in enumerate(nums):
      if target - n in hash:
        return [hash[target-n], i]
      hash[n] = i