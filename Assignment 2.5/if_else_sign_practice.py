def main():

    '''ask the user for their age. If the user is 25 or older, tell them they can buy alcohol, nicotine products, and they can rent a car
        If they're 21 or older but younger than 25, tell them they can buy alcohol and nicotine products, but cannot rent a car
        If they're 18 and older but younger than 21, tell them they can only buy nicotine products in some states
        If they're less than 18, they can only purchase candy cigarettes and sody pops
    '''

age = int(input("Enter Your Age:"))
print(age)
if age >= 25 :
    print("You can buy alcohol and nicotine products and rent a car.")
elif age >= 21 and age < 25 :
    print("You can buy alcohol and nicotine products, but you cannot rent a car.")
elif age >= 18 and age < 21 :
    print("You can only buy nicotine products in some states.")
elif age < 18 :
    print("You can only purchase candy cigarettes and sody pops.")
  
  
  
main()
