#function to convert miles to kilometers
def miles_to_km(miles):
    return miles * 1.60934

#main part of the program (code inside this block will excute - when script is run directly)
if __name__ == "__main__":
    #prompt user to enter value (in this case the distance in miles)
    miles = float(input("Please enter the distance in miles: "))

    #convert miles to km
    kilometers = miles_to_km(miles)
    
    #print the result
    print(f"{miles} miles is equal to {kilometers:.2f} Kilometers.")
