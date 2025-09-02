# 🚀 Crypto Data Downloader

> Professional cryptocurrency historical data downloader for backtesting and analysis.

## ⚡ Quick Start

```bash
# Clone and setup
git clone https://github.com/yusufcmg/crypto-data-downloader.git
cd crypto-data-downloader
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run
python src/main.py
```

## 📊 Features

- **15+ Cryptocurrencies**: BTC, ETH, SOL, XRP, BNB, ADA, DOGE, SHIB, AVAX, DOT...
- **5 Timeframes**: 1h, 4h, 1d, 1w, 1M
- **Complete History**: From each coin's Binance listing date
- **Backtest Ready**: CSV output compatible with popular libraries
- **100+ Exchanges**: Binance, Bybit, Kucoin, OKX via CCXT

## ⚙️ Configuration

Edit `config/config.py`:

```python
# Add/remove coins
COINS_WITH_DATES = {
    'BTC/USDT': '2017-08-17T00:00:00Z',
    'YOUR/COIN': '2023-01-01T00:00:00Z'
}

# Change exchange
EXCHANGE_ID = 'binance'  # or bybit, kucoin, okx...
```

## 📁 Output

```
data/
├── BTC/
│   ├── binance_BTC_USDT_1h_*.csv
│   └── binance_BTC_USDT_1d_*.csv
└── ETH/
    └── ...
```

CSV format: `timestamp, Open, High, Low, Close, Volume`

## 🔧 Backtest Integration

```python
import pandas as pd
data = pd.read_csv('data/BTC/binance_BTC_USDT_1h_*.csv')
# Ready for Backtrader, Backtesting.py, VectorBT, Zipline
```

## 📞 Contact

- **GitHub**: [@yusufcmg](https://github.com/yusufcmg)
- **Email**: yusufdev.bunkhouse251@simplelogin.com

## 📄 License

MIT License - Free for personal and commercial use.

---

⭐ Star this repo if it helped you!
