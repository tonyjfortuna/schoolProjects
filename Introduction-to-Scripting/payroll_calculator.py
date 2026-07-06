"""
Introduction to Scripting: Weekly Payroll Calculator

Calculates weekly pay based on hours worked, applying overtime pay
for any hours worked beyond 40 in a week.

Implemented from original course pseudocode.
"""

REGULAR_RATE = 20
OVERTIME_RATE = 30
REGULAR_HOURS = 40


def calculate_pay(hours_worked):
    if hours_worked <= REGULAR_HOURS:
        return hours_worked * REGULAR_RATE

    overtime_hours = hours_worked - REGULAR_HOURS
    return (REGULAR_HOURS * REGULAR_RATE) + (overtime_hours * OVERTIME_RATE)


def main():
    hours_worked = float(input("Enter hours worked this week: "))
    pay = calculate_pay(hours_worked)
    print(f"Total weekly pay: ${pay:.2f}")


if __name__ == "__main__":
    main()
