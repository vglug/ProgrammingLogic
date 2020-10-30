# check the input whether is it a integer or not
try:
   # take input for the calculation value
   num = int(input("Eneter Number to multiplay : "))
   
   # check the input for range whether is it a integer or not
   try:

      # take input for the range 
      x = int(input("Eneter range : "))

      # loop for change values
      for i in range(1,x+1):

         # print the values
         print(num, 'x', i, '=', num*i)
   
   # if input for range is not a integer then print error on here
   except:
      print("Input Type Error!")

# if input for calculation value is not a integer then print error on here
except:
   print("Input Type Error!")
