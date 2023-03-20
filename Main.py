from account_bt import Account
from order_bt import Order


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

    account_1 = Account(1000 * 500)

    order_1 = Order(0.9, 0.002, 0)
    account_1.add_order(order_1)
    update_account_status(account_1, 0.91)
    print("equity", account_1.get_equity())
