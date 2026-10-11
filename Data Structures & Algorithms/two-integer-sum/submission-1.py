class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            summation = target - num

            if summation in seen:
                return [seen[summation],i]
            #stores as dictionary {3:0}
            #the number 3 is at index 0
            seen[num]=i
