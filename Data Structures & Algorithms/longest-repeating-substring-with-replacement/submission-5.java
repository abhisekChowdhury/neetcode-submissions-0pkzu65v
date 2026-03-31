class Solution {
    public int characterReplacement(String s, int k) {
        // Create a frequency array of size 26
        // Count the frequency of each character in the string
        // Get the maximum value from the array
        // Return maximum value + k

        int[] frequency = new int[26];
        int left = 0;
        int windowSize = 0;
        int length = s.length();
        int maxLength = 0;

        for (int right = 0; right < length; right++) { 
            frequency[s.charAt(right) - 'A']++;
            windowSize = Math.max(windowSize, frequency[s.charAt(right)-'A']);

            while (right - left + 1 - windowSize > k) {
                frequency[s.charAt(left) - 'A']--;
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
