import os
import pandas as pd

def excel_to_html(input_file, output_file):
    # Read the Excel file (using the first sheet by default)
    df = pd.read_excel(input_file)
    
    # Convert the DataFrame to an HTML table (without the DataFrame index)
    html_table = df.to_html(index=False)
    
    # Create a complete HTML page with simple styling
    html_page = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{os.path.basename(input_file)} Data</title>
    <style>
      table {{ border-collapse: collapse; width: 100%; }}
      th, td {{ border: 1px solid #ddd; padding: 8px; }}
      th {{ background-color: #f2f2f2; text-align: left; }}
    </style>
</head>
<body>
    <h1>{os.path.basename(input_file)} Data</h1>
    {html_table}
</body>
</html>
"""
    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_page)
    
    print(f"HTML file generated: {output_file}")

def main():
    input_file = input("Enter the path to your Excel file: ").strip()
    output_file = input("Enter the desired output HTML file name (e.g., output.html): ").strip()
    
    # If no output file name is provided, use a default name
    if not output_file:
        output_file = "output.html"
    
    try:
        excel_to_html(input_file, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
