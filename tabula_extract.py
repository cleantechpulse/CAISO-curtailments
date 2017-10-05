import tabula
import pandas as pd

# read pdf into dataframe
#df = tabula.read_pdf('data/Wind_SolarReal-TimeDispatchCurtailmentReportApr02_2017.pdf', pages=[3,4])
df = tabula.read_pdf('http://www.caiso.com/Documents/Wind_SolarReal-TimeDispatchCurtailmentReportOct02_2017.pdf', pages=4)

# split hour and curtailment type columns using regular expressions
df['HOUR'] = df.iloc[:,1].str.extract('(\d+)', expand=False)
df['CURT TYPE'] = df.iloc[:,1].str.extract('([A-Za-z]+)', expand=False)


# drop extra columns
df = df.loc[:,['DATE', 'HOUR', 'CURT TYPE', 'REASON', 'FUEL TYPE', 'CURTAILED MWH', 'CURTAILED MW']]

print(df)
#df.to_csv('data/curtailments_2017-04-02.csv')