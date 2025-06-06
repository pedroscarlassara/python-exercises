import datetime

# Input asking user's born year
prompt = int(input('Em que ano você nasceu?\nR: '))

# Get current year using datetime library
current_year = datetime.datetime.today().year

# Calculation to get user age
user_age = current_year - prompt

# Years remaining to the user be able to list to the Army
years_remaining = 18 - user_age

# If user age equals or are greater than 18 it says he can list to the Army
if user_age >= 18:
    print('Você pode se alistar no exercito.')

# If user is a minor and there's one year remaining it says he cant list to the Army (The one year remaining check is for text formatting)
elif user_age < 18 and years_remaining > 1:
    print(f'Você ainda não pode se alistar, faltam {years_remaining} anos.')

    # If user is a minor and there's one year remaining it says he cant list to the Army (The one year remaining check is for text formatting)
else:
    print(f'Você ainda não pode se alistar, falta {years_remaining} ano.')


