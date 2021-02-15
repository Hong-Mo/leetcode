class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = []
        count = 0

        for i in range(1, len(groupSizes) +1):

            while i in groupSizes :
                team = []
                for j in range(0, i):
                    k = groupSizes.index(i)
                    team.append(k)
                    groupSizes[k] = 0
                    count += 1

                group.append(team)

            if count == len(groupSizes):
                break

        return group