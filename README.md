# 📊 GenAI Business Report Generator

An AI-powered web application that analyzes any CSV or Excel dataset and automatically generates a professional PDF business report with executive summaries, key findings, and actionable recommendations.

---

## 🚀 Live Demo
> Deploy on Streamlit Cloud and add your link here

---

## ✨ Features

- 📂 Upload any CSV or Excel file
- 🤖 AI-generated insights using Groq API + LLaMA 3.3
- 📄 Auto-generated downloadable PDF report
- 📊 Data preview and quick statistics
- 🎯 Multiple business contexts (Sales, HR, Finance, Marketing, etc.)
- 💯 100% Free — no paid APIs required

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web UI |
| Groq API | AI insights (LLaMA 3.3) |
| Pandas | Data analysis |
| FPDF2 | PDF generation |
| OpenPyXL | Excel file support |

---

## 📁 Project Structure

```
genai-report-generator/
├── app.py                  # Main Streamlit web app
├── data_analyzer.py        # Pandas data analysis logic
├── report_generator.py     # Groq AI API integration
├── pdf_generator.py        # PDF creation logic
├── requirements.txt        # Dependencies
├── .gitignore              # Git ignore rules
└── sample_sales.csv        # Sample dataset for testing
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/bhavanamv19/genai-report-generator.git
cd genai-report-generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your free Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up for free
- Create an API key

### 4. Add your API key
Open `report_generator.py` and replace:
```python
client = Groq(api_key="YOUR_GROQ_API_KEY")
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 📊 How It Works

```
Upload CSV/Excel → Auto Analysis (Pandas) → AI Insights (Groq + LLaMA 3.3) → PDF Report
```

1. Upload any CSV or Excel file
2. Select your business context (Sales, HR, Finance, etc.)
3. Click "Generate AI Report"
4. Download your professional PDF report instantly

---

## 📄 Sample Report Sections

- **Executive Summary** — High-level overview of the data
- **Key Findings** — 5 data-driven bullet points
- **Trends & Patterns** — Observed patterns in the dataset
- **Risks & Data Quality** — Issues identified in the data
- **Actionable Recommendations** — 3-5 concrete next steps

---



---

## 🙋‍♀️ Author

**Bhavana M V**
- 📧 [- 📧 [bhavanamv19@gmail.com](mailto:bhavanamv19@gmail.com)]
- 💼 [LinkedIn](https://linkedin.com/in/bhavanamv19)
- 🐙 [GitHub](https://github.com/bhavanamv19)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
