class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        seen = set()

        ret = []
        i = 0
        while i < len(nums):
            if nums[i] not in seen:
                seen.add(nums[i])
                currtarget = 0 - nums[i]

                l, r = i + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == currtarget:
                        ret.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    elif nums[l] + nums[r] > currtarget:
                        r -= 1
                    else:
                        l += 1
            i += 1

        return ret