#The Programming File
def capitalize_the_word(name):
    return name.capitalize()
#The Below Texting File
import unittest
import Cap

class Testcap(unittest.TestCase):
    def the_one_word(self):
        text="python"
        result=Cap.capitalize_the_word(text)
        self.assertEqual(result,"Python")
    def the_one_word(self):
        text="python everyone"
        result=Cap.capitalize_the_word(text)
        self.assertEqual(result,"Python")
if __name__=='__main__':
    unittest.main() 
