"""
Configuration settings for Crypto Data Downloader
"""

# Exchange settings
EXCHANGE_ID = 'binance'

# Cryptocurrencies and their first Binance listing dates
COINS_WITH_DATES = {
    'BTC/USDT': '2017-08-17T00:00:00Z',
    'ETH/USDT': '2017-08-17T00:00:00Z',
    # 'XRP/USDT': '2018-05-01T00:00:00Z',
    # 'SOL/USDT': '2020-08-11T00:00:00Z',
    # 'BNB/USDT': '2017-08-17T00:00:00Z',
    # 'ADA/USDT': '2018-04-17T00:00:00Z',
    # 'DOGE/USDT': '2019-07-05T00:00:00Z',
    # 'SHIB/USDT': '2021-05-10T00:00:00Z',
    # 'AVAX/USDT': '2020-09-22T00:00:00Z',
    # 'DOT/USDT': '2020-08-19T00:00:00Z',
    # 'MATIC/USDT': '2019-04-26T00:00:00Z',
    # 'LTC/USDT': '2017-12-13T00:00:00Z',
    # 'LINK/USDT': '2019-01-16T00:00:00Z',
    # 'UNI/USDT': '2020-09-17T00:00:00Z',
    # 'ATOM/USDT': '2019-04-22T00:00:00Z',
}

# Timeframes to download
TIMEFRAMES = ['1h', '4h', '1d', '1w', '1M']

# API settings
API_RATE_LIMIT = 1
MAX_RETRIES = 3

# Data saving settings
DATA_DIRECTORY = 'data'
CSV_DATE_FORMAT = '%Y%m%d_%H%M%S'
