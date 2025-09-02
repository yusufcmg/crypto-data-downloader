"""
Crypto Data Downloader
Professional cryptocurrency historical data downloader for backtesting and analysis.
"""

import sys
import os
from typing import List

# Add project root to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from utils.data_fetcher import ExchangeDataFetcher
from utils.file_operations import DataSaver
from config.config import COINS_WITH_DATES, TIMEFRAMES, EXCHANGE_ID


def print_header():
    """Print program startup information"""
    print("=" * 60)
    print("🚀 CRYPTO DATA DOWNLOADER v1.0")
    print("=" * 60)
    print("📊 Professional cryptocurrency data downloader")
    print("🎯 Perfect for backtesting and technical analysis")
    print("💼 GitHub: https://github.com/yusufcmg/crypto-data-downloader")
    print("=" * 60)
    print()


def download_crypto_data():
    """Main data download function"""
    print_header()
    
    # Initialize classes
    fetcher = ExchangeDataFetcher(EXCHANGE_ID)
    saver = DataSaver()
    
    # Statistics
    total_operations = len(COINS_WITH_DATES) * len(TIMEFRAMES)
    successful_downloads = 0
    failed_downloads = 0
    saved_files = []
    
    print(f"📋 Download plan:")
    print(f"   • Exchange: {EXCHANGE_ID.upper()}")
    print(f"   • Coins: {len(COINS_WITH_DATES)}")
    print(f"   • Timeframes: {', '.join(TIMEFRAMES)}")
    print(f"   • Total operations: {total_operations}")
    print()
    
    # Fetch data for each coin
    for i, (symbol, start_date) in enumerate(COINS_WITH_DATES.items(), 1):
        print(f"💰 [{i}/{len(COINS_WITH_DATES)}] Processing {symbol}...")
        print(f"   📅 Start date: {start_date}")
        
        # For each timeframe
        for timeframe in TIMEFRAMES:
            print(f"   ⏱️  {timeframe} timeframe...")
            
            # Fetch data
            data = fetcher.fetch_all_ohlcv(
                symbol=symbol,
                timeframe=timeframe,
                since=start_date
            )
            
            if not data.empty:
                # Save data
                file_path = saver.save_ohlcv_data(
                    exchange_id=EXCHANGE_ID,
                    symbol=symbol,
                    timeframe=timeframe,
                    data=data
                )
                
                if file_path:
                    successful_downloads += 1
                    saved_files.append(file_path)
                else:
                    failed_downloads += 1
            else:
                failed_downloads += 1
        
        print()
    
    # Report results
    print_summary(successful_downloads, failed_downloads, saved_files)


def print_summary(successful: int, failed: int, files: List[str]):
    """Summarize download results"""
    print("=" * 60)
    print("📊 DOWNLOAD REPORT")
    print("=" * 60)
    print(f"✅ Successful downloads: {successful}")
    print(f"❌ Failed downloads: {failed}")
    print(f"📁 Total files: {len(files)}")
    print()
    
    if files:
        print("📋 Saved files:")
        for file_path in files:
            file_name = os.path.basename(file_path)
            print(f"   • {file_name}")
        print()
    
    print("=" * 60)
    print("🎉 Process completed!")
    print("💡 Files ready for backtesting in 'data' folder!")
    print("🔄 Use these files with backtesting libraries")
    print("=" * 60)


if __name__ == "__main__":
    try:
        download_crypto_data()
    except KeyboardInterrupt:
        print("\n⚠️ Process stopped by user!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
