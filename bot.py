from Trader import *
from logger import *
import sys


def check_account():
    try:
        pass
    except Exception as e:
        lg.error('Unable to fetch account info')
        lg.info(str(e))
        sys.exit() 
def close_open_orders():
    open_orders = ''
    lg.info('List of open orders')
    lg.info(str(open_orders))

    for order in open_orders:
        lg.info('Order {} closed'.format(str(order.id)))
    lg.info('All open orders closed')

def main():
    initialize_logging()

    check_account()

    close_open_orders()

    ticker = input('Input ticker to trade: ')

    trader = Trader(ticker)

    trader.run()

if __name__ == '__main__':
    main()