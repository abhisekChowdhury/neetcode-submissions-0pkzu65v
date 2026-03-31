class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int s1Length = s1.length();
        int s2Length = s2.length();
        String currentString = "";

        int[] s1Count = new int[26];
        int[] s2Count = new int[26];

        // initial window
        for (int i = 0; i < s1Length; i++) {
            s1Count[s1.charAt(i) - 'a']++;
            s2Count[s2.charAt(i) - 'a']++;
        }

        if (Arrays.equals(s1Count, s2Count)) return true;

        for (int i = s1Length; i < s2Length; i++) {
            // sliding window
            // adding right element
            s2Count[s2.charAt(i) - 'a']++;
            // removing left element
            s2Count[s2.charAt(i-s1Length) - 'a']--;
        
            if (Arrays.equals(s1Count, s2Count)) return true;
        }

        return false;
    }
}
