class Solution(object):
    def find_indexInNums(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) == target:
                    return [i,j]
        return [-1,-1]

if __name__ == '__main__':
    s = Solution()
    nums = range(100)
    target = 102

    print(s.find_indexInNums(nums,target))


