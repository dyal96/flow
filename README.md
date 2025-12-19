# 🌊 Flow Accounting (Personal Edition)

**Flow Accounting** is a premium, single-file personal finance application designed for privacy, speed, and ease of use. Built with a "local-first" philosophy, your financial data never leaves your device and is encrypted securely in your browser.

![Dashboard Preview](https://github.com/dyal96/flow/blob/main/demo/screenshot.jpg)

## ✨ Key Features

### 🔒 Privacy & Security
- **Client-Side Encryption:** All data used in the app is encrypted using industry-standard Web Crypto API before being stored in your browser's LocalStorage.
- **Offline First:** Works completely offline. No server, no cloud, no subscriptions.
- **Password Protection:** Secure your financial data with a login password.
- **Recovery Options:** Set up security keywords to recover your account if you forget your password.

### 💸 Financial Management
- **Dashboard:** Real-time overview of your Net Worth, Income vs Expenses, and Monthly Cash Flow.
- **Comprehensive Accounts:** Manage Bank Accounts, Cash, Credit Cards, Loans, Investments (FDs), and "Person" accounts (for tracking debts/receivables).
- **Transactions:** Quick and easy entry for Income, Expenses, and Transfers.
- **Categorization:** Custom categories for detailed tracking.
- **Budgeting:** Set monthly budgets per category and track your progress with visual progress bars.

### 📊 Reports & Analytics
- **Visual Charts:** Interactive charts for Spending Breakdown, Income Analysis, and Monthly Trends.
- **Filters:** Powerful filtering by date range, account, type, and category.
- **Export Data:** Export your data to **CSV** (Excel) or **PDF** reports.
- **SQL Export:** For advanced users, export your entire database as SQL commands.

### ⚡ Power User Features
- **Keyboard Shortcuts:** Navigate the entire app without a mouse. Press `?` to view the cheat sheet.
  - `Q` / `N`: Quick Add Transaction
  - `D`: Dashboard
  - `A`: Accounts
  - `T`: Transactions
  - `/`: Open Search
- **Dark Mode:** Beautifully designed Dark Mode for comfortable night usage.
- **Custom Themes:** Choose from multiple themes (Default Blue, Sea Blue, Pink, Pastels).
- **Import/Backup:** Easy JSON backup and restore functionality.


---

## � Future Roadmap: Enterprise & Server Editions

We are planning a complete rebuild of Flow Accounting to support enterprise-grade features and multi-user environments.

### **Phase 2: Python + SQL Server Edition (Coming Soon)**
A robust, server-hosted version built with **Python** (Django/FastAPI) and **SQL Server**.
-   **👥 Multi-User Architecture:** Support for unlimited users with role-based access control.
-   **🗄️ Centralized Database:** Robust data management using Microsoft SQL Server.
-   **� Server-Side Security:** Enterprise-grade authentication and data protection.
-   **☁️ Self-Hosted / Cloud Ready:** Deploy on AWS, Azure, or your own local server using Docker.

### **Phase 3: PHP Shared Hosting Edition**
A lightweight version optimized for standard shared hosting environments (cPanel/LAMP stack) for easy personal deployment.

### **Planned Features for Server Editions:**
-   **🪓 Split Transactions & Budget Rollover**
-   **🎯 Savings Goals & Forecasting**
-   **✅ Bank Reconciliation**
-   **🗑️ Bulk Actions**
-   **📅 Calender with Heatmap**

> **Note:** The current `index.html` version is a **fully functional Personal Demo Edition**. It works perfectly for individual use, requires no server, and demonstrates the core UI/UX concepts.

---

## 🚀 Getting Started

Getting started with Flow Accounting is instant. There is no installation required.

1.  **Download** the preferred version (see below).
2.  **Open** the HTML file in any modern web browser.
3.  **Setup:** Set a password to secure your local vault.
4.  **Enjoy:** Start adding your accounts and transactions!

---

## 📂 Application Editions

Flow Accounting comes in different "editions" to suit your environment:

| File | Edition | Best For... |
| :--- | :--- | :--- |
| **[index.html](index.html)** | **Offline (Default)** | Maximum privacy and reliability. Loads all assets (Tailwind, Chart.js, etc.) from the local `assets/` folder. Works completely without internet. |
| **[Online.html](Online.html)** | **Web Ready (CDN)** | Quick deployment on static hosts (GitHub Pages, Vercel). Fetches libraries via high-speed CDNs. No local assets required. |
| **[simple.html](simple.html)** | **Lightweight** | Users who want a clutter-free experience. Removes complex features like Banking, Credit Cards, and Budgets, focusing on core Cash tracking. |

---

### Deployment (Optional)
Since Flow is a single static file, you can host it anywhere:
- **GitHub Pages:** Rename the file to `index.html` and push to a GitHub repository. Enable Pages in settings.
- **Netlify/Vercel:** Drag and drop the file to deploy instantly.
- **Local:** Just keep it on your desktop!

### 🐳 Docker Deployment
You can also run Flow Accounting in a Docker container:

1.  **Build & Run:**
    ```bash
    docker-compose up -d
    ```
2.  **Access:** Open `http://localhost:8080`


---

## 🛠️ Technology Stack
- **Core:** HTML5, Modern JavaScript (ES6+)
- **Styling:** TailwindCSS (via CDN)
- **Icons:** FontAwesome
- **Charts:** Chart.js
- **Encryption:** Web Crypto API
- **PDF Generation:** jsPDF
- **CSV Parsing:** PapaParse

---

## ⌨️ Keyboard Shortcuts Cheat Sheet

| Key | Action |
| :--- | :--- |
| **Navigation** | |
| `D` | Go to **Dashboard** |
| `A` | Go to **Accounts** |
| `T` | Go to **Transactions** |
| `R` | Go to **Reports** |
| `S` | Go to **Settings** |
| **Actions** | |
| `Q` / `N` | **Quick Add** Transaction |
| `I` / `+` | Add **Income** |
| `O` / `-` | Add **Expense** |
| `Ctrl + Z` | Undo last action |
| `Ctrl + Y` | Redo last action |
| `Shift + T` | Toggle Theme |
| `Shift + H` | Toggle Privacy Mode (Hide Numbers) |

---

*Flow Accounting is a project by Dyal.*

