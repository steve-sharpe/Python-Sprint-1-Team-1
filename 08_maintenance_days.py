# Program to produce report on car maintenance schedule.
# Program Author: Robot Group 1
# Program Date: December 12, 2023

# Import libraries
import datetime
import FormatValues as fv
import runpy

today = datetime.datetime.now()
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Maintenance Schedule Report
print()
print()
print("                           HAB Taxi Service")
print("                       2023 Maintenance Report")
print()
print("    Car     Start        Service            Service       Total Days ")
print("   Number   Date          Type               Date       Car Unavailable")
print("   =====================================================================")

# Open the cars.dat file in read mode
cars = open("cars.dat", "r")
# Loop through records to calculate service days
maintenanceDays = 0
for carRecord in cars:
    carLst = carRecord.split(",")
    # Assign variables to items in list
    carNumber = carLst[0].strip()
    carStart = carLst[1].strip()

    carStart = datetime.datetime.strptime(carStart, "%Y-%m-%d")
    regServiceDate = carStart + datetime.timedelta(days=15)
    regDays = 1

    majorServiceDate = regServiceDate + datetime.timedelta(days=75)
    majorDays = 1
    semiAnnualServiceDate = majorServiceDate + datetime.timedelta(days=90)
    semiDays = 2

    CarDaysUnavailable = regDays + majorDays + semiDays

    # Print the report
    print(
        f" {carNumber:>5}      {carStart.strftime('%Y-%m-%d')}   Regular Service    {regServiceDate.strftime('%Y-%m-%d')}        {regDays:>2}"
    )
    print(
        f"                         Major Service      {majorServiceDate.strftime('%Y-%m-%d')}        {majorDays:>2}"
    )
    print(
        f"                         Semi-Annual        {semiAnnualServiceDate.strftime('%Y-%m-%d')}        {semiDays:>2}"
    )
    print("                         ===============================================")
    print(
        f"                                                              {CarDaysUnavailable:>2}"
    )
    print()
    print("   =====================================================================")
print(f"                     Report printed on {today}")
print()
print("        * Numbers of days car is unavailable is subject to change *")
print("             based on repairs or other incidents that may occur. ")
print()
print()

print()
BackToMenu = input("Press enter to return to menu.")
print()

runpy.run_path("00_main_menu.py")
