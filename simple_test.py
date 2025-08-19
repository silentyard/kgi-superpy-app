import sys
import os
sys.path.append('d:\\_coding\\kgi_superpy')

print("Testing imports...")
try:
    from kgi_trading_app.client import KGITradingClient
    print("OK: KGITradingClient imported")
    
    import superpy as sp
    print("OK: superpy imported")
    
    print("All tests passed!")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
