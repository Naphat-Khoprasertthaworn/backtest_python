from account_bt import Account
from order_bt import Order
from database_bt import Database
import globals
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


# mabe use this https://pythonguides.com/matplotlib-update-plot-in-loop/ animate func



def process(account, current_data, database):
    n = 10
    current_index = globals.global_index
    new_df = database.get_df_period( max(0,current_index - n), current_index+1)
    mv_bid = new_df.Bid.mean( axis=0 )
    mv_ask = new_df.Ask.mean( axis=0 )
    database.get_data_frame()['mv_bid'][current_index] = mv_bid
    database.get_data_frame()['mv_ask'][current_index] = mv_ask
    return


def animate_plot(inp):
    x_plot = list(range(0, inp+1))
    bid_plot = db.get_data_frame().iloc[:inp+1]['Bid'].values
    ask_plot = db.get_data_frame().iloc[:inp+1]['Ask'].values
    mv_bid_plot = db.get_data_frame().iloc[:inp+1]['mv_bid'].values
    mv_ask_plot = db.get_data_frame().iloc[:inp+1]['mv_ask'].values

    line1.set_data(x_plot, bid_plot)
    #line2.set_data(x_plot, ask_plot)
    #line3.set_data(x_plot, mv_bid_plot)
    line4.set_data(x_plot, mv_ask_plot)

    #return line1,line2,line3,line4,
    return line1,line4,


if __name__ == '__main__':
    globals.initialize()
    db = Database("TEST2.txt")

    print(db.get_data_frame().head())

    account_1 = Account(1000 * 500)
    i = 0

    dataNum = 1000

    db.get_data_frame()['mv_bid'] = 0
    db.get_data_frame()['mv_ask'] = 0

    while i < dataNum:
        current_data = db.get_df_index(globals.global_index)
        current_index = globals.global_index
        process(account_1, current_data, db)
        globals.update_global_index()
        i += 1

    plt.ion()
    figure, ax = plt.subplots(figsize=(10, 8))
    x = []
    bid = []
    ask = []
    mv_bid = []
    mv_ask = []
    ax.set_xlim(0,dataNum+1)

    line1, = ax.plot(x, bid)
    line2, = ax.plot(x, ask)
    line3, = ax.plot(x, mv_bid)
    line4, = ax.plot(x, mv_ask)


    y_margin = 0.0001
    ax.set_ylim( min(db.get_data_frame().iloc[:dataNum+1]['Bid'].values)-y_margin ,max(db.get_data_frame().iloc[:dataNum+1]['Ask'].values)+y_margin  )
    ani = animation.FuncAnimation(figure, animate_plot,frames=dataNum, interval=10, blit=True)

    plt.show(block=True)
    #plt.show()

