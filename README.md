# 📊 Stock Market Dashboard

An interactive **Stock Market Analysis Web App** built with **Flask**, **Plotly**, and **Pandas**, deployed on **Render**, and version-controlled with **GitHub**.  
This project allows users to upload stock market CSV data, select tickers, and visualize stock price trends in an intuitive dashboard.

---

## 📂 About the Data
- Input: **CSV file** with stock market data  
- Required columns: `Date`, `Close`, (and optionally `Ticker`)  
- Use cases:  
  - Visualizing closing prices  
  - Comparing multiple tickers  
  - Generating quick insights via the `/report` page  

---

## ⚙️ Why These Technologies?
- **Flask** → Backend framework to handle routing and rendering.  
- **Pandas** → Data processing and CSV handling.  
- **Plotly** → Interactive charts for stock price visualization.  
- **Bootstrap** → Simple, responsive UI styling.  
- **Render** → Cloud deployment platform integrated with GitHub.  

---

## 🚀 Complete Process (From Start to Finish)
1. **Create Project Folder**  
   Example: `D:\stock_market_dashboard`  

2. **Create & Activate Virtual Environment**  
   - Windows:  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS/Linux:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**  
   ```bash
   pip install flask pandas plotly gunicorn
   pip freeze > requirements.txt
   ```

4. **Build Flask Application**  
   - `app.py` contains routes:  
     - `/` → Upload CSV & dashboard  
     - `/report` → Insights report page  
   - Uses Flask for backend, Pandas for CSV handling, Plotly for chart rendering.  

5. **Add Project Files**  
   - `app.py` → Main Flask app  
   - `templates/` → HTML (home, report)  
   - `static/` → CSS & JS  
   - `requirements.txt` → Installed dependencies  
   - `Procfile` → For Render deployment (`web: gunicorn app:app`)  

6. **Initialize Git & Push to GitHub**  
   ```bash
   git init
   git remote add origin https://github.com/YOUR-USERNAME/stock_market_dashboard.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

7. **Deploy on Render**  
   1. Go to [Render](https://render.com)  
   2. Create a new **Web Service**  
   3. Connect your GitHub repository  
   4. Set build/start commands:  
      - **Build Command:** `pip install -r requirements.txt`  
      - **Start Command:** `gunicorn app:app`  
   5. Deploy 🚀  

---

## ✅ Features
- Upload custom stock market CSV data  
- Interactive Plotly visualizations  
- Select ticker dropdown for comparison  
- Report page with insights  
- Fully hosted on Render  

---

## 💻 Run Locally
1. Clone repo:  
   ```bash
   git clone https://github.com/afridmd12/stock_marketing.git
   ```
2. Navigate:  
   ```bash
   cd stock_market_dashboard
   ```
3. Create virtual environment & activate  
4. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
5. Run app:  
   ```bash
   python app.py
   ```
6. Open in browser:  
   `http://127.0.0.1:5000`  

---

## 🌐 Deployment
- Hosted on **Render**  
- Live URL: [https://stock-marketing.onrender.com](https://stock-marketing.onrender.com)  

---

## 📝 Author
👤 Mohammed Afrid  
📌 GitHub: [afridmd12](https://github.com/afridmd12)
