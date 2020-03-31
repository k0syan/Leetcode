from typing import List


def rob(nums: List[int]) -> int:
    ri, rj = 0, 0
    for i in range(len(nums)):
        if i % 2 == 0:
            ri = max(ri + nums[i], rj)
        else:
            rj = max(rj + nums[i], ri)
    return max(ri, rj)


print(rob([2, 1, 1, 2]))
