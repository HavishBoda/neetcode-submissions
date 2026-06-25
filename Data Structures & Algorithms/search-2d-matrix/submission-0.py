class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        low = 0
        high = ROWS-1

        while low <= high:
            mid = low + (high-low)//2
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                if target == matrix[mid][COLS-1]:
                    return True
                elif target < matrix[mid][COLS-1]:
                    # binary search in this row
                    l = 0
                    r = COLS-1
                    while l <= r:
                        middle = l + (r-l)//2
                        if target == matrix[mid][middle]:
                            return True
                        elif target > matrix[mid][middle]:
                            l = middle + 1
                        else:
                            r = middle - 1
                    return False
                else:
                    low = mid + 1
            else:
                if mid == 0:
                    return False
                if target > matrix[mid-1][0]:
                    # binary search in this row
                    l = 0
                    r = COLS-1
                    while l <= r:
                        middle = l + (r-l)//2
                        if target == matrix[mid-1][middle]:
                            return True
                        elif target > matrix[mid-1][middle]:
                            l = middle + 1
                        else:
                            r = middle - 1
                    return False
                else:
                    high = mid-1
        
        return False
