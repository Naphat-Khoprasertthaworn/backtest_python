from account_bt import Account
from order_bt import Order
from database_bt import Database
import globals
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


# mabe use this https://pythonguides.com/matplotlib-update-plot-in-loop/ animate func
# def initialize(database):
#     database['mv_bid'] = 0
#     database['mv_ask'] = 0


def process(account, current_data, database):
    n = 10
    current_index = globals.global_index
    new_df = database.get_df_period(current_index - n, current_index + 1)
    # print(new_df)
    mv_bid = sum(new_df.Bid) / min(n, current_index + 1)
    mv_ask = sum(new_df.Ask) / min(n, current_index + 1)
    # database['mv_bid'][current_index] = mv_bid
    # database['mv_ask'][current_index] = mv_ask
    # print(mv_bid, mv_ask)

    return


def animate_plot(inp):
    x_plot = range(0, 101)
    y_plot = db.get_data_frame().iloc[:101]['Bid'].values

    print(y_plot)

    line1.set_data(x_plot, y_plot)
    return line1,


if __name__ == '__main__':
    globals.initialize()
    db = Database("TEST.txt")
    # initialize(db)

    print(db.get_data_frame().head())

    plt.ion()
    figure, ax = plt.subplots(figsize=(10, 8))
    x = []
    y = []
    line1, = ax.plot(x, y)
    # plt.show()
    account_1 = Account(1000 * 500)
    i = 0
    # while i < 20:
    #     current_data = db.get_df_index(globals.global_index)
    #     current_index = globals.global_index
    #
    #     process(account_1, current_data, db)
    #     '''
    #     print(db.get_df_index(current_index))
    #     print(db.get_data_frame().info())
    #     print(db.get_data_frame().iloc[:current_index+1]['DateTime'].values)
    #     print(db.get_data_frame().iloc[current_index]['Bid'])
    #     '''
    #     print(range(0,current_index+1))
    #     print(db.get_data_frame().iloc[:current_index+1]['Bid'].values)
    #     line1.set_xdata(list(range(0,current_index+1)))
    #     line1.set_ydata(db.get_data_frame().iloc[:current_index+1]['Bid'].values)
    #     # plt.pause(1)
    #     figure.canvas.draw()
    #     figure.canvas.flush_events()
    #     time.sleep(1)
    #
    #     globals.update_global_index()
    #     i += 1

    ani = animation.FuncAnimation(figure, animate_plot, frames=100, interval=100, blit=True)
    #ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()



#%%
