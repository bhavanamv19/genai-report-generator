import pandas as pd
import os
import subprocess
import sys

from data_analyzer import analyze_data
from report_generator import generate_insights
from pdf_generator import create_pdf

# ── CONFIG ──────────────────────────────────────────
CSV_PATH         = "sample_sales.csv"
BUSINESS_CONTEXT = "Sales"
OUTPUT_PDF       = "outputs/report.pdf"
# ────────────────────────────────────────────────────

os.makedirs("outputs", exist_ok=True)

print("📂 Loading data...")
df = pd.read_csv(CSV_PATH)
print(f"   Loaded: {df.shape[0]} rows × {df.shape[1]} columns")

print("\n🔍 Analyzing data...")
analysis = analyze_data(df)

print("\n🤖 Generating AI insights (Gemini API)...")
insights = generate_insights(analysis, BUSINESS_CONTEXT)

print("\n📄 Creating PDF report...")
create_pdf(insights, analysis, OUTPUT_PDF)

print("\n📊 Insights Preview:")
print("=" * 60)
print(insights)
print("=" * 60)

# Auto-open PDF
print("\n🚀 Opening PDF...")
if sys.platform == "win32":
    os.startfile(os.path.abspath(OUTPUT_PDF))
elif sys.platform == "darwin":
    subprocess.call(["open", OUTPUT_PDF])
else:
    subprocess.call(["xdg-open", OUTPUT_PDF])