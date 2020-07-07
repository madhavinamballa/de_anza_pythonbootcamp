# range(stop) takes one argument. 
# range(start, stop) takes two arguments.
# range(start, stop, step) takes three arguments.

#========================
for i in range(10): 
    print(i, end =" ") 
#======================== 
scores = [10, 20, 30, 40] 
for i in range(len(scores)): 
    print(scores[i], end =" ") 
#=====================================  
# performing sum of natural number 
sum = 0
for i in range(1, 11): 
    sum = sum + i 
print("\n Sum of first 10 natural number :", sum) 
#====================
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  