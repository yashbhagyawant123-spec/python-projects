# BMI Calculator
# Underweight = <18.5
# Normal weight = 18.5-24.9
# Overweight = 25-29.9
# Obesity = BMI of 30 or greater
while True: 

    height = float(input('Enter your hight: \n'))
    height = height / 100
    weight =float(input('Enter your weight: \n'))
 
    BMI =round(weight / (height * height),2)
    print(f'your body mass index (BMI) is {BMI}')
    if(BMI<=18.5):
         print('you are underweeight')
    elif(BMI<=24.9):
         print('you are healthy')
    elif(BMI<=29.9):
         print('You are overweight')
    else:
         print('you are obese')
    userWantsToContinue = input('Do you want to continue? (yes/no): \n') 
    if(userWantsToContinue == 'no'):
        print('thank you')
        break