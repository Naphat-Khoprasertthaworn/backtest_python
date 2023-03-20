from order_bt import Order


class Account:
    __order_list = []
    __equity = 0

    def __init__(self, equity):
        self.__order_list = list()

        self.__equity = equity

    def get_equity(self):
        return self.__equity

    def set_equity(self, equity):  # return false if bankrupt
        self.__equity = equity
        return self.__equity > 0

    def get_order_list(self):
        return self.__order_list

    def add_order(self, order):
        if isinstance(order, Order):
            self.__order_list.append(order)
            return True
        return False

    def close_order(self, order):
        if isinstance(order, Order):
            index = self.search_order(order.get_order_number())
            if index < 0:
                return False
            self.__order_list.pop(index)
            return True
        return False

    def search_order(self, order_number):
        left = 0
        right = len(self.__order_list)
        while True:
            mid = (left + right) // 2
            if right <= left:
                return -1
            if self.__order_list[mid].get_order_number() < order_number:
                right = mid
            elif self.__order_list[mid].get_order_number() > order_number:
                left = mid
            else:
                return mid
