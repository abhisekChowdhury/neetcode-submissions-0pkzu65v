class Solution {
    public int lengthOfLongestSubstring(String s) {
        // two pointers initialized to 0
        int left = 0;
        int right = 0;
        // size of string
        int strLength = s.length();
        Set<Character> set = new HashSet<>();
        //Char sArray[] = s.toCharArray();
        int maxSize = 0;

        while (right < strLength) {
            if (!set.contains(s.charAt(right))) {
                set.add(s.charAt(right));
                right++;
            } else {
                while (set.contains(s.charAt(right))){
                    set.remove(s.charAt(left));
                    left++;
                }
            }

            maxSize = Math.max(right - left, maxSize);
        }

        return maxSize;
    }
}
