"""
Quick test script for KGI Trading Application

This script runs a minimal test to verify the application works.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def quick_test():
    """Run a quick test without creating SuperPy instances."""
    print("=" * 40)
    print("Quick Test - KGI Trading Application")
    print("=" * 40)
    
    try:
        # Test import
        from kgi_trading_app.client import KGITradingClient
        print("✓ Successfully imported KGITradingClient")
        
        # Test that we can import superpy
        import superpy as sp
        print("✓ Successfully imported superpy")
        print(f"  SuperPy available at: {sp.__file__}")
        
        print("\n✓ All imports successful!")
        print("✓ Application is ready to use!")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = quick_test()
    print("\nQuick test completed.")
    if success:
        print("Ready to test main application!")
    sys.exit(0 if success else 1)
