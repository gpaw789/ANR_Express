import json

#generate a blank data template to be used
def generate_data():
    data = {
    "hospital_address":"Test Hospital",
    "location":"12345678",
    "sales":"12345678",
    "product_number" : "12345678",
    "serial_number" : "DE1234567",
    "completed_date" : "19/06/2017",
    "job_number" : "87654321",
    "completed_per_instruction" : True,
    "completed_by_factory" : False,
    "not_comp_not_affected" : False,
    "not_comp_required_parts" : False,
    "not_comp_refused" : False,
    "customer_name" : "Joe Blogg",
    "customer_title" : "Biomedical Supervisor",
    "branch_region_dealer" : "Philips Australia",
    "customer_services_engineer" : "John Doe",
    "signed_date" : "19/06/2017",
    }
    json_data = json.dumps(data)

    with open("data.txt", "w") as sfile:
        sfile.write(json_data)
    return 0

#read the current data template, return the json dump
def get_json():
    with open("data.txt", "r") as sfile:
        raw_data = sfile.read()
    return json.loads(raw_data)

