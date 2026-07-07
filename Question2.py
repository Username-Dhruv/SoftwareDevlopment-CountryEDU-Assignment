from bisect import bisect_left
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
        
    tails = []

    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


# Examples:
if __name__ == "__main__":
    print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(lengthOfLIS([7, 7, 7, 7, 7]))  
    print(lengthOfLIS([]))