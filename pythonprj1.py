print('Welcome to  PYTHON PROJECT1 GROUP COMPANY')





name = input('Enter your name ')
from datetime import date
c_d = input('Enter appointment date in this format (mm/dd/yyyy): ')

try:
    input_date = date.strptime(c_d, '%m-%d-%Y')
    formatted_date = input_date.strftime('%m-%d-%Y ')
    print(c_d)
except ValueError:
      print('incorrect format entered. please use mm/dd/yyyy format.')

from datetime import datetime, time      
c_t = input('Enter appointment time in this format (HH:MM): ')      
try:
    hours, minutes = map(int, c_t.split(':'))
    ap_time = time(hours, minutes)
    print(ap_time)
except ValueError:
     print('Error: pls enter the time in the correct format (HH:MM)')    




     

file_name = "class-work/prj1.txt"
with open(pythonprjy1.py, 'r') as file:
    a = f"{name} {c_d} {c_t}\n"
    file.write(a)


with open(pythonprj1.py, 'r') as file:
    print("\nContents of the file: ")
    for line in file:
            print(line.strip()) 
    # find()      

#find("name", "c_d", "c_t")
    
# int main():

#      string_str = " This is an example of how use substring"

#     #   string temp = str.subst(0, 4):
#     #  cout << endl; */


#      int index = str.find("example, 7")

#       string temp = str.subtry

#     int index = str, find(str.find('example'))
#       return 0;                                                                                                                                                     


#file.write("")
#exit()