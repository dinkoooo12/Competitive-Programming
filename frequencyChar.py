from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        charFreq = defaultdict(int)
        for char in s:
            charFreq[char] += 1

        sortedChars = sorted(charFreq.keys(), key=lambda x: charFreq[x], reverse=True)
        sortedString = ''.join(char * charFreq[char] for char in sortedChars)
        return sortedString