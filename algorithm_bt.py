from account_bt import Account
from order_bt import Order
from database_bt import Database
import globals 

def process(account, current_data, database):

    n = 10
    current_index = globals.global_index
    new_df = database.get_df_period( current_index - n ,current_index + 1 )

    mv_bid = sum(new_df.Bid) / min(n,current_index)
    mv_ask = sum(new_df.Ask) / min(n,current_index)

    print(mv_bid,mv_ask)


    return


if __name__ == '__main__':


    
