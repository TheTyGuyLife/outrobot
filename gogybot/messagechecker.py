
import os
from difflib import SequenceMatcher




def messagechecker(guild, message):
  opener = open("./Servers/{}".format(guild),'r')
  reader = opener.readlines()
  #print("called messagechecker")
  finalreaderlist = []
  for i in reader:
    x = i.replace('\n','')
    finalreaderlist.append(x)
  #print(finalreaderlist)
  for i in finalreaderlist:
    index = finalreaderlist.index(i)
    if (index % 2) == 0:
      pass

    else:
      #print(index)
      ratio = SequenceMatcher(None, message, i)
      counterratio = ratio.ratio()
      #print(counterratio)
      if counterratio >= 0.95:

        returnmessage = finalreaderlist[index+1]
        #print(returnmessage)
        #print('got here')
        return returnmessage
