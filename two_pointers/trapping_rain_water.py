# SC: O(n), TC: O(n)
class Solution1:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        maxL, maxR = [0] * n, [0] * n

        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i - 1])
            maxR[n - i - 1] = max(maxR[n - i], height[n - i])

        totalWater = 0
        for i in range(n):
            trappedWater = max(min(maxR[i], maxL[i]) - height[i], 0)
            totalWater += trappedWater

        return totalWater

class Solution2:
    def trap(self, height: list[int]) -> int:
        ans, maxL, maxR = 0, 0, 0

        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                if height[l] < maxL:
                    ans += maxL - height[l]
                else:
                    maxL = height[l]
                l += 1
            else:
                if height[r] < maxR:
                    ans += maxR - height[r]
                else:
                    maxR = height[r]
                r -= 1
        
        return ans

