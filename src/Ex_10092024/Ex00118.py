# try :
#      # try this code, if error
# except:
#       # execute the code if has some error.
try:
    import math
    math.exp(1000) # overflowerror : math range error
except Exception as e:
    print(e)
    print("Plz try to use the lower exp value")