from sortedcontainers import SortedList

class StockPrice:
    def __init__(self):
        self.max_timestamp = -1
        self.price_map = {}
        self.price_list = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        self.max_timestamp = max(self.max_timestamp, timestamp)
        if timestamp in self.price_map:
            old_price = self.price_map[timestamp]
            self.price_list.remove(old_price)

        self.price_map[timestamp] = price
        self.price_list.add(price)
        
    def current(self) -> int:
        return self.price_map[self.max_timestamp]

    def maximum(self) -> int:
        return self.price_list[-1]
        
    def minimum(self) -> int:
        return self.price_list[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
