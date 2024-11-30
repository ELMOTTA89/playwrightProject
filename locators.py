
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright :
    browser=playwright.chromium.launch(headless=False , slow_mo=2000)
    page=browser.new_page()
    page.goto("https://bootswatch.com/default/")

    #Locators

    #select Button
    btn=page.get_by_role("button",name="Default button")
    btn.highlight()
    btn.click()

    #Select heading
    heading=page.get_by_role("heading",name='Heading 2')
    heading.highlight()

    #Select radio button
    radio_btn=page.get_by_role("radio", name="Option two can be something else and selecting it will deselect option one")
    radio_btn.highlight()

    #Select checkboxes
    checkboxes_btn=page.get_by_role("checkbox",name="Default checkbox")
    checkboxes_btn.highlight()
    checkboxes_btn.check()

    #Input field locators
    email_input=page.get_by_label("Email address")
    email_input.highlight()
    password_input=page.get_by_label("Password")
    password_input.highlight()
    example_area=page.get_by_label("Example textarea")
    example_area.highlight()
    address_email=page.get_by_placeholder("Enter email")
    address_email.highlight()

    #inner Text locator
    page.get_by_text("with faded secondary text").highlight()

    #select image
    #page.goto("https://unsplash.com/fr")
    #page.get_by_alt_text("Une femme assise devant un ordinateur portable").highlight()

    #select by title
    page.get_by_title("attribute").highlight()
    




    time.sleep(3)


    browser.close()
