import csv
from collections import Counter, defaultdict
import datetime
from decimal import Decimal

output_filepath = "C:/Users/Copy/Downloads/output.csv"
input_filepath = "C:/Users/Copy/Downloads/paywall_data_combo.csv"
date_format = "%m/%d/%Y %H:%M"
counter = []
with open(output_filepath, "w", newline="") as f_output:
    csv_output = csv.writer(f_output)
    
    with open(input_filepath) as f_input:
        csv_input = csv.reader(f_input)
        #Use next to skip the header row for counting
        header = csv_input.__next__()
        for record in csv_input:
            #Set a default that has a high timedelta so that any paywall can replace it
            current_min = (datetime.timedelta.max, 2)
            has_paid = record[1]
            if has_paid == '1':
                payment_date = datetime.datetime.strptime(record[2], date_format)
                #Use a slice to save on looping
                for idx, paywall_str in enumerate(record[5:]):
                    #Skip if the date isn't present (no paywall hit)
                    if paywall_str != '':
                        #idx+5 to compensate for the slice used above
                        paywall_hit_date = datetime.datetime.strptime(record[idx+5], date_format)
                        one_day = datetime.timedelta(days=1)
                        #24 hour window check
                        if (paywall_hit_date) <= (payment_date) <= (paywall_hit_date + one_day):
                            if payment_date - paywall_hit_date < current_min[0]:
                                #Save a new min when condition is met
                                current_min = (payment_date - paywall_hit_date, idx+5)
                #Add the ID, the name of the paywall, and the dollar amount for the record
                counter.append([record[0], header[current_min[1]], record[3]])
                   
converted_hits = []
#Make a dictionary where the names are keys and value for each is 0
revenue_sums = defaultdict(int)
for item in counter:
    print(item[0],item[1],item[2])
    #Append item name to a list for use with Counter data structure from collections
    converted_hits.append(item[1])
    #Lookup the item by converted paywall name in the revenue_sums dict, and add the dollar amount from the record as a decimal
    revenue_sums[item[1]] += Decimal(item[2])
cnt = Counter(converted_hits)

print(cnt)
print(revenue_sums)
print("Total Paid" + str(len(counter)))
print("Complete")

