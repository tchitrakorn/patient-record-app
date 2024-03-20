import sys
from record_processor import RecordProcessor

if __name__ == '__main__':
    # get the instructions filename
    filename = sys.argv[1]

    # read the instructions file
    instructions_f = open(filename, 'r')
    instructions = instructions_f.readlines()

    # initialize RecordProcessor object in order to process instructions
    processor = RecordProcessor()

    # process the instructions one at a time
    for instruction in instructions:
        processor.process_instruction(instruction.strip())

    # print the formatted output after all instructions have been processed
    pass