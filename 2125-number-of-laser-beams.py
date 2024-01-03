class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        total = 0
        x = 0
        counter = 1
        while x + counter < len(bank):
            r1 = bank[x].count("1")
            r2 = bank[x + counter].count("1")

            if r1 == 0:
                x += 1
                continue
            elif r2 == 0:
                counter += 1
                continue
            else:
                total += r1 * r2
                x += counter
                counter = 1

        return total

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfBeams(["011001","000000","010100","001000"]))