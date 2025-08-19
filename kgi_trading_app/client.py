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
        self.stock_account = None
        self.futopt_account = None
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def login(self, user_id: str, password: str, fetch_contract: bool = True) -> bool:
        """
        Login to KGI Securities system.
        
        Args:
            user_id (str): User ID for login
            password (str): Password for login
            fetch_contract (bool): Whether to fetch contract data (default: True)
            
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
                self.logger.info(f"Login successful. Found {len(self.accounts)} accounts.")
                
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
    
    def _set_default_accounts(self):
        """Set default stock and futures/options accounts."""
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
    
    def get_client_info(self) -> dict:
        """
        Get client information.
        
        Returns:
            dict: Client information
        """
        return {
            "simulation_mode": self.simulation,
            "logged_in": self.is_logged_in,
            "account_count": len(self.accounts),
            "has_stock_account": self.stock_account is not None,
            "has_futures_account": self.futopt_account is not None,
            "contracts_status": self.get_contracts_status()
        }
