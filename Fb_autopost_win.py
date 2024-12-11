import os
import random
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

fb_username = os.getenv('FB_USERNAME')
fb_password = os.getenv('FB_PASSWORD')

user_data_dir = r'C:\Users\Wan\Documents\FB_autopost_image\EdgeProfile'

image_folder = 'C:\\Users\\Wan\\Documents\\FB_autopost_image'

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# List of Facebook group URLs
group_urls = [
    'https://www.facebook.com/groups/1861082954211686',
    'https://www.facebook.com/groups/aamuar',
    # Add more groups as needed
]

# List of copywriting content
copywriting_list = [
   """ 𝗣𝗔𝗞𝗘𝗝 𝗦𝗨𝗥𝗣𝗥𝗜𝗦𝗘 𝗗𝗘𝗟𝗜𝗩𝗘𝗥𝗬 𝗨𝗡𝗧𝗨𝗞 𝗬𝗔𝗡𝗚 𝗧𝗘𝗥𝗦𝗔𝗬𝗔𝗡𝗚 ❤️🌹
📲 http://www.wasap.my/+60122205489/SurpriseDelivery
Order Hari ini‼️ Delivery Hari ini ‼️
Jom beli jiwa kesayangan🎂👨‍👩‍👧‍👦
Bila2 masa dan di mana saja uolls berada.
🎂 Birthday ❣️ Special Day
💞 Anniversary 🙏 Minta maaf
🎓 Graduasi 👶🏻 Newborn
💌 I love you 🎉 Congratulation
👋 Farewell 🌹 Get well soon
.
Nak order kek sahaja nk bt mkn sendiri pon boleh.. Kami juga terima order yg banyak untuk event/dessert table.
✅ 𝗣𝗲𝗹𝗯𝗮𝗴𝗮𝗶 𝗽𝗮𝗸𝗲𝗷 𝗯𝗮𝗷𝗲𝘁 𝗵𝗶𝗻𝗴𝗴𝗮 𝘆𝗮𝗻𝗴 𝗲𝗸𝘀𝗸𝗹𝘂𝘀𝗶𝗳
✅ 𝗧𝗲𝗿𝗶𝗺𝗮 𝗹𝗮𝘀𝘁 𝗺𝗶𝗻𝘂𝘁𝗲 𝗼𝗿𝗱𝗲𝗿, 𝘀𝗮𝗺𝗲 𝗱𝗮𝘆 𝗱𝗲𝗹𝗶𝘃𝗲𝗿𝘆
✅ Boleh delivery seluruh sem malaysia & Singapore
🚗✅ Delivery area:
Seluruh Pagoh, Pagohjaya, Paya Redan, Lenga, Gombang, Bukit Kepong, Paya Panjang, Bukit Pasir, Bakri, Muar, Kesang, Panchor, Gersik, Kundang Ulu, Bukit Serampang, Sawah Ring,  Sengkang, Bukit Gambir, Sagil, Serom, Sungai Mati, Tangkak, Seluruh muar & Seluruh Parit Sulong serta Batu Pahat
#mamasab #bouquetmurah #bouquetmamasab #bouquetbajet #anniversary #birthdaycake #birthdaygift #bouquetcoklat #surprisedelivery
#surprisegift #mamasabsuprisedelivery #mamasabviral #mamasabloversforever """,
    """ #OrderHariIni #DapatHariIni
#SurpriseDeliverySemenanjungMalaysia
Tercari-cari surprise delivery service last minit? Tak last minit pun boleh… last minit pun boleh sangat 😍x
𝐊𝐚𝐝𝐚𝐧𝐠-𝐤𝐚𝐝𝐚𝐧𝐠 𝐛𝐮𝐬𝐲 𝐬𝐚𝐧𝐠𝐚𝐭 𝐝𝐞𝐧𝐠𝐚𝐧 𝐤𝐞𝐫𝐣𝐚, 𝐭𝐞𝐫𝐥𝐮𝐩𝐚 𝐭𝐚𝐫𝐢𝐤𝐡 𝐢𝐬𝐭𝐢𝐦𝐞𝐰𝐚.... 𝐑𝐚𝐬𝐚 𝐛𝐞𝐫𝐬𝐚𝐥𝐚𝐡😩 𝐭𝐚𝐩𝐢 𝐧𝐚𝐤 #𝐮𝐫𝐠𝐞𝐧𝐭𝐝𝐞𝐥𝐢𝐯𝐞𝐫𝐲 𝐛𝐮𝐤𝐚𝐧 𝐬𝐞𝐦𝐮𝐚 𝐬𝐮𝐫𝐩𝐫𝐢𝐬𝐞 𝐩𝐥𝐚𝐧𝐧𝐞𝐫 𝐛𝐨𝐥𝐞𝐡 𝐛𝐮𝐚𝐭😅
Serahkan pada saya… saya bantu urus buatkan si dia tersenyum sepanjang hari😘
Kadang-kadang bukan birthday je nak bagi.. tapi sebab:
🧸 Saje nak wish I love you
🧸 Farewell
🧸 Nak cakap I am sorry
🧸 Bertunang
🧸 Sempena Anniversary
🧸 Kawan-kawan Retirement
Saya bantu uruskan. Awak pilih je nak macam mana…. Okay?
Tekan link ni okay:
📲 http://www.wasap.my/+60122205489/SurpriseDelivery
🚗✅ Delivery area:
Seluruh Pagoh, Pagohjaya, Paya Redan, Lenga, Gombang, Bukit Kepong, Paya Panjang, Bukit Pasir, Bakri, Muar, Kesang, Panchor, Gersik, Kundang Ulu, Bukit Serampang, Sawah Ring,  Sengkang, Bukit Gambir, Sagil, Serom, Sungai Mati, Tangkak, Seluruh muar & Seluruh Parit Sulong serta Batu Pahat """,
    # Add more copywriting content as needed
]

