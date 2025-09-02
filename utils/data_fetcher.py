
import ccxt
import pandas as pd
from datetime import datetime as dt
import time


class ExchangeDataFetcher:
    """
    Fetches OHLCV data from cryptocurrency exchanges
    """
    
    def __init__(self, exchange_id: str):
        """
        Args:
            exchange_id (str): Exchange ID (e.g., 'binance', 'bybit')
        """
        self.exchange_id = exchange_id
        self.exchange = self._initialize_exchange()
    
    def _initialize_exchange(self):
        try:
            exchange_class = getattr(ccxt, self.exchange_id)
            return exchange_class({
                'enableRateLimit': True,
                'timeout': 30000
            })
        except AttributeError:
            raise ValueError(f"Unsupported exchange: {self.exchange_id}")
        except Exception as e:
            raise Exception(f"Error initializing exchange: {e}")
    
    def fetch_all_ohlcv(self, symbol: str, timeframe: str, since: str) -> pd.DataFrame:
        """
        Fetch OHLCV data for a trading pair
        
        Args:
            symbol (str): Trading pair symbol (e.g., 'BTC/USDT')
            timeframe (str): Time interval (e.g., '1h', '4h', '1d')
            since (str): Start date (ISO 8601 format)
            
        Returns:
            pd.DataFrame: OHLCV data
        """
        try:
            print(f"📊 Fetching {symbol} {timeframe} data...")
            
            # Convert date to timestamp
            since_timestamp = int(dt.fromisoformat(since.replace('Z', '+00:00')).timestamp() * 1000)
            
            all_ohlcv = []
            current_timestamp = since_timestamp
            limit = 1000
            
            while True:
                ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, current_timestamp, limit)
                
                if not ohlcv:
                    break
                
                all_ohlcv.extend(ohlcv)
                print(f"📈 Fetched {len(ohlcv)} candles. Total: {len(all_ohlcv)}")
                
                current_timestamp = ohlcv[-1][0] + self._get_timeframe_duration(timeframe)
                
                if current_timestamp >= int(dt.now().timestamp() * 1000):
                    break
                
                time.sleep(1)
            
            if not all_ohlcv:
                print(f"⚠️ No data found for {symbol} {timeframe}")
                return pd.DataFrame()
            
            df = pd.DataFrame(all_ohlcv, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume'
            ])
            
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            
            print(f"✅ {symbol} {timeframe}: {len(df)} candles fetched successfully")
            return df
            
        except Exception as e:
            print(f"❌ Error fetching {symbol} {timeframe}: {e}")
            return pd.DataFrame()
    
    def _get_timeframe_duration(self, timeframe: str) -> int:
        """
        Get timeframe duration in milliseconds
        
        Args:
            timeframe (str): Timeframe string
            
        Returns:
            int: Duration in milliseconds
        """
        timeframe_map = {
            '1m': 60 * 1000,
            '5m': 5 * 60 * 1000,
            '15m': 15 * 60 * 1000,
            '30m': 30 * 60 * 1000,
            '1h': 60 * 60 * 1000,
            '4h': 4 * 60 * 60 * 1000,
            '1d': 24 * 60 * 60 * 1000,
            '1w': 7 * 24 * 60 * 60 * 1000,
            '1M': 30 * 24 * 60 * 60 * 1000,
        }
        return timeframe_map.get(timeframe, 60 * 60 * 1000)


def fetch_all_ohlcv(exchange_id: str, symbol: str, timeframe: str, since: str) -> pd.DataFrame:
    """Global fetch_all_ohlcv function for backward compatibility"""
    fetcher = ExchangeDataFetcher(exchange_id)
    return fetcher.fetch_all_ohlcv(symbol, timeframe, since)
