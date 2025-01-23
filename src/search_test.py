from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the browser
driver = webdriver.Chrome()

try:
    # Open the e-commerce site
    driver.get("https://example.com")

    # Find the search bar and input search query
    search_bar = driver.find_element(By.NAME, "q")  # Adjust the locator to the actual website
    search_bar.send_keys("Laptop")
    search_bar.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(3)

    # Verify search results are displayed
    results = driver.find_elements(By.CLASS_NAME, "product-item")  # Adjust the locator to the actual website
    assert len(results) > 0, "No search results found."

    print("Search test passed successfully!")

finally:
    # Close the browser
    driver.quit()
