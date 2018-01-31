from vowels import remove_vowels
from char_loc import character_locator
from multable import multiplication_table
from calcarea import calcarea
from dict import create_dict
from stars import mario_pyramid

import unittest

class TestAss1(unittest.TestCase):
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels('mobile'), 'mbl')
        self.assertEqual(remove_vowels('MOBILE'), 'MBL')
        self.assertEqual(remove_vowels('MobIlE'), 'Mbl')
        self.assertEqual(remove_vowels('samar nasef'), 'smr nsf')
    
    def test_character_locator(self):
        self.assertEqual(character_locator('This is javaScript','i'),[2,5,15])
        self.assertEqual(character_locator('samar nasef','a'),[1,3,7])
        
    def test_multiplication_table(self):
        self.assertEqual(multiplication_table(3),[[1], [2, 4], [3, 6, 9]])
        self.assertEqual(multiplication_table(4),[[1], [2, 4], [3, 6, 9], [4, 8, 12, 16]])
        self.assertEqual(multiplication_table(5),[[1], [2, 4], [3, 6, 9], [4, 8, 12, 16], [5, 10, 15, 20, 25]])

    def test_calcarea(self):
        self.assertEqual(calcarea('t',4,8),16)
        self.assertEqual(calcarea('s',5),25)
        self.assertEqual(calcarea('r',5,3),15)
        self.assertEqual(calcarea('c',3),18.84)
    
    def test_create_dict(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        l2=["samar","eman","hhh","sara","sss"]
        d2={'e': ['eman'], 's': ['samar', 'sara', 'sss'],'h': ['hhh']}
        self.assertEqual(create_dict(l1),d1)
        self.assertEqual(create_dict(l2),d2)

    def test_mario_pyramid(self):
        pyramid1 = '   *\n  **\n ***\n'
        pyramid2 = '    *\n   **\n  ***\n ****\n'
        self.assertEqual(mario_pyramid(3),pyramid1)    
        self.assertEqual(mario_pyramid(4),pyramid2)
        
if __name__ == '__main__':
    unittest.main()