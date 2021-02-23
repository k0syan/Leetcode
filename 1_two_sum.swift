class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict: [[Int: Int]] = []
        for i in 0...nums.count - 1 {
            let n = nums[i]
            let m = target - n
            let x = dict.first {
                $0.first?.key == m
            }
            if x != nil {
                return[x!.first!.value, i]
            } else {
                dict.append([n:i])
            }
        }
        return [0, 0]
    }
}
