import unittest
""" Refactored version with methods """

def welcome():
    """ Welcome users and tell them how to use the app """
    print('Welcome to the GPA Calculator')
    print('Please enter all your letter grades, one per line')
    print('Enter a blank line to designate the end.')

def gather_grades():
    done = False
    while not done:
        grade= input()
        if grade == '':
            done = True
        elif grade not in points:
            print("Unknown grade '{0}' being ingored".format(grade))
    
    
def calculate(grades):
    """ Map from letter grade to point value with comma separated list of grades """
    points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67, 
          'C+':2.33, 'C':2.0, 'C-':1.67, 'D+':1.33, 'D':1.0, 'F':0.0} 
    grade_list = grades.split(",")
    num_courses = len(grade_list)
    total_points = 0
    # total_points+= points[grade]
    for i in grade_list:
        total_points += points[i]
    if num_courses >0: #avoid division by zero
        return('Your GPA is {0:.3}'.format(total_points / num_courses))
        # menu()
      
def menu():
    """ Either end or enter more grades for conversion """
    print('Enter 1 to exit or 2 to convert more grades')
    choice = input()
    if choice == 1:
        exit()
    else:
        calculate()
        
class TestGPACalculator(unittest.TestCase):
    
    def test_calculator(self):
        gpa = calculate('A,B,D')
        self.assertEqual('Your GPA is 2.67', gpa)

        
""" Run the program """
if __name__ == "__main__":
    unittest.main()



