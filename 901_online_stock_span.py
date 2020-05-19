class StockSpanner:
    def __init__(self):
        self.struct = []
        
    def next(self, price: int) -> int:
        weight = 1
        while self.struct and self.struct[-1][0] <= price:
            weight += self.struct.pop()[1]
        self.struct.append((price, weight))
        return weight
