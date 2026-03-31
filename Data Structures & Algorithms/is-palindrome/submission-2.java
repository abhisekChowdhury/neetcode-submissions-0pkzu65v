class Solution {
    public boolean isPalindrome(String s) {
        String temp = s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();
        int left = 0;
        char[] charS = temp.toCharArray();
        //System.out.println(charS);
        int right = charS.length-1;
        while (left < right){
            if (charS[left] != charS[right]){
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
