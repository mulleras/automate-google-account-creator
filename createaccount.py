from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialize the ChromeDriver instance
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=options)

# Navigate to the Google account page
driver.get("https://accounts.google.com/")

# Wait for the page to load
time.sleep(5)  # Adjust the sleep time if necessary

try:
    # Find and click the 'Create account' button
    elements = driver.find_elements(By.TAG_NAME, 'span')
    for elem in elements:
        if elem.text == "Create account":
            print(elem.text)
            elem.click()
            break  # Exit the loop once the element is clicked

    # Wait for the next page to load
    time.sleep(5)  # Adjust the sleep time if necessary

    # Find and click the 'For my personal use' option
    elements = driver.find_elements(By.TAG_NAME, 'span')
    for elem in elements:
        if elem.text == "For my personal use":
            print(elem.text)
            elem.click()
            break  # Exit the loop once the element is clicked

except StaleElementReferenceException:
    print("Element is no longer attached to the DOM.")
except NoSuchElementException:
    print("Element not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Wait for the field to be interactable
time.sleep(5)  # Adjust the sleep time if necessary

try:
    # Find the 'firstName' field and enter text
    first_name_field = driver.find_element(By.ID, "firstName")
    first_name_field.send_keys("amharic movies")
    print("Entered text in 'firstName' field.")
except NoSuchElementException:
    print("Field not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Wait for any final interactions
time.sleep(5)  # Adjust the sleep time if necessary

# Close the browser window
driver.quit()
