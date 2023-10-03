import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Receipt
from .forms import ReceiptForm

def criar_e_salvar_pdf(receipt):
    buffer = BytesIO()

    # criar o PDF com o ReportLab
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Recebemos de: {receipt.name_recipient}")
    p.drawString(100, 730, f"O Valor: R$ {receipt.amount}")
    p.drawString(100, 710, f"Referente a: {receipt.referent}")
    p.showPage()
    p.save()

    # local temporário 
    temp_file_path = os.path.join("C:\\Users\\BC2G8585\\Desktop\\py\\receiptGenerator\\temp", f"recibo_{receipt.id}.pdf")
    with open(temp_file_path, "wb") as pdf_file:
        pdf_file.write(buffer.getvalue())

    return temp_file_path


def criar_recibo(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save()
            # criar o pdf.
            temp_file_path = criar_e_salvar_pdf(receipt)
            with open(temp_file_path, "rb") as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type="application/pdf")
                response["Content-Disposition"] = f"attachment; filename=recibo_{receipt.id}.pdf"
                return response
    else:
        form = ReceiptForm()
    return render(request, 'receipt_app/receipt_form.html', {'form': form})

