import os
import pdfplumber
import pandas as pd

# Directory containing the PDF files
pdf_directory = "." 

# Get a list of PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.endswith(".pdf")]

# Create an empty DataFrame to store the combined tables
combined_data = pd.DataFrame()

# Iterate through PDF files and extract tables
for pdf_file in pdf_files:
    full_pdf_path = os.path.join(pdf_directory, pdf_file)

    # Use pdfplumber to extract tables from the PDF
    with pdfplumber.open(full_pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()

            # Iterate through tables and add them to the combined DataFrame
            for table in tables:
                table_df = pd.DataFrame(table)
                combined_data = pd.concat([combined_data, table_df])

# Save the combined data to an Excel file
output_excel_file = "combined_tables_to_excel.xlsx"
combined_data.to_excel(output_excel_file, index=False)

print(f"Combined tables data saved to {output_excel_file}")
