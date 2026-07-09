class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        half = totalLen//2

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        l = 0       
        r = len(A) - 1

        while True:
            
            i = (l+r)//2 # A
            j = half - i - 2 # B

            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i+1] if i+1 < len(A) else float("inf")
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j+1] if j+1 < len(B) else float("inf")

            if ALeft <= BRight and BLeft <= ARight:
                # if odd
                if totalLen % 2 == 1:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight))/2
            if ALeft > BRight:
                r = i-1
            else:
                l = i+1