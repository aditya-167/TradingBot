#encoding utf-8
import logging as lg
import sys
class Trader(object):
    def __init__(self, ticker):
        self.ticker = ticker
        lg.info('HKAdi Trader Initialized! with ticker: {}'.format(self.ticker))
    
    def ticker_tradable(self):
        asset = None
        try:
            if not asset.tradable:
                lg.info('The asset {} is not tradable'.format(self.ticker))
                return False
            else:
                lg.info('The asset {} is tradable'.format(self.ticker))
                return True
        except:
            lg.error('The asset {} not responding'.format(self.ticker))
            return False
    
    def set_stopLoss(self,positionPrice, position, stopLosspct =None,stopLossPrice = None):
        if stopLosspct is not None and stopLossPrice is not None:
            stopLosspct = None
        try:
            if position == 'long' and stopLossPrice == None:
                stopLoss = positionPrice*(1-stopLosspct) 
                return stopLoss
            
            elif position == 'long' and stopLosspct == None:
                stopLoss = positionPrice-stopLossPrice 
                return stopLoss
            
            elif position == 'short' and stopLossPrice == None:
                stopLoss = positionPrice*(1+stopLosspct) 
                return stopLoss
            
            elif position == 'short' and stopLosspct == None:
                stopLoss = positionPrice+stopLossPrice 
                return stopLoss
            
            else:
                raise ValueError
        except Exception as e:
            lg.error('The position {} is incorrect'.format(position))
            sys.exit()
        return stopLoss
    
    def set_takeProfit(self,positionPrice, position, takeProfitpct =None,takeProfitPrice = None):
        if takeProfitpct is not None and takeProfitPrice is not None:
            takeProfit = None
        try:
            if position == 'long' and takeProfitPrice == None:
                takeProfit = positionPrice*(1+takeProfitpct) 
                return takeProfit
            
            elif position == 'long' and takeProfitpct == None:
                takeProfit = positionPrice+takeProfitPrice 
                return takeProfit
            
            elif position == 'short' and takeProfitPrice == None:
                takeProfit = positionPrice*(1-takeProfitpct) 
                return takeProfit
            
            elif position == 'short' and takeProfitpct == None:
                takeProfit = positionPrice-takeProfitPrice 
                return takeProfit
            else:
                raise ValueError
        except Exception as e:
            lg.error('The position {} is incorrect'.format(position))
            sys.exit()
        return takeProfit
    def run_trade():
        pass