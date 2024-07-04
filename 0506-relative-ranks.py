class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse=True)
        idxMap = {}
        for i in range(len(sorted_score)):
            idxMap[sorted_score[i]] = i

        output = []
        for s in score:
            pos = idxMap[s]
            if pos == 0:
                output.append("Gold Medal")
            elif pos == 1:
                output.append("Silver Medal")
            elif pos == 2:
                output.append("Bronze Medal")
            else:
                output.append(str(pos+1))
        return output