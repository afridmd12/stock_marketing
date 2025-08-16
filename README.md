# 📊 Stock Market Dashboard

A web-based interactive dashboard built with **Flask** and **Plotly** to analyze stock market data.  
Easily upload CSV files, select tickers, and visualize stock price trends.  
Deployed live on **Render** 👉 [Stock Market Dashboard](https://stock-marketing.onrender.com)

---

## 🚀 Features
- 📂 **Upload CSV** with stock market data (Date, Close, etc.)
- 📈 **Interactive Charts** powered by Plotly
- 🔍 **Select Ticker Dropdown** (AAPL, NFLX, etc.)
- 📊 **Dynamic Stock Price Analysis**
- 📑 **/report page** with additional insights
- ☁️ **Deployed on Render**

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap, Plotly.js
- **Deployment:** Render
- **Version Control:** Git & GitHub

---

## 📂 Project Structure
stock_marketing/
│
├── app.py # Flask app entry point
├── requirements.txt # Python dependencies
├── Procfile # Render deployment config
├── static/ # CSS, JS, images
├── templates/ # HTML templates (dashboard, report, etc.)
└── README.md # Project documentation


---

## ⚙️ Installation & Local Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/afridmd12/stock_marketing.git
   cd stock_marketing

2. Create Virtual environment
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux

3. Install dependencies
   pip install -r requirements.txt

4. Run the app
   python app.py
  Visit 👉 http://127.0.0.1:3001
