global global_order_number
global LOT_CONSTANT
global global_index


def initialize():
    global global_order_number
    global LOT_CONSTANT
    global global_index
    LOT_CONSTANT = 100000
    global_order_number = 1
    global_index = 0


def update_global_order_number():
    global global_order_number
    global_order_number += 1


def update_global_index():
    global global_index
    global_index += 1
