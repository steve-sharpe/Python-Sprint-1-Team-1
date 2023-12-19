# Program to write HAB Taxi Company Revenue inputs to Data File
# Program Author: Robot Group 1
# Program Date: December 12, 2023

# Import libraries
import datetime
import FormatValues as fv
import runpy

# Open the Defaults.dat file, read the values into variables
defaults = open("defaults.dat", "r")
nextTransNum = int(defaults.readline())
nextDriverNum = int(defaults.readline())
monthlyStandFee = float(defaults.readline())
dailyRentalFee = float(defaults.readline())
weeklyRentalFee = float(defaults.readline())
hstRate = float(defaults.readline())
defaults.close()
print()
print()
print("Welcome to the HAB Taxi Company Revenue Tracking.")
print()
while True:
    # Define Inputs
    tranID = nextTransNum
    driverNum = nextDriverNum
    while True:
        try:
            tranDate = input("Enter the transaction date (YYYY-MM-DD): ")
            tranDate = datetime.datetime.strptime(tranDate, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid input. Please enter the transaction date in the format (YYYY-MM-DD).")
    while True:
        tranDescription = input(
            "Enter the transaction description (M = monthly stand fee, D = daily car rental, W = weekly car rental): "
        ).upper()
        if tranDescription == "":
            print("Error. Please enter M, D, or W to continue.")
        elif (
            tranDescription != "M" and tranDescription != "D" and tranDescription != "W"
        ):
            print("Error. Please enter M, D, or W to continue.")
        else:
            break
    if tranDescription == "M":
        tranDescription = "Monthly Stand Fee"
        transCost = monthlyStandFee
    elif tranDescription == "D":
        tranDescription = "Daily Car Rental"
        transCost = dailyRentalFee
    else:
        tranDescription = "Weekly Car Rental"
        transCost = weeklyRentalFee
    # Calculations
    tranHST = transCost * hstRate
    tranTotal = transCost + tranHST
    # Print Outputs to terminal
    print()
    print("Transaction #: " + str(nextTransNum))
    print("Date:          " + str(tranDate.strftime("%Y-%m-%d")))
    print("Fee charged:   " + str(tranDescription))
    print("Driver ID:     " + str(driverNum))
    print("Fee Amount:    " + str(fv.FDollar2(transCost)))
    print("HST:           " + str(fv.FDollar2(tranHST)))
    print("Total:         " + str(fv.FDollar2(tranTotal)))
    print()
    # Write the new values to the revenue.dat file
    f = open("revenue.dat", "a")
    f.write("{}, ".format(str(nextTransNum)))
    f.write("{}, ".format(tranDate.strftime("%Y-%m-%d")))
    f.write("{}, ".format(tranDescription))
    f.write("{}, ".format(str(driverNum)))
    f.write("{}, ".format(fv.FComma2(transCost)))
    f.write("{}, ".format(fv.FComma2(tranHST)))
    f.write("{}\n".format(fv.FComma2(tranTotal)))
    f.close()
    print("Revenue Data has been saved to revenue.dat file")
    nextTransNum += 1
    nextDriverNum += 1
    cont = input("Do you want to enter another transaction? (Y/N): ").upper()
    if cont == "N":
        print()
        BackToMenu = input("Press enter to return to menu.")
        runpy.run_path("00_main_menu.py")

# Write the new values to the defaults.dat file
f = open("defaults.dat", "w")
f.write("{}\n".format(str(nextTransNum)))
f.write("{}\n".format(str(nextDriverNum)))
f.write("{}\n".format(str(monthlyStandFee)))
f.write("{}\n".format(str(dailyRentalFee)))
f.write("{}\n".format(str(weeklyRentalFee)))
f.write("{}\n".format(str(hstRate)))
f.close()
print()
print()
print("Thank you for using the HAB Taxi Company Revenue Data File program.")
print()
print("                  Have a safe and enjoyable day!")
print()
print()
