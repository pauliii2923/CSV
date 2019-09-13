from CSV import CSV

# load data in from csv file (from https://catalog.data.gov/dataset/local-weather-archive)
weather_data = CSV().DictRead("rdu-weather-history.csv",delimiter=";")

# print headers

print(weather_data[0].keys())

# write data to a new file
CSV().DictWrite(weather_data,"weather_data.csv")


# convert the csv file to an excel file
CSV().CsvToXlsx("weather_data.csv")


# test converting the excel file data back to csv
CSV().XlsxToCsv("Workbook.xlsx",sheet="Sheet")