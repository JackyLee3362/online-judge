var StockSpanner = function() {
    this.stack = [];
};

/** 
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function(price) {
    next = [price, 1];
    while(this.stack.length && price >= this.stack[this.stack.length-1][0])
    {
        var tmp = this.stack.pop();
        next[1] += tmp[1];
    }
    this.stack.push(next);
    return next[1];
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */
const nums = [100, 80, 60, 70, 60, 75, 85];
var stock = new StockSpanner();
for(var i = 0; i < nums.length; i++){
    console.log(stock.next(nums[i]));
}