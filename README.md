# patient-record-app

## Overview
Patient Record is a command-line application that processes a set of instructions regarding patients' information and produces an easily digestible aggregated output for users in the console. It is built entirely with Python.

## Usage
1. Clone this repo and go to the main directory with `cd patient-record app`
2. [Optional] Put an instructions file (`.txt` format) in the `instructions` folder. Otherwise, a sample one has already been provided.
3. To process the instructions, enter the following command: `python src/patient_record_app.py instructions/instructions.txt` or `python <app-file-path> <instructions-file-path>` See the sample output below:

## Development Process
### Project Setup
First, I setup the project with relevant files and methods, including testing skeletons to get a sense of what each component should behave. 
The idea is to break the overall task into two subcomponents:
1. Patient Record app that reads in instructions and returns appropriate output.
2. RecordProcessor class that processes instructions, holds data in-memory, and aggregates patient information accordingly.

There are several reasons behind breaking the project down this way. For instance:
* Modular code can be tested more robustly and easier for new feature implementations 
* RecordProcessor is more portable and reusable as its own separate class

Related PRs:
[Project setup 1](https://github.com/tchitrakorn/patient-record-app/pull/1), [Project setup 2](https://github.com/tchitrakorn/patient-record-app/pull/2)

### Development
Then, I incrementally built Patient Record app and RecordProcessor class.

Related PR:
[Feature development](https://github.com/tchitrakorn/patient-record-app/pull/3)

### Testing
I added several unit tests to test the basic functionalities of RecordProcessor and end-to-end test for Patient Record to ensure that the application is working.

Related PR:
[Unit and end-to-end tests](https://github.com/tchitrakorn/patient-record-app/pull/4)

### Revision

## Testing
To run all tests and coverage, `python -m coverage run -m unittest --verbose`. 

To get coverage report, `python -m coverage report -m`.
See below for testing results:

## Author's Notes
* More detailed notes can be found in the comments inside this repo.
* Test cases are developed accordingly to the provided instructions. Patient Record app currently does not support input validation and all instructions are assumed to be valid.
* Patient IDs and exam IDs are assumed to be unique
* Output is printed directly to the console (my interpretation based on the instructions sheet). However, for future improvement, it possible to write this output to a file to make it permanent.
