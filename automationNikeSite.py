from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():

    driver = webdriver.Chrome('chromedriver')

    # Navigate to the Nike website.
    driver.get('https://www.nike.com/')

    # Wait for the search input field to be visible.
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@name="q"]'))
    )

    # Enter a product name in the search input field.
    product_name = 'Jordan 4 Bred'
    search_input.send_keys(product_name)

    # Submit the search form.
    search_input.submit()

    # Wait for the search results page to load.
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-test="product-grid"]'))
    )

    # Find the first product in the search results.
    product_link = driver.find_element(By.XPATH, '//div[@data-test="product-grid"]//a')

    # Get the product details.
    product_name = product_link.text
    product_url = product_link.get_attribute('href')

    print("Product Name:", product_name)
    print("Product URL:", product_url)

    # Open the product page
    driver.get(product_url)

    # Select the desired size
    size_selector = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-qa="size-selector"]'))
    )
    size_selector.click()

    size_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//ul[@data-qa="size-dropdown-menu"]'))
    )

    size_option = size_dropdown.find_element(By.XPATH, f'//li[@data-qa="size-option"]/button[contains(text(), "9")]')
    size_option.click()

    # Add the product to the cart
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-qa="add-to-cart"]'))
    )
    add_to_cart_button.click()

    # Proceed to checkout or continue shopping depending on your requirements

    # Finally, close the browser window.
    driver.quit()

if __name__ == "__main__":
    main()
