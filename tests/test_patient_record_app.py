import unittest
import subprocess

class TestPatientRecordApp(unittest.TestCase):
    def setUp(self):
        self.APP_FILE_PATH = 'src/patient_record_app.py'
        self.INSTRUCTIONS_FILE_PATH = 'instructions/instructions.txt'
        return super().setUp()
    
    def test_process(self):
        actual_output = subprocess.run(['python', self.APP_FILE_PATH, self.INSTRUCTIONS_FILE_PATH], capture_output=True)
        expected_output = 'Name: JOHN DOE, Id: 123, Exam Count: 0\nName: JANE CROW, Id: 789, Exam Count: 2\n'
        self.assertEqual(actual_output.stdout.decode('utf-8'), expected_output)