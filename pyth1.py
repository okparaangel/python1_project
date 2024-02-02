def search_str(project1,word):
        with open(project1.py, 'r') as file:
                #read all content of a content of a file
                content = file.read()            
#check if string present in a file
if c_d:
        print('string exist in a file')
else:
        print('string does not exist in a file')  

file_name = "prj1.txt"  
with open(file_name, 'a+') as file:  
        file.write(f"{name} \n")
        file.write(f"{c_d} \n")
        file.write(f"{c_t} \n")

with open(file_name, 'r') as file:
        print("\nContentents of the file: ")
        for line in file:
                print(line.strip())
       