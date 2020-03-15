#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print(len(enron_data))
salary_count = 0
email_count = 0
poi_count = 0
no_data = 0
for person in enron_data:
	if enron_data[person]["salary"] != "NaN":
		salary_count += 1
	if enron_data[person]["email_address"] != "NaN":
		email_count += 1
	if enron_data[person]["total_payments"] == "NaN":
		no_data += 1
	if enron_data[person]["poi"] == True:
		poi_count += 1
print(salary_count)
print(email_count)
print(no_data)
print(poi_count)
