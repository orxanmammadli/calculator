from replit import clear
from art import logo
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2  
def multiply(n1,n2):
  return n1*n2  
def divide(n1,n2):
  return n1/n2
operations={
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
} 
def calculation():
  print(logo)
  num1=float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
  cont_this=True
  while cont_this:
    
    operation_symbol=input("Pick an operation : ")  
    num2=float(input("What is the next number?: "))    
    calculation_function=operations[operation_symbol] 
    answer=calculation_function(num1,num2)
    
    print(f"{num1}{operation_symbol}{num2}={answer}")
  
    ask = input("Do you want to contunue or do new calculation? y or n: ")
    if ask=="y":
      num1=answer
    else:
      cont_with = False
      clear()
      calculation()
calculation()    
