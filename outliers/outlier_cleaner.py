#!/usr/bin/python


def outlierCleaner(predictions, salary, bonus):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    ### your code goes here
    print(predictions)
    print(len(predictions))
    for i in range(len(predictions)):
        cleaned_data.append((salary[i][0], bonus[i][0], abs(bonus[i][0] - predictions[i][0])))
    print("cleaned_data:",cleaned_data)
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    print(len(cleaned_data))
    return cleaned_data[0:81]

