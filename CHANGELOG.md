# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Multi-account type support (Stock and Futures accounts)
- Account type selection during login
- Dynamic account type switching without re-login
- Detailed account information display
- Account capabilities testing functionality
- Enhanced GUI with account type selection
- Comprehensive test suite for multi-account functionality

### Changed
- Enhanced `KGITradingClient` class with multi-account support
- Updated login method to accept `account_type` parameter
- Improved client status information with detailed account statistics
- Enhanced GUI layout with additional action buttons
- Updated CLI interface with account type selection menu

### Fixed
- Account switching functionality using stored account data
- Improved account filtering logic
- Better error handling for account operations

## [1.1.0] - 2025-08-21

### Added
- 🎯 **Multi-Account Type Support**: Support for both Stock and Futures accounts
- 🔄 **Dynamic Account Switching**: Switch between account types without re-login
- 📊 **Enhanced Account Information**: Detailed account statistics and capabilities
- 🖥️ **Improved GUI Interface**: New account type selection and testing features
- 🧪 **Comprehensive Testing**: Multi-account functionality testing suite

### New Features

#### KGITradingClient Enhancements
- `account_type` parameter in `login()` method ("all", "stock", "futures")
- `get_available_account_types()` method for account statistics
- `switch_account_type()` method for dynamic switching
- `get_all_account_details()` method for detailed account information
- `test_account_capabilities()` method for functionality testing

#### GUI Improvements
- Account type selection radio buttons (All/Stock/Futures)
- "Account Details" button for comprehensive account information
- "Test Functions" button for account capability testing
- "Switch Type" button for account type switching
- Enhanced status display with detailed statistics

#### CLI Enhancements
- Account type selection during login process
- "Switch Account Type" menu option
- Enhanced client status display
- Improved account information presentation

#### Testing Framework
- `test_multi_accounts.py` - Comprehensive multi-account testing
- Real login testing capability
- Account switching validation
- Detailed account analysis tools

### Technical Improvements
- Added `all_accounts` storage for complete account data preservation
- Fixed account switching logic to use stored data instead of API calls
- Enhanced error handling and logging
- Improved account filtering and management
- Better thread safety in GUI operations

### Usage Examples

#### Login with Specific Account Type
```python
# Login with all accounts
client.login(user_id, password, account_type="all")

# Login with stock accounts only
client.login(user_id, password, account_type="stock")

# Login with futures accounts only
client.login(user_id, password, account_type="futures")
```

#### Switch Account Types
```python
# Switch to view only stock accounts
client.switch_account_type("stock")

# Switch back to all accounts
client.switch_account_type("all")
```

#### Get Account Information
```python
# Get available account types
types = client.get_available_account_types()
# Returns: {"stock": 1, "futures": 1, "total": 2}

# Get detailed account information
details = client.get_all_account_details()

# Test account capabilities
capabilities = client.test_account_capabilities()
```

### Files Added
- `test_multi_accounts.py` - Multi-account testing suite

### Files Modified
- `kgi_trading_app/client.py` - Enhanced with multi-account support
- `main.py` - Updated CLI with account type selection
- `gui_main.py` - Enhanced GUI with new features
- `README.md` - Updated with new features documentation

## [1.0.0] - 2025-08-20

### Added
- Initial release of KGI Securities Trading Application
- Basic login/logout functionality using kgisuperpy API
- Support for both simulation and production modes
- Modern GUI interface with tkinter
- Interactive command-line interface
- Multi-threaded GUI operations for smooth user experience
- Comprehensive error handling and logging
- Chinese language support for GUI
- Account information display
- Client status monitoring

### Features
- 🔐 Secure login/logout functionality
- 📊 Account information display  
- 🎯 Support for simulation and production modes
- 🖥️ Modern graphical user interface (GUI)
- 💻 Interactive command-line interface
- 📱 Simple API wrapper
- 🌐 Multi-threaded GUI for smooth user experience

### Technical Details
- Built with Python 3.12+
- Uses kgisuperpy library for KGI API integration
- tkinter-based GUI with modern styling
- Argparse-based CLI with multiple options
- Comprehensive logging system
- Thread-safe operations

### Files Structure
```
kgi_superpy/
├── kgi_trading_app/
│   ├── __init__.py
│   └── client.py
├── main.py
├── gui_main.py
├── requirements.txt
├── README.md
├── LICENSE
├── start_gui.bat
├── examples/
│   ├── basic_usage.py
│   └── gui_usage.py
└── tests/
    ├── test_client.py
    └── quick_test.py
```

### Requirements
- Python 3.8+
- kgisuperpy
- tkinter (usually included with Python)

### Initial Setup
- KGI Securities account required
- API service agreement must be signed
- API access permissions needed
