class Solution {
    public int trap(int[] height) {
        int totalUnits = 0;
        int arrLength = height.length;
        int maxHeight = 0;
        int currentUnits = 0;
        int[] maxRightToLeft = new int[arrLength];
        int[] maxLeftToRight = new int[arrLength];

        // Populate maxRightToLeft array from left to right
        maxLeftToRight[0] = 0;
        for (int i = 1; i < arrLength-1; i++){
            maxHeight = Math.max(height[i-1], maxHeight);
            maxLeftToRight[i] = maxHeight;
        }

        // Populate maxLeftToRight array from right to left
        maxRightToLeft[arrLength-1] = 0;
        maxHeight = 0;
        for (int i = arrLength-2; i >= 0; i--) {
            maxHeight = Math.max(height[i+1],maxHeight);
            maxRightToLeft[i] = maxHeight;
        }

        System.out.println(Arrays.toString(maxLeftToRight));
        System.out.println(Arrays.toString(maxRightToLeft));

        // Calculate number of water units for each space and add with totalUnits;
        for (int i = 0; i < arrLength-1; i++) {
            currentUnits = Math.min(maxRightToLeft[i], maxLeftToRight[i]) - height[i];
            if (currentUnits <= 0) {
                currentUnits = 0;
            }

            totalUnits += currentUnits;

            System.out.println("Current Units " + currentUnits);
            System.out.println("Total Units " + totalUnits);
        }

        return totalUnits;
    }
}
