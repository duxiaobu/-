class Solution:
    def romanToInt(self, s: str) -> int:
        Roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        Int = 0

        for index in range(len(s) - 1):
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
                Int -= Roman2Int[s[index]]
            else:
                Int += Roman2Int[s[index]]

        return Int + Roman2Int[s[-1]]


if __name__ == '__main__':
    # 输入: "MCMXCIV"
    # 输出: 1994
    # 解释: M = 1000, CM = 900, XC = 90, IV = 4
    x = 'MCMXCIV'
    s = Solution()
    print(s.romanToInt(x))
