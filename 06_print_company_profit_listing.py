# This is a program to print the company profit listing.
# Program Author: Robot Group 1
# Program Date: December 12, 2023

# Import the required modules.
import datetime
import FormatValues as fv
import runpy

# Define defaults.
DATE_DAYS = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
DATE_MONTHS = ["01","02","03","04","05","06","07","08","09","10","11","12"]
f = open("defaults.dat", "r")
NextTransNumDef = f.readline()
NextDriveNumDef = f.readline()
MonthStandFeeRate = float(f.readline())
DayRentalFeeRate = float(f.readline())
WeekRentalFeeRate = float(f.readline())
HSTRate = float(f.readline())
f.close()

# Initiate counters.
MonthlyStandFee = 0
DailyCarRentalFee = 0
WeeklyCarRentalFee = 0
TotalRevenue = 0
ExpenseTypeOneFee = 0
ExpenseTypeTwoFee = 0
ExpenseTypeThreeFee = 0
TotalExpense = 0

Today = datetime.datetime.now().strftime("%Y-%m-%d")

# Open the revenues file.
f = open("revenue1.dat", "r")

for RevenueRecord in f:
    RevenueList = RevenueRecord.split(",")
    TranType = RevenueList[2].strip()
    Amount = float(RevenueList[4].strip())

    if TranType == "Monthly Stand Fee":
        MonthlyStandFee += Amount
    elif TranType == "Daily Rental Fee":
        DailyCarRentalFee += Amount
    elif TranType == "Weekly Rental Fee":
        WeeklyCarRentalFee += Amount

f.close()

# Open the expense file.
f = open("Expense.dat", "r")

for ExpenseRecord in f:
    ExpenseList = ExpenseRecord.split(",")
    ExpenseType = ExpenseList[4].strip()
    Amount = float(ExpenseList[7].strip())

    if ExpenseType == "Light Bulb":
        ExpenseTypeOneFee += Amount
    elif ExpenseType == "Brake Fluid":
        ExpenseTypeTwoFee += Amount
    elif ExpenseType == "Winter Tires":
        ExpenseTypeThreeFee += Amount

f.close()

while True:
    # Get the current date and time.
    now = datetime.datetime.now().strftime("%Y-%m-%d")

    # Gather date input from the user.
    print()
    while True:
        StartDate = input(
            "Enter the report start date (YYYY-MM-DD) or press ENTER for all: "
        )
        if StartDate == "":
            StartDate = "1900-01-01"
            break

        try:
            datetime.datetime.strptime(StartDate, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid input. Please enter the start date in the format (YYYY-MM-DD).")

    print()
    while True:
        EndDate = input(
            "Enter the report end date (YYYY-MM-DD) or press ENTER for today: "
        )
        if EndDate == "":
            EndDate = now
            break

        try:
            datetime.datetime.strptime(EndDate, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid input. Please enter the end date in the format (YYYY-MM-DD).")

    print()
    BackToMenu = input("Press enter to continue.")
    print()

    print()
    print("           HAB TAXI SERVICES")
    print("        COMPANY PROFIT LISTING")
    print("=========================================")
    print()
    print("       START DATE: ", StartDate)
    print("       END DATE: ", " ", EndDate)
    print()
    print("REVENUES")
    print("=========================================")
    print(f"MONTHLY STAND FEE:             {fv.FDollar2(MonthlyStandFee):>10}")
    print(f"DAILY CAR RENTAL FEE:          {fv.FDollar2(DailyCarRentalFee):>10}")
    print(f"WEEKLY CAR RENTAL FEE:         {fv.FDollar2(WeeklyCarRentalFee):>10}")
    print("                                =========")
    print(
        f"TOTAL REVENUES:               {fv.FDollar2(MonthlyStandFee + DailyCarRentalFee + WeeklyCarRentalFee):>11}"
    )
    print()
    print()
    print("EXPENSES")
    print("=========================================")
    print(f"LIGHT BULB:                    {fv.FDollar2(ExpenseTypeOneFee):>10}")
    print(f"BRAKE FLUID:                   {fv.FDollar2(ExpenseTypeTwoFee):>10}")
    print(f"WINTER TIRES:                  {fv.FDollar2(ExpenseTypeThreeFee):>10}")
    print("                                =========")
    print(
        f"TOTAL EXPENSES:               {fv.FDollar2(ExpenseTypeOneFee + ExpenseTypeTwoFee + ExpenseTypeThreeFee):>11}"
    )
    print()
    print("=========================================")
    print()
    print(
        f"PROFIT (LOSS):                {fv.FDollar2(MonthlyStandFee + DailyCarRentalFee + WeeklyCarRentalFee - ExpenseTypeOneFee - ExpenseTypeTwoFee - ExpenseTypeThreeFee):>11}"
    )
    print()
    break

print()
BackToMenu = input("Press enter to return to menu.")
print()

runpy.run_path("00_main_menu.py")
