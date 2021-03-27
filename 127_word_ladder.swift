class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        let chars = Array("abcdefghijklmnopqrstuvwxyz")
        let wordsList = Set(wordList)
        var distances: [String: Int] = [:]
        var wordsQueue: [String] = []
        var startPos = 0
        var endPos = 1
        distances[beginWord] = 1
        wordsQueue.append(beginWord)
        if !wordsList.contains(endWord) {
            return 0
        }

        while startPos < endPos {
            let curWord = wordsQueue[startPos]
            let curentWord = Array(curWord)
            let value = distances[curWord]
            for i in 0..<curentWord.count {
                for c in chars {
                    var newWord = curentWord
                    newWord[i] = c
                    let newWordString = String(newWord)
                    if newWordString == endWord {
                        return value! + 1
                    }
                    if wordsList.contains(newWordString) && distances[newWordString] == nil {
                        distances[newWordString] = value! + 1
                        wordsQueue.append(newWordString)
                        endPos += 1
                    }
                }
            }
            startPos += 1
        }

        return 0
    }
}
