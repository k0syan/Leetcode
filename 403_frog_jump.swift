class Solution {
    func canCross(_ stones: [Int]) -> Bool {
        var visited: [[Int]: Bool] = [:]
        var stoneIndexes: [Int: Bool] = [:]
        for s in stones {
            stoneIndexes[s] = true
        }
        let finish = stones.last

        func jump(start: Int, step: Int) -> Bool {
            // het gnal kam mnal texum animasta
            if step < 1 {
                return false
            }

            let end = start + step
            // hasanq tex
            if end == finish {
                return true
            }

            // ho jury chyngar aper
            if stoneIndexes[end] == nil {
                return false
            }

            // es qaylov stegh exel enq
            if visited[[start, step]] != nil {
                return false
            }

            visited[[start, step]] = true

            // k-1, k, k+1 stepov nuyn bany stugel
            return jump(start: end, step: step - 1) || jump(start: end, step: step) || jump(start: end, step: step + 1)
        }

        return jump(start: stones[0], step: 1)
    }
}
