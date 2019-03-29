#For versions there are two or more kinds for writting
# First one is Major.Minor which can can consider as float number
# Second is Major.Minor.Patch as string
#I will create  two methods to implement that 

# v1 and v2 are float
def  standardVersion(v1,v2):
 try:
  
  if float(v1) < float(v2) :
    
    print("V1 is older than V2")
  
  elif float(v1) > float(v2) :
    
    print("V1 is greater than V2.")
  
  else :
   
    print("V1 and V2 are the same.")

 except  ValueError :
    print("The value entered, it isn't a valid number!  Please try again...")

def semanticVersion(v1,v2):
  
  result = 0;

  v1Splited = v1.split(".")

  v2Splited = v2.split(".")
  
  if len(v1Splited) == 3  and len(v2Splited) == 3:
      
    for i in range(0,3):
      try:
       
       if compareTwoValues(int(v1Splited[i]),int(v2Splited[i])) == 1:
         
         return 1

       elif compareTwoValues(int(v1Splited[i]),int(v2Splited[i])) == -1:

         return -1  

      except ValueError :
           print("invalid number value!")
      
    return  result

  else :
      print("Wrong versions format!")
      
  return -2
    

def  compareTwoValues(v1,v2):

  if v1 < v2 :
    return -1;
  elif v1 > v2 :
    return 1;
  else :
    return 0;
