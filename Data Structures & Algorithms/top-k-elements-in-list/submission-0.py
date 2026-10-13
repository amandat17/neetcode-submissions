from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kCount= Counter(nums)
        most_frequent = kCount.most_common(k)
        result =[]
        for num, count in most_frequent:
            result.append(num)
        return result

        


