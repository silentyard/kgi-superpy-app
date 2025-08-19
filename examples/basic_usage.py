"""
Example usage of KGI Trading Application

This script demonstrates how to use the KGI trading client.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kgi_trading_app.client import KGITradingClient


def example_basic_usage():
    """Example of basic client usage."""
    print("Example: Basic Usage")
    print("-" * 30)
    
    # Create client in simulation mode
    client = KGITradingClient(simulation=True)
    
    # Check initial status
    print("Initial client status:")
    info = client.get_client_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    print(f"\nClient connected: {client.is_connected()}")
    print(f"Account count: {len(client.get_account_list())}")
    
    # Note: Actual login requires valid credentials
    print("\n(Note: Actual login requires valid KGI Securities credentials)")
    
    return client


def example_error_handling():
    """Example of error handling."""
    print("\nExample: Error Handling")
    print("-" * 30)
    
    client = KGITradingClient(simulation=True)
    
    # Try to logout when not logged in
    result = client.logout()
    print(f"Logout when not logged in: {result}")
    
    # Try to get account info when not logged in
    accounts = client.get_account_list()
    print(f"Accounts when not logged in: {len(accounts)}")
    
    # Try to get contract status when not logged in
    status = client.get_contracts_status()
    print(f"Contract status when not logged in: {status}")


def example_simulation_vs_production():
    """Example showing simulation vs production mode."""
    print("\nExample: Simulation vs Production Mode")
    print("-" * 30)
    
    # Simulation mode client
    sim_client = KGITradingClient(simulation=True)
    sim_info = sim_client.get_client_info()
    print(f"Simulation mode: {sim_info['simulation_mode']}")
    
    # Production mode client
    prod_client = KGITradingClient(simulation=False)
    prod_info = prod_client.get_client_info()
    print(f"Production mode: {prod_info['simulation_mode']}")
    
    print("\nRecommendation: Always test with simulation mode first!")


def main():
    """Run all examples."""
    print("=" * 50)
    print("KGI Trading Application - Usage Examples")
    print("=" * 50)
    
    try:
        example_basic_usage()
        example_error_handling()
        example_simulation_vs_production()
        
        print("\n" + "=" * 50)
        print("Examples completed successfully!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\nExample error: {str(e)}")


if __name__ == "__main__":
    main()
