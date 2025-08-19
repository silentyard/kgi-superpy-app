"""
KGI Securities Trading Application Main Entry Point

This script demonstrates basic login/logout functionality using the kgisuperpy library.
"""

import os
import sys
from kgi_trading_app.client import KGITradingClient
import argparse
import getpass


def main():
    """Main entry point for the KGI trading application."""
    
    parser = argparse.ArgumentParser(description='KGI Securities Trading Application')
    parser.add_argument('--simulation', action='store_true', default=True,
                       help='Use simulation mode (default: True)')
    parser.add_argument('--production', action='store_true',
                       help='Use production mode (overrides simulation)')
    parser.add_argument('--user-id', type=str,
                       help='User ID for login')
    parser.add_argument('--interactive', action='store_true', default=True,
                       help='Interactive mode (default: True)')
    parser.add_argument('--gui', action='store_true',
                       help='Launch GUI version instead of command line')
    
    args = parser.parse_args()
    
    # Check if GUI mode is requested
    if args.gui:
        try:
            import tkinter as tk
            from gui_main import KGITradingGUI
            print("啟動 GUI 版本...")
            root = tk.Tk()
            app = KGITradingGUI(root)
            root.mainloop()
            return
        except ImportError:
            print("錯誤: tkinter 未安裝，無法啟動 GUI 版本")
            print("正在啟動命令行版本...")
        except Exception as e:
            print(f"GUI 啟動錯誤: {e}")
            print("正在啟動命令行版本...")
    
    # Determine mode
    simulation_mode = args.simulation and not args.production
    
    print("=" * 60)
    print("    KGI Securities Trading Application")
    print("    Basic Login/Logout Functionality Demo")
    print("=" * 60)
    print(f"Mode: {'SIMULATION' if simulation_mode else 'PRODUCTION'}")
    print()
    
    # Create client
    client = KGITradingClient(simulation=simulation_mode)
    
    try:
        if args.interactive:
            interactive_mode(client, args.user_id)
        else:
            # Non-interactive mode (for automated testing)
            if args.user_id:
                password = os.environ.get('KGI_PASSWORD', '')
                if password:
                    demo_login_logout(client, args.user_id, password)
                else:
                    print("Error: Password not provided in environment variable KGI_PASSWORD")
            else:
                print("Error: User ID required for non-interactive mode")
                
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    except Exception as e:
        print(f"Application error: {str(e)}")
    finally:
        # Ensure logout
        if client.is_connected():
            print("\nLogging out...")
            client.logout()
        
        # Force cleanup
        client.cleanup()
        
        print("Application terminated.")
        # Force exit to handle hanging SuperPy threads
        import os
        os._exit(0)


def interactive_mode(client, user_id=None):
    """Run the application in interactive mode."""
    
    while True:
        print("\n" + "=" * 40)
        print("KGI Trading Application Menu")
        print("=" * 40)
        print("1. Login")
        print("2. Show Account Information")
        print("3. Show Client Status")
        print("4. Logout")
        print("5. Exit")
        print()
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            handle_login(client, user_id)
        elif choice == '2':
            handle_account_info(client)
        elif choice == '3':
            handle_client_status(client)
        elif choice == '4':
            handle_logout(client)
        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("Invalid option. Please select 1-5.")
    
    # Force clean exit
    import os
    os._exit(0)


def handle_login(client, user_id=None):
    """Handle login process."""
    if client.is_connected():
        print("Already logged in. Please logout first.")
        return
    
    try:
        if not user_id:
            user_id = input("Enter User ID: ").strip()
        
        if not user_id:
            print("User ID cannot be empty.")
            return
            
        password = getpass.getpass("Enter Password: ")
        
        if not password:
            print("Password cannot be empty.")
            return
        
        print("Attempting to login...")
        success = client.login(user_id, password)
        
        if success:
            print("✓ Login successful!")
        else:
            print("✗ Login failed. Please check your credentials.")
            
    except Exception as e:
        print(f"Login error: {str(e)}")


def handle_account_info(client):
    """Handle account information display."""
    if not client.is_connected():
        print("Not logged in. Please login first.")
        return
    
    accounts = client.get_account_list()
    
    if accounts:
        print(f"\nFound {len(accounts)} accounts:")
        for i, account in enumerate(accounts):
            account_type = "Stock" if "Stock" in str(type(account)) else "Future"
            signed_status = "✓ Signed" if hasattr(account, 'signed') and account.signed else "✗ Not Signed"
            
            print(f"\nAccount {i+1}: {account_type}")
            print(f"  Person ID: {account.person_id}")
            print(f"  Broker ID: {account.broker_id}")
            print(f"  Account ID: {account.account_id}")
            print(f"  Status: {signed_status}")
            
            if hasattr(account, 'trader') and account.trader:
                print(f"  Trader: {account.trader}")
    else:
        print("No accounts found.")


def handle_client_status(client):
    """Handle client status display."""
    info = client.get_client_info()
    
    print("\nClient Status:")
    print(f"  Simulation Mode: {info['simulation_mode']}")
    print(f"  Logged In: {'✓' if info['logged_in'] else '✗'}")
    print(f"  Account Count: {info['account_count']}")
    print(f"  Has Stock Account: {'✓' if info['has_stock_account'] else '✗'}")
    print(f"  Has Futures Account: {'✓' if info['has_futures_account'] else '✗'}")
    print(f"  Contracts Status: {info['contracts_status']}")


def handle_logout(client):
    """Handle logout process."""
    if not client.is_connected():
        print("Not logged in.")
        return
    
    print("Logging out...")
    success = client.logout()
    
    if success:
        print("✓ Logout successful!")
    else:
        print("✗ Logout failed.")


def demo_login_logout(client, user_id, password):
    """Demonstrate login/logout functionality (non-interactive)."""
    print(f"Demo: Attempting to login with user ID: {user_id}")
    
    # Login
    success = client.login(user_id, password)
    if success:
        print("✓ Login successful!")
        
        # Show account info
        accounts = client.get_account_list()
        print(f"Found {len(accounts)} accounts")
        
        # Show client status
        info = client.get_client_info()
        print(f"Client status: {info}")
        
        # Logout
        print("Logging out...")
        client.logout()
        print("✓ Logout successful!")
    else:
        print("✗ Login failed!")


if __name__ == "__main__":
    main()
