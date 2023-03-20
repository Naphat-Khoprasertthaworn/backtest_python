from account_bt import Account
from order_bt import Order
import globals


def update_account_status(account, current_exchange):
    lis = account.get_order_list()
    profit = 0
    for order in lis:
        if order.get_order_type() == 0:
            profit += (current_exchange - order.get_price()) * order.get_lot()
        else:
            profit += (order.get_price() - current_exchange) * order.get_lot()
    status = account.set_equity(account.get_equity() + profit)
    if status is False:
        print("Bankrupt")
        quit()


if __name__ == '__main__':
    globals.initialize()
    account_1 = Account(1000 * 500)

    order_1 = Order(0.9, 0.02, 0)
    order_2 = Order(1, 0.04, 1)
    order_3 = Order(0.7, 0.02, 1)
    order_4 = Order(1.5, 0.03, 0)
    order_5 = Order(0.85, 0.04, 0)
    account_1.add_order(order_1)
    account_1.add_order(order_2)
    account_1.add_order(order_3)
    account_1.add_order(order_4)
    account_1.add_order(order_5)
    update_account_status(account_1, 0.80)
    print("equity", account_1.get_equity())
    for i in account_1.get_order_list():
        print(i)