def select_random_images(image_folder, num_images=5):
    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png'))]
    selected_images = random.sample(image_files, min(num_images, len(image_files)))  # Adjust for fewer images
    return selected_images

daily_copywriting = random.choice(copywriting_list)

edge_driver_path = r'C:\Users\Wan\Documents\FB_autopost_image\edgedriver_win64\msedgedriver.exe'

# Initialize the WebDriver with the Edge driver
service = EdgeService(executable_path=edge_driver_path)
edge_options = EdgeOptions()
edge_options.use_chromium = True  # Ensure EdgeDriver uses the Chromium version of Edge
edge_options.add_argument(f"user-data-dir={user_data_dir}")
edge_options.add_argument("no-sandbox")
edge_options.add_argument("disable-dev-shm-usage")
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


driver.get('https://www.facebook.com')


def login(driver, fb_username, fb_password):
    try:
        email_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        print("Email input found")
    except TimeoutException:
        print("Timeout waiting for email input")
        driver.quit()
        exit(1)

    username_box = driver.find_element(By.ID, 'email')
    username_box.send_keys(fb_username)
    password_box = driver.find_element(By.ID, 'pass')
    password_box.send_keys(fb_password)
    password_box.send_keys(Keys.RETURN)

login(driver, fb_username, fb_password)





# Loop over each group URL
for url in group_urls:
    driver.get(url)
    time.sleep(5)
    
    try:
        post_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe'] span[class='x1lliihq x6ikm8r x10wlt62 x1n2onr6']"))
        )
        driver.execute_script("arguments[0].value = arguments[1];", post_box, daily_copywriting)
    except TimeoutException:
        print("Timeout while waiting for the post box using CSS Selector. Trying another selector.")
        try:
            post_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[contains(@aria-label, 'Write something')]"))
            )
            driver.execute_script("arguments[0].value = arguments[1];", post_box, daily_copywriting)
        except (TimeoutException, ElementNotInteractableException):
            print("Unable to find the post box. Skipping this group.")
            continue  # This continue needs to be inside the loop

    time.sleep(2)

    images = select_random_images(image_folder)
    for image in images:
        upload_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        upload_button.send_keys(image)
        time.sleep(2)

    post_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@data-testid, 'react-composer-post-button')]"))
    )
    post_button.click()
    time.sleep(5)
    time.sleep(60)


driver.quit()
