# Import necessary stufss
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Go to your Streamlit app
app_url = "http://13.213.202.48/"
driver.get(app_url)

# Click the "Upload Training Data (CSV)" button
training_data_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Upload Training Data (CSV)"]'))
)
training_data_button.click()

# Find the file input elements
file_inputs = driver.find_elements(By.CSS_SELECTOR, '[data-testid="stDropzoneInput"]')

# Upload the training data CSV
file_inputs[0].send_keys(r"D:\internshala assignment 2\data\Train.csv")

# Click the "Upload Testing Data (CSV)" button
testing_data_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Upload Testing Data (CSV)"]'))
)
testing_data_button.click()

# Upload the testing data CSV
file_inputs[1].send_keys(r"D:\internshala assignment 2\data\Test.csv")

# Wait for a moment
time.sleep(10)

# Click the "Start Training" button
buttons = driver.find_elements(By.CSS_SELECTOR, "[data-testid='baseButton-secondary']")
buttons[2].click()

# Wait for training to start
time.sleep(10)

# Check if the download button for predictions is visible
download_button = driver.find_element(By.CSS_SELECTOR, 'div.stDownloadButton')

# Ensure the download button is displayed
assert download_button.is_displayed()

# Close the browser
driver.quit()
