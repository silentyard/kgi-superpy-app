# GitHub 上傳指南

## 方法 1: 使用 GitHub 網頁界面

### 步驟 1: 建立新的 GitHub 儲存庫
1. 前往 [GitHub.com](https://github.com)
2. 點擊右上角的 "+" 按鈕
3. 選擇 "New repository"
4. 填寫儲存庫資訊：
   - **Repository name**: `kgi-superpy-app`
   - **Description**: `KGI Securities Trading Application with GUI and CLI support`
   - **Visibility**: Public 或 Private（您的選擇）
   - **不要**勾選 "Initialize this repository with a README"
5. 點擊 "Create repository"

### 步驟 2: 連接本地儲存庫到 GitHub
在您的本地專案目錄執行以下命令：

```bash
# 添加遠端儲存庫（請替換為您的 GitHub 用戶名）
git remote add origin https://github.com/YOUR_USERNAME/kgi-superpy-app.git

# 設定預設分支名稱
git branch -M main

# 推送到 GitHub
git push -u origin main
```

## 方法 2: 使用 GitHub Desktop

1. 下載並安裝 [GitHub Desktop](https://desktop.github.com/)
2. 開啟 GitHub Desktop
3. 點擊 "File" > "Add Local Repository"
4. 選擇您的專案資料夾 `d:\_coding\kgi_superpy`
5. 點擊 "Publish repository"
6. 填寫儲存庫名稱和描述
7. 點擊 "Publish Repository"

## 方法 3: 使用 VS Code 的 Git 整合

1. 在 VS Code 中開啟您的專案
2. 點擊左側的 Git 圖示
3. 點擊 "Publish to GitHub"
4. 選擇 "Publish to GitHub public repository" 或私人儲存庫
5. 填寫儲存庫名稱：`kgi-superpy-app`
6. 點擊 "Publish"

## 完成後的檢查

上傳成功後，您的 GitHub 儲存庫應該包含：

```
kgi-superpy-app/
├── .github/
│   └── copilot-instructions.md
├── examples/
│   ├── basic_usage.py
│   └── gui_usage.py
├── kgi_trading_app/
│   ├── __init__.py
│   └── client.py
├── tests/
│   ├── quick_test.py
│   └── test_client.py
├── .gitignore
├── gui_main.py
├── LICENSE
├── main.py
├── PROJECT_SUMMARY.md
├── README.md
├── requirements.txt
├── simple_test.py
└── start_gui.bat
```

## 建議的儲存庫設定

### 標籤 (Topics)
在 GitHub 儲存庫頁面右側，添加以下標籤：
- `python`
- `trading`
- `securities`
- `kgi`
- `gui`
- `tkinter`
- `api`
- `finance`

### 保護設定
建議啟用以下設定：
- 分支保護規則
- 要求 pull request 審查
- 啟用自動安全更新

### Release 版本
考慮建立第一個版本：
1. 前往 "Releases" 頁面
2. 點擊 "Create a new release"
3. 標籤版本：`v1.0.0`
4. 發布標題：`Initial Release - KGI SuperPy Trading App`
5. 描述版本特性和變更

## 後續維護

### 更新專案
```bash
# 當您有新的更改時
git add .
git commit -m "描述您的更改"
git push origin main
```

### 創建分支進行開發
```bash
# 創建新功能分支
git checkout -b feature/new-feature

# 完成後合併回主分支
git checkout main
git merge feature/new-feature
git push origin main
```

---

**注意**: 請確保不要將真實的 KGI 證券憑證提交到公開儲存庫！
