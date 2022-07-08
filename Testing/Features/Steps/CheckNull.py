from behave import*
import pandas as pd


@given('Open the file from the given location')
def readfile(context):
    f = pd.read_csv(r'C:\Users\Garg\Desktop\XEBIAINTERN\Chicago_Crimes_2001_to_2004.csv', on_bad_lines='skip',low_memory=False)


@when('The file is opened and read')
def readfile(context):
    df = pd.read_csv(r'C:\Users\Garg\Desktop\XEBIAINTERN\Chicago_Crimes_2001_to_2004.csv', on_bad_lines='skip',low_memory=False)
    return df


@then('Check if NULL values exist')
def CheckForNull(context):
    df = pd.read_csv(r'C:\Users\Garg\Desktop\XEBIAINTERN\Chicago_Crimes_2001_to_2004.csv', on_bad_lines='skip',low_memory=False)
    for (colName, colData) in df.iteritems():
        if(df[colName].isnull().values.any()):
            return True
    return False
