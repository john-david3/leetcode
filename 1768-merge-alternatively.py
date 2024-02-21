class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        n = min(len(word1), len(word2))
        for i in range(n):
            merged_str += word1[i]
            merged_str += word2[i]
        if len(word1) > len(word2):
            merged_str += word1[i+1:]
        else:
            merged_str += word2[i+1:]
        return merged_str