# This module should be used to store immutable configuration parameters of the pipeline / analysis

# Predefined sourcedata and derivatives directory paths
from pathlib import Path
sourcedata_dir = Path().absolute().parents[1] / 'sourcedata'
derivatives_dir = Path().absolute().parents[1] / 'derivatives'

# Subjects being fully excluded from analysis:
exclusions=(
    117,165,183,189,
    201,217,247,254,265,270,278,283,284,
    300,307,323
)

new_columns = {
    # ED-1 & ED-2
    'face':'facepic', 'runnum':'block', 'trialnum':'trial',
    'fracrt':'choicert', 'fracst':'choicest','facert':'outcomert', 'facest':'outcomest',
    'probrt':'esttaskrt', 'probst':'esttaskst','optionchosen':'stockchosen',
    'probgood':'estimation','trueprobgood':'trueprob', 'totalpayout':'bankaccount',
    
    # ED-3
    'originalparticipant':'subjnum', 'experimenter':'experimentername',
    'stockimagename':'stockpic', 'bondimagename':'bondpic', 'faceimage':'facepic',
    'originalblock':'block', 'originaltrialorder':'trial',
    'rt':'choicert', 'estimationvalue':'estimation',
    'trueprobability':'trueprob', 'accuracy':'genderjudgment',
    'confidencevalue':'confidence',
    # duplicate:
    #   'facert':'outcomert',
    # excluded for processing in a different way:
    #   'stockfractallocationtype':'cueonleft', 'bondfractallocationtype':'cueonright',
}

## Prefer to import the above dict - should only have to use below if 
## there is overlap in the original column names between the datasets

new_df_1_columns = {
    'face':'facepic', 'runnum':'block', 'trialnum':'trial',
    'fracrt':'choicert', 'fracst':'choicest','facert':'outcomert', 'facest':'outcomest',
    'probrt':'esttaskrt', 'probst':'esttaskst','optionchosen':'stockchosen',
    'probgood':'estimation','trueprobgood':'trueprob', 'totalpayout':'bankaccount',
    
}
new_df_2_columns = new_df_1_columns

new_df_3_columns = {
    'originalparticipant':'subjnum', 'experimenter':'experimentername',
    'stockimagename':'stockpic', 'bondimagename':'bondpic', 'faceimage':'facepic',
    'originalblock':'block', 'originaltrialorder':'trial',
    #'stockfractallocationtype':'cueonleft', 'bondfractallocationtype':'cueonright',
    'rt':'choicert', 'estimationvalue':'estimation',
    'trueprobability':'trueprob', 'accuracy':'genderjudgment',
    'confidencevalue':'confidence', 'facert':'outcomert'
    }