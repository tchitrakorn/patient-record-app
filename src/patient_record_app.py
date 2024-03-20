import sys
from record_processor import RecordProcessor

if __name__ == '__main__':
    # get the instructions filename
    filename = sys.argv[1]

    # read the instructions file
    instructions_f = open(filename, 'r')
    lines = instructions_f.readlines()
    instructions = [line.strip() for line in lines]

    # initialize RecordProcessor object in order to process instructions
    processor = RecordProcessor()

    # process all instructions
    processor.process_instructions(instructions)

    # print the formatted output after all instructions have been processed
    aggregated_patient_info = processor.aggregate_patient_info()
    for patient_id, patient_info in aggregated_patient_info.items():
        patient_name = patient_info['patient_name']
        exams = patient_info['exams']
        print(
            f'Name: {patient_name}, Id: {patient_id}, Exam Count: {len(exams)}')
