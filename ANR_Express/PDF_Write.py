from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

import StringIO
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#custom
import data

def write_to_pdf():
    #read variables from data.txt
    json_data = data.get_json()

    #conver true false to X
    if json_data["completed_per_instruction"] is True:
        completed_per_instruction_text = "X"
    else:
        completed_per_instruction_text = ""
    if json_data["completed_by_factory"] is True:
        completed_by_factory_text = "X"
    else:
        completed_by_factory_text = ""
    if json_data["not_comp_not_affected"] is True:
        not_comp_not_affected_text = "X"
    else:
        not_comp_not_affected_text = ""
    if json_data["not_comp_required_parts"] is True:
        not_comp_required_parts_text = "X"
    else:
        not_comp_required_parts_text = ""
    if json_data["not_comp_refused"] is True:
        not_comp_refused_text = "X"
    else:
        not_comp_refused_text = ""

    packet = StringIO.StringIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    #can.drawString(PositionX, PositionY, "STRING")
    #see translation.xlsx for the conversion
    can.drawString(173, 654, str(json_data["hospital_address"]))
    can.drawString(188, 633, str(json_data["location"]))
    can.drawString(440, 631, str(json_data["sales"]))
    can.drawString(201, 600, str(json_data["product_number"]))
    can.drawString(201, 566, str(json_data["serial_number"]))
    can.drawString(74, 503, completed_per_instruction_text)
    can.drawString(264, 503, str(json_data["completed_date"]))
    can.drawString(364, 503, str(json_data["job_number"]))
    can.drawString(74, 472, completed_by_factory_text)
    can.drawString(74, 438, not_comp_not_affected_text)
    can.drawString(74, 397, not_comp_required_parts_text)
    can.drawString(74, 363, not_comp_refused_text)
    can.drawString(104, 279, str(json_data["customer_name"]))
    can.drawString(380, 279, str(json_data["customer_title"]))
    can.drawString(133, 194, str(json_data["branch_region_dealer"]))
    can.drawString(84, 162, str(json_data["customer_services_engineer"]))
    can.drawString(368, 162, str(json_data["signed_date"]))

    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader("template.pdf")
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    file_path = os.path.relpath("_output/ANR_%s.pdf" % str(json_data["serial_number"]))
    outputStream = open(file_path, "wb")
    output.write(outputStream)
    outputStream.close()