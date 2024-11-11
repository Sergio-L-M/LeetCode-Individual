class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        prevDup = nums[0]
        output.append([prevDup])
        i = 1
        pointerOutput = 1
        lenNum = len(nums)
        
        while(i < lenNum):
            if prevDup == nums[i]:
                if len(output) <= pointerOutput + 1:
                    output.append([nums[i]])
                else:
                    output[pointerOutput + 1].append(nums[i])
                pointerOutput += 1
            else:
                pointerOutput = 0
                prevDup = nums[i]
                output[pointerOutput].append(nums[i])
            
            i += 1
        return output
