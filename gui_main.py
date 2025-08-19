"""
KGI Securities Trading Application GUI

This module provides a graphical user interface for the KGI trading application
using tkinter with modern styling.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import threading
import queue
import sys
import os
from datetime import datetime

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kgi_trading_app.client import KGITradingClient


class KGITradingGUI:
    """
    Graphical User Interface for KGI Securities Trading Application.
    """
    
    def __init__(self, root):
        """Initialize the GUI."""
        self.root = root
        self.root.title("KGI Securities Trading Application")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize client
        self.client = None
        self.simulation_mode = True
        
        # Thread-safe queue for updating GUI from worker threads
        self.message_queue = queue.Queue()
        
        # Setup GUI theme
        self.setup_theme()
        
        # Create GUI elements
        self.create_widgets()
        
        # Start message queue processor
        self.process_queue()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_theme(self):
        """Setup modern theme for the application."""
        style = ttk.Style()
        
        # Configure style
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Title.TLabel', 
                       font=('Arial', 16, 'bold'),
                       foreground='#2c3e50')
        
        style.configure('Subtitle.TLabel',
                       font=('Arial', 12, 'bold'),
                       foreground='#34495e')
        
        style.configure('Status.TLabel',
                       font=('Arial', 10),
                       foreground='#7f8c8d')
        
        style.configure('Success.TLabel',
                       font=('Arial', 10),
                       foreground='#27ae60')
        
        style.configure('Error.TLabel',
                       font=('Arial', 10),
                       foreground='#e74c3c')
        
        style.configure('Login.TButton',
                       font=('Arial', 10, 'bold'))
        
        style.configure('Action.TButton',
                       font=('Arial', 9))
    
    def create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, 
                               text="KGI Securities Trading Application",
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Mode selection frame
        mode_frame = ttk.LabelFrame(main_frame, text="Trading Mode", padding="10")
        mode_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        mode_frame.columnconfigure(1, weight=1)
        
        self.mode_var = tk.StringVar(value="simulation")
        
        sim_radio = ttk.Radiobutton(mode_frame, text="Simulation Mode (Safe Testing)", 
                                   variable=self.mode_var, value="simulation",
                                   command=self.on_mode_change)
        sim_radio.grid(row=0, column=0, sticky=tk.W, padx=(0, 20))
        
        prod_radio = ttk.Radiobutton(mode_frame, text="Production Mode (Real Trading)", 
                                    variable=self.mode_var, value="production",
                                    command=self.on_mode_change)
        prod_radio.grid(row=0, column=1, sticky=tk.W)
        
        # Login frame
        login_frame = ttk.LabelFrame(main_frame, text="Login Credentials", padding="10")
        login_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        login_frame.columnconfigure(1, weight=1)
        
        # User ID
        ttk.Label(login_frame, text="User ID:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.user_id_var = tk.StringVar()
        self.user_id_entry = ttk.Entry(login_frame, textvariable=self.user_id_var, width=30)
        self.user_id_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 5), padx=(10, 0))
        
        # Password
        ttk.Label(login_frame, text="Password:").grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(login_frame, textvariable=self.password_var, 
                                       show="*", width=30)
        self.password_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 10), padx=(10, 0))
        
        # Login button
        self.login_button = ttk.Button(login_frame, text="Login", 
                                      style='Login.TButton',
                                      command=self.login_async)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Connection Status", padding="10")
        status_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        status_frame.columnconfigure(1, weight=1)
        
        self.status_label = ttk.Label(status_frame, text="Not connected", 
                                     style='Status.TLabel')
        self.status_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        
        # Actions frame
        actions_frame = ttk.LabelFrame(main_frame, text="Actions", padding="10")
        actions_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Action buttons
        self.show_accounts_btn = ttk.Button(actions_frame, text="Show Accounts", 
                                           style='Action.TButton',
                                           command=self.show_accounts,
                                           state='disabled')
        self.show_accounts_btn.grid(row=0, column=0, padx=(0, 10), pady=(0, 5))
        
        self.show_status_btn = ttk.Button(actions_frame, text="Show Client Status", 
                                         style='Action.TButton',
                                         command=self.show_client_status,
                                         state='disabled')
        self.show_status_btn.grid(row=0, column=1, padx=(0, 10), pady=(0, 5))
        
        self.logout_btn = ttk.Button(actions_frame, text="Logout", 
                                    style='Action.TButton',
                                    command=self.logout_async,
                                    state='disabled')
        self.logout_btn.grid(row=0, column=2, pady=(0, 5))
        
        # Information display frame
        info_frame = ttk.LabelFrame(main_frame, text="Information", padding="10")
        info_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        info_frame.columnconfigure(0, weight=1)
        info_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(info_frame)
        text_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        self.info_text = tk.Text(text_frame, height=12, wrap=tk.WORD,
                                font=('Consolas', 9))
        self.info_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, 
                                 command=self.info_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.info_text.configure(yscrollcommand=scrollbar.set)
        
        # Clear button
        clear_btn = ttk.Button(info_frame, text="Clear Log", 
                              command=self.clear_log)
        clear_btn.grid(row=1, column=0, pady=(10, 0))
        
        # Initialize client
        self.initialize_client()
        
        # Add welcome message
        self.add_log("歡迎使用 KGI Securities Trading Application GUI")
        self.add_log("請選擇交易模式並輸入您的登入憑證")
        self.add_log("建議: 請先使用模擬模式進行測試")
        self.add_log("-" * 60)
    
    def initialize_client(self):
        """Initialize the trading client."""
        try:
            self.client = KGITradingClient(simulation=self.simulation_mode)
            mode_text = "模擬模式" if self.simulation_mode else "正式模式"
            self.add_log(f"交易客戶端已初始化 ({mode_text})")
        except Exception as e:
            self.add_log(f"客戶端初始化錯誤: {str(e)}", "ERROR")
    
    def on_mode_change(self):
        """Handle mode change."""
        self.simulation_mode = (self.mode_var.get() == "simulation")
        
        # Reinitialize client if not logged in
        if not self.client or not self.client.is_connected():
            self.initialize_client()
        
        mode_text = "模擬模式" if self.simulation_mode else "正式模式"
        self.add_log(f"交易模式已切換至: {mode_text}")
        
        if not self.simulation_mode:
            result = messagebox.askquestion(
                "警告", 
                "您已選擇正式模式！\n這將使用真實資金進行交易。\n確定要繼續嗎？",
                icon='warning'
            )
            if result != 'yes':
                self.mode_var.set("simulation")
                self.simulation_mode = True
                self.initialize_client()
    
    def add_log(self, message, level="INFO"):
        """Add a message to the log display."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if level == "ERROR":
            formatted_message = f"[{timestamp}] ❌ {message}\n"
        elif level == "SUCCESS":
            formatted_message = f"[{timestamp}] ✅ {message}\n"
        elif level == "WARNING":
            formatted_message = f"[{timestamp}] ⚠️ {message}\n"
        else:
            formatted_message = f"[{timestamp}] ℹ️ {message}\n"
        
        # Thread-safe GUI update
        self.message_queue.put(('log', formatted_message))
    
    def update_status(self, status, level="INFO"):
        """Update the status label."""
        self.message_queue.put(('status', status, level))
    
    def process_queue(self):
        """Process messages from the queue (called periodically)."""
        try:
            while True:
                item = self.message_queue.get_nowait()
                
                if item[0] == 'log':
                    self.info_text.insert(tk.END, item[1])
                    self.info_text.see(tk.END)
                elif item[0] == 'status':
                    status, level = item[1], item[2] if len(item) > 2 else "INFO"
                    
                    if level == "ERROR":
                        self.status_label.configure(text=status, style='Error.TLabel')
                    elif level == "SUCCESS":
                        self.status_label.configure(text=status, style='Success.TLabel')
                    else:
                        self.status_label.configure(text=status, style='Status.TLabel')
                elif item[0] == 'buttons':
                    logged_in = item[1]
                    self.update_button_states(logged_in)
                    
        except queue.Empty:
            pass
        
        # Schedule next check
        self.root.after(100, self.process_queue)
    
    def update_button_states(self, logged_in):
        """Update button states based on login status."""
        if logged_in:
            self.login_button.configure(text="Logout", command=self.logout_async)
            self.show_accounts_btn.configure(state='normal')
            self.show_status_btn.configure(state='normal')
            self.logout_btn.configure(state='normal')
            self.user_id_entry.configure(state='disabled')
            self.password_entry.configure(state='disabled')
        else:
            self.login_button.configure(text="Login", command=self.login_async)
            self.show_accounts_btn.configure(state='disabled')
            self.show_status_btn.configure(state='disabled')
            self.logout_btn.configure(state='disabled')
            self.user_id_entry.configure(state='normal')
            self.password_entry.configure(state='normal')
    
    def clear_log(self):
        """Clear the log display."""
        self.info_text.delete(1.0, tk.END)
    
    def login_async(self):
        """Perform login in a separate thread."""
        def login_worker():
            try:
                user_id = self.user_id_var.get().strip()
                password = self.password_var.get().strip()
                
                if not user_id or not password:
                    self.add_log("請輸入用戶ID和密碼", "ERROR")
                    return
                
                self.add_log(f"正在嘗試登入用戶: {user_id}")
                self.update_status("登入中...", "INFO")
                
                # Reinitialize client with current mode
                self.client = KGITradingClient(simulation=self.simulation_mode)
                
                success = self.client.login(user_id, password)
                
                if success:
                    self.add_log("登入成功！", "SUCCESS")
                    self.update_status("已連線", "SUCCESS")
                    self.message_queue.put(('buttons', True))
                    
                    # Show account information
                    accounts = self.client.get_account_list()
                    self.add_log(f"找到 {len(accounts)} 個帳戶")
                    
                    for i, account in enumerate(accounts):
                        account_type = "證券" if "Stock" in str(type(account)) else "期貨"
                        signed_status = "已簽署" if hasattr(account, 'signed') and account.signed else "未簽署"
                        
                        self.add_log(f"帳戶 {i+1}: {account_type}")
                        self.add_log(f"  身份證字號: {account.person_id}")
                        self.add_log(f"  券商代碼: {account.broker_id}")
                        self.add_log(f"  帳戶代碼: {account.account_id}")
                        self.add_log(f"  狀態: {signed_status}")
                        
                        if hasattr(account, 'trader') and account.trader:
                            self.add_log(f"  交易員: {account.trader}")
                else:
                    self.add_log("登入失敗！請檢查您的憑證", "ERROR")
                    self.update_status("登入失敗", "ERROR")
                    
            except Exception as e:
                self.add_log(f"登入錯誤: {str(e)}", "ERROR")
                self.update_status("連線錯誤", "ERROR")
        
        # Start login in background thread
        thread = threading.Thread(target=login_worker, daemon=True)
        thread.start()
    
    def logout_async(self):
        """Perform logout in a separate thread."""
        def logout_worker():
            try:
                if self.client and self.client.is_connected():
                    self.add_log("正在登出...")
                    self.update_status("登出中...", "INFO")
                    
                    success = self.client.logout()
                    
                    if success:
                        self.add_log("登出成功", "SUCCESS")
                        self.update_status("未連線", "INFO")
                        self.message_queue.put(('buttons', False))
                        self.password_var.set("")  # Clear password
                    else:
                        self.add_log("登出失敗", "ERROR")
                else:
                    self.add_log("尚未登入", "WARNING")
                    
            except Exception as e:
                self.add_log(f"登出錯誤: {str(e)}", "ERROR")
        
        thread = threading.Thread(target=logout_worker, daemon=True)
        thread.start()
    
    def show_accounts(self):
        """Show account information."""
        if not self.client or not self.client.is_connected():
            self.add_log("尚未登入", "WARNING")
            return
        
        accounts = self.client.get_account_list()
        
        if accounts:
            self.add_log("-" * 40)
            self.add_log("帳戶資訊:")
            
            for i, account in enumerate(accounts):
                account_type = "證券" if "Stock" in str(type(account)) else "期貨"
                signed_status = "✅ 已簽署" if hasattr(account, 'signed') and account.signed else "❌ 未簽署"
                
                self.add_log(f"\n帳戶 {i+1}: {account_type}")
                self.add_log(f"  身份證字號: {account.person_id}")
                self.add_log(f"  券商代碼: {account.broker_id}")
                self.add_log(f"  帳戶代碼: {account.account_id}")
                self.add_log(f"  狀態: {signed_status}")
                
                if hasattr(account, 'trader') and account.trader:
                    self.add_log(f"  交易員: {account.trader}")
            
            self.add_log("-" * 40)
        else:
            self.add_log("未找到帳戶", "WARNING")
    
    def show_client_status(self):
        """Show client status information."""
        if not self.client:
            self.add_log("客戶端未初始化", "ERROR")
            return
        
        info = self.client.get_client_info()
        
        self.add_log("-" * 40)
        self.add_log("客戶端狀態:")
        self.add_log(f"  模擬模式: {'是' if info['simulation_mode'] else '否'}")
        self.add_log(f"  已登入: {'✅' if info['logged_in'] else '❌'}")
        self.add_log(f"  帳戶數量: {info['account_count']}")
        self.add_log(f"  證券帳戶: {'✅' if info['has_stock_account'] else '❌'}")
        self.add_log(f"  期貨帳戶: {'✅' if info['has_futures_account'] else '❌'}")
        self.add_log(f"  合約狀態: {info['contracts_status']}")
        self.add_log("-" * 40)
    
    def on_closing(self):
        """Handle window close event."""
        try:
            if self.client and self.client.is_connected():
                result = messagebox.askquestion(
                    "確認", 
                    "您仍處於登入狀態。確定要退出應用程式嗎？",
                    icon='question'
                )
                if result == 'yes':
                    self.client.logout()
                    self.client.cleanup()
                else:
                    return
            
            self.root.quit()
            self.root.destroy()
            
            # Force exit to handle any hanging threads
            import os
            os._exit(0)
            
        except Exception as e:
            print(f"關閉錯誤: {e}")
            import os
            os._exit(0)


def main():
    """Main entry point for the GUI application."""
    try:
        root = tk.Tk()
        app = KGITradingGUI(root)
        root.mainloop()
    except KeyboardInterrupt:
        print("應用程式被用戶中斷")
    except Exception as e:
        print(f"應用程式錯誤: {e}")
    finally:
        import os
        os._exit(0)


if __name__ == "__main__":
    main()
