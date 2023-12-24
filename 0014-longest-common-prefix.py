class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix_str = strs[0]

        while True:
            for string in enumerate(strs):
                if string[0] == len(strs) - 1 and prefix_str in string[1][:len(prefix_str)]:
                    return prefix_str
                if prefix_str not in string[1][:len(prefix_str)]:
                    prefix_str = prefix_str[:-1]
                    break


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flowers","flow","flight"]))