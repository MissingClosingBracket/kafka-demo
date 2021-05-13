import unittest
  
class TestInputOutputFiles(unittest.TestCase):

    # test_01: 1000 new objects added should mean 1000 objects and 1000 of each event. It is enough to test for total lines in .out file (should be 5000).
    def test_01(self):
        output_file_test_01 = open('test_01.out')
        total_lines_output_file = sum(1 for line in output_file_test_01)
        output_file_test_01.close()
        self.assertEqual( total_lines_output_file, 5000)

    # test_02: 1000 new objects added. After each new object, user wants to immediatly retrieve the tags for it. 
    # since the event: event_user_retrieves tags only gets created if mads indeed returns a stream of tags, the count in the output file should be 6000.    

    def test_02(self):
        output_file_test_02 = open('test_02.out')
        total_lines_output_file = sum(1 for line in output_file_test_02)
        output_file_test_02.close()
        self.assertEqual( total_lines_output_file, 6000)    

    # test_03: 1000 new objects added. After that, the user wants to retrieve all the tags starting from object with id 1. 
    # like in test_02, the total number of events should be 6000.
    def test_03(self):
        output_file_test_03 = open('test_03.out')
        total_lines_output_file = sum(1 for line in output_file_test_03)
        output_file_test_03.close()
        self.assertEqual( total_lines_output_file, 6000)
  
if __name__ == '__main__':
    unittest.main()