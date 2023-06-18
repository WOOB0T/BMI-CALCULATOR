print('𓍝  Body Mass Index Calculator  𓍝')
print()

name = input("☆ What do you prefer to be called? ")
print()

print("Hello, " + name + ". Welcome to this script! My name is Jessy and i want to introduce you "
                         "to my beta version of a Body Mass Index, also know as BMI, calculator.")
print()

print("We have those options to choose!")
print()

print("[ 1 ] Metric")
print("[ 2 ] Imperial")
print()

print("Remembering: imperial is calculate with feet, inches and pounds, "
      "meanwhile metric is calculate with centimeters and kilograms")
print()

measures = int(input("☆ Now choose, by the number, the option you want to follow: "))
print()
print("𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝•𓍝")
print()

if measures == 1:

    height = float(input('☆ Type your height in centimeters: '))
    print()

    weight = float(input('☆ Type your weight in kilograms: '))
    print()

    BMI = weight / height ** 2

elif measures == 2:

    feet = float(input('☆ Type your height in feet: '))
    inches = float(input('☆ Now, in inches: '))
    print()

    weight = float(input('☆ Type your weight in pounds: '))
    print()

    height = (feet * 12) + inches
    BMI = 703 * (weight / height ** 2)

print("Calculating...")
print()


if BMI < 16:
    print("𓍝", name + ', this is terrifying!\nYour body mass index is', round(BMI, 1),
          'and it is classified as Severe Thinness.'
          '\nSeek immediately a nutritionist doctor to track your weight gain in a healthy way!')

elif BMI == 16 or BMI < 17:
    print("𓍝", name + ', your body mass index is', round(BMI, 1),
          'and it is classified as Moderate Thinness.\nSince you are very close to the Severe Thinness level, '
          'is recommended that you seek a nutritionist doctor to track your weight gain in a healthy way!')

elif BMI == 17 or BMI < 18.5:
    print("𓍝", name + ', your body mass index is', round(BMI, 1),
          'and it is classified as Mild Thinness.\nSince you are a little close to the Severe Thinness level, '
          'is recommended that you seek a nutritionist doctor to track your weight gain in a healthy way!')

elif BMI == 18.5 or BMI < 25:
    print("𓍝", name + ", i'm glad to report that your body mass index is", round(BMI, 1),
          "and it is classified as Healthy!\n You're doing great. "
          "Hope that you keep taking care of your body like that!")

elif BMI == 25 or BMI < 30:
    print("𓍝", name + ', your body mass index is', round(BMI, 1),
          'and it is classified as Overweight.\nSince you are very close to the Obese Class I level, '
          'is recommended that you seek a nutritionist doctor to track your weight loss in a healthy way!')

elif BMI == 30 or BMI < 35:
    print("𓍝", name + ", i'm worried to report that your body mass index is", round(BMI, 1),
          "and it is classified as Obese Class I,\nbecause of it is recommended that "
          "you seek a nutritionist doctor to track your weight loss in a healthy way!")

elif BMI == 35 or BMI < 40:
    print("𓍝", name + ", i'm worried to report that your body mass index is", round(BMI, 1),
          "and it is classified as Obese Class II,\nthis level is considered as severe and, because of it, "
          "is recommended that you immediately seek a nutritionist doctor to track your weight loss in a healthy way!")

else:
    print("𓍝", name + ", that's so worrying! your body mass index is", round(BMI, 1),
          "and it is classified as Obese Class III, level that is considered MORTAL"
          "\nseek immediately a nutritionist doctor to track your weight loss in a healthy way!")
