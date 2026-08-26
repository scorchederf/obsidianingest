import os, sys, json

if len(sys.argv) != 2:
    print("Error: Incorrect number of arguments.")
    print("Usage: python3 " + sys.argv[0] + " [json-file]")
    exit(-1)

filename = sys.argv[1] #filename should now contain the path to the json file.
if not os.path.exists(filename):
    print("Error: Json file does not exist.")
    exit(-1)


isEqual = False
#Implement your json parsing code here:
f = open (filename, "r")
  
# Reading from file
data = json.loads(f.read())

#print (data)
  
# Iterating through the json
# list
try:
    number1 = int(data['Values'][0]['Number'], data['Values'][0]['Base'])
    # print(number1)
    number2 = int(data['Values'][1]['Number'], data['Values'][1]['Base'])
    # print(number2)
    if number1 == number2:
        isEqual = True
except:
    isEqual = False 

# Closing file
f.close()

if isEqual:
    print("1")
else:
    print("0")




    



  
