# raise keyword used to rethrow

stats1={
    "Company":['Accenture','Wipro','TCS','Infoview','MindTree'],
    "Year":[2006,2002,2018,2016,2012],
    "Count":[67,10,6,32,19],
    "Day":[1,4,2,1,2]
}

def getInfo():
    try:
        column = input("Tell us on which title based info you need: ")
        print(stats1[column])
    except KeyError as kerror:
        raise kerror

try:
    getInfo()
except KeyError as error:
    print(error, "\nCan't find title")
    getInfo()