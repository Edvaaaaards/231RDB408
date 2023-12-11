import pandas as pd
from selenium import webdriver

# Function to read people.csv and return a DataFrame
def read_people_csv(file_path):
    return pd.read_csv(file_path)

# Function to scrape CRC32 hash for each employee using Selenium
def get_crc32_hash(full_name):
    driver = webdriver.Chrome()  # Adjust the path to your ChromeDriver executable
    driver.get("https://emn178.github.io/online-tools/crc32.html")

    # Fill in the full name in the web form
    input_element = driver.find_element_by_name("text")
    input_element.send_keys(full_name)

    # Click the "CRC32" button to calculate the hash
    crc32_button = driver.find_element_by_id("crc32")
    crc32_button.click()

    # Get the CRC32 hash result
    result_element = driver.find_element_by_id("result")
    crc32_hash = result_element.text

    driver.quit()
    return crc32_hash

# Function to process the data and identify the common salary for each employee
def process_data(people_df, salary_file):
    # Read the salary data
    salary_df = pd.read_excel(salary_file)

    # Create a new column for CRC32 hash in people_df
    people_df['CRC32'] = people_df.apply(lambda row: get_crc32_hash(row['First Name'] + ' ' + row['Last Name']), axis=1)

    # Merge people_df with salary_df on the CRC32 column
    merged_df = pd.merge(people_df, salary_df, left_on='CRC32', right_on='Codet name value')

    # Identify the common salary for each employee
    common_salary = merged_df.groupby(['First Name', 'Last Name'])['salary'].mean()

    return common_salary

# Example usage
people_csv_path = 'people.csv'  # Replace with the actual path to your people.csv file
salary_xlsx_path = 'salary.xlsx'  # Replace with the actual path to your salary.xlsx file

people_data = read_people_csv(people_csv_path)
result = process_data(people_data, salary_xlsx_path)

# Print the result
print(result)
