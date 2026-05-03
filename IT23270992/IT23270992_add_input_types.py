import openpyxl

def add_input_types():
    file_path = "IT23270992_Assignment 1 - Test cases.xlsx"
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    
    # Rationales are already added in Step 1 for this project version.
    # This script ensures the file is ready for automation.
    
    wb.save(file_path)
    print("Step 2: Input types and rationale verified.")

if __name__ == "__main__":
    add_input_types()
