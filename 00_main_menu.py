# This is the main menu for the HAB Taxi Services Company Services System.
# Program Author: Robot Group 1
# Program Date: December 12, 2023

# Import modules
import runpy
import datetime
import os
import FormatValues as fv


# Main menu loop

# Define the path to the file where the last run date will be stored
last_run_file = "last_run.txt"

# Get the current date
now = datetime.datetime.now()

# Check if the file exists
if os.path.exists(last_run_file):
    # Read the last run date from the file
    with open(last_run_file, "r") as file:
        last_run_date = datetime.datetime.strptime(file.read(), "%Y-%m-%d")

    # Check if the last run date is in a different month than the current date
    if last_run_date.month != now.month or last_run_date.year != now.year:
        print()
        print("This is the first run of the month!")
        print("Balance due will be updated now.")

        # Open the Employees.dat file, read the values into variables
        employees = open("employees.dat", "r")
        nextDriverNum = int(employees.readline())
        DriverFName = employees.readline()
        DriverLName = employees.readline()
        DriverAddress = employees.readline()
        DriverCity = employees.readline()
        DriverProvince = employees.readline()
        DriverPostalCode = employees.readline()
        DriverPhoneNum = employees.readline()
        DriverLicenseNum = employees.readline()
        DriverLicenseExp = employees.readline()
        DriverInsuranceCompany = employees.readline()
        DriverInsuranceNum = employees.readline()
        DriverRentOwn = employees.readline()
        DriverBalanceDue = float(employees.readline())

        # Open the Defaults.dat file, read the values into variables

        defaults = open("defaults.dat", "r")
        nextTransNum = int(defaults.readline())
        EmployeeNum = int(defaults.readline())
        monthlyStandFee = float(defaults.readline())
        dailyRentalFee = float(defaults.readline())
        weeklyRentalFee = float(defaults.readline())
        hstRate = float(defaults.readline())
        defaults.close()

        if DriverRentOwn == "O":
            DriverBalanceDue = DriverBalanceDue + monthlyStandFee

            # Write the new values to the employees.dat file
            f = open("employees.dat", "w")
            f.write("{}\n".format(str(nextDriverNum)))
            f.write("{}\n".format(DriverFName))
            f.write("{}\n".format(DriverLName))
            f.write("{}\n".format(DriverAddress))
            f.write("{}\n".format(DriverCity))
            f.write("{}\n".format(DriverProvince))
            f.write("{}\n".format(DriverPostalCode))
            f.write("{}\n".format(DriverPhoneNum))
            f.write("{}\n".format(DriverLicenseNum))
            f.write("{}\n".format(DriverLicenseExp))
            f.write("{}\n".format(DriverInsuranceCompany))
            f.write("{}\n".format(DriverInsuranceNum))
            f.write("{}\n".format(DriverRentOwn))
            f.write("{}\n".format(fv.FComma2(DriverBalanceDue)))
            f.close()

else:
    print()
    print("This is the first run of the month!")
    print("Balance due will be updated now.")

    # Open the Employees.dat file, read the values into variables
    employees = open("employees.dat", "r")
    nextDriverNum = employees.readline()
    DriverFName = employees.readline()
    DriverLName = employees.readline()
    DriverAddress = employees.readline()
    DriverCity = employees.readline()
    DriverProvince = employees.readline()
    DriverPostalCode = employees.readline()
    DriverPhoneNum = employees.readline()
    DriverLicenseNum = employees.readline()
    DriverLicenseExp = employees.readline()
    DriverInsuranceCompany = employees.readline()
    DriverInsuranceNum = employees.readline()
    DriverRentOwn = employees.readline()
    DriverBalanceDue = employees.readline()
    employees.close()

    # Open the Defaults.dat file, read the values into variables

    defaults = open("defaults.dat", "r")
    nextTransNum = int(defaults.readline())
    EmployeeNum = int(defaults.readline())
    monthlyStandFee = float(defaults.readline())
    dailyRentalFee = float(defaults.readline())
    weeklyRentalFee = float(defaults.readline())
    hstRate = float(defaults.readline())
    defaults.close()

    if DriverRentOwn == "O":
        DriverBalanceDue = DriverBalanceDue + monthlyStandFee

        # Write the new values to the employees.dat file
        f = open("employees.dat", "w")
        f.write("{}\n".format(str(nextDriverNum)))
        f.write("{}\n".format(DriverFName))
        f.write("{}\n".format(DriverLName))
        f.write("{}\n".format(DriverAddress))
        f.write("{}\n".format(DriverCity))
        f.write("{}\n".format(DriverProvince))
        f.write("{}\n".format(DriverPostalCode))
        f.write("{}\n".format(DriverPhoneNum))
        f.write("{}\n".format(DriverLicenseNum))
        f.write("{}\n".format(DriverLicenseExp))
        f.write("{}\n".format(DriverInsuranceCompany))
        f.write("{}\n".format(DriverInsuranceNum))
        f.write("{}\n".format(DriverRentOwn))
        f.write("{}\n".format(DriverBalanceDue))
        f.close()

# Write the current date to the file
with open(last_run_file, "w") as file:
    file.write(now.strftime("%Y-%m-%d"))
    file.close()

while True:
    print()
    print("            HAB Taxi Services")
    print("            Company Services System")
    print()
    print("1.  Enter a New Employee (driver).")
    print("2.  Enter Company Revenue.")
    print("3.  Enter Company Expenses.")
    print("4.  Track Car Rentals.")
    print("5.  Record Employee Payment.")
    print("6.  Print Company Profit Listing.")
    print("7.  Print Driver Financial Listing.")
    print("8.  Maintenance Report")
    print("9.  Quit Program.")
    print()

    while True:
        Choice = input("           Enter choice (1-9): ")
        if (
            Choice == "1"
            or Choice == "2"
            or Choice == "3"
            or Choice == "4"
            or Choice == "5"
            or Choice == "6"
            or Choice == "7"
            or Choice == "8"
            or Choice == "9"
        ):
            break
        else:
            print()
            print("           Invalid choice. Try again.")
            print()

    if Choice == "1":
        print()
        print("New driver has been saved to the file.")
        print()
        BackToMenu = input("Press enter to return to menu.")
        print()
    elif Choice == "2":
        runpy.run_path("02_revenue_inputs.py")
    elif Choice == "3":
        print()
        print("New company expenses have been saved to the file.")
        print()
        BackToMenu = input("Press enter to return to menu.")
        print()
    elif Choice == "4":
        runpy.run_path("04_car_rentals.py")
    elif Choice == "5":
        print()
        print("This option is current offline for maintenance.")
        print("Please try again later.")
        print()
        BackToMenu = input("Press enter to return to menu.")
        print()
    elif Choice == "6":
        runpy.run_path("06_print_company_profit_listing.py")
    elif Choice == "7":
        print()
        print("This option is current offline for maintenance.")
        print("Please try again later.")
        print()
        BackToMenu = input("Press enter to return to menu.")
        print()
    elif Choice == "8":
        runpy.run_path("08_maintenance_days.py")
    elif Choice == "9":
        print()
        print("           Thank You from...")
        print()
        print("           HAB Taxi Services")
        print()
        exit()
