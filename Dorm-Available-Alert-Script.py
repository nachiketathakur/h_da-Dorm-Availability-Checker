from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yagmail

# === CONFIGURATION ===
EMAIL_TO_NOTIFY = "enter_your_email@gmail.com"
CHECK_INTERVAL = 60  # check every 60 seconds

# === SETUP EMAIL ALERT ===
yag = yagmail.SMTP("enter_your_email.com", "app_password_see_instructions")

# === SETUP SELENIUM ===
driver = webdriver.Chrome()  # Make sure ChromeDriver is in PATH
driver.get("https://mse-application-hda.de/dashboard/index.html")

# === MANUAL LOGIN ===
input("🔐 Please log in manually, then press Enter to start checking...")

# === CHECK LOOP ===
print("🔄 Starting periodic check...")
while True:
    try:
        print("🔁 Reloading the page via .get() for full refresh...")
        #driver.get("https://mse-application-hda.de/dashboard/index.html")
        driver.refresh()
        time.sleep(5)  # wait for page to load

        # Step 1: Locate the heading "Payment"
        payment_heading = driver.find_element(By.XPATH, "//h2[contains(text(), 'Payment')]")

        # Step 2: Get the table immediately following the heading
        payment_table = payment_heading.find_element(By.XPATH, "following-sibling::table[1]")

        # Step 3: Count only the data rows (skip header)
        rows = payment_table.find_elements(By.XPATH, ".//tr")[1:]  # skip table header

        print(f"🔎 Found {len(rows)} payment options.")
        if len(rows) >= 3:
            print("✅ Third payment option is now available!")
            yag.send(
                to=EMAIL_TO_NOTIFY,
                subject="🏠 Housing Option Available!",
                contents="The third payment option has appeared in your college portal. Log in and apply ASAP!"
            )
            break  # stop loop after notifying
        else:
            print(f"❌ Only {len(rows)} options. Will check again in {CHECK_INTERVAL} seconds.")

    except Exception as e:
        print("⚠️ Error occurred:", e)

    time.sleep(CHECK_INTERVAL)

driver.quit()
