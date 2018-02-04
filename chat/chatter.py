def putout(methodology,txt,f):
 methodologies=["Info","Action","Speech"]
 putoutStr=methodologies[methodology]+": "+txt
 print(putoutStr)
 f.write(putoutStr+"\n")
