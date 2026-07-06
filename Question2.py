from bisect import bisect_left
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0

    # tails[i] = smallest possible tail value of an increasing subsequence of length i+1
    tails = []

    for num in nums:
        pos = bisect_left(tails, num)  # find first index >= num
        if pos == len(tails):
            tails.append(num)          # num extends the largest subsequence so far
        else:
            tails[pos] = num           # num replaces an existing tail, keeping it minimal

    return len(tails)


# ---- Test ----
if __name__ == "__main__":
    print(lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
    print(lengthOfLIS([7, 7, 7, 7, 7]))      # 1
    print(lengthOfLIS([]))                    # 0