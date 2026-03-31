class Solution {
    public boolean isPalindrome(String s) {
        String cleaned = s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();

        String reversed = new StringBuilder(cleaned).reverse().toString();
        if (cleaned.equals(reversed)){
            return true;
        } else {
            return false;
        }
    }
}
