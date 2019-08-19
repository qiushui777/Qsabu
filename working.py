"""
import abupy
from abupy import EMarketSourceType,EDataCacheType,EMarketTargetType,ABuSymbolPd,EMarketDataFetchMode,abu
from abupy import ABuDateUtil
import time

abupy.env.g_market_source = EMarketSourceType.E_MARKET_SOURCE_binance
abupy.env.g_data_fetch_mode = EMarketDataFetchMode.E_DATA_FETCH_NORMAL
print(ABuSymbolPd.make_kl_df(symbol='QsETHUSDT'))


"""
"""
#binance api test
import requests
import abupy


#print(requests.get(url='https://api.binance.com/api/v1/klines',params={"symbol":"BTCUSDT","interval": "1d", 
    #"startTime":1543104000000, "endTime":1543248000000}).text)
print(requests.get(url='https://api.binance.com/api/v1/klines',params={"symbol":"BTCUSDT","interval": "1d"}).text)


"""
#huobi api test
import websockets
import asyncio
 
async def hello():
    async with websockets.connect('wss://api.huobi.pro/ws') as websocket:
        name = { "sub": "market.ethbtc.kline.1min",  "id": "id1"}
        await websocket.send(name)
        print(f"send server:{name}")
        greeting = await websocket.recv()
        print(f"receive from server:{greeting}")

asyncio.get_event_loop().run_until_complete(hello())
