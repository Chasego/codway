# @ cchen
# based on the lecture of 'Two Pointers' in Advanced Programming Class

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        res = 0

        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            tmp = min(height[i], height[j]) * (j - i)
            res = max(res, tmp)
        return res
