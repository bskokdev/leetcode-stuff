class StockSpanner:

    def __init__(self):
        # store a pair of (price, less_count)
        # less_count defaults to 1
        self.stack = []
        
    def next(self, price: int) -> int:
        # the span is max num of days (going backwards) for which stock price was <= to this day
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            cur_price, cur_span = self.stack.pop()
            res += cur_span
        self.stack.append((price, res))
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)