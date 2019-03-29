import linesOverlap as overlap 
import versionChecker as check

def test_overlap():

    line1 = overlap.setLineCoordinates(2,7)

    line2 = overlap.setLineCoordinates(5,17)
    result = overlap.checkLinesOverlap(line1,line2)

def test_versions():

  result = check.semanticVersion("1.5.4","0.3.3")

  if result == -1 :    
    print("V1 is older than V2")
  
  elif  result == 1 :    
    print("V1 is greater than V2.")

  elif result == 0:   
    print("V1 and V2 are the same.")
  


  print("#------ Case 2 ");
  check.standardVersion(0.5,1.3)
  check.standardVersion(4.2,2.3)
  check.standardVersion(4.2,4.2)


test_overlap()

print("----------------")

test_versions()
