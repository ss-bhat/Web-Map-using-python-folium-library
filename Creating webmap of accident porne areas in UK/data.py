import pandas

data = pandas.read_csv("garda_stations.csv", encoding="latin-1")
col_name = ["2004","2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"]

print(data.columns)