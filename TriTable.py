#Pattern Number
#Ndou Pfarelo Rudolph, 2019/09/30, 22:00
#A program that print number in patterns.

for i in range(1, 10): #outer loop to handle number of rows 
  for num in range(1, i + 1): #inner loop to handle number of columns
      print(i*num, end =" ") #printing number 
  print("\n") # print each statement on new line