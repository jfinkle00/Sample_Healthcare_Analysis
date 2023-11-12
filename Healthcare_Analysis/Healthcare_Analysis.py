import csv
import tabulate
from tabulate import tabulate
#vars

def average_value(total:int,sample_size:int)->float:
    return total / sample_size
def make_table(data:[], header)->[]:
    return tabulate(data, headers= [header, "Average Insurance Cost", "Difference in Cost"], tablefmt="fancy_grid")


#overall vars
sample_size_total = 0
insurance_cost_total = 0
#smoking vs nonsmoking
smoker_sample_size = 0
non_smoker_sample_size = 0
smoker_insurance_cost = 0
non_smoker_insurance_cost =0
#gender vars
male_sample_size = 0
female_sample_size = 0
male_cost_insurance_total = 0
female_cost_insurance_total = 0
#regional vars
northeast_count = 0
northwest_count = 0
southeast_count = 0
southwest_count = 0
northeast_insurance_total = 0
northwest_insurance_total = 0
southeast_insurance_total = 0
southwest_insurance_total = 0
#BMI vars
underweight_cost_insurance_total = 0
underweight_sample = 0
normal_weight_cost_insurance_total = 0
normal_weight_sample = 0
obease_cost_insurance_total = 0
obease_sample = 0
#Age vars
insurance_total_18to30 = 0
sample_size_18to30 = 0
insurance_total_31to50 = 0
sample_size31to50 = 0
insurance_total_over50 = 0
sample_size_over50 = 0
#Children Vars
insurance_total_children = 0
sample_size_parents = 0
insurance_total_no_children = 0
sample_size_childless = 0


insurance_file = open("insurance.csv")

insurance_read = insurance_file.read()

insurance_split = insurance_read.split("\n")

for insurance in insurance_split:
    sample_size_total += 1

for insurance in insurance_split:
    if "yes" in insurance:
        smoker_sample_size += 1
    elif "no" in insurance_split:
        non_smoker_sample_size += 1

for insurance in insurance_split:
    if "female" not in insurance:
        male_sample_size += 1
    elif "female" in insurance:
        female_sample_size += 1

for insurance in insurance_split:
    if "northeast" in insurance:
        northeast_count += 1
    elif "northwest" in insurance:
        northwest_count += 1
    elif "southeast" in insurance:
        southeast_count += 1
    elif "southwest" in insurance:
        southwest_count += 1


insurance_values = []




for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[6] != "charges":
        insurance_values.append(float(insurance[6]))
        insurance_cost_total += float(insurance[6])


for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[1] == "male":
        male_cost_insurance_total += float(insurance[6])
    elif len(insurance) > 1 and insurance[1] == "female":
        female_cost_insurance_total += float(insurance[6])

   
#BMI vars
underweight = 18.5
overweight = 25
obease = 30

for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[2] != "bmi" and float(insurance[2]) < 18.5:
        underweight_cost_insurance_total += float(insurance[6])
        underweight_sample += 1
for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[2] != "bmi" and float(insurance[2]) >= 18.5 and float(insurance[2]) < 25:
        normal_weight_cost_insurance_total += float(insurance[6])
        normal_weight_sample += 1
for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[2] != "bmi" and float(insurance[2]) >= 30:
        obease_cost_insurance_total += float(insurance[6])
        obease_sample += 1
for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[4] == "yes":
        smoker_insurance_cost += float(insurance[6])
        smoker_sample_size += 1
    elif len(insurance) > 1 and insurance[4] == "no":
        non_smoker_insurance_cost += float(insurance[6])
        non_smoker_sample_size += 1
for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[0] != "age" and int(insurance[0]) < 31:
        insurance_total_18to30 += float(insurance[6])
        sample_size_18to30 += 1
for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[0] != "age" and int(insurance[0]) >= 31 and int(insurance[0]) < 51:
        insurance_total_31to50 += float(insurance[6])
        sample_size31to50 += 1
for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[0] != "age" and int(insurance[0]) >= 51:
        insurance_total_over50 += float(insurance[6])
        sample_size_over50 += 1
for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[3] != "children" and int(insurance[3]) > 0:
        insurance_total_children += float(insurance[6])
        sample_size_parents += 1
    elif len(insurance) > 1 and insurance[3] != "children" and int(insurance[3]) == 0:
        insurance_total_no_children += float(insurance[6])
        sample_size_childless += 1

for insurance in insurance_split:
    insurance = insurance.split(",")
    if len(insurance) > 1 and insurance[5] == "northeast":
        northeast_insurance_total += float(insurance[6])
    elif len(insurance) > 1 and insurance[5] == "northwest":
        northwest_insurance_total += float(insurance[6])
    elif len(insurance) > 1 and insurance[5] == "southeast":
        southeast_insurance_total += float(insurance[6])
    elif len(insurance) > 1 and insurance[5] == "southwest":
        southwest_insurance_total += float(insurance[6])
    



