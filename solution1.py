class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        duplicatesNums = {}
        output = []
        for num in nums:
            duplicatesNums[num] = duplicatesNums.get(num, 0) + 1
        for num, duplicates in duplicatesNums.items():
            for i in range(duplicates):
                if len(output) <= i:
                    output.append([])
                output[i].append(num)
        return output
