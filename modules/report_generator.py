from fpdf import FPDF
import io
import os
from datetime import datetime

def generate_pdf_report(drug_name: str, analysis_text: str) -> bytes:
    """
    Analiz sonucunu PDF olarak oluştur ve bytes döndür.
    """
    pdf = FPDF()
    pdf.add_page()

    # Türkçe karakter desteği için font
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, "..", "assets", "Roboto-Regular.ttf")
    font_path_bold = os.path.join(current_dir, "..", "assets", "Roboto-Bold.ttf")
    
    pdf.add_font("Roboto", "", font_path, uni=True)
    pdf.add_font("Roboto", "B", font_path_bold, uni=True)

    # Başlık
    pdf.set_font("Roboto", "B", 16)
    pdf.cell(0, 12, f"İlaç Analiz Raporu: {drug_name}", ln=True, align="C")
    pdf.set_font("Roboto", "", 10)
    pdf.cell(0, 8, f"Oluşturulma: {datetime.now().strftime('%d.%m.%Y %H:%M')}", ln=True, align="C")
    pdf.ln(5)

    # Uyarı kutusu
    pdf.set_fill_color(255, 243, 205)
    pdf.set_font("Roboto", "B", 10)
    pdf.multi_cell(0, 8,
        "UYARI: BU RAPOR BİLGİLENDİRME AMAÇLIDIR. TIBBİ TAVSİYE DEĞİLDİR. "
        "İLAÇ KULLANMADAN ÖNCE DOKTORUNUZA DANIŞINIZ.",
        fill=True)
    pdf.ln(5)

    # Analiz içeriği
    pdf.set_font("Roboto", "", 11)
    # Markdown başlıklarını temizle
    clean_text = analysis_text.replace("##", "").replace("**", "").replace("*", "")
    pdf.multi_cell(0, 7, clean_text)

    # PDF'i bytes olarak döndür
    pdf_output = pdf.output(dest="S")
    if isinstance(pdf_output, str):
        return pdf_output.encode("latin-1")
    return bytes(pdf_output)
