# KGI Securities Trading Application

[繁體中文](#繁體中文) | [English](#english)

---

## 繁體中文

一個使用 kgisuperpy 函式庫提供基本證券登入登出功能的 Python 應用程式，現在支援多帳戶類型管理。

### 🆕 最新功能 (v1.1.0)

- 🎯 **多帳戶類型支援**：同時支援證券和期貨帳戶
- 🔄 **動態帳戶切換**：無需重新登入即可切換帳戶類型
- 📊 **詳細帳戶資訊**：完整的帳戶統計和功能測試
- 🧪 **綜合測試套件**：多帳戶功能驗證工具

### 功能特色

- 🔐 安全的登入/登出功能
- 📊 帳戶資訊顯示與詳細分析
- 🎯 支援模擬和正式模式
- 🖥️ **圖形用戶界面 (GUI)** 採用現代化設計
- 💻 互動式命令行界面
- 📱 簡單易用的 API 封裝
- 🌐 多執行緒 GUI 提供流暢的用戶體驗
- 🔄 **多帳戶類型管理**（證券/期貨/全部）
- 🧪 **帳戶功能測試**工具

### 安裝

1. 複製此儲存庫：
```bash
git clone https://github.com/yourusername/kgi-superpy-app.git
cd kgi-superpy-app
```

2. 安裝必要的依賴項：
```bash
pip install -r requirements.txt
```

### 使用前提

在使用此應用程式之前，您需要：

1. **開立 KGI 證券帳戶**
2. **簽署 API 服務協議**（證券API服務風險預告書暨使用同意書）
3. **申請 API 存取權限**：[KGI API 申請](https://h5webtrade.kgieworld.com.tw/ServicesWeb/Auth/Login?orign=o&applytype=21)

### 使用方式

#### GUI 版本（建議新手使用）

啟動現代化圖形界面：

```bash
# 方法 1: 使用 main.py 的 GUI 選項
python main.py --gui

# 方法 2: 直接啟動 GUI
python gui_main.py

# 方法 3: Windows 批次文件（雙擊即可）
start_gui.bat
```

GUI 提供以下功能：
- 🎨 現代化、用戶友好的界面
- 🔒 安全的密碼輸入
- 📊 即時狀態更新
- 📝 完整的日誌記錄
- ⚡ 多執行緒操作（非阻塞 UI）
- 🌍 中文語言支援
- 🎯 **帳戶類型選擇**：可選擇全部/證券/期貨帳戶
- 🔄 **動態切換**：登入後可切換不同帳戶類型
- 📋 **詳細資訊**：查看帳戶詳情和功能測試
- 🧪 **功能測試**：測試各帳戶類型的可用功能

##### 🆕 多帳戶功能使用

1. **選擇帳戶類型**：在登入前選擇要顯示的帳戶類型
   - **全部帳戶**：顯示所有可用的證券和期貨帳戶
   - **僅證券**：只顯示證券帳戶
   - **僅期貨**：只顯示期貨帳戶

2. **登入後操作**：
   - 點擊 **"Account Details"** 查看所有帳戶的詳細資訊
   - 點擊 **"Test Functions"** 測試各帳戶類型的功能
   - 點擊 **"Switch Type"** 動態切換帳戶類型
   - 點擊 **"Client Status"** 查看連線和帳戶統計

#### 命令行界面

適合進階用戶的終端機介面：

執行互動式模式：

```bash
python main.py
```

這將啟動互動式選單，您可以：
- 使用您的憑證登入
- **選擇帳戶類型**（全部/證券/期貨）
- 查看帳戶資訊
- **切換帳戶類型**（無需重新登入）
- 檢查客戶端狀態
- 登出

##### 🆕 多帳戶功能使用流程

1. **登入時選擇帳戶類型**：
   ```
   Account Type Options:
   1. All accounts       # 顯示所有帳戶
   2. Stock accounts only    # 僅顯示證券帳戶  
   3. Futures accounts only  # 僅顯示期貨帳戶
   ```

2. **登入後使用新功能**：
   - 選項 4：**Switch Account Type** - 動態切換帳戶類型
   - 查看詳細的帳戶統計資訊
   - 測試不同帳戶類型的功能

#### 命令行選項

##### GUI 版本
```bash
# 直接啟動 GUI
python gui_main.py

# 通過 main.py 啟動 GUI
python main.py --gui

# Windows 用戶可以雙擊
start_gui.bat
```

##### 命令行版本
```bash
# 在模擬模式運行（預設）
python main.py --simulation

# 在正式模式運行
python main.py --production

# 指定用戶 ID
python main.py --user-id YOUR_USER_ID

# 非互動模式（需要 KGI_PASSWORD 環境變數）
python main.py --user-id YOUR_USER_ID --interactive=False
```

#### 環境變數

對於非互動模式，將您的密碼設定為環境變數：

```bash
# Windows
set KGI_PASSWORD=your_password

# Linux/Mac
export KGI_PASSWORD=your_password
```

### 程式結構

```
kgi-superpy-app/
├── kgi_trading_app/
│   ├── __init__.py          # 套件初始化
│   └── client.py            # 主要交易客戶端類別（🆕 多帳戶支援）
├── main.py                  # 命令行應用程式入口點（🆕 帳戶類型選擇）
├── gui_main.py             # GUI 應用程式入口點（🆕 增強界面）
├── test_multi_accounts.py   # 🆕 多帳戶功能測試程式
├── start_gui.bat           # Windows GUI 啟動器
├── requirements.txt         # Python 依賴項
├── README.md               # 本文件（🆕 多帳戶功能說明）
├── CHANGELOG.md            # 🆕 版本變更記錄
├── LICENSE                 # 授權條款
├── examples/               # 使用範例
│   ├── basic_usage.py      # 基本使用範例
│   └── gui_usage.py        # GUI 使用範例
├── tests/                  # 測試檔案
│   ├── test_client.py      # 客戶端測試
│   └── quick_test.py       # 快速功能測試
└── .github/
    └── copilot-instructions.md
```

#### 🆕 新增檔案說明

- **`test_multi_accounts.py`**：專門測試多帳戶功能的綜合測試程式
- **`CHANGELOG.md`**：記錄所有版本的變更歷史
- 增強的 **`client.py`**：新增多帳戶類型支援和功能測試
- 更新的 **`main.py`** 和 **`gui_main.py`**：支援帳戶類型選擇和切換

### GUI 截圖和功能

#### 主要界面
GUI 提供現代化、用戶友好的界面，包含以下組件：

1. **交易模式選擇**
   - 模擬/正式模式的單選按鈕
   - 正式模式的自動安全警告

2. **🆕 帳戶類型選擇**
   - 全部帳戶/僅證券/僅期貨的單選按鈕
   - 登入前預先選擇要顯示的帳戶類型

3. **登入區域**
   - 用戶 ID 輸入欄位
   - 安全的密碼輸入（遮蔽顯示）
   - 登入/登出按鈕與狀態管理

4. **連線狀態**
   - 即時連線狀態顯示
   - 彩色狀態指示器

5. **🆕 增強操作按鈕**
   - **Show Accounts**：顯示當前可見的帳戶資訊
   - **Account Details**：🆕 顯示所有帳戶的詳細資訊
   - **Client Status**：顯示詳細客戶端資訊和統計
   - **Switch Type**：🆕 動態切換帳戶類型
   - **Test Functions**：🆕 測試各帳戶類型的可用功能
   - **Logout**：安全登出與確認

6. **資訊顯示**
   - 可滾動的日誌區域與時間戳記
   - 中文語言支援
   - 清除日誌功能
   - 背景操作的即時更新

#### GUI 安全特性
- 🛡️ **模式警告**：切換到正式模式時的確認對話框
- 🔒 **密碼保護**：遮蔽的密碼輸入，登出時清除
- ✅ **狀態驗證**：所有操作都會先檢查登入狀態
- 🧵 **執行緒安全**：基於佇列的 GUI 更新，確保操作流暢
- 🚪 **自動登出**：應用程式關閉時自動登出和清理
- ⚠️ **錯誤處理**：完整的異常處理，提供用戶友好的錯誤訊息

### API 參考

#### KGITradingClient 類別

##### 初始化
```python
from kgi_trading_app.client import KGITradingClient

# 在模擬模式建立客戶端
client = KGITradingClient(simulation=True)

# 在正式模式建立客戶端
client = KGITradingClient(simulation=False)
```

##### 登入
```python
# 基本登入
success = client.login(user_id="YOUR_USER_ID", password="YOUR_PASSWORD")

# 🆕 登入並指定帳戶類型
success = client.login(user_id="YOUR_USER_ID", password="YOUR_PASSWORD", account_type="all")
success = client.login(user_id="YOUR_USER_ID", password="YOUR_PASSWORD", account_type="stock")
success = client.login(user_id="YOUR_USER_ID", password="YOUR_PASSWORD", account_type="futures")
```

##### 🆕 多帳戶管理
```python
# 取得可用帳戶類型統計
types = client.get_available_account_types()
# 回傳: {"stock": 1, "futures": 1, "total": 2}

# 切換帳戶類型（無需重新登入）
success = client.switch_account_type("stock")    # 切換到證券帳戶
success = client.switch_account_type("futures")  # 切換到期貨帳戶
success = client.switch_account_type("all")      # 切換到所有帳戶

# 取得詳細帳戶資訊
details = client.get_all_account_details()
# 回傳詳細的帳戶資訊，包含：
# - total_accounts: 總帳戶數
# - current_visible_accounts: 目前可見帳戶數
# - accounts: 每個帳戶的詳細資訊

# 測試帳戶功能
capabilities = client.test_account_capabilities()
# 測試證券和期貨帳戶的可用功能
```

##### 登出
```python
success = client.logout()
```

##### 取得帳戶資訊
```python
# 基本帳戶資訊
accounts = client.get_account_list()          # 取得當前可見的帳戶列表
client_info = client.get_client_info()       # 取得客戶端基本資訊

# 🆕 詳細帳戶資訊
all_details = client.get_all_account_details()  # 取得所有帳戶詳細資訊
account_types = client.get_available_account_types()  # 取得帳戶類型統計
```

### 安全特性

- **預設模擬模式**：應用程式預設以模擬模式啟動，防止意外的真實交易
- **安全密碼輸入**：使用 `getpass` 進行安全的密碼輸入
- **錯誤處理**：完整的錯誤處理和日誌記錄
- **自動登出**：應用程式終止時確保登出

### 🧪 測試工具

#### 多帳戶功能測試

使用專門的測試程式來驗證多帳戶功能：

```bash
python test_multi_accounts.py
```

此測試程式會：
- 🔍 檢查登入前後的帳戶狀態
- 🧪 測試不同帳戶類型的登入
- 🔄 驗證帳戶切換功能
- 📊 分析帳戶詳細資訊
- ✅ 測試各帳戶的可用功能

**注意**：要進行完整測試，需要：
1. 擁有同時包含證券和期貨權限的真實帳號
2. 修改測試程式中的 `test_real_login = True`
3. 輸入真實的帳號密碼

#### 快速功能測試

檢查各個功能模組是否正常運作：

```bash
# 測試基本客戶端功能
python tests/quick_test.py

# 測試客戶端類別
python tests/test_client.py
```

### 使用範例

#### 基本使用範例
```python
from kgi_trading_app.client import KGITradingClient

# 建立客戶端
client = KGITradingClient(simulation=True)

# 登入
if client.login("your_user_id", "your_password"):
    print("登入成功！")
    
    # 取得帳戶資訊
    accounts = client.get_account_list()
    print(f"找到 {len(accounts)} 個帳戶")
    
    # 取得客戶端狀態
    status = client.get_client_info()
    print(f"客戶端狀態: {status}")
    
    # 登出
    client.logout()
else:
    print("登入失敗！")
```

#### 🆕 多帳戶使用範例
```python
from kgi_trading_app.client import KGITradingClient

# 建立客戶端
client = KGITradingClient(simulation=True)

# 登入並顯示所有帳戶
if client.login("your_user_id", "your_password", account_type="all"):
    print("登入成功！")
    
    # 檢查可用的帳戶類型
    types = client.get_available_account_types()
    print(f"證券帳戶: {types['stock']} 個，期貨帳戶: {types['futures']} 個")
    
    # 取得詳細帳戶資訊
    details = client.get_all_account_details()
    print(f"總共 {details['total_accounts']} 個帳戶")
    
    # 切換到只顯示證券帳戶
    if client.switch_account_type("stock"):
        print("已切換到證券帳戶模式")
        print(f"可見帳戶數: {len(client.get_account_list())}")
    
    # 測試帳戶功能
    capabilities = client.test_account_capabilities()
    if capabilities['stock_account_test']:
        print("證券帳戶功能正常")
    if capabilities['futures_account_test']:
        print("期貨帳戶功能正常")
    
    # 登出
    client.logout()
```

### 📝 版本資訊

**當前版本**：v1.1.0 (2025-08-21)

**主要更新**：
- ✨ 新增多帳戶類型支援（證券/期貨）
- 🔄 動態帳戶切換功能
- 📊 詳細帳戶資訊和功能測試
- 🧪 綜合測試套件

**查看完整更新記錄**：[CHANGELOG.md](CHANGELOG.md)

### 📋 功能對比表

| 功能 | v1.0.0 | v1.1.0 |
|------|--------|--------|
| 基本登入/登出 | ✅ | ✅ |
| 模擬/正式模式 | ✅ | ✅ |
| GUI 界面 | ✅ | ✅ |
| 命令行界面 | ✅ | ✅ |
| 帳戶資訊顯示 | ✅ | ✅ |
| **多帳戶類型支援** | ❌ | ✅ |
| **動態帳戶切換** | ❌ | ✅ |
| **詳細帳戶分析** | ❌ | ✅ |
| **功能測試工具** | ❌ | ✅ |
| **綜合測試套件** | ❌ | ✅ |

### 重要注意事項

⚠️ **交易風險**：本應用程式僅供教育和示範用途。真實交易涉及財務風險。

⚠️ **API 限制**：請確保遵守 KGI 證券 API 使用政策和速率限制。

⚠️ **憑證安全**：請勿將憑證提交到版本控制。使用環境變數或安全的憑證管理。

### 疑難排解

#### 常見問題

1. **登入失敗**
   - 驗證您的憑證
   - 確保您已簽署 API 服務協議
   - 檢查您的帳戶是否已啟用 API 存取

2. **匯入錯誤**
   - 確保已安裝 kgisuperpy：`pip install kgisuperpy`
   - 檢查 Python 版本相容性

3. **連線問題**
   - 檢查您的網路連線
   - 驗證 KGI 證券伺服器是否可存取

### 開發

#### 執行測試

```bash
# 在模擬模式執行應用程式進行測試
python main.py --simulation --user-id test_user
```

#### 貢獻

1. Fork 此儲存庫
2. 建立功能分支
3. 進行更改
4. 在模擬模式中徹底測試
5. 提交 pull request

### 授權

本專案採用 MIT 授權 - 詳見 LICENSE 文件。

### 免責聲明

本應用程式與 KGI 證券無官方關聯。這是使用公開可用的 kgisuperpy 函式庫的獨立實作。使用風險自負。

### 支援

如有此應用程式的問題，請在 GitHub 建立 issue。

如需 KGI 證券 API 支援，請直接聯繫 KGI 證券。

### 版本歷史

- **1.0.0** - 初始版本，包含基本登入/登出功能和 GUI 界面

---

## English

A Python application that provides basic securities login/logout functionality using the kgisuperpy library.

## Features

- 🔐 Secure login/logout functionality
- 📊 Account information display
- 🎯 Both simulation and production mode support
- 🖥️ **Graphical User Interface (GUI)** with modern design
- 💻 Interactive command-line interface
- 📱 Simple and easy-to-use API wrapper
- 🌐 Multi-threaded GUI for smooth user experience

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/kgi-superpy-app.git
cd kgi-superpy-app
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Prerequisites

Before using this application, you need to:

1. **Open an account** with KGI Securities
2. **Sign the API service agreement** (證券API服務風險預告書暨使用同意書)
3. **Apply for API access** at: [KGI API Application](https://h5webtrade.kgieworld.com.tw/ServicesWeb/Auth/Login?orign=o&applytype=21)

## Usage

### GUI Version (Recommended for New Users)

Launch the modern graphical interface:

```bash
# Method 1: Using main.py with GUI flag
python main.py --gui

# Method 2: Direct GUI launch
python gui_main.py

# Method 3: Windows batch file (double-click)
start_gui.bat
```

The GUI provides:
- 🎨 Modern, user-friendly interface
- 🔒 Secure password input
- 📊 Real-time status updates
- 📝 Comprehensive logging
- ⚡ Multi-threaded operation (non-blocking UI)
- 🌍 Chinese language support

### Command Line Interface

For advanced users who prefer terminal:

Run the application in interactive mode:

```bash
python main.py
```

This will start an interactive menu where you can:
- Login with your credentials
- View account information
- Check client status
- Logout

### Command Line Options

#### GUI Version
```bash
# Launch GUI directly
python gui_main.py

# Launch GUI through main.py
python main.py --gui

# Windows users can double-click
start_gui.bat
```

#### Command Line Version
```bash
# Run in simulation mode (default)
python main.py --simulation

# Run in production mode
python main.py --production

# Specify user ID
python main.py --user-id YOUR_USER_ID

# Non-interactive mode (requires KGI_PASSWORD environment variable)
python main.py --user-id YOUR_USER_ID --interactive=False
```

### Environment Variables

For non-interactive mode, set your password as an environment variable:

```bash
# Windows
set KGI_PASSWORD=your_password

# Linux/Mac
export KGI_PASSWORD=your_password
```

## Code Structure

```
kgi-superpy-app/
├── kgi_trading_app/
│   ├── __init__.py          # Package initialization
│   └── client.py            # Main trading client class
├── main.py                  # Command-line application entry point
├── gui_main.py             # GUI application entry point
├── start_gui.bat           # Windows GUI launcher
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── .github/
    └── copilot-instructions.md
```

## GUI Screenshots and Features

### Main Interface
The GUI provides a modern, user-friendly interface with the following components:

1. **Trading Mode Selection**
   - Radio buttons for Simulation/Production mode
   - Automatic safety warnings for production mode

2. **Login Section**
   - User ID input field
   - Secure password input (masked)
   - Login/Logout button with state management

3. **Connection Status**
   - Real-time connection status display
   - Color-coded status indicators

4. **Action Buttons**
   - Show Accounts (displays account information)
   - Show Client Status (displays detailed client info)
   - Logout (secure logout with confirmation)

5. **Information Display**
   - Scrollable log area with timestamps
   - Chinese language support
   - Clear log functionality
   - Real-time updates from background operations

### GUI Safety Features
- 🛡️ **Mode Warnings**: Confirmation dialog when switching to production mode
- 🔒 **Password Protection**: Masked password input, cleared on logout
- ✅ **State Validation**: All operations check login status first
- 🧵 **Thread Safety**: Queue-based GUI updates for smooth operation
- 🚪 **Auto Logout**: Automatic logout and cleanup on application close
- ⚠️ **Error Handling**: Comprehensive exception handling with user-friendly messages

## API Reference

### KGITradingClient Class

#### Initialization
```python
from kgi_trading_app.client import KGITradingClient

# Create client in simulation mode
client = KGITradingClient(simulation=True)

# Create client in production mode
client = KGITradingClient(simulation=False)
```

#### Login
```python
success = client.login(user_id="YOUR_USER_ID", password="YOUR_PASSWORD")
```

#### Logout
```python
success = client.logout()
```

#### Get Account Information
```python
accounts = client.get_account_list()
client_info = client.get_client_info()
```

## Safety Features

- **Simulation Mode by Default**: The application starts in simulation mode to prevent accidental real trades
- **Secure Password Input**: Uses `getpass` for secure password entry
- **Error Handling**: Comprehensive error handling and logging
- **Automatic Logout**: Ensures logout on application termination

## Example Usage

```python
from kgi_trading_app.client import KGITradingClient

# Create client
client = KGITradingClient(simulation=True)

# Login
if client.login("your_user_id", "your_password"):
    print("Login successful!")
    
    # Get account information
    accounts = client.get_account_list()
    print(f"Found {len(accounts)} accounts")
    
    # Get client status
    status = client.get_client_info()
    print(f"Client status: {status}")
    
    # Logout
    client.logout()
else:
    print("Login failed!")
```

## Important Notes

⚠️ **Trading Risks**: This application is for educational and demonstration purposes. Real trading involves financial risks.

⚠️ **API Limitations**: Ensure you comply with KGI Securities API usage policies and rate limits.

⚠️ **Credentials Security**: Never commit credentials to version control. Use environment variables or secure credential management.

## Troubleshooting

### Common Issues

1. **Login Failed**
   - Verify your credentials
   - Ensure you have signed the API service agreement
   - Check if your account has API access enabled

2. **Import Errors**
   - Ensure kgisuperpy is installed: `pip install kgisuperpy`
   - Check Python version compatibility

3. **Connection Issues**
   - Check your internet connection
   - Verify KGI Securities servers are accessible

## Development

### Running Tests

```bash
# Run the application in simulation mode for testing
python main.py --simulation --user-id test_user
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly in simulation mode
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is not officially affiliated with KGI Securities. It is an independent implementation using the publicly available kgisuperpy library. Use at your own risk.

## Support

For issues with this application, please create an issue on GitHub.

For KGI Securities API support, contact KGI Securities directly.

## Version History

- **1.0.0** - Initial release with basic login/logout functionality
