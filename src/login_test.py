from selenium import webdriver

# Initialize the browser
driver = webdriver.Chrome()

# Open a website
driver.get("https://example.com")

# Verify the title
assert "Example Domain" in driver.title

# Close the browser
driver.quit()
