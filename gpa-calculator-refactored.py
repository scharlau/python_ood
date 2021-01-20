""" Refactored version with methods """

def welcome():
    """ Welcome users and tell them how to use the app """
    print('Welcome to the GPA Calculator')
    print('Please enter all your letter grades, one per line')
    print('Enter a blank line to designate the end.')

def calculate():
    """ Map from letter grade to point value """
    points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67, 
          'C+':2.33, 'C':2.0, 'C-':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}
    num_courses = 0
    total_points = 0
    done = False
    while not done:
        grade= input()
        if grade == '':
            done = True
        elif grade not in points:
            print("Unknown grade '{0}' being ingored".format(grade))
        else:
            num_courses+=1
            total_points+= points[grade]
    if num_courses >0: #avoid division by zero
        print('Your GPA is {0:.3}'.format(total_points / num_courses))
        menu()
      
def menu():
    """ Either end or enter more grades for conversion """
    print('Enter 1 to exit or 2 to convert more grades')
    choice = input()
    if choice == 1:
        exit()
    else:
        calculate()
        
        
""" Run the program """
welcome()
calculate()


