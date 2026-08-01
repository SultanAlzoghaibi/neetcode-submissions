class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for str1 in strs:
            num = len(str1)
            ans += str(num) + '#' + str1
        print(ans)
        return ans




    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            n = int(s[i:j])

            ans.append( s[j+1 : j+1+n])

            i = j + 1 + n

        return ans
