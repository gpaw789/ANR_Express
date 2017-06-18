#Author: George Paw
#This GUI is meant to be used to assist in ANR sign off

from PySide.QtCore import *
from PySide.QtGui import *
import sys
import os
import json

#custom
import data
import PDF_Write

__appname__ = "ANR Express v0.2 by GPAW"

class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        #setting up objects to be on the layout
        self.setWindowTitle(__appname__)
        self.hospital_address_label = QLabel("Hospital/Address:")
        self.hospital_address = QLineEdit()
        self.location_label = QLabel("Location/FW Site No.:")
        self.location = QLineEdit()
        self.sales_label = QLabel("Sales Order No.:")
        self.sales = QLineEdit()
        self.product_number_label = QLabel("Product Number:")
        self.product_number = QLineEdit()
        self.serial_number_label = QLabel("Unit Serial Number:")
        self.serial_number = QLineEdit()
        self.completed_date_label = QLabel("Action Date:")
        self.completed_date = QLineEdit()
        self.job_number_label = QLabel("Job No./Service Incident NO.:")
        self.job_number = QLineEdit()
        self.completed_per_instruction_box = QCheckBox("Completed per Instruction")
        self.completed_by_factory_box = QCheckBox("Completed by the factory prior to delivery")
        self.not_comp_not_affected_box = QCheckBox("Not Completed as this unit is not affected per instruction because:(state reason)")
        self.not_comp_required_parts_box = QCheckBox("Not completed because required parts & instructions are received by the customer")
        self.not_comp_refuse_box = QCheckBox("Not completed because customer refuses to install FCO:(state reason)")
        self.customer_name_label = QLabel("Customer Name (Please Print):")
        self.customer_name = QLineEdit()
        self.customer_title_label = QLabel("Customer Title")
        self.customer_title = QLineEdit()
        self.branch_region_dealer_label = QLabel("Branch Region Dealer::")
        self.branch_region_dealer = QLineEdit()
        self.customer_services_engineer_label = QLabel("Customer Services Engineer:")
        self.customer_services_engineer = QLineEdit()
        self.signed_date_label = QLabel("Signed Date:")
        self.signed_date = QLineEdit()
        self.contact_label = QLabel("Contact: george.paw(at)philips.com")

        write2pdf = QPushButton("Generate ANR")


        #putting objects into layout
        layout = QVBoxLayout()      #Q vertical box layout, can do horizontal
        #layout = QWidget()

        layout.addWidget(self.hospital_address_label)
        layout.addWidget(self.hospital_address); self.setLayout(self.hospital_address.setFixedWidth(600))
        layout.addWidget(self.location_label)
        layout.addWidget(self.location); self.setLayout(self.location.setFixedWidth(600))
        layout.addWidget(self.sales_label)
        layout.addWidget(self.sales); self.setLayout(self.sales.setFixedWidth(600))
        layout.addWidget(self.product_number_label)
        layout.addWidget(self.product_number); self.setLayout(self.product_number.setFixedWidth(600))
        layout.addWidget(self.serial_number_label)
        layout.addWidget(self.serial_number); self.setLayout(self.serial_number.setFixedWidth(600))
        layout.addWidget(self.completed_date_label)
        layout.addWidget(self.completed_date); self.setLayout(self.completed_date.setFixedWidth(600))
        layout.addWidget(self.job_number_label)
        layout.addWidget(self.job_number); self.setLayout(self.job_number.setFixedWidth(600))
        layout.addWidget(self.completed_per_instruction_box)
        layout.addWidget(self.completed_by_factory_box)
        layout.addWidget(self.not_comp_not_affected_box)
        layout.addWidget(self.not_comp_required_parts_box)
        layout.addWidget(self.not_comp_refuse_box)
        layout.addWidget(self.customer_name_label)
        layout.addWidget(self.customer_name); self.setLayout(self.customer_name.setFixedWidth(600))
        layout.addWidget(self.customer_title_label)
        layout.addWidget(self.customer_title); self.setLayout(self.customer_title.setFixedWidth(600))
        layout.addWidget(self.branch_region_dealer_label)
        layout.addWidget(self.branch_region_dealer); self.setLayout(self.branch_region_dealer.setFixedWidth(600))
        layout.addWidget(self.customer_services_engineer_label)
        layout.addWidget(self.customer_services_engineer); self.setLayout(self.customer_services_engineer.setFixedWidth(600))
        layout.addWidget(self.signed_date_label)
        layout.addWidget(self.signed_date); self.setLayout(self.signed_date.setFixedWidth(600))
        layout.addWidget(write2pdf)
        layout.addWidget(self.contact_label)



        #set the layout
        self.setLayout(layout)



        #connecting the objects to a trigger action
        self.connect(write2pdf, SIGNAL("clicked()"), self.write_to_data)


        #pre setting values
        json_data = data.get_json()
        self.hospital_address.setText(str(json_data["hospital_address"]))
        self.location.setText(str(json_data["location"]))
        self.sales.setText(str(json_data["sales"]))
        self.product_number.setText(str(json_data["product_number"]))
        self.serial_number.setText(str(json_data["serial_number"]))
        self.completed_date.setText(str(json_data["completed_date"]))
        self.job_number.setText(str(json_data["job_number"]))
        if json_data["completed_per_instruction"] is True:
            self.completed_per_instruction_box.setChecked(1)
        if json_data["completed_by_factory"] is True:
            self.completed_by_factory_box.setChecked(1)
        if json_data["not_comp_not_affected"] is True:
            self.not_comp_not_affected_box.setChecked(1)
        if json_data["not_comp_required_parts"] is True:
            self.not_comp_required_parts_box.setChecked(1)
        if json_data["not_comp_refused"] is True:
            self.not_comp_refuse_box.setChecked(1)
        self.customer_name.setText(str(json_data["customer_name"]))
        self.customer_title.setText(str(json_data["customer_title"]))
        self.branch_region_dealer.setText(str(json_data["branch_region_dealer"]))
        self.customer_services_engineer.setText(str(json_data["customer_services_engineer"]))
        self.signed_date.setText(str(json_data["signed_date"]))


        self.db_path = None
        self.mtr_path = None


    def dialogOpen(self):
        initValues = {"mainSpinBox": self.mainSpinBox.value(), "mainCheckBox": self.mainCheckBox.isChecked(),
          }
        dialog = Dialog(initValues)  # using dict is better than using a structed argument entries - more flexible
        if dialog.exec_():  # link the value from another class in
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())


    def write_to_data(self):
        #read the actual values of the text and re-generate the json again, this will get picked up by the PDF_Write
        #re-create the json to be used as a placeholder, just ignore the values
        json_data = {
            "hospital_address": "Fiona Stanley Hospital",
            "location": "94400693",
            "sales": "NA",
            "product_number": "866064",
            "serial_number": "DE35109690",
            "completed_date": "28/12/2016",
            "job_number": "44866128",
            "completed_per_instruction": True,
            "completed_by_factory": False,
            "not_comp_not_affected": False,
            "not_comp_required_parts": False,
            "not_comp_refused": False,
            "customer_name": "Andrea (Kunnikorn) Pantazis",
            "customer_title": "Siemens MES Supervisor",
            "branch_region_dealer": "Philips Australia",
            "customer_services_engineer": "George Paw",
            "signed_date": "28/12/2016",
        }

        json_data["hospital_address"] = self.hospital_address.text()
        json_data["location"] = self.location.text()
        json_data["sales"] = self.sales.text()
        json_data["product_number"] = self.product_number.text()
        json_data["serial_number"] = self.serial_number.text()
        json_data["completed_date"] = self.completed_date.text()
        json_data["job_number"] = self.job_number.text()
        json_data["completed_per_instruction"] = self.completed_per_instruction_box.isChecked()
        json_data["completed_by_factory"] = self.completed_by_factory_box.isChecked()
        json_data["not_comp_not_affected"] = self.not_comp_not_affected_box.isChecked()
        json_data["not_comp_required_parts"] = self.not_comp_required_parts_box.isChecked()
        json_data["not_comp_refused"] = self.not_comp_refuse_box.isChecked()
        json_data["customer_name"] = self.customer_name.text()
        json_data["customer_title"] = self.customer_title.text()
        json_data["branch_region_dealer"] = self.branch_region_dealer.text()
        json_data["customer_services_engineer"] = self.customer_services_engineer.text()
        json_data["signed_date"] = self.signed_date.text()

        #converting to json data and write to file, then call the PDF writer
        json_data = json.dumps(json_data)
        with open("data.txt", "w") as sfile:
            sfile.write(json_data)
        PDF_Write.write_to_pdf()

        #inform user the pdf has been generated
        QMessageBox.information(self, __appname__, str("ANR for %s generated" % self.serial_number.text()))

        return 0




#check for json

def check_data():
    if os.path.isfile("data.txt"):
        return 0
    else:
        data.generate_data()

#check for output folder
def check_folder():
    if os.path.exists("_output"):
        return 0
    else:
        os.makedirs("_output")

check_data()
check_folder()
app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()