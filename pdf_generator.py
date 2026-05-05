from fpdf import FPDF
import datetime

class ReportPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(30, 80, 162)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, 'GenAI Business Analytics Report', ln=True, fill=True, align='C')
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Generated on {datetime.date.today()} | Powered by Gemini AI', align='C')


def create_pdf(insights: str, analysis: dict, filename: str = "outputs/report.pdf"):
    import os
    os.makedirs("outputs", exist_ok=True)
    
    pdf = ReportPDF()
    pdf.add_page()

    # Dataset Overview
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(30, 80, 162)
    pdf.cell(0, 10, 'Dataset Overview', ln=True)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(3)

    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f"Rows: {analysis['shape'][0]}    |    Columns: {analysis['shape'][1]}", ln=True)
    pdf.cell(0, 7, f"Columns: {', '.join(analysis['columns'])}", ln=True)
    pdf.ln(4)

    # AI Insights
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(30, 80, 162)
    pdf.cell(0, 10, 'AI-Generated Insights', ln=True)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(3)

    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(0, 0, 0)
    clean = insights.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 7, clean)

    pdf.output(filename)
    print(f"\n✅ PDF saved at: {filename}")
    return filename