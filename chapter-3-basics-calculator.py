# Data Science Academy (DSA) - wwww.datascienceacademy.com.br
# Course:  Python Fundamentos para Análise de Dados (PT-BR)
#          Python Fundamentals to Data Analysis (ENG-US)
# Student: Leonardo Travagini Delboni
# Chapter 3 - Lopps, Conditionals, Methods and Functions
# Lab2 - Creating a calculator using Python


# Validator:
validation = 0

# Credits:
print('')
print('Welcome to the Basics Calculator in Python.')
print('Developed by Leonardo Travagini Delboni')
print('Proposed by Data Science Academy (DSA) - https://wwww.datascienceacademy.com.br')
print('Lab2 of the Python Fundamentals to Data Sciece course. \n')

#  Complete Program:
while validation == 0:

    # Inputs:
    print('Please, insert the desired operation, as per legend below. \n')
    print('1 for Sum \n2 for Difference \n3 for Multiplication \n4 for Division')
    print('5 for Exponentiation \n6 for Rooting\n7 for all these options above\n0 to Exit the Program.\n')
    aux = int(input('Desired option: \n'))

    # Main Program:
    if aux == 0:
        validation == 1
        print('Thank you very much! \nSee you another time!\n')
        break
    elif aux >= 1 and aux <= 7:
        num1 = int(input('Now, please, insert the first number: \n'))
        num2 = int(input('Now, please, insert the second number: \n'))
        print('')
        result1 = num1 + num2
        result2 = num1 - num2
        result3 = num1 * num2
        result4 = round(float(num1 / num2),2)
        result5 = pow(num1, num2)
        result6 = round(float(pow(num1, (1/num2))),2)
        # Conditionals:
        if aux == 1:
            print('The sum of ' + str(num1) + ' and ' + str(num2) + ' is equal to ' + str(result1) + '\n')
        elif aux == 2:
            print('The difference of ' + str(num1) + ' and ' + str(num2) + ' is equal to ' + str(result2)+ '\n')
        elif aux == 3:
            print('The multiplication of ' + str(num1) + ' and ' + str(num2) + ' is equal to ' + str(result3)+ '\n')
        elif aux == 4:
            print('The division of ' + str(num1) + ' and ' + str(num2) + ' is equal to ' + str(result4)+ '\n')
        elif aux == 5:
            print('The exponential of ' + str(num1) + ' per ' + str(num2) + ' is equal to ' + str(result5)+ '\n')
        elif aux == 6:
            print('The rooting of ' + str(num1) + ' per ' + str(num2) + ' is equal to ' + str(result6)+ '\n')
        elif aux == 7:
            print('The sum of ' + str(num1) + ' and ' + str(num2) + ' is equal to ' + str(result1))
            print('The difference of ' + str(num1) + ' and ' + str(num2) + ' is equal to ' + str(result2))
            print('The multiplication of ' + str(num1) + ' and ' + str(num2) + ' is equal to ' + str(result3))
            print('The division of ' + str(num1) + ' and ' + str(num2) + ' is equal to ' + str(result4))
            print('The exponential of ' + str(num1) + ' per ' + str(num2) + ' is equal to ' + str(result5))
            print('The rooting of ' + str(num1) + ' per ' + str(num2) + ' is equal to ' + str(result6)+ '\n')
    else:
        print('Not a valid selection. Try it again.\n')