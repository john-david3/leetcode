class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        indexes = {}
        for i in range(len(list1)):
            indexes[list1[i]] = i

        output = []
        lowest = float("inf")
        for j in range(len(list2)):
            if list2[j] in list1:
                total = j + indexes[list2[j]]
                if total < lowest:
                    output = []
                    output.append(list2[j])
                    lowest = total
                elif total == lowest:
                    output.append(list2[j])
        return output