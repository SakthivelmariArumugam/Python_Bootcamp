class Book:
  def __init__(self,Book_name,Author,Pages):
    self.Book_name=Book_name
    self.Author=Author
    self.Pages=Pages
  
  def __str__(self):
    return "The Atomic Habits"
  
  def __len__(self):
    return self.Pages
  
  def __del__(self):
    print("The Book Deleted")

c = Book("Atomic Habits", "James Clear", 320)
print(str(c))
print(c)
print(len(c))
del c
print(c)