def main():
    
    #Can you print out "Hello" 8 times? I gave you a tiny hint to start...
    for x in range(8):
        print("Hello")

    #What about as a while loop?
    loops = 1
    while (loops <= 8):
        print("Hello")
        loops = loops + 1
        
    
    #The loop iterations are one behind in a non-programming counting way... how can we fix this?
    count = 1
    while (count <= 3):
        print("While loop iteration", count)
        count = count + 1
        
    #Same deal here!
    x = 1
    for x in range(1,4):
        print("For loop iteration:", x)
        x = x + 1
     
    #Uh oh I messed up and made an infinite loop... so silly of me!   
    endless = 4
    while (endless < 5):
        print("I'm stuck in this loop!!!!")
        endless = endless + 1
    
    #print out your last name one letter at a time
    for x in "Cavicchi":
        print(x)
       
     #aw i suck i made another infinite loop.. use that thing I taught you about to get out once it prints once... starts with a b... br....
    found = 0
    found == False
    while found == False:
        print("i only printed once")
        break

    #can you fill this out so that it prints found when it hits the letter r?
    for x in "Marist":
        print(x)
        if x == "r":
            print("found")
            break
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(numbers)
    #you could print out the list using print(numbers) OR you could go the long way and use a for loop to print out the value of each index :)
    for x in range(len(numbers)):
        n = numbers[x]
        print(x,n)

    #what if I wanted you to print out only the even numbers in this range I made?
    for x in range (20, 501):
        #i feeeeel like modulooooooo is neededddd
        if x % 2 == 0 :
            print(x)

main()
