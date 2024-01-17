class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrence_map = {}
        for number in arr:
            if number not in occurrence_map:
                occurrence_map[number] = 1
            else:
                occurrence_map[number] += 1

        occurrences = []
        for item in occurrence_map:
            if occurrence_map[item] not in occurrences:
                occurrences.append(occurrence_map[item])
            else:
                return False
        return True
            
if __name__ == "__main__":
    sol = Solution()
    ans = sol.uniqueOccurrences([1,2,2,1,1,3])
    print(ans)
    