import csv
import statistics


#enter date, press enter if todays date
date = input("date of run (mm/dd/yyyy) :")

#1st km minutes
first_km_min = int(input("how many minutes for first km?"))
#1st km seconds
first_km_sec = int(input("how many seconds on first km?"))
#2nd km minutes
second_km_min = int(input("how many minutes for second km?"))
#2nd km seconds
second_km_sec = int(input("how many seconds on second km?"))
#3rd km minutes
third_km_min = int(input("how many minutes for third km?"))
#3rd km seconds
third_km_sec = int(input("how many seconds on third km?"))
#4th km minutes
fourth_km_min = int(input("how many minutes for fourth km?"))
#4th km seconds
fourth_km_sec = int(input("how many seconds on fourth km?"))
#5th km minutes
fifth_km_min = int(input("how many minutes for fifth km?"))
#5th km seconds
fifth_km_sec = int(input("how many seconds on fifth km?"))
#additional minutes
additional_km_min = int(input("how many minutes for additional distance?"))
#additional seconds
additional_km_sec = int(input("how many seconds on additional didstance?"))
#additional distance
additional_distance = float(input("how far beynd 5km did you run?"))
#5k run type code letter
run_code = input("what is the run code for this run?")

#generate decimal minute variables for each km and additional distance
#decimal = minutes + seconds/60

first_km_time = first_km_min + (first_km_sec/60)
second_km_time = second_km_min + (second_km_sec/60)
third_km_time = third_km_min + (third_km_sec/60)
fourth_km_time = fourth_km_min + (fourth_km_sec/60)
fifth_km_time = fifth_km_min + (fifth_km_sec/60)
additional_km_time = additional_km_min + (additional_km_sec/60)
five_k_times = [first_km_time,second_km_time,third_km_time,fourth_km_time,fifth_km_time]
average_km = statistics.mean(five_k_times)

#append to csv with date 1km, 2km, 3km, 4km, 5km, addi_time, addi_distance, code


fields=[date,first_km_time,second_km_time,third_km_time,fourth_km_time,fifth_km_time,additional_km_time,additional_distance,run_code,average_km]
with open(r'5k_training.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

#exit
quit()
