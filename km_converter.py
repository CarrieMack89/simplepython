def miles_to_km(miles):
    return miles * 1.60934


if __name__ == "__main__":
    miles = float(input("Please enter the distance in miles: "))

    kilometers = miles_to_km(miles)

    print(f"{miles} miles is equal to {kilometers:.2f} Kilometers.")
