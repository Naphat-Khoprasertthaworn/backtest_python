from account_bt import Account
from order_bt import Order
import globals
from database_bt import Database
import algorithm_bt
import time


def update_account_status(account, current_bid, current_ask):
    lis = account.get_order_list()
    profit = 0
    for order in lis:
        if order.get_order_type() == 0:
            profit += (current_ask - order.get_price()) * order.get_lot()
        else:
            profit += (order.get_price() - current_bid) * order.get_lot()
    status = account.set_equity(account.get_equity() + profit)
    if status is False:
        print("Bankrupt")
        quit()


if __name__ == '__main__':
    ''''
    globals.initialize()

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

    account_1.set_equity(10)
    order_6 = Order(0.85, 1, 0)
    account_1.add_order(order_6)
    update_account_status(account_1, 0.1)
    print("equity", account_1.get_equity())
    '''

    globals.initialize()
    db = Database("DAT_ASCII_EURUSD_T_202302.csv")
    account_1 = Account(1000 * 500)
    '''
    print(db.get_df_index(2401100))
    c = db.get_df_index(-1)
    print(c)
    print( float(c.Ask) )
    print(c.DateTime)
    print(c.Bid)
    #print(db.get_df_index(-1))
    '''
    rows = len(db.get_data_frame().index)
    while globals.global_index < rows:
        current_data = db.get_df_index(globals.global_index)
        algorithm_bt.process(account_1,current_data,db)
        update_account_status(account_1, float(current_data.Bid), float(current_data.Ask))
        globals.update_global_index()

        '''
        print(current_data)
        time.sleep(1)
        if globals.global_index > 5:
            break
        '''
