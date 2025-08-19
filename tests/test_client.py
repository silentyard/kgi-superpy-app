"""
Test script for KGI Trading Application

This script tests the basic functionality of the trading client.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kgi_trading_app.client import KGITradingClient


def test_client_initialization():
    """Test client initialization."""
    print("Testing client initialization...")
    
    # Test simulation mode
    client_sim = KGITradingClient(simulation=True)
    assert client_sim.simulation == True
    assert client_sim.is_logged_in == False
    print("✓ Simulation mode client initialized")
    
    # Test production mode
    client_prod = KGITradingClient(simulation=False)
    assert client_prod.simulation == False
    assert client_prod.is_logged_in == False
    print("✓ Production mode client initialized")
    
    # Clean up to prevent hanging
    del client_sim
    del client_prod


def test_client_info():
    """Test client info functionality."""
    print("\nTesting client info...")
    
    client = KGITradingClient(simulation=True)
    info = client.get_client_info()
    
    assert isinstance(info, dict)
    assert 'simulation_mode' in info
    assert 'logged_in' in info
    assert 'account_count' in info
    assert info['simulation_mode'] == True
    assert info['logged_in'] == False
    assert info['account_count'] == 0
    print("✓ Client info functionality working")
    
    # Clean up
    del client


def test_contract_status():
    """Test contract status functionality."""
    print("\nTesting contract status...")
    
    client = KGITradingClient(simulation=True)
    status = client.get_contracts_status()
    
    # Should return "Not logged in" when not connected
    assert status == "Not logged in"
    print("✓ Contract status functionality working")
    
    # Clean up
    del client


def test_account_list():
    """Test account list functionality."""
    print("\nTesting account list...")
    
    client = KGITradingClient(simulation=True)
    accounts = client.get_account_list()
    
    # Should return empty list when not logged in
    assert isinstance(accounts, list)
    assert len(accounts) == 0
    print("✓ Account list functionality working")
    
    # Clean up
    del client


def main():
    """Run all tests."""
    print("=" * 50)
    print("KGI Trading Application - Unit Tests")
    print("=" * 50)
    
    try:
        test_client_initialization()
        test_client_info()
        test_contract_status()
        test_account_list()
        
        print("\n" + "=" * 50)
        print("✓ All tests passed!")
        print("=" * 50)
        
        # Force exit to prevent hanging
        import gc
        gc.collect()
        
        return True
        
    except Exception as e:
        print(f"\n✗ Test failed: {str(e)}")
        return False


if __name__ == "__main__":
    success = main()
    print("Test execution completed.")
    sys.exit(0 if success else 1)
