# Method to let enduser to enter the coordinates
def getLineCoordinates(msg,indx):
   
    while True:
            try:
                xStart =  int(input(msg+" x"+repr(indx)+" : "))
                xEnd   =  int(input(msg+" x"+repr(indx+1)+" : "))
                
                #end point should be greater than the start point

                if xStart <= xEnd :
                  
                  #The line is a set of point, I transfer it to list of values
                  
                  return list(range(xStart,xEnd+1))
                
                else:
                  print("Error : X%d should be greater than X%d" % (indx+1,indx)) 
                
            except ValueError :
                
                print("The value entered, it isn't a valid number!  Please try again...")

# Method to set coordinates
def setLineCoordinates(xStart,xEnd):
           
      try:
            if xStart <= xEnd :
                                
              #The line is a set of point, I transfer it to list of values
              
              return list(range(xStart,xEnd+1))
            
            else:
              
              print("Error : xEnd should be greater than xStart" )
              
      except ValueError :            
            print("The value entered, it isn't a valid number!  Please try again...")
                   
def checkLinesOverlap(firstLine,secondLine):
    
    # the intersection between the two lines (list) 

    result = list(set(firstLine) & set(secondLine))

    if result :
      print("These two lines are overlap")
    else:
      print("These two lines aren't overlap")
