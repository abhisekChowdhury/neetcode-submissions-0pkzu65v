class Solution {
    public int maxProfit(int[] prices) {
        // set two pointers, buy and sell to 0
        int buy = 0;
        int sell = 0;
        int maxProfit = 0;
        int arrLength = prices.length;

        while (sell < arrLength) {
            if (prices[buy] <= prices[sell]) {
                maxProfit = Math.max(prices[sell] - prices[buy], maxProfit);
            } else {
                buy = sell;
            }

            sell++;
        }

        return maxProfit;
    }
}
