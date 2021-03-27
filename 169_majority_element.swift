class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var mem: [Int: Int] = [:]
        for n in nums {
            if mem[n] != nil {
                mem[n]! += 1
            } else {
                mem[n] = 1
            }
        }
        let max = mem.max {a, b in a.value < b.value}
        return max!.key
    }
}
