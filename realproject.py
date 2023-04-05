import csv
from collections import defaultdict, Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('data2020.csv')

conditions=[
    df['MainBranch']=='I am a developer by profession',
    df['MainBranch']=='I used to be a developer by profession, but no longer am',
]

#print(df.isnull().sum())
a=df.dropna()
print(a.isnull().sum())
a.to_csv('newfile.csv',index=False)   

new_rows=[]

for i, row in a.iterrows():
    languages=row['LanguageWorkedWith'].split(';')

    for language in languages:
        new_row={'Respondent':row['Respondent'],'LanguageWorkedWith':language}
        new_rows.append(new_row)
new_df=pd.DataFrame(new_rows)


new_data=[]

for x,k in a.iterrows():
    databases=k['DatabaseWorkedWith'].split(';')

    for database in databases:
        new_k={'Respondent':k['Respondent'],'DatabaseWorkedWith':database}
        new_data.append(new_k)
new_df=pd.DataFrame(new_data)
new_df.to_csv("databaseworkedwith.csv",index=False)


new_plat=[]

for c,b in a.iterrows():
    platforms=b['PlatformWorkedWith'].split(';')

    for platform in platforms:
        new_b={'Respondent':b['Respondent'],'PlatformWorkedWith':platform}
        new_plat.append(new_b)
new_df=pd.DataFrame(new_plat)
new_df.to_csv("Platformworkedwith.csv",index=False)


new_tools=[]

for f,m in a.iterrows():
    tools=m['NEWCollabToolsWorkedWith'].split(';')

    for tool in tools:
        new_m={'Respondent':m['Respondent'],'NEWCollabToolsWorkedWith':tool}
        new_tools.append(new_m)
new_df=pd.DataFrame(new_tools)
new_df.to_csv("ToolsWorkedWith.csv",index=False)


new_frame=[]

for l,g in a.iterrows():
    frames=g['WebframeWorkedWith'].split(';')

    for frame in frames:
        new_g={'Respondent':g['Respondent'],'WebframeWorkedWith':frame}
        new_frame.append(new_g)
new_df=pd.DataFrame(new_frame)
new_df.to_csv("FrameworkWorkedWith.csv",index=False)



new_factors=[]

for q,w in a.iterrows():
    factors=w['JobFactors'].split(';')

    for factor in factors:
        new_w={'Respondent':w['Respondent'],'JobFactors':factor}
        new_factors.append(new_w)
new_df=pd.DataFrame(new_factors)
new_df.to_csv("RealJobFactors.csv",index=False)



new_titles=[]

for v,n in a.iterrows():
    titles=n['DevType'].split(';')

    for title in titles:
        new_n={'Respondent':n['Respondent'],'DevType':title}
        new_titles.append(new_n)
new_df=pd.DataFrame(new_titles)
new_df.to_csv("DevTypes.csv",index=False)



new_platforms=[]

for r,t in a.iterrows():
    platforms=t['PlatformWorkedWith'].split(';')

    for platform in platforms:
        new_t={'Respondent':t['Respondent'],'PlatformWorkedWith':platform}
        new_platforms.append(new_t)
new_df=pd.DataFrame(new_platforms)
new_df.to_csv("RealPlatformWorkedWith.csv",index=False)












a['Experience']=''
a.loc[a['YearsCodePro']=='Less than 1 year','Experience']='Less than 1 year'
a.loc[a['YearsCodePro']=='1','Experience']='1 year or less'
a.loc[a['YearsCodePro'].isin(['2','3','4','5']),'Experience']='2 to 5 years'
a.loc[a['YearsCodePro'].isin(['6','7','8','9']),'Experience']='6 to 9 years'
a.loc[a['YearsCodePro'].isin(['10','11','12','13','14']),'Experience']='10 to 15 years'
a.loc[a['YearsCodePro'].isin(['15','16','17','18','19']),'Experience']='More than 15 years'
a.loc[a['YearsCodePro'].isin(['20','21','22','23','24']),'Experience']='More than 20 years'
a.loc[a['YearsCodePro'].isin(['25','26','27','28','29']),'Experience']='More than 25 years'
a.loc[a['YearsCodePro'].isin(['30','31','32','33','34']),'Experience']='More than 30 years'
a.loc[a['YearsCodePro'].isin(['35','36','37','38','39']),'Experience']='More than 35 years'
a.loc[a['YearsCodePro'].isin(['40','41','42','43','44']),'Experience']='More than 40 years'
a.loc[a['YearsCodePro'].isin(['45','46','47','48','49']),'Experience']='More than 45 years'
a.loc[a['YearsCodePro'].isin(['50','51','52','53','54']),'Experience']='More than 50 years'

a.to_csv('experience.csv',index=False) 









# import pandas as pd

# def split_and_save_data(filename, column_name, new_filename):
#     new_rows = []

#     a = pd.read_csv(filename)

#     for i, row in a.iterrows():
#         values = row[column_name].split(';')
#         for value in values:
#             new_row = {'Respondent': row['Respondent'], column_name: value}
#             new_rows.append(new_row)

#     new_df = pd.DataFrame(new_rows)
#     new_df.to_csv(new_filename, index=False)

# split_and_save_data('survey_results_public.csv', 'LanguageWorkedWith', 'languages_worked_with.csv')
# split_and_save_data('survey_results_public.csv', 'DatabaseWorkedWith', 'databases_worked_with.csv')
# split_and_save_data('survey_results_public.csv', 'PlatformWorkedWith', 'platforms_worked_with.csv')
# split_and_save_data('survey_results_public.csv', 'NEWCollabToolsWorkedWith', 'tools_worked_with.csv')
# split_and_save_data('survey_results_public.csv', 'WebframeWorkedWith', 'frameworks_worked_with.csv')
# split_and_save_data('survey_results_public.csv', 'JobFactors', 'job_factors.csv')


# def split_database_worked_with(a):
#     new_data=[]
#     for x,k in a.iterrows():
#         databases=k['DatabaseWorkedWith'].split(';')
#         for database in databases:
#             new_k={'Respondent':k['Respondent'],'DatabaseWorkedWith':database}
#             new_data.append(new_k)
#     new_df=pd.DataFrame(new_data)
#     new_df.to_csv("databaseworkedwith.csv",index=False)
#     return new_df
# new_df = split_database_worked_with(a)


