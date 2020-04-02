#The print command is what generates output
print("Hello World!")

#Statements can be extended over multiple lines by adding \
number=1+2+3+4+5+6
number2=1+2+3 \
       +4+5+6

print("This is the first number:", number)
print("This is the second number:", number2)

#Or by putting content in parentheses

number3=(1+2+3+
         4+5+6)

print("This is the third number:", number3)

#Multiple statements, single line
a=1; b=2; c=3

for i in range(1,11):
    print(i)
    if i == 5:
        break
