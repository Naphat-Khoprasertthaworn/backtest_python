from constant import global_order_number, update_global_order_number, LOT_CONSTANT


class Order:
    __price = 0
    __lot = 0
    __order_number = 0
    __type_order = 0  # 0 = bid , 1 = ask

    def __init__(self, price, lot, type_order):
        self.__price = price
        self.__lot = lot*LOT_CONSTANT
        self.__order_number = global_order_number
        self.__type_order = type_order
        update_global_order_number()

    def get_price(self):
        return self.__price

    def get_lot(self):
        return self.__lot

    def get_order_number(self):
        return self.__order_number

    def get_order_type(self):
        return self.__type_order
