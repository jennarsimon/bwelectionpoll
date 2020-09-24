import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("2020 Election Poll - Lehigh University (Responses)").sheet1

# Extract and print all of the values
list_of_lists = sheet.get_all_values()

headers = ['Timestamp', 'LehighAffiliation', 'UndergradYear', 'UndergradCollege', 'UndergradMajor',	'UndergradGreek', 'UndergradInternational',	
'GradDegree', 'GradCollege', 'GradProgram', 'GradGraduation', 'GradInternational', 'FacultyCollege', 'FacultyDepartment', 'FacultyYears',
'Gender', 'GenderSelfIdentify',	'Race/Ethnicity', 'Hispanic/Latino', 'Age', 'VoteLikelihood', 'VoteRegistered', 'VoteInPA', 'VoteFactors',	
'VoteLocal', 'PartyAffiliation', 'Ideology', 'PresidentialSupport', 'PresidentialSupportStrength', 'VoteMethod', 'SupportImpact', 
'EnvironmentGovInvolvement', 'EnvironmentParis', 'EnvironmentImportance', 'HealthcareSinglePayer', 'HealthcareCOVID', 'HealthcareImportance',	
'TaxIncreaseUpperBrackets', 'TaxCorps', 'TaxMinimumWage', 'TaxMarijuana', 'TaxImportance', 'ImmigrationWall', 'ImmigrationGovPrograms',	
'ImmigrationDACA', 'ImmigrationImportance',	'ForeignMilitarySpending', 'ForeignMoreRefugees', 'ForeignImportance', 'EducationTuitionSupport',	
'EducationStandardizedTests', 'EducationImportance', 'VotingElectoralCollege', 'VotingSameDay', 'VotingFelon', 'LGBTQDiscriminationLaws',	
'LGBTQImportance', 'ReproductivePlannedParenthood', 'ReproductiveAbortion',	'ReproductiveBirthControl',	'ReproductiveImportance',	
'GunsRestrictions',	',GunsOpenCarry', 'GunsImportance',	'PolicingDefund', 'PolicingImportance',	'OtherIssues']						

df = pd.DataFrame(list_of_lists)
df.columns = headers
df = df.reindex(df.index.drop(0)).reset_index(drop=True)
df.columns.name = None

# Undergrad specific
undergrad = df[df['LehighAffiliation'] == 'Undergraduate student'].iloc[:, np.r_[0, 2:7, 15:67]]

# Grad specific
grad = df[df['LehighAffiliation'] == 'Graduate student'].iloc[:, np.r_[0, 7:12, 15:67]]

# Faculty specific
faculty = df[df['LehighAffiliation'] == 'Faculty'].iloc[:, np.r_[0, 12:67]]

college = []
for row in df.index :
    if df['LehighAffiliation'][row] == 'Undergraduate student' :
        college.append(df['UndergradCollege'][row])
    elif df['LehighAffiliation'][row] == 'Graduate student' :
        college.append(df['GradCollege'][row])
    elif df['LehighAffiliation'][row] == 'Faculty' :
        college.append(df['FacultyCollege'][row])
    else :
        college.append('')

df['College'] = college

cleanedData = df.iloc[:, np.r_[0:2, 67, 15:67]]

issueQuestions = cleanedData.iloc[:, np.r_[0:8, 19:55]]
generalQuestions = cleanedData.iloc[:, np.r_[0:19]]

print(cleanedData)

# with pd.ExcelWriter(r'CleanedElectionData.xlsx') as writer:
#     cleanedData.to_excel(writer, sheet_name='Cleaned Data')
#     undergrad.to_excel(writer, sheet_name='Undergrad Data')
#     grad.to_excel(writer, sheet_name='Grad Data')
#     faculty.to_excel(writer, sheet_name='Faculty Data')
#     issueQuestions.to_excel(writer, sheet_name='Issue Questions')
#     generalQuestions.to_excel(writer, sheet_name='General Questions')
