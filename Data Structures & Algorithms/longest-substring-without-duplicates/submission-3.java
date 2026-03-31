class Solution {
    public int lengthOfLongestSubstring(String s) {
        int sLength = s.length();
        int left = 0;
        int right = 0;
        int maxSize = 0;
        Set<Character> sHash = new HashSet<>();

        while (right < sLength) {
            if (sHash.contains(s.charAt(right))){
                while(sHash.contains(s.charAt(right))) {
                    sHash.remove(s.charAt(left));
                    left++;
                }
            } else {
                sHash.add(s.charAt(right));
                right++;
            }

            maxSize = Math.max(right-left, maxSize);
        }

        return maxSize;
    }
}
