class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # find the matrix row which could contain the target
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break
        
        searchlist = matrix[(l + r)//2]
        l, r = 0, len(searchlist) - 1

        # search within the row which could contain the target
        while l <= r:
            mid = (l + r)//2

            if searchlist[mid] == target:
                return True
            elif searchlist[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False