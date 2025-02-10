#!/usr/bin/env python3

import openpyxl

# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Sheet1"

# Add data
sheet.append(["Name", "Age", "City"])
sheet.append(["Alice", 25, "New York"])
sheet.append(["Bob", 30, "San Francisco"])

# Save the Excel file locally
file_path = "output.xlsx"
wb.save(file_path)

print(f"Excel file created: {file_path}")
