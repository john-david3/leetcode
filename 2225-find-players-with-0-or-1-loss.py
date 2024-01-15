class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loser_map = {}
        for match in matches:
            if match[1] not in loser_map:
                loser_map[match[1]] = 1
            elif match[1] in loser_map:
                loser_map[match[1]] += 1

            if match[0] not in loser_map:
                loser_map[match[0]] = 0

        no_losses = []
        one_loss = []

        for match in loser_map:
            if loser_map[match] == 0:
                no_losses.append(match)
            elif loser_map[match] == 1:
                one_loss.append(match)

        no_losses.sort()
        one_loss.sort()

        return [no_losses, one_loss]
        
if __name__ == "__main__":
    sol = Solution()
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    ans = sol.findWinners(matches)
    print(ans)