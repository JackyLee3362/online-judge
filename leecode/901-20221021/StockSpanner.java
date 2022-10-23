import java.util.Stack;

class StockSpanner {
    Stack<Integer> prices, weights;

    public StockSpanner() {
        prices = new Stack<Integer>();
        weights = new Stack<Integer>();
    }

    public int next(int price) {
        int w = 1;
        while (!prices.isEmpty() && price >= prices.peek()) {
            prices.pop();
            w += weights.pop();
        }
        prices.push(price);
        weights.push(w);

        return w;

    }

    public static void main(String args[]) {
        System.out.println("test");
        StockSpanner obj = new StockSpanner();
        int[] nums = { 100, 80, 60, 70, 60, 75, 85 };
        for (int i = 0; i < nums.length; i++) {
            System.out.println(obj.next(nums[i]));
        }
    }
}