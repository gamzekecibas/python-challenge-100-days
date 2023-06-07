## Day 10 - Beginner | Functions with Outputs
## 07.06.2023
## Exercises

## Exercise - 0
#length = len(formatted_name)

def format_name(f_name, l_name):
    """
    Take a first and last name and format it
    to return the title case version of the name
    """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Results: {formatted_f_name} {formatted_l_name}"



## Exercise - 1
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("Leap year.")
                return True
            else:
                # print("Not leap year.")
                return False
        else:
            # print("Leap year.")
            return True
    else:
        # print("Not leap year.")
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_bool = is_leap(year)
    month_idx = month - 1
    if (is_leap_bool == True and month == 2):
        current_month_days = month_days[month_idx] + 1
    else:
        current_month_days = month_days[month_idx]

    return current_month_days


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







