import datetime
import logging



# Get current iso date and time integer  (YYYYMMDD)
isoDate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

#input variables	

logfilefuse  = r'in\dss-badge-api-logs\fuse.log'
logfilefuse1 = r'in\dss-badge-api-logs\fuse.log.1'

logfileInnedfuse  = r'in\ineed-notification-api-logs\fuse.log'
logfileInnedfuse1 = r'in\ineed-notification-api-logs\fuse.log.1'

#output variables

outFileApi = 'out\extractApi_'+isoDate+'.txt'
outFilePass = 'out\extractPass_'+isoDate+'.txt'

outSingleFile = 'out\extractInvoke_api_01.txt'
outSingleIneedFileStart = 'out\extractIneed_api_03_Start.txt'
outSingleIneedFileEnd = 'out\extractIneed_api_03_End.txt'

outSingleSCPFile = 'out\extractSCP_api_05.txt'
outSingleRFSFile = 'out\extractRFS_api_05.txt'

#1.	Access Pass API Invocation: 
#catching: 
#        InvokeID |PayloadOrResponseCode  |StartDate               |RFS               |EndDate
#        InvokeID |400                    |2023-07-28 15:12:14,322 | RFS-1-7811140234 |2023-07-28 15:12:15,322

def getApiInvoke(fileIn, fileOut):
  outFile = open(fileOut, 'a')
  #header
  filterLn = "InvokeID|PayloadOrResponseCode|StartDate|RFS|EndDate\n"
  outFile.write(filterLn)
  filterLn = ""

  with open(fileIn, 'r') as read:
    for line in read:
      if line.startswith('ID: '):
        #taking last 4 characters of the line excep line break
        filterLn = line[0:-1] + "|"
      if 'Payload: {"txnType":"AP-SEP-C' in line:
        filterLn += line[11:18] + "|"
      if 'Response-Code:' in line:
        filterLn =  filterLn.replace('ID: ','' )
        filterLn += line[-4:-1] + "|"+ "|" 
      if ("inside direct:createBadge route" in line):
        if filterLn.startswith('ID:'):
          #REPLACE ID: with empty string
          filterLn =  filterLn.replace('ID: ','' )
          filterLn += line[:23] + "|"
      if ("<ns:SRNum>RFS-1-" in line):
        #identify the char index of <ns:SRNum>RFS-1-
        index = line.find("<ns:SRNum>RFS-1-")
        filterLn += line[index+10:index+26] + "|"
        filterLn += line[:23]+ "\n"
        outFile.write(filterLn)

#3.	Ineed Response Log:
def getIneedInvoke(fileIn, fileOutStart, fileOutEnd):
    outFileStart = open(fileOutStart, 'a')
    outFileEnd = open(fileOutEnd, 'a')
    #header
    filterLn = "StartDate|RFS|EndDate\n"
    outFileStart.write(filterLn)
    outFileEnd.write(filterLn)	
    filterLn = ""
    RFS = ""
    nextRFS = ""
    flagInRFSCall = False
    with open(fileIn, 'r') as read:
      for line in read:
        index = line.find("RFS-1-")
        if index != -1:
          RFS = line[index:index+16]
        if 'Inside IneedNotificationRouteBuilder - str:' in line :
          filterLn = "Start|" +line[:23] + "|" + RFS  + "\n" 
          outFileStart.write(filterLn)
          flagInRFSCall = True
        #closing call
        if 'direct:processAccessPassAPREQ...After writing to local folder...' in line:
          if flagInRFSCall:
            filterLn = "End|" +line[:23] + "|" + RFS + "\n" 
            flagInRFSCall = False
            outFileEnd.write(filterLn)
                  


#5.	SCP response log:
def getSCPresponse(fileIn, fileOut):
    outFile = open(fileOut, 'a')
    #header
    filterLn = "StartDate|EndDate\n"
    outFile.write(filterLn)
    filterLn = ""
    flagInRFSCall = False
    with open(fileIn, 'r') as read:
      for line in read:
        index = line.find("RFS-1-")
        if index != -1:
          RFS = line[index:index+16]
        if 'SCP route started' in line:
          filterLn = line[:23] + "|" + RFS + "|" + "\n" 
          flagInRFSCall = True
          outFile.write(filterLn)
        if False and 'SCP route completed!' in line:
          filterLn += line[:23] + "\n" 
          flagInRFSCall = False
          outFile.write(filterLn)


#5.	SCP response log:
def getRFS(fileIn, fileOut):
    print("getRFS started")
    outFile = open(fileOut, 'a')
    filterLn = ""
    with open(fileIn, 'r') as read:
      for line in read:
        if 'RFS-1-' in line:
          filterLn = filterLn + "\n" 
          outFile.write(filterLn)


     
if False:
  getApiInvoke(logfilefuse, outSingleFile)
  getApiInvoke(logfilefuse1, outSingleFile)
if False:
  getIneedInvoke(logfileInnedfuse, outSingleIneedFileStart, outSingleIneedFileEnd)
  getIneedInvoke(logfileInnedfuse1, outSingleIneedFileStart, outSingleIneedFileEnd)
if True:
  getSCPresponse(logfileInnedfuse, outSingleSCPFile)
  getSCPresponse(logfileInnedfuse1, outSingleSCPFile)
if False:
  getRFS(logfileInnedfuse, outSingleRFSFile)
  getRFS(logfileInnedfuse1, outSingleRFSFile)

