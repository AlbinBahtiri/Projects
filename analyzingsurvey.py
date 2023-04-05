import csv
from collections import defaultdict, Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('data2020.csv')

conditions = [
    df['MainBranch'] == 'I am a developer by profession',
    df['MainBranch'] == 'I used to be a developer by profession, but no longer am'
]

values = [
    'I am a developer by profession',
    'I used to be a developer by profession, but no longer am'
]

df['profession'] = np.select(conditions, values, default='Other')

filtered_df = df[df['profession'].isin(values)]
filtered_df.loc[:, 'salary'] = 0
print(filtered_df.head(10))
filtered_df.to_csv('filtered_data.csv', index=False)



with open('filtered_data.csv') as f:
    csv_reader=csv.DictReader(f)
    total=0
    
    
    df=pd.read_csv('filtered_data.csv')
    country_split=df['Country']
    frame_split=df['WebframeWorkedWith']
    sat_split=df['JobSat']
    edlevel_split=df['EdLevel']



    country_counter=Counter()
    language_counter=Counter()
    

    for line in csv_reader:
        languages=line['LanguageWorkedWith'].split(';')
        
        language_counter.update(languages)
        total+=1
with open('language_file.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Language', 'Percentage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for language, value in language_counter.most_common(10):
        language_pct = round((value / total) * 100, 2)
        writer.writerow({'Language': language, 'Percentage': f'{language_pct}%'})

framework_counts=Counter()
pct_framework=0 
for frame in frame_split:
    if isinstance(frame,str):
        frame_items=frame.split(';')
        pct_framework+=len(frame_items)
        for frames in frame_items:
            frame=frame.strip()
        if frames=='':
            continue
        if frames in framework_counts:
            framework_counts[frame]+=1
        else:
            framework_counts[frame]=1

a=10
most_common_frameworks=framework_counts.most_common(a)
for frameworks, count in most_common_frameworks:
    percentagefr=count/pct_framework *100
    print(f'{frameworks}: {percentagefr: .2f}%')
    print('--------------------------------------')



country_counts=Counter()
pct_result=0
for value in country_split:
    if isinstance(value,str):
        items=value.split(',')
        pct_result+=len(items)
        for item in items:
            item=item.strip()
        if item=="":
            continue
        if item in country_counts:
            country_counts[item]+=1
        else:
            country_counts[item]=1

n=10
most_common_countries=country_counts.most_common(n)
for country, count in most_common_countries:
    percentage=count / pct_result *100
    print(f'{country}: {percentage: .2f}%')
    print('--------------------------------------')


collab_tools = df["NEWCollabToolsWorkedWith"]  
collab_tools.dropna(inplace = True)  
collab_tools = collab_tools.str.split(";")

tool_counts = collab_tools.explode().value_counts()

tool_percentages = tool_counts / tool_counts.sum() * 100

print(tool_percentages.apply(lambda x: '{:.2f}%'.format(x)))


sat_counts=Counter()
pct_sat=0
for sat in sat_split:
    if isinstance(sat,str):
        sat_items=sat.split(',')
        pct_sat+=len(sat_items)
        for ss in sat_items:
            ss=ss.strip()
        if ss=="":
            continue
        if ss in sat_counts:
            sat_counts[ss]+=1
        else:
            sat_counts[ss]=1

s=5
most_common_sat=sat_counts.most_common(s)
for sat, count in most_common_sat:
    pcc=count / pct_sat*100
    print(f'{sat}: {pcc: .2f}%')
    print('--------------------------------------')


edcounts = df['EdLevel'].value_counts()
pct_ed = edcounts.apply(lambda x: x / df.shape[0] * 100)
formatted_pct = pct_ed.apply(lambda x: f'{x:.2f}%')
print(formatted_pct)
#formatted_pct.to_csv('education_percentage.csv', index=True, header=['Percentage'])
print('--------------------------------------')

df = df[df['Gender'].isin(['Man', 'Woman'])]
grouped = df.groupby(['Gender', 'JobFactors']).size().reset_index(name='counts')
gender_counts = df['Gender'].value_counts()
grouped['pct'] = grouped.apply(lambda x: x['counts'] / gender_counts[x['Gender']] * 100, axis=1)
pivoted = grouped.pivot(index='Gender', columns='JobFactors', values='pct')
pivoted = pivoted.applymap(lambda x: f"{x:.2f}%")

#pivoted.to_csv('result.csv',index=True)


job_factor=df['JobFactors']
job_factor.dropna(inplace=True)
job_factor=job_factor.str.split(';')

job_factor_counts=pd.Series([j for i in job_factor.tolist()for j in i]).value_counts()

job_factor_percentage=job_factor_counts / job_factor_counts.sum() *100
for factor, percentage in job_factor_percentage.items():
    #job_factor_percentage.to_csv("job_factor_percentage.csv")

    print(f"{factor}: {percentage:.2f}%")
    print("_--------------------------------------_")



hours_worked_per_week = df["WorkWeekHrs"] 
hours_worked_per_week.dropna(inplace =True) 

def logics_for_work_hours(hours_worked_per_week):

    less_than_30_hours = []
    thirty_to_34_hours = []
    thirtyfive_to_39_hours = []
    fourty_to_44_hours = []
    fourtyfive_to_49_hours = []
    fifty_to_54_hours = []
    fiftyfive_to_59_hours = []
    sixty_to_64_hours = []
    sixtyfive_to_69_hours = []
    seventy_hours_or_more = []

    for i in hours_worked_per_week:
        if int(i) in list(range(0,30)):
            less_than_30_hours.append(i)
        elif int(i) in list(range(30,35)):
            thirty_to_34_hours.append(i)
        elif int(i) in list(range(35,40)):
            thirtyfive_to_39_hours.append(i)
        elif int(i) in list(range(40,45)):
            fourty_to_44_hours.append(i)
        elif int(i) in list(range (45,50)):
            fourtyfive_to_49_hours.append(i)
        elif int(i) in list(range(50,55)):
            fifty_to_54_hours.append(i)
        elif int(i) in list(range (55,60)):
            fiftyfive_to_59_hours.append(i)
        elif int(i) in list(range (60,65)):
            sixty_to_64_hours.append(i)
        elif int(i) in list(range (65,70)):
            sixtyfive_to_69_hours.append(i)
        else:
            seventy_hours_or_more.append(i)

    len_less_than_30_hours = len(less_than_30_hours)
    len_thirty_to_34_hours = len(thirty_to_34_hours)
    len_thirtyfive_to_39_hours = len(thirtyfive_to_39_hours)
    len_fourty_to_44_hours = len(fourty_to_44_hours)
    len_fourtyfive_to_49_hours = len(fourtyfive_to_49_hours) 
    len_fifty_to_54_hours = len(fifty_to_54_hours)
    len_fiftyfive_to_59_hours = len(fiftyfive_to_59_hours)
    len_sixty_to_64_hours = len(sixty_to_64_hours)
    len_sixtyfive_to_69_hours = len(sixtyfive_to_69_hours)
    len_seventy_hours_or_more = len(seventy_hours_or_more)

    global key_Phrases  
    global Quantity      

    
    key_Phrases = ["Less than 30 hours", "30 to 34 hours", "35 to 39 hours", "40 to 44 hours", "45 to 49 hours", "50 to 54 hours",
                    "55 to 59 hours", "60 to 64 hours", "65 to 69 hours", "70 hours or more"]
    Quantity = [len_less_than_30_hours, len_thirty_to_34_hours, len_thirtyfive_to_39_hours, len_fourty_to_44_hours, 
                len_fourtyfive_to_49_hours, len_fifty_to_54_hours, len_fiftyfive_to_59_hours, len_sixty_to_64_hours,
                len_sixtyfive_to_69_hours, len_seventy_hours_or_more]

logics_for_work_hours(hours_worked_per_week)

key_Phrases.reverse()
Quantity.reverse()

total = sum(Quantity)
pct_sal = [(value/total)*100 for value in Quantity]
for i in range(len(key_Phrases)):
    print(key_Phrases[i]," : ",round(pct_sal[i],2), "%")

    print("_--------------------------------------_")



hours_worked_per_week = df["WorkWeekHrs"]   
hours_worked_per_week.dropna(inplace = True) 


countries = ["United Kingdom"  , "Brazil" , "Germany" , "India" , "France" , "Albania" , "United States" ]

key_Phrases=[]    
Quantity=[]

for i in countries:
    hours_worked_per_week_by_country =  df[(hours_worked_per_week != "nan") & (df["Country"] == i)]  
    Hours_worked_per_week_by_country = hours_worked_per_week_by_country["WorkWeekHrs"] 
    number_of_people = len(Hours_worked_per_week_by_country)
    sum_hours = sum(Hours_worked_per_week_by_country)
    average_hours  = round(sum_hours / number_of_people,1 )

    key_Phrases.append(i)  
    Quantity.append(average_hours)

total_sum=sum(Quantity)
pct_sum=[round((value/total_sum)*100,1)for value in Quantity]

for i in range(len(countries)):
    print(key_Phrases[i] + ": " + str(Quantity[i]) + " (" + str(pct_sum[i]) + "%)")

    print("_--------------------------------------_")

#EXPERIENCE

data_name=df["YearsCodePro"]
data_name.dropna(inplace=True)

def logics_for_less_than_5s(data_name):

    less_than_5 = []
    five_to_9 = []
    ten_to_14 = []
    fifteen_to_19 = []
    twenty_to_24 = []
    twentyfive_to_29 = []
    thirty_to_34 = []
    thirtyfive_to_39 = []
    fourty_to_44 = []
    fourtyfive_to_49 = []
    fifty_or_more = []

    for i in data_name:
        if int(i) in list(range(0,5)):
            less_than_5.append(i)
        elif int(i) in list(range(5,10)):
            five_to_9.append(i)
        elif int(i) in list(range(10,15)):
            ten_to_14.append(i)
        elif int(i) in list(range(15,20)):
            fifteen_to_19.append(i)
        elif int(i) in list(range (20,25)):
            twenty_to_24.append(i)
        elif int(i) in list(range(25,30)):
            twentyfive_to_29.append(i)
        elif int(i) in list(range (30,35)):
            thirty_to_34.append(i)
        elif int(i) in list(range (35,40)):
            thirtyfive_to_39.append(i)
        elif int(i) in list(range (40,45)):
            fourty_to_44.append(i)
        elif int(i) in list(range(45,50)):
            fourtyfive_to_49.append(i)
        else:
            fifty_or_more.append(i)

    len_less_than_5 = len(less_than_5)
    len_five_to_9 = len(five_to_9)
    len_ten_to_14 = len(ten_to_14)
    len_fifteen_to_19 = len(fifteen_to_19)
    len_twenty_to_24 = len(twenty_to_24)
    len_twentyfive_to_29 = len(twentyfive_to_29)
    len_thirty_to_34 = len(thirty_to_34)
    len_thirtyfive_to_39 = len(thirtyfive_to_39)
    len_fourty_to_44 = len(fourty_to_44)
    len_fourtyfive_to_49 = len(fourtyfive_to_49)
    len_fifty_or_more = len(fifty_or_more)
    
    global key_Phrases   
    global Quantity     

    key_Phrases = ["Less than 5 years", "5 to 9 years", "10 to 14 years", "15 to 19 years", "20 to 24 years", "25 to 29 years", 
                 "30 to 34 years", "35 to 39 years", "40 to 44 years", "45 to 49 years", "50 years or more"]
    Quantity = [len_less_than_5, len_five_to_9, len_ten_to_14, len_fifteen_to_19, len_twenty_to_24, len_twentyfive_to_29,
               len_thirty_to_34, len_thirtyfive_to_39, len_fourty_to_44, len_fourtyfive_to_49, len_fifty_or_more ]

def print_percentages(key_Phrases, Quantity):
    total = sum(Quantity)
    for i in range(len(key_Phrases)):
        percent = (Quantity[i] / total) * 100
        print(key_Phrases[i] + ': ' + str(round(percent, 2)) + '%')
        
data_name = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]
logics_for_less_than_5s(data_name)
print_percentages(key_Phrases, Quantity)


sopart=df['SOPartFreq']
sopart.dropna(inplace=True)
sopart=sopart.str.split(':')

sopart_counts=pd.Series([z for i in sopart.tolist()for z in i]).value_counts()
sopart_pct=sopart_counts / sopart_counts.sum() * 100
for so, pct_freq in sopart_pct.items():
    print(f'{so}: {pct_freq:.2f}%')



def sort_dict_by_value(Dictionary, reverse=False):
    return dict(sorted(Dictionary.items(), key=lambda x: x[1], reverse=reverse))

platforms_worked_with = df["PlatformWorkedWith"]
platforms_worked_with.dropna(inplace=True)

platforms_with_no_others = []
for i in platforms_worked_with:
    if i == "Other(s):":
        a = 6
    else:
        platforms_with_no_others.append(i.split(";"))

union = []
for i in platforms_with_no_others:
    for k in i:
        if k == "Other(s):":
            a = 5
        else:
            union.append(k)

counted = Counter(union)
Counted = sort_dict_by_value(counted, False)

key_Phrases = []
Quantity = []

total_count = sum(Counted.values())  

items = Counted.items()
for item in items:
    key_Phrases.append(item[0])
    Quantity.append(item[1])

    percentage = (item[1] / total_count) * 100
    print(f"{item[0]}: {percentage:.2f}%")
    
with open('platforms_percentages.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Platform', 'Percentage'])

    for item in items:
        platform = item[0]
        percentage = (item[1] / total_count) * 100
        writer.writerow([platform, percentage])