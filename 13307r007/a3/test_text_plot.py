from text_plot import is_array
from text_plot import each_element_number
from text_plot import is_len_equal
from text_plot import get_canvas
from text_plot import modify_canvas
#Imported all the functions defined in text_plot.py

import unittest
#Importing the unittest library

class TestPlot(unittest.TestCase):
    #Writing tests below
    def test_each_element_number(self):
        """Test for the function each_element_number"""
        self.assertTrue(each_element_number((2,34,-1,0)))
        self.assertFalse(each_element_number(('1',3,4)))
    def test_is_array(self):
        """Test for the function is_array"""
        self.assertTrue(is_array([1,2]))
        self.assertFalse(is_array('hello'))
    def test_is_len_equal(self):
        """Test for the function is_len_equal"""
        self.assertTrue(is_len_equal([1,4,1,'a'],[2,3,4,1]))
        self.assertFalse(is_len_equal([],[1]))
        self.assertTrue(is_len_equal('string','rakesh'))
    def test_get_canvas(self):
        """Test for the function get_canvas"""
        matrix=get_canvas([10,10])
        for i in range(10):
            for j in range(10):
                self.assertFalse(matrix[i][j]!=' ')
    def test_modify_canvas(self):
        """Test for the function modify_canvas"""
        screen_size=[10,10]
        print_list=get_canvas(screen_size)
        x=[0,1]
        y=[0,1]
        matrix=modify_canvas(x,y,print_list,screen_size)
        for i in range(screen_size[0]):
            for j in range(screen_size[1]):
                if i==0 and j==0:
                    self.assertTrue(matrix[i][j]=='*')
                elif i==screen_size[0]-1 and j==screen_size[1]-1:
                    self.assertTrue(matrix[i][j]=='*')
                else:
                    self.assertTrue(matrix[i][j]==' ')

if __name__ == '__main__':
    #If __main__, then test
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPlot)
    unittest.TextTestRunner(verbosity=2).run(suite)

