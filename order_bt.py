import globals


class Order:
    __price = 0
    __lot = 0
    __order_number = 0
    __order_type = 0  # 0 = bid , 1 = ask

    def __init__(self, price, lot, type_order):
        self.__price = price
        self.__lot = lot*globals.LOT_CONSTANT
        self.__order_number = globals.global_order_number

        self.__order_type = type_order
        globals.update_global_order_number()

    def __str__(self):
        return "{order_number="+str(self.__order_number)+" order_type="+str(self.__order_type)+" order_lot="+str(self.__lot)+" price="+str(self.__price)+"}"

    def get_price(self):
        return self.__price

    def get_lot(self):
        return self.__lot

    def get_order_number(self):
        return self.__order_number

    def get_order_type(self):
        return self.__order_type
