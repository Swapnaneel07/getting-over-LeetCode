class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxa=0
        while r>l:
            h,b=min(height[r],height[l]),r-l
            ar=h*b
            if ar>maxa:maxa=ar
            
            if height[r]>height[l]:l=l+1
            else:r=r-1
        return maxa


        