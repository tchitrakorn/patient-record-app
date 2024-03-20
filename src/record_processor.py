from collections import defaultdict

class RecordProcessor:
    def __init__(self):
        """
        initialize a RecordProcessor object with three data structures

        (1) ids_to_patients - a dictionary that maps patient id to patient's name
        (2) ids_to_exams - a dictionary that maps patient id to a list of exam ids
            Note: There is an assumption that a patient can have multiple exams
        (3) exams_to_ids - a dictionary that maps exam id to patient id
            Note: There is an assumption that an exam id is unique and can only be mapped to one patient
        """
        pass

    def process_instruction(self, instruction):
        """
        process an instruction by determining appropriate actions and storing data in memory

        currently four actions are supported:
        (1) ADD PATIENT - instruction will be broken down into four components (operation, type, patient_id, patient_name)
        (2) ADD EXAM - instruction will be broken down into four components (operation, type, patient_id, exam_id)
        (3) DEL PATIENT - instruction will be broken down into three components (operation, type, patient_id)
        (4) DEL EXAM - instruction will be broken down into three components (operation, type, exam_id)

        argument:
        instruction (str) - a pre-validated string of space-delimited segments
            Note: There is an assumption that all instructions are valid as specified in the assignment instructions
        
        return: None
        """
        pass

    def aggregate_patient_info(self):
        """
        return a dictionary containing relevant patient's info split by patient_id
        example structure:
        {
            patient_id: {
                            patient_name: str,
                            exams: list<str>
                        }
        }
        """
        pass