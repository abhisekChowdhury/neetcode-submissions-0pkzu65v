class Solution {
    public boolean isAnagram(String s, String t) {
        // 1. Store s and t in character arrays
        // 2. Sort s and t
        // 3. Compare the strings

        char sChar[] = s.toCharArray();
        char tChar[] = t.toCharArray();

        Arrays.sort(sChar);
        Arrays.sort(tChar);

        // System.out.println("sChar: " + Arrays.toString(sChar) + "\n");
        // System.out.println("tChar: " + Arrays.toString(tChar));

        if (Arrays.toString(sChar).equals(Arrays.toString(tChar))){
            return true;
        } 

        return false;
    }
}
