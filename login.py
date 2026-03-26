from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    # Go to login page
    page.goto("https://staging.pomhealth.co/login")

    page.locator("//a[text()='click here to log in']").click()

    # Wait for the Sign-In button and click it
    sign_in = page.locator("//button[contains(., 'Sign in with Google')]")
    sign_in.wait_for(state="visible", timeout=30000)

    # --- Wait for popup and handle it ---
    with context.expect_page() as popup_info:
        sign_in.click()  # clicking the Google Sign-In button
    popup = popup_info.value  # this is the new popup window

    # Wait for the email input in the popup
    email_input = popup.locator("//input[@id='identifierId']")
    email_input.wait_for(state="visible", timeout=30000)
    email_input.fill("productbox@pomhealth.co")
    email_input.press("Enter")

    # Wait for password field to appear
    password_input = popup.locator("//input[@name='Passwd']")
    password_input.wait_for(state="visible", timeout=30000)
    password_input.fill("malcomax773172")
    password_input.press("Enter")

    # Wait for a bit after login
    popup.wait_for_timeout(10000)

