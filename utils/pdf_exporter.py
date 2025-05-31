# utils/pdf_exporter.py

from fpdf import FPDF

def export_wallet_pdf(wallet):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="Cold Wallet Paper Backup", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Address: {wallet['address']}", ln=True)
    pdf.cell(200, 10, txt=f"Private Key: {wallet['private_key']}", ln=True)
    pdf.ln(10)

    # Gambar QR (jika ada)
    try:
        pdf.image("address.png", x=10, y=60, w=80)
        pdf.image("private_key.png", x=110, y=60, w=80)
    except:
        pass

    pdf.output("cold_wallet.pdf")
