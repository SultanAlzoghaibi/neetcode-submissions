class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        countHash = defaultdict(int)
        mostFreqNum = 0
        mostFreq = "n"
        l, r = 0, 0
        maxSize = 0
        size = 0

        while r < len(s):
            countHash[s[r]] += 1

            # Update most frequent char count in the current window
            mostFreqNum = max(mostFreqNum, countHash[s[r]])

            size = r - l + 1  # include r, not abs(l - r)

            # If we need to replace more than k letters, shrink the window
            if size - mostFreqNum > k:
                countHash[s[l]] -= 1
                l += 1
                size = r - l + 1  # recalculate after shrink

            maxSize = max(maxSize, size)
            r += 1
            
        return maxSize


