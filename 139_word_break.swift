class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {
        var mem = [Bool](repeating: false, count: s.count + 1)
        let arrayWord = Array(s)
        mem[0] = true
        for i in 0...arrayWord.count - 1 {
            for j in i...arrayWord.count - 1 {
                let tmpWord = String(arrayWord[i...j])
                if mem[i] && wordDict.contains(tmpWord) {
                    mem[j + 1] = true
                }

            }
        }
        return mem[mem.count - 1]
    }
}
