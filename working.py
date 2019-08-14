import websockets
import asyncio
 
async def hello():
	async with websockets.connect('wss://api.huobi.pro/ws') as websocket:
		name = { "sub": "market.btccny.kline.1min",  "id": "id1"}
		await websocket.send(name)
		print(f"send server:{name}")
		greeting = await websocket.recv()
		print(f"receive from server:{greeting}")

asyncio.get_event_loop().run_until_complete(hello())







"""
import abupy
from abupy import EMarketSourceType,EDataCacheType,EMarketTargetType,ABuSymbolPd,EMarketDataFetchMode,abu

abupy.env.g_market_source = EMarketSourceType.E_MARKET_SOURCE_hb_tc
abupy.env.g_data_fetch_mode = EMarketDataFetchMode.E_DATA_FETCH_NORMAL
ABuSymbolPd.make_kl_df('btc').tail()
"""