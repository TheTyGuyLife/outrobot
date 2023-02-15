import os

def filecreation(guild):
  creator = open("./Servers/{}".format(guild),'w')
  creator.close()
  return
