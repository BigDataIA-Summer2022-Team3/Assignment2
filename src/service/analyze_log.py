
import os


def analyze_log():
    
    logLists = []
    infoNum = 0
    warnNum = 0

    docsNum = 0
    openapiNum = 0
    locationNum = 0
    coordinatesNum = 0
    displayNum = 0
    countNum = 0
    givenNumberNum = 0
    maximumNum = 0
    truncatedNum = 0
    
    if os.stat("src/service/log/logfile.log").st_size == 0:
        return 'File is empty'
    else:
        fp = open("src/service/log/logfile.log", 'r')
        for line in fp.readlines():
            data = line.split(" ")
            list = []
            if(data[2] == "loglevel=INFO"):
                list.append(data[2])
                list.append(data[5].split("\n")[0])
            else:
                list.append(data[2])
                list.append(data[3].split("\n")[0])
            logLists.append(list)
        fp.close
        
        for part in logLists:
            if(part[0] == 'loglevel=INFO'): infoNum = infoNum + 1
            elif(part[0] == 'loglevel=WARNING'): warnNum = warnNum + 1
            
            if(part[1] == '/docs'): docsNum = docsNum + 1
            elif(part[1] == '/openapi.json'): openapiNum = openapiNum + 1
            elif(part[1] == '/img/airplane/location'): locationNum = locationNum + 1
            elif(part[1] == '/img/airplanes/coordinates'): coordinatesNum = coordinatesNum + 1
            elif(part[1] == '/img/display'): displayNum = displayNum + 1
            elif(part[1] == '/img/airplanes/count'): countNum = countNum + 1
            elif(part[1] == '/img/airplanes/givenNumber'): givenNumberNum = givenNumberNum + 1
            elif(part[1] == '/img/airplanes/maximum'): maximumNum = maximumNum + 1
            elif(part[1] == '//img/airplanes/truncated'): truncatedNum = truncatedNum + 1
            
        finalList = []
        finalList.append(['infoNum', infoNum - warnNum])
        finalList.append(['warnNum', warnNum])
        finalList.append(['docsNum', docsNum])
        finalList.append(['openapiNum', openapiNum])
        finalList.append(['locationNum', locationNum])
        finalList.append(['coordinatesNum', coordinatesNum])
        finalList.append(['displayNum', displayNum])
        finalList.append(['countNum', countNum])
        finalList.append(['givenNumberNum', givenNumberNum])
        finalList.append(['maximumNum', maximumNum])
        finalList.append(['truncatedNum', truncatedNum])
        
        return finalList

#print(analyze_log())