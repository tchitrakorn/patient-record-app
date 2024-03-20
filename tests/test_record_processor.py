import unittest
from src.record_processor import RecordProcessor

class TestRecordProcessor(unittest.TestCase):
    """
    TEST ADD PATIENT
    """
    def test_add_new_patient(self):
        pass

    def test_add_existing_patient(self):
        pass

    """
    TEST ADD EXAM
    """
    def test_add_exam_to_existing_patient(self):
        pass

    def test_add_exam_to_nonexisting_patient(self):
        pass

    def test_add_existing_exam(self):
        pass

    """
    TEST DEL PATIENT
    """
    def test_delete_existing_patient(self):
        pass

    def test_delete_existing_patient_with_exam(self):
        pass
    
    def test_delete_nonexisting_patient(self):
        pass

    """
    TEST DEL EXAM
    """
    def test_delete_existing_exam(self):
        pass

    def test_delete_nonexisting_exam(self):
        pass