#Author - Sivakumar Swaminathan
#FIRST PART of the script is to define all the variable [Analysis ID, DSetId, DSourceId, Template ID] with the only input of Dashboard Id
import boto3
import sys
import re
import subprocess
import json

#PREPARING THE ENVIRONMENT VARIABLES
#Account ID ==> 
AAI='404931103732'
#Dashboard ID ==> d1667c8d-027d-4045-9791-141b21e4ea61
DashboardId=sys.argv[1]

client = boto3.client('quicksight')

Dashboard_desc = client.describe_dashboard(
    AwsAccountId= AAI,
    DashboardId=DashboardId,
)
#Dashboard Name ==> 
Dashboard_Name=Dashboard_desc['Dashboard']['Name']
Dashboard_Name="".join(re.split(r'[\\\-\/\ ]', Dashboard_Name))

#Analysis ID ==> 
#Describing Dashbaord to fetch the analysis id
Arn=Dashboard_desc['Dashboard']['Version']['SourceEntityArn']
AnalysisId = Arn[51:]

#Data Set Id ==> in list
#Describing Dashbaord and iterating over the number of datasets to fetch the data set ids
DSetId=[]
datasets=Dashboard_desc['Dashboard']['Version']['DataSetArns']
for n in datasets:
    DSetId.append(n[50:])  #List of Datasets

#Data Source Id ==> in list
#Iterating and describing the fetched dataset to fetch the data source ids
DSourceId=[]
for n in DSetId:
    dataset_desc = client.describe_data_set(
        AwsAccountId=AAI,
        DataSetId=n
    )
    mid_value1=dataset_desc['DataSet']['PhysicalTableMap']
    datasources=dataset_desc['DataSet']['PhysicalTableMap'][list(mid_value1.keys())[0]]['RelationalTable']['DataSourceArn']
    DSourceId.append(datasources[53:])  #List of Datasources

#Template ID ==> 
TemplateId=Dashboard_Name
########################### ALL THE VARIABLES ARE DESCRIBED AND INSCRIBED IN THE 'Ids.txt' FILE ############################

#MIDDLE PART of the script is to create the folder structure 
subprocess.call(['sh','shell_scripts/create_directory_tree.sh', Dashboard_Name, DashboardId, AnalysisId])
############################################################################################################################

#LAST PART of the script is to create the template, Analysis, Dashboard, Dataset and Datasource of each resource in the approriate folders
subprocess.call(['sh','shell_scripts/template_creation.sh', AAI, AnalysisId, TemplateId, Dashboard_Name])

for n in DSetId:
    subprocess.call(['sh','shell_scripts/dataset_creation.sh', AAI, n, Dashboard_Name])

subprocess.call(['sh','shell_scripts/analysis_dashboard_creation.sh', AAI, AnalysisId, TemplateId, DashboardId, Dashboard_Name])

for n in DSourceId:
    subprocess.call(['sh','shell_scripts/datasource_creation.sh', AAI, n, Dashboard_Name])

####################################################### END OF SCRIPT ######################################################