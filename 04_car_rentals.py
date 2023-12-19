# HAB Taxi Service
# Track Car Rentals
# Program Author: Robot Group 1
# Program Date: December 12, 2023

# imports
import datetime
import FormatValues as FV
import runpy

Today = datetime.datetime.now()
TodayDsp = datetime.datetime.strftime(Today, "%Y-%m-%d")

# define constants
f = open("Defaults.dat", "r")
NextTransNum = int(f.readline())
NextDriveNum = int(f.readline())
MonthStandFee = float(f.readline())
DayRentalFee = float(f.readline())
WeekRentalFee = float(f.readline())
HSTRate = float(f.readline())
f.close()

# set up headings
# Print main headings and column headings.
print()
print(" HAB TAXI SERVICE")
print(f" CAR RENTAL TRACKING {TodayDsp}")
print()
print(" RENTAL   DRIVER     START      CAR     NUMBER     RENTAL    HST      TOTAL")
print("   ID     NUMBER     DATE      NUMBER   OF DAYS     COST                   ")
print(" ===========================================================================")

# Initialize counters and accumulators for summary / analytics.
TotalAcc = 0

# Open the file with the "r" mode for read.
f = open("Rentals.dat", "r")

# Assign variables to each item in the list that are required in the report.
for DriverRecord in f:
    # Input - read the first record and split into a list.
    DriveLst = DriverRecord.split(",")

    # Assign variables
    # .strip() method
    RentalID = DriveLst[0].strip()
    DriverNum = DriveLst[1].strip()
    StartDate = DriveLst[2].strip()
    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    CarNum = int(DriveLst[3].strip())
    RentalDays = int(DriveLst[4].strip())

    # calculations/ if startements
    if RentalDays == 7:
        RentalCost = WeekRentalFee
    elif RentalDays == 0:
        RentalCost == MonthStandFee
    else:
        RentalCost = RentalDays * DayRentalFee

    Taxes = RentalCost * 0.15
    Total = Taxes + RentalCost

    StartDateDsp = datetime.datetime.strftime(StartDate, "%Y-%m-%d")

    TotalAcc += Total

    print(
        f"   {RentalID:<4}    {DriverNum:<4s}  {StartDateDsp:>12s}    {CarNum:>1}        {RentalDays:>1}     {FV.FDollar2(RentalCost):>9s}{FV.FDollar2(Taxes):>9s} {FV.FDollar2(Total):>9s}"
    )

# close the file
f.close()
print(f" ===========================================================================")
print(
    f" Total Rental Costs:                                               {FV.FDollar2(TotalAcc):>9s}"
)
print()

print()
BackToMenu = input("Press enter to return to menu.")
print()

runpy.run_path("00_main_menu.py")
