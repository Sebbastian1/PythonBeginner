def calculate_bmi(weight_kg, height_cm):
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    return bmi


def bmi_category(bmi):

    if bmi < 18.5:
        cathegory = 'niedowaga'
    elif bmi >= 18.5 and bmi <= 24.9:
        cathegory = 'norma'
    elif bmi >= 25.0 and bmi <= 29.9:
        cathegory = 'nadwaga'
    else:
        cathegory = 'otyłość'

    return cathegory


def run_cli():
    weight = float(input("Podaj wagę w kg: "))
    height = float(input("Podaj wzrost w cm: "))
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    print("BMI: " + "%.2f" % bmi + " - " + category)

run_cli()
