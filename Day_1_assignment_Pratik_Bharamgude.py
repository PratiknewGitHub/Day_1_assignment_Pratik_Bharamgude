#1) After running the following code, what does the variable bacon contain?
#bacon = 22
#bacon + 1

#Ans- 23

#2) What should the values of the following two terms be?
#'spam' + 'spamspam'
#'spam' * 3

#Ans- spamspamspam
#     spamspamspam

#3) How can you tell the difference between break and continue?

#Ans- The break statement terminates the loop containing it.Control of the program flows to the statement immediately after the body of the loop.
#The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
#Loop does not terminate but continues on with the next iteration.

#4) In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

#Ans- Output remains same for above 3 inputs. 1st one directly takes numbers from 0 to 9, 2nd one we can give start and end of range, 3rd one indicates start,end with steps of 1.

#5) Using a for loop, write a short programme that prints the numbers 1 to 10 Then, using a while loop, create an identical programme that prints the numbers 1 to 10.

#Ans-
for i in range(1,11):
    print(i)

a = 1
while a < 11:
    print(a)
    a += 1

    
#6) Given a number x, determine whether the given number is Armstrong number or not.
#Ans-
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



#7) Program to find Sum of squares of first n natural numbers.

#Ans-
n = int(input('enter a number :'))
result = (n)*(n + 1)*((2*n) + 1)/6
print(result)

#8) Program to Reverse words in a given String in Python.
#Ans-
string = str(input('Enter a string :'))
words = string.split()
words = list(reversed(words))
print(" ".join(words))

#9) Given a list of numbers, write a Python program to find the sum of all the elements in the list.
#Ans-
lst = [10,12,13]
total = 0
for i in lst:
    total += i
print(total)

#10) Write a Python program to print all even numbers between 10-1000.
#Ans-
for i in range(10,1000+1):
    if i % 2 == 0:
        print(i)
