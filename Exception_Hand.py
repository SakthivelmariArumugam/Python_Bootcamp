a=int(input("Enter Number a:"))
b=int(input("Enter number b:"))
try:
  print(a/b)
except Exception:
  print("zero division error")
  b=int(input("Enter Number b:"))
  print(a/b)

print("bye")

#Exception print with that name
try:
  print(a/b)
except Exception as e:
  print(e)
  b=int(input("Enter Number b:"))
  print(a/b)

#Exception Handling with Finally 
try:
  print("Resource has opened")
  a=int(input("Enter Number A:"))
  b=int(input("Enter Number B:"))
  print(a/b)
except Exception as e:
  b=int(input("Enter Number B Again:"))
  print(a/b)
finally:
  print("Resource has closed")