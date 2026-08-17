class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        num1=num1+num2
        num1.sort()
        mid=len(num1)//2
        if len(num1)%2!=0:
            return float(num1[mid])
        else:return (num1[mid-1]+ num1[mid])/2.0
        