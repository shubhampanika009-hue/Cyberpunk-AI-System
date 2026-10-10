# Trading & Market Analyst Agent
import yfinance as yf

def analyze_stock(ticker_symbol):
    print(f"[Trading Agent] {ticker_symbol} का बाजार डेटा विश्लेषण किया जा रहा है...")
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="5d")
        if not hist.empty:
            current_price = hist['Close'].iloc[-1]
            print(f"[+] {ticker_symbol} का नवीनतम मूल्य: ${current_price:.2f}")
        else:
            print("[-] डेटा उपलब्ध नहीं है।")
    except Exception as e:
        print(f"त्रुटि: {e}")

if __name__ == "__main__":
    print("📈 Trading & Market Analyst Agent एक्टिव है।")
    analyze_stock("AAPL")
