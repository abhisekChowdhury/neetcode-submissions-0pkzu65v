class Solution {
    public int maxProfit(int[] prices) {
        // set two pointers - buy and sell
        int buy = 0;
        int sell = 0;
        int profit = 0;
        int length = prices.length;

        while (sell < length) {
            if (prices[buy] < prices[sell]) {
                profit = Math.max(prices[sell] - prices[buy], profit);
            } else {
                buy = sell;
            }

            sell++;
        }

        return profit;
    }
}
