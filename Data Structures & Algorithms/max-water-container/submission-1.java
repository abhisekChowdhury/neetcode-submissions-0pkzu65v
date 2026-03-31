class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length-1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            //find the minimum height since that is the limiting factor
            int minHeight = Math.min(heights[left],heights[right]);
            int area = width*minHeight;

            maxArea = Math.max(maxArea,area);

            // bring the lower height inward
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
}
