
import os
from difflib import SequenceMatcher




def statuschecker(check):
  opener = open("./Status/{}.txt".format(check),'r')
  reader = opener.readlines()
  #print("called messagechecker")
  if reader == "True":
      return True
  elif reader == "False":
      return False
  else:
      return True
