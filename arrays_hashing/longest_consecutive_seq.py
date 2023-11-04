class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        maxlen = 1
        numset = set(nums)
        for num in nums:
            if num - 1 not in numset:
                currlen = 1
                temp = num
                while temp + 1 in numset:
                    currlen += 1
                    temp += 1
                
                maxlen = max(maxlen, currlen)

        return maxlen

if __name__ == "__main__":
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

