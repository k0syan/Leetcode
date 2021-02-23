class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        var ans = [-1, -1]
        if nums.count == 0 {
            return ans
        }

        var low = 0
        var high = nums.count - 1

        while low < high {
            let mid = (low + high) / 2
            if nums[mid] < target {
                low = mid + 1
            } else {
                high = mid
            }
        }

        if nums[low] != target {
            return ans
        }
        ans[0] = low

        high = nums.count - 1
        while low < high {
            let mid = (low + high) / 2 + 1
            if nums[mid] > target {
                high = mid - 1
            } else {
                low = mid
            }
        }

        ans[1] = high

        return ans
    }
}
