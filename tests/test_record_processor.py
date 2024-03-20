import unittest
from src.record_processor import RecordProcessor


class TestAddPatient(unittest.TestCase):
    def test_add_new_patient(self):
        instruction = 'ADD PATIENT 123 JOHN DOE'
        processor = RecordProcessor()
        processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JOHN DOE',
                'exams': []
            }
        }
        self.assertEqual(actual_output, expected_output)

    def test_add_existing_patient(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'ADD PATIENT 123 JANE DOE'
                        ]
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JOHN DOE',
                'exams': []
            }
        }
        self.assertEqual(actual_output, expected_output)


class TestAddExam(unittest.TestCase):
    def test_add_exam_to_existing_patient(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'ADD EXAM 123 456'
                        ]
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JOHN DOE',
                'exams': ['456']
            }
        }
        self.assertEqual(actual_output, expected_output)

    def test_add_exam_to_nonexisting_patient(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'ADD EXAM 125 456'
                        ]
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JOHN DOE',
                'exams': []
            }
        }
        self.assertEqual(actual_output, expected_output)

    def test_add_existing_exam(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'ADD EXAM 123 456',
                        'ADD PATIENT 125 JANE DOE',
                        'ADD EXAM 125 456'
                        ]
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JOHN DOE',
                'exams': ['456']
            },
            '125': {
                'patient_name': 'JANE DOE',
                'exams': []
            }

        }
        self.assertEqual(actual_output, expected_output)


class TestDelPatient(unittest.TestCase):
    def test_delete_existing_patient(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'DEL PATIENT 123'
                        ]
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {}
        self.assertEqual(actual_output, expected_output)

    def test_delete_existing_patient_with_exam(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'ADD EXAM 123 456',
                        'DEL PATIENT 123',
                        'ADD PATIENT 123 JANE DOE'
                        ]
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JANE DOE',
                'exams': []
            }
        }
        self.assertEqual(actual_output, expected_output)

    def test_delete_nonexisting_patient(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'DEL PATIENT 125'
                        ]
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JOHN DOE',
                'exams': []
            }
        }
        self.assertEqual(actual_output, expected_output)


class TestDelExam(unittest.TestCase):
    def test_delete_existing_exam(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'ADD EXAM 123 456',
                        'ADD EXAM 123 457',
                        'DEL EXAM 456']
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JOHN DOE',
                'exams': ['457']
            }
        }
        self.assertEqual(actual_output, expected_output)

    def test_delete_nonexisting_exam(self):
        instructions = ['ADD PATIENT 123 JOHN DOE',
                        'ADD EXAM 123 456',
                        'DEL EXAM 500']
        processor = RecordProcessor()
        for instruction in instructions:
            processor.process_instruction(instruction)
        actual_output = processor.aggregate_patient_info()
        expected_output = {
            '123': {
                'patient_name': 'JOHN DOE',
                'exams': ['456']
            }
        }
        self.assertEqual(actual_output, expected_output)
