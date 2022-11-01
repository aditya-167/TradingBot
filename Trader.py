#encoding utf-8
import logging as lg
import sys, time, os, pytz
import pandas as pd
import datetime as datetime
from math import ceil
import alpaca_trade_api as tradeapi

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
    
    def get_open_position(self, assetId):
        postitions = None
        for position in positions:
            if position.symbol == assetId:
                return True
            else:
                return False
    
    def check_position(self,asset):
        attempt = 1
        maxAttempt = 10
        while attempt <= maxAttempt:
            try:
                curr_price = position.current_price
                lg.info('The position was checked. Current price :- %.4f' % curr_price)
                return True
            except:
                lg.info('The position not found, searching... attempt {}'.format(attempt))
                time.sleep(5)
                attempt+=1
        lg.info('No positions found for asset {}'.format(asset))
        return False
    
    def get_overall_trend(self,asset):
        attempts = 1
        maxAttempt = 10
        waitTime = 60
        try:
            while True:
                ema_shortest = None
                ema_short = None
                ema_long = None
                lg.info('% overall trend EMAs : [%.2f,%.2f,%.2f]'%(asset,ema_shortest,ema_short,ema_long))
                if condition:
                    lg.info('Trend detected for asset {}: Upward'.format(asset))
                    return 'long'
                elif condition2:
                    lg.info('Trend detected for asset {}: Downward'.format(asset))
                    return short
                elif attempts<=maxAttempt:
                    lg.info('Overall Trend not clear, waiting...')
                    attempts+=1
                    time.sleep(waitTime*maxAttempt)
                else:
                    lg.info('No Trend detected & Timeout')
                    return 'no trend'
        except Exception as e:
            lg.error('Something went wrong to get overall trend')
            lg.error(e)
            sys.exit()

    def get_instant_trend(self,asset,overall_trend):
        attempts = 1
        maxAttempt = 10
        waitTime = 30
        try:
            while True:
                #get data
                ema_shortest = None
                ema_short = None
                ema_long = None
                lg.info('% instant trend EMAs : [%.2f,%.2f,%.2f]'%(asset,ema_shortest,ema_short,ema_long))
                if overall_trend == 'long' and (ema_shortest>ema_short) and (ema_short>ema_long):
                    lg.info('Long instant trend Confirmed for asset {}'.format(asset))
                    return True
                elif overall_trend == 'short' and (ema_shortest<ema_short) and (ema_short<ema_long):
                    lg.info('Short instant trend detected for asset {}'.format(asset))
                    return True 
                elif attempts<=maxAttempt:
                    lg.info('Instant Trend not clear, waiting...')
                    attempts+=1
                    time.sleep(waitTime*maxAttempt)
                else:
                    lg.info('No instant trend detected & Timeout')
                    return 'no trend'
        except Exception as e:
            lg.error('Something went wrong to get instant trend')
            lg.error(e)
            sys.exit()

    def run_trade():
        pass