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
        self.ids_to_patients = defaultdict(str) 
        self.ids_to_exams = defaultdict(list)
        self.exams_to_ids = defaultdict(str)

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
        # break the instruction down into components
        components = instruction.split(' ')
        operation = components[0]
        type = components[1]

        # case 1: ADD PATIENT
        if operation == 'ADD' and type == 'PATIENT':
            patient_id = components[2]
            patient_name = ' '.join(components[3:])
            # edge case: only add if patient_id does not already exist
            if patient_id not in self.ids_to_patients:
                self.ids_to_patients[patient_id] = patient_name

        # case 2: ADD EXAM
        elif operation == 'ADD' and type == 'EXAM':
            patient_id = components[2]
            exam_id = components[3]
            # edge case: only add if patient_id exists and exam_id does not already exist
            if patient_id in self.ids_to_patients and exam_id not in self.exams_to_ids:
                self.ids_to_exams[patient_id].append(exam_id)
                self.exams_to_ids[exam_id] = patient_id

        # case 3: DEL PATIENT
        elif operation == 'DEL' and type == 'PATIENT':
            patient_id = components[2]
            # edge case: only delete if patient_id exists
            if patient_id in self.ids_to_patients:
                del self.ids_to_patients[patient_id]
                # delete all exams affaliated with this patient_id if any
                try:
                    affiliated_exams = self.ids_to_exams[patient_id]
                    del self.ids_to_exams[patient_id]
                    for exam in affiliated_exams:
                        del self.exams_to_ids[exam]
                except:
                    pass

        # case 4: DEL EXAM
        elif operation == 'DEL' and type == 'EXAM':
            exam_id = components[2]
            # edge case: only delete if exam_id exists
            if exam_id in self.exams_to_ids:
                patient_id = self.exams_to_ids[exam_id]
                self.ids_to_exams[patient_id].remove(exam_id)
                del self.exams_to_ids[exam_id]

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
        output = defaultdict()
        for patient_id, patient_name in self.ids_to_patients.items():
            output[patient_id] = {
                'patient_name': patient_name,
                'exams': self.ids_to_exams[patient_id]
            }
        return output