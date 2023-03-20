from Account import Account
from Order import Order

global global_order_number
global LOT_CONSTANT


def update_global_order_number():
    global global_order_number
    global_order_number += 1


def update_account_status(account, current_exchange):
    lis = account.get_order_list()
    profit = 0
    for order in lis:
        if order.get_order_type() == 0:
            profit += (current_exchange - order.get_price()) * order.get_lot()
        else:
            profit += (order.get_price - current_exchange) * order.get_lot()
    status = account.set_equity(account.get_equity() + profit)
    if status is False:
        print("Bankrupt")
        quit()


if __name__ == '__main__':
    LOT_CONSTANT = 100000
    global_order_number = 1

    account_1 = Account(1000)
