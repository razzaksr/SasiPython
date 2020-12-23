stats1={
    "Company":['Accenture','Wipro','TCS','Infoview','MindTree'],
    "Year":[2006,2002,2018,2016,2012],
    "Count":[67,10,6,32,19],
    "Day":[1,4,2,1,2]
}

def getInfo(attempts=1):
    try:
        column = input("Tell us on which title based info you need: ")
        print(stats1[column])
    except KeyError as kerror:
        print(kerror,"\nCan't find title",column)
        attempts+=1
        if attempts<=3:getInfo(attempts)
        else:print("Maximum attempts obtained try later")

getInfo()

'''print(stats1)

print(stats1['Year'])'''