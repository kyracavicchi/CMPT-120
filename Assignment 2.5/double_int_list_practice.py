def main():
  
  #set this to any double
  doubleValue = 2.4
  
  #set this to any int
  intValue = 9
  
  #print out addition, subtraction, multiplication, and division of these two values
  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue)
  
  
  #populate this list
  myFriends = ["Caitlyn", "Liv", "Steve", "Maddie"]
  print(myFriends[2])
  print(myFriends[3])
  #print out your friends at index 2 and index 3
  
  
  #populate this list with five numbers
  fiveNumbers = [13,4,69,22,5]
  print(fiveNumbers)
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0] + fiveNumbers[1])
  print(fiveNumbers[2] - fiveNumbers[3])
  print(fiveNumbers[4] * fiveNumbers[3])
  print(fiveNumbers[2] / fiveNumbers[0])
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[3] = 7
  fiveNumbers[4] = 90
  #print out the list
  print(fiveNumbers)
  
main()
