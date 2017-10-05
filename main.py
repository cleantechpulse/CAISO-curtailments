import pdf_miner_extract as pdf

pdf_text = pdf.convert_pdf_to_txt('data/Wind_SolarReal-TimeDispatchCurtailmentReportApr02_2017.pdf')

print(pdf_text)
