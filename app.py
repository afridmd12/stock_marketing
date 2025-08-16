from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def index():
    chart_html = ""
    tickers = []

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            df = pd.read_csv(file)
            df['Date'] = pd.to_datetime(df['Date'])
            tickers = df['Ticker'].unique().tolist()

            ticker = request.form.get("ticker", tickers[0] if tickers else None)
            if ticker:
                subset = df[df['Ticker'] == ticker]
                fig = px.line(subset, x='Date', y='Close', title=f'{ticker} Closing Prices')
                chart_html = pio.to_html(fig, full_html=False)

    return render_template("index.html", chart_html=chart_html, tickers=tickers)

# Optional route to view the pre-generated report (if present)
@app.route("/report")
def report():
    report_path = os.path.join(app.root_path, "stock_analysis_report.html")
    if os.path.exists(report_path):
        # serve the report file
        with open(report_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Report not found.", 404

if __name__ == "__main__":
    # Use PORT env var if provided (Render sets $PORT)
    port = int(os.environ.get("PORT", 3001))
    app.run(host="0.0.0.0", port=port)
