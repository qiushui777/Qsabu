import abupy
from abupy import EMarketSourceType,EDataCacheType,EMarketTargetType,ABuSymbolPd,EMarketDataFetchMode,abu

abupy.env.g_market_source = EMarketSourceType.E_MARKET_SOURCE_hb_tc
abupy.env.g_data_fetch_mode = EMarketDataFetchMode.E_DATA_FETCH_NORMAL
ABuSymbolPd.make_kl_df('btc').tail()