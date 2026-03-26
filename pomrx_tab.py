from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()

    # Go to login page
    page.goto("https://staging.pomhealth.co/login")
    page.wait_for_timeout(1000)

    # Click login link
    page.locator("//a[text()='click here to log in']").click()
    page.wait_for_timeout(1000)

    # Click Google Sign-In and handle popup
    sign_in = page.locator("//button[contains(., 'Sign in with Google')]")
    sign_in.wait_for(state="visible", timeout=30000)

    with context.expect_page() as popup_info:
        sign_in.click()

    popup = popup_info.value

    # Enter email
    popup.locator("#identifierId").fill("farzeen.ali4248@gmail.com")
    popup.keyboard.press("Enter")
    page.wait_for_timeout(1000)

    # Enter password
    popup.locator("input[name='Passwd']").wait_for(state="visible", timeout=30000)
    popup.locator("input[name='Passwd']").fill("Engineer2023")
    popup.keyboard.press("Enter")

    # Wait for popup to close
    popup.wait_for_event("close")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    # Select workspace / user
    page.get_by_text("staging test test").click()
    page.wait_for_timeout(1000)
    page.get_by_text("PomRx").click()
    page.wait_for_timeout(1000)

    # ---------------- GOALS ----------------
    page.get_by_role("button", name="Add Patient Goal").click()
    page.wait_for_timeout(500)
    page.locator("input[placeholder='Patient Goal title']").fill("My new patient goal")
    page.wait_for_timeout(500)

    # Save goal
    page.locator("div:has-text('My new patient goal')").get_by_role("button", name="save goal").first.click()
    page.wait_for_timeout(1000)

    # Delete goal
    page.locator("div:has-text('My new patient goal')").get_by_role("button", name="delete goal").first.click()
    page.wait_for_timeout(500)
    page.locator("button:has-text('Delete')").first.click()
    page.wait_for_timeout(1000)

    # Select goal from Healthie modal
    page.locator("//div[p[text()='Pulled from Healthie']]").first.click()
    page.wait_for_timeout(500)
    page.locator("svg.css-q7mezt").nth(0).locator("..").click()  # select specific goal
    page.wait_for_timeout(500)
    page.locator("//button[text()='Add Goals']").click()
    page.wait_for_timeout(1000)

    # ---------------- HOMEWORK ----------------
    page.get_by_role("button", name="Add Homework").click()
    page.wait_for_timeout(500)
    page.locator("input[placeholder='Homework title']").fill("My Homework Title")
    page.wait_for_timeout(500)

    # Save homework
    page.locator("svg.css-vh810p").first.click()
    page.wait_for_timeout(500)

    # Delete homework
    page.get_by_role("button", name="delete goal").first.click()
    page.wait_for_timeout(500)
    page.locator("button:has-text('Delete')").first.click()
    page.wait_for_timeout(1000)

    # Select homework from Healthie modal
    page.locator("div:has(p:text('Pulled from Healthie'))").first.click()
    page.wait_for_timeout(500)
    page.locator("svg.css-q7mezt").nth(0).locator("..").click()  # select specific homework
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Add Homework").click()
    page.wait_for_timeout(1000)

    # ---------------- LESSON PLAN ----------------
    # Create Custom Lesson
    page.locator("div:has(p:text('Create Custom'))").click()
    page.wait_for_timeout(500)
    page.locator("textarea[placeholder='Enter description']").fill("This is my lesson description.")
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Add Lesson").click()
    page.wait_for_timeout(1000)

    # From Template
    page.locator("div:has(p:text('From Template'))").click()
    page.wait_for_timeout(500)
    page.locator("div:has(span:text('Select'))").first.click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Add Lessons").click()
    page.wait_for_timeout(1000)

    # Edit lesson
    page.locator(
        "button:has(svg path[d='M3 17.25V21h3.75L17.81 9.94l-3.75-3.75zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83 3.75 3.75z'])"
    ).click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Cancel").click()
    page.wait_for_timeout(500)

    # Delete lesson
    page.locator(
        "button:has(svg path[d='M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6zM19 4h-3.5l-1-1h-5l-1 1H5v2h14z'])"
    ).click()
    page.wait_for_timeout(500)

    # ---------------- PATIENT VIEW ----------------
    page.get_by_role("button", name="View Patient-Facing Mode").click()
    page.wait_for_timeout(5000)  # observe

    # Close browser
    browser.close()