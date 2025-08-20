#!/usr/bin/env python3
"""
詳細測試程式 - 驗證證券和期貨帳戶功能

這個程式會測試：
1. 登入後是否能看到所有帳戶
2. 切換帳戶類型功能
3. 各帳戶的詳細信息
4. 帳戶的可用功能
"""

from kgi_trading_app.client import KGITradingClient
import json

def print_separator(title=""):
    """列印分隔線"""
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)

def print_json_pretty(data, title=""):
    """美化列印JSON數據"""
    if title:
        print(f"\n--- {title} ---")
    print(json.dumps(data, indent=2, ensure_ascii=False))

def test_account_functionality():
    """測試帳戶功能的主要函數"""
    
    print_separator("KGI 多帳戶功能測試")
    
    # 創建客戶端
    client = KGITradingClient(simulation=True)
    print("✓ 客戶端已創建 (模擬模式)")
    
    # 測試登入前的狀態
    print_separator("登入前狀態檢查")
    info_before = client.get_client_info()
    print_json_pretty(info_before, "登入前客戶端信息")
    
    # 模擬登入過程（這裡需要真實的帳號密碼才能測試）
    print_separator("登入測試指南")
    print("注意：要完整測試多帳戶功能，需要：")
    print("1. 一個同時擁有證券和期貨帳戶的真實帳號")
    print("2. 在下面的代碼中輸入真實的帳號密碼")
    print("3. 將 test_real_login 設為 True")
    print()
    
    # 是否進行真實登入測試
    test_real_login = True
    
    if test_real_login:
        # 請在這裡輸入您的真實帳號密碼進行測試
        user_id = input("請輸入您的用戶ID: ").strip()
        password = input("請輸入您的密碼: ").strip()
        
        if user_id and password:
            print_separator("開始登入測試")
            
            # 測試不同的帳戶類型登入
            account_types = ["all", "stock", "futures"]
            
            for account_type in account_types:
                print(f"\n--- 測試帳戶類型: {account_type} ---")
                
                # 重新創建客戶端以確保乾淨的狀態
                client = KGITradingClient(simulation=False)
                
                try:
                    success = client.login(user_id, password, account_type=account_type)
                    
                    if success:
                        print(f"✓ 登入成功 (帳戶類型: {account_type})")
                        
                        # 獲取詳細帳戶信息
                        details = client.get_all_account_details()
                        print_json_pretty(details, f"帳戶詳情 ({account_type})")
                        
                        # 測試帳戶功能
                        capabilities = client.test_account_capabilities()
                        print_json_pretty(capabilities, f"帳戶功能測試 ({account_type})")
                        
                        # 測試切換功能
                        if account_type == "all":
                            print("\n--- 測試帳戶切換功能 ---")
                            for switch_type in ["stock", "futures", "all"]:
                                switch_success = client.switch_account_type(switch_type)
                                if switch_success:
                                    print(f"✓ 成功切換到 {switch_type} 帳戶")
                                    current_details = client.get_all_account_details()
                                    print(f"  可見帳戶數: {current_details['current_visible_accounts']}")
                                else:
                                    print(f"✗ 切換到 {switch_type} 帳戶失敗")
                        
                        # 登出
                        client.logout()
                        print(f"✓ 已登出")
                        
                    else:
                        print(f"✗ 登入失敗 (帳戶類型: {account_type})")
                        
                except Exception as e:
                    print(f"✗ 登入過程發生錯誤: {str(e)}")
    
    else:
        print_separator("模擬測試模式")
        print("目前運行在模擬測試模式")
        print("要進行真實測試，請：")
        print("1. 修改 test_real_login = True")
        print("2. 輸入真實的帳號密碼")
        print()
        
        # 測試不需要登入的功能
        print("--- 測試可用方法 ---")
        available_methods = [method for method in dir(client) 
                           if not method.startswith('_') and callable(getattr(client, method))]
        print("客戶端可用方法:")
        for method in available_methods:
            print(f"  - {method}")
    
    print_separator("測試完成")
    print("如果您有同時包含證券和期貨的帳戶，")
    print("請修改程式中的 test_real_login = True 並輸入真實帳號進行測試")

def check_account_types_after_login():
    """
    檢查登入後的帳戶類型分佈
    這個函數專門用來調試帳戶過濾問題
    """
    print_separator("帳戶類型調試檢查")
    
    client = KGITradingClient(simulation=True)
    
    # 這裡需要真實帳號密碼
    print("注意：此函數需要真實帳號密碼才能有效測試")
    print("請確保您的帳號同時擁有證券和期貨權限")
    
    # 取消註解下面的代碼來進行真實測試
    """
    user_id = "您的帳號"
    password = "您的密碼"
    
    success = client.login(user_id, password, account_type="all")
    
    if success:
        print("登入成功！正在分析帳戶...")
        
        # 檢查原始帳戶數據
        print(f"總帳戶數: {len(client.all_accounts)}")
        print(f"當前可見帳戶數: {len(client.accounts)}")
        
        # 分析每個帳戶
        for i, account in enumerate(client.all_accounts):
            print(f"帳戶 {i+1}:")
            print(f"  類型字串: {str(type(account))}")
            print(f"  是否為股票: {'Stock' in str(type(account))}")
            print(f"  是否為期貨: {'Future' in str(type(account))}")
            print(f"  帳戶ID: {getattr(account, 'account_id', 'N/A')}")
            print(f"  簽署狀態: {getattr(account, 'signed', 'N/A')}")
    """
    import os
    os._exit(0)

if __name__ == "__main__":
    test_account_functionality()
    print("\n")
    check_account_types_after_login()