#Average stats
average_insurance_cost = average_value(insurance_cost_total,sample_size_total)

#Gendered stats
female_average_insurance = average_value(female_cost_insurance_total, female_sample_size)
male_average_insurance = average_value(male_cost_insurance_total, male_sample_size)

#BMI stats
average_underwieght_cost = average_value(underweight_cost_insurance_total, underweight_sample)
average_normal_weight_cost = average_value(normal_weight_cost_insurance_total, normal_weight_sample)
average_obease_cost = average_value(obease_cost_insurance_total, obease_sample)

#Smoking stats
average_smoker_cost = average_value(smoker_insurance_cost, smoker_sample_size)
average_non_smoker_cost = average_value(non_smoker_insurance_cost, non_smoker_sample_size)

#Age stats
average_insurance_cost_18to30 = average_value(insurance_total_18to30,sample_size_18to30)
average_insurance_cost_31to50 = average_value(insurance_total_31to50, sample_size31to50)
average_insurance_cost_over50 = average_value(insurance_total_over50,sample_size_over50)

#Parental stats
average_insurance_cost_parents = average_value(insurance_total_children, sample_size_parents)
average_insurance_cost_childless = average_value(insurance_total_no_children, sample_size_childless)

#Region stats
average_cost_northeast = average_value(northeast_insurance_total,northeast_count)
average_cost_northwest = average_value(northwest_insurance_total,northwest_count)
average_cost_southeast = average_value(southeast_insurance_total,southeast_count)
average_cost_southwest = average_value(southwest_insurance_total,southwest_count)



#Difference Stats

#Gendered differences
gender_average_cost_dif = female_average_insurance - male_average_insurance

#BMI differences
diff_cost_normal_underweight = average_underwieght_cost - average_insurance_cost
diff_cost_normal_obease = average_normal_weight_cost - average_insurance_cost
diff_cost_normal_average = average_obease_cost - average_insurance_cost

#Smoking differences
smoking_cost_diff = average_smoker_cost - average_non_smoker_cost

#Age differences
age_cost_diff_young = average_insurance_cost_18to30 - average_insurance_cost
age_cost_diff_middle = average_insurance_cost_31to50 - average_insurance_cost
age_cost_diff_old =  average_insurance_cost_over50 - average_insurance_cost

#Parental status differences
parent_nonparent_cost_diff = average_insurance_cost_parents - average_insurance_cost_childless

#Region differences
northeast_diff_avg = average_cost_northeast - average_insurance_cost
northwest_diff_avg = average_cost_northwest - average_insurance_cost
southeast_diff_avg = average_cost_southeast - average_insurance_cost
southwest_diff_avg = average_cost_southwest - average_insurance_cost


#Tables

#Gender

gender_table = [["Male", male_average_insurance,abs(gender_average_cost_dif)], ["Female", female_average_insurance, gender_average_cost_dif]]
gender_table_final = make_table(gender_table, "Gender")
#BMI

BMI_table = [["Underweight", average_underwieght_cost,diff_cost_normal_underweight], ["Normal Weight", average_normal_weight_cost,diff_cost_normal_average *-1],
              ["Obease", average_obease_cost, abs(diff_cost_normal_obease)]]
BMI_table_final = make_table(BMI_table, "BMI Range")

#Smoking

smoking_table = [["Smoker", average_smoker_cost,smoking_cost_diff],["non-Smoker", average_non_smoker_cost,smoking_cost_diff * -1]]

smoking_table_final = make_table(smoking_table, "Smoking Status")

#Age

age_table = [["18 to 30", average_insurance_cost_18to30,age_cost_diff_young],["31 to 50", average_insurance_cost_31to50,age_cost_diff_middle],
              ["Over 50", average_insurance_cost_over50, age_cost_diff_old]]
age_table_final = make_table(age_table,"Age Group")

#Parental Status

parent_table = [["Parent",average_insurance_cost_parents,parent_nonparent_cost_diff], ["non-Parent",average_insurance_cost_childless,parent_nonparent_cost_diff * -1]]

parent_table_final = make_table(parent_table,"Parental_Status")

#Regions

region_table = [["Northeast",average_cost_northeast,northeast_diff_avg],["Northwest", average_cost_northwest,northwest_diff_avg],
                 ["Southeast", average_cost_southeast,southeast_diff_avg], ["Southwest",average_cost_southwest,southwest_diff_avg]]
region_table_final = make_table(region_table, "Region")


print(gender_table_final)
print(BMI_table_final)
print(smoking_table_final)
print(parent_table_final)
print(region_table_final)
print(age_table_final)






















insurance_file.close()


