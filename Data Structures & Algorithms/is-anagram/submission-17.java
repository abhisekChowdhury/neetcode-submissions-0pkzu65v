class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        } else {
            HashMap<Character, Integer> sHash = new HashMap<Character, Integer>();
            HashMap<Character, Integer> tHash = new HashMap<Character, Integer>();

            for (char c : s.toCharArray()) {
                sHash.put(c, sHash.getOrDefault(c,0) + 1);
            }

            for (char c : t.toCharArray()) {
                tHash.put(c, tHash.getOrDefault(c,0) + 1);
            }

            if (!sHash.equals(tHash)) {
                return false;
            }

            System.out.println(sHash);
            System.out.println(tHash);
            
            return true;
        }
    }
}
