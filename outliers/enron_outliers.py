#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

max_bonus = 0
max_salary = 0
### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    max_bonus = max(max_bonus, bonus)
    max_salary = max(max_salary, salary)
    matplotlib.pyplot.scatter( salary, bonus )

print(max_bonus)
print(max_salary)
print(data_dict)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


