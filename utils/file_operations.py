
import os
import pandas as pd
from datetime import datetime
from typing import Optional


class DataSaver:
   
    def __init__(self, base_directory: str = 'data'):
        """
        Args:
            base_directory (str): Base directory for saving data
        """
        self.base_directory = base_directory
        self._ensure_directory_exists()
    
    def _ensure_directory_exists(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.base_directory):
            os.makedirs(self.base_directory)
    
    def save_ohlcv_data(
        self, 
        exchange_id: str, 
        symbol: str, 
        timeframe: str, 
        data: pd.DataFrame,
        timestamp_format: str = '%Y%m%d_%H%M%S'
    ) -> Optional[str]:
        """
        Save OHLCV data to CSV file
        
        Args:
            exchange_id (str): Exchange ID
            symbol (str): Trading pair symbol
            timeframe (str): Timeframe
            data (pd.DataFrame): Data to save
            timestamp_format (str): Timestamp format for filename
            
        Returns:
            str: Full path of saved file, None if error
        """
        try:
            # Create coin directory
            coin_name = symbol.split('/')[0]
            coin_dir = os.path.join(self.base_directory, coin_name)
            if not os.path.exists(coin_dir):
                os.makedirs(coin_dir)
            
            # Generate filename
            current_time = datetime.now().strftime(timestamp_format)
            clean_symbol = symbol.replace('/', '_')
            filename = f"{exchange_id}_{clean_symbol}_{timeframe}_{current_time}.csv"
            
            # Full file path
            file_path = os.path.join(coin_dir, filename)
            
            # Format for backtesting and save
            formatted_data = self._format_data_for_backtest(data.copy())
            formatted_data.to_csv(file_path, index=False)
            
            print(f"✅ Data saved: {file_path}")
            return file_path
            
        except Exception as e:
            print(f"❌ File save error: {e}")
            return None
    
    def _format_data_for_backtest(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Format data for backtesting libraries
        
        Args:
            data (pd.DataFrame): Raw OHLCV data
            
        Returns:
            pd.DataFrame: Formatted data
        """
        # Capitalize column names for backtesting libraries
        data.rename(columns={
            'open': 'Open',
            'high': 'High',
            'low': 'Low',
            'close': 'Close',
            'volume': 'Volume'
        }, inplace=True)
        
        return data
    
    def get_saved_files_info(self) -> dict:
        
        try:
            files = [f for f in os.listdir(self.base_directory) if f.endswith('.csv')]
            
            return {
                'total_files': len(files),
                'files': files,
                'directory': self.base_directory
            }
        except Exception as e:
            print(f"❌ Dosya bilgileri alınırken hata: {e}")
            return {'total_files': 0, 'files': [], 'directory': self.base_directory}
