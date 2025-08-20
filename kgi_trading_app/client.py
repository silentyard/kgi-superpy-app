"""
KGI Securities Trading Client

This module provides a simple interface for login/logout functionality
using the kgisuperpy API.
"""

import superpy as sp
from typing import Optional, List
import logging
from datetime import datetime


class KGITradingClient:
    """
    A client for KGI Securities trading operations.
    Provides basic login/logout functionality.
    """
    
    def __init__(self, simulation: bool = True):
        """
        Initialize the KGI Trading Client.
        
        Args:
            simulation (bool): Whether to use simulation mode (default: True)
        """
        self.simulation = simulation
        self.api = sp.SuperPy(simulation=simulation)
        self.is_logged_in = False
        self.accounts = []
        self.all_accounts = []  # Store all accounts from original login
        self.stock_account = None
        self.futopt_account = None
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def login(self, user_id: str, password: str, fetch_contract: bool = True, 
              account_type: str = "all") -> bool:
        """
        Login to KGI Securities system.
        
        Args:
            user_id (str): User ID for login
            password (str): Password for login
            fetch_contract (bool): Whether to fetch contract data (default: True)
            account_type (str): Account type to use ("stock", "futures", "all")
            
        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            self.logger.info(f"Attempting to login with user ID: {user_id}")
            
            # Perform login
            self.accounts = self.api.login(
                userID=user_id,
                password=password,
                fetch_contract=fetch_contract,
                contracts_timeout=10000,
                subscribe_trade=True,
                receive_window=30000
            )
            
            if self.accounts:
                self.is_logged_in = True
                self.all_accounts = self.accounts.copy()  # Save all accounts
                self.logger.info(f"Login successful. Found {len(self.accounts)} accounts.")
                
                # Filter accounts based on type preference
                self._filter_accounts_by_type(account_type)
                
                # Set default accounts
                self._set_default_accounts()
                
                # Display account information
                self._display_account_info()
                
                return True
            else:
                self.logger.error("Login failed - no accounts returned")
                return False
                
        except Exception as e:
            self.logger.error(f"Login error: {str(e)}")
            return False
    
    def logout(self) -> bool:
        """
        Logout from KGI Securities system.
        
        Returns:
            bool: True if logout successful, False otherwise
        """
        try:
            if self.is_logged_in:
                self.api.logout()
                self.is_logged_in = False
                self.accounts = []
                self.all_accounts = []
                self.stock_account = None
                self.futopt_account = None
                self.logger.info("Logout successful")
                
                # Clean up API object to prevent hanging
                try:
                    del self.api
                except:
                    pass
                    
                return True
            else:
                self.logger.warning("Not logged in")
                return False
                
        except Exception as e:
            self.logger.error(f"Logout error: {str(e)}")
            return False
    
    def cleanup(self):
        """Force cleanup of resources to prevent hanging."""
        try:
            if hasattr(self, 'api'):
                if self.is_logged_in:
                    self.logout()
                del self.api
        except:
            pass
    
    def _filter_accounts_by_type(self, account_type: str):
        """Filter accounts based on requested type."""
        if account_type.lower() == "stock":
            self.accounts = [acc for acc in self.accounts if "Stock" in str(type(acc))]
            self.logger.info(f"Filtered to stock accounts only: {len(self.accounts)} accounts")
        elif account_type.lower() == "futures":
            self.accounts = [acc for acc in self.accounts if "Future" in str(type(acc))]
            self.logger.info(f"Filtered to futures accounts only: {len(self.accounts)} accounts")
        # "all" - keep all accounts
    
    def get_available_account_types(self) -> dict:
        """
        Get available account types from current login.
        
        Returns:
            dict: Available account types with counts
        """
        if not self.is_logged_in:
            return {"stock": 0, "futures": 0}
            
        stock_count = len([acc for acc in self.accounts if "Stock" in str(type(acc))])
        futures_count = len([acc for acc in self.accounts if "Future" in str(type(acc))])
        
        return {
            "stock": stock_count,
            "futures": futures_count,
            "total": len(self.accounts)
        }
    
    def switch_account_type(self, account_type: str) -> bool:
        """
        Switch to specific account type without re-login.
        
        Args:
            account_type (str): Account type ("stock", "futures", "all")
            
        Returns:
            bool: True if switch successful
        """
        if not self.is_logged_in:
            self.logger.warning("Not logged in")
            return False
            
        # Use stored all_accounts instead of calling API again
        if account_type.lower() == "stock":
            filtered_accounts = [acc for acc in self.all_accounts if "Stock" in str(type(acc))]
        elif account_type.lower() == "futures":
            filtered_accounts = [acc for acc in self.all_accounts if "Future" in str(type(acc))]
        else:  # "all"
            filtered_accounts = self.all_accounts.copy()
            
        if filtered_accounts:
            self.accounts = filtered_accounts
            self._set_default_accounts()
            self.logger.info(f"Switched to {account_type} accounts: {len(self.accounts)} accounts")
            return True
        else:
            self.logger.warning(f"No {account_type} accounts found")
            return False
    
    def _set_default_accounts(self):
        """Set default stock and futures/options accounts."""
        self.stock_account = None
        self.futopt_account = None
        
        for account in self.accounts:
            if hasattr(account, 'signed') and account.signed:
                if 'Stock' in str(type(account)):
                    if not self.stock_account:
                        self.stock_account = account
                elif 'Future' in str(type(account)):
                    if not self.futopt_account:
                        self.futopt_account = account
    
    def _display_account_info(self):
        """Display account information."""
        self.logger.info("=== Account Information ===")
        for i, account in enumerate(self.accounts):
            account_type = "Stock" if "Stock" in str(type(account)) else "Future"
            signed_status = "Signed" if hasattr(account, 'signed') and account.signed else "Not Signed"
            
            self.logger.info(f"Account {i+1}: {account_type}")
            self.logger.info(f"  Person ID: {account.person_id}")
            self.logger.info(f"  Broker ID: {account.broker_id}")
            self.logger.info(f"  Account ID: {account.account_id}")
            self.logger.info(f"  Status: {signed_status}")
            
            if hasattr(account, 'trader') and account.trader:
                self.logger.info(f"  Trader: {account.trader}")
            
            self.logger.info("")
    
    def get_account_list(self) -> List:
        """
        Get list of available accounts.
        
        Returns:
            List: List of account objects
        """
        if self.is_logged_in:
            return self.accounts
        else:
            self.logger.warning("Not logged in")
            return []
    
    def set_default_account(self, account):
        """
        Set default account for trading.
        
        Args:
            account: Account object to set as default
        """
        try:
            self.api.set_default_account(account)
            
            if 'Stock' in str(type(account)):
                self.stock_account = account
                self.logger.info(f"Set default stock account: {account.account_id}")
            elif 'Future' in str(type(account)):
                self.futopt_account = account
                self.logger.info(f"Set default futures account: {account.account_id}")
                
        except Exception as e:
            self.logger.error(f"Error setting default account: {str(e)}")
    
    def get_contracts_status(self) -> str:
        """
        Get contracts download status.
        
        Returns:
            str: Contracts status
        """
        if self.is_logged_in:
            try:
                return self.api.Contracts.status
            except Exception as e:
                self.logger.error(f"Error getting contracts status: {str(e)}")
                return "Error"
        else:
            return "Not logged in"
    
    def is_connected(self) -> bool:
        """
        Check if client is connected and logged in.
        
        Returns:
            bool: True if connected and logged in
        """
        return self.is_logged_in
    
    def get_all_account_details(self) -> dict:
        """
        Get detailed information about all available accounts.
        
        Returns:
            dict: Detailed account information
        """
        if not self.is_logged_in:
            return {"error": "Not logged in", "accounts": []}
        
        account_details = {
            "total_accounts": len(self.all_accounts),
            "current_visible_accounts": len(self.accounts),
            "accounts": []
        }
        
        for i, account in enumerate(self.all_accounts):
            account_type = "Stock" if "Stock" in str(type(account)) else "Future"
            signed_status = "Signed" if hasattr(account, 'signed') and account.signed else "Not Signed"
            is_visible = account in self.accounts
            
            account_info = {
                "index": i + 1,
                "type": account_type,
                "person_id": getattr(account, 'person_id', 'N/A'),
                "broker_id": getattr(account, 'broker_id', 'N/A'),
                "account_id": getattr(account, 'account_id', 'N/A'),
                "signed": signed_status,
                "is_visible_in_current_filter": is_visible,
                "is_default_stock": account == self.stock_account,
                "is_default_futures": account == self.futopt_account
            }
            
            if hasattr(account, 'trader') and account.trader:
                account_info['trader'] = account.trader
                
            account_details["accounts"].append(account_info)
        
        return account_details
    
    def test_account_capabilities(self) -> dict:
        """
        Test what capabilities each account type has.
        
        Returns:
            dict: Test results for different account types
        """
        if not self.is_logged_in:
            return {"error": "Not logged in"}
        
        results = {
            "stock_account_test": None,
            "futures_account_test": None,
            "contracts_info": None
        }
        
        # Test stock account capabilities
        if self.stock_account:
            try:
                # Try to access stock-related methods
                results["stock_account_test"] = {
                    "account_id": self.stock_account.account_id,
                    "type": str(type(self.stock_account)),
                    "signed": getattr(self.stock_account, 'signed', False),
                    "available_methods": [method for method in dir(self.stock_account) 
                                        if not method.startswith('_') and callable(getattr(self.stock_account, method))]
                }
            except Exception as e:
                results["stock_account_test"] = {"error": str(e)}
        
        # Test futures account capabilities  
        if self.futopt_account:
            try:
                results["futures_account_test"] = {
                    "account_id": self.futopt_account.account_id,
                    "type": str(type(self.futopt_account)),
                    "signed": getattr(self.futopt_account, 'signed', False),
                    "available_methods": [method for method in dir(self.futopt_account) 
                                        if not method.startswith('_') and callable(getattr(self.futopt_account, method))]
                }
            except Exception as e:
                results["futures_account_test"] = {"error": str(e)}
        
        # Test contracts information
        try:
            if hasattr(self.api, 'Contracts'):
                results["contracts_info"] = {
                    "status": getattr(self.api.Contracts, 'status', 'Unknown'),
                    "available_methods": [method for method in dir(self.api.Contracts) 
                                        if not method.startswith('_')]
                }
        except Exception as e:
            results["contracts_info"] = {"error": str(e)}
        
        return results

    def is_connected(self) -> bool:
        """
        Check if client is connected and logged in.
        
        Returns:
            bool: True if connected and logged in
        """
        return self.is_logged_in
    
    def get_client_info(self) -> dict:
        """
        Get client information.
        
        Returns:
            dict: Client information
        """
        account_types = self.get_available_account_types()
        
        return {
            "simulation_mode": self.simulation,
            "logged_in": self.is_logged_in,
            "account_count": len(self.accounts),
            "total_accounts": account_types.get("total", 0),
            "stock_accounts": account_types.get("stock", 0),
            "futures_accounts": account_types.get("futures", 0),
            "has_stock_account": self.stock_account is not None,
            "has_futures_account": self.futopt_account is not None,
            "contracts_status": self.get_contracts_status()
        }
