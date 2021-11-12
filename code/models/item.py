class Item:
    def __init__(self, album, support, cost, selling_price, in_stock, ordered, pre_booked, id = None):
        self.album = album
        self.support = support
        self.cost = cost
        self.selling_price = selling_price
        self.in_stock = in_stock
        self.ordered = ordered
        self.pre_booked = pre_booked
        self.id = id
