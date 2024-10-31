import time
from selenium import webdriver
from stealthenium import stealth


url = "https://www.browserscan.net/bot-detection"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
chrome_options.add_experimental_option('useAutomationExtension', False)

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--incognito")

chrome_options.add_argument('--user-agent={}'.format(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"))
try:
    # 启动浏览器
    driver = webdriver.Remote(
        command_executor='http://167.179.65.227:4444/wd/hub',
        options=chrome_options
    )
    # 隐藏浏览器特征
    # stealth(driver,
    #     languages=["en-US", "en"],
    #     vendor="Google Inc.",
    #     platform="Win32",
    #     webgl_vendor="Intel Inc.",
    #     renderer="Intel Iris OpenGL Engine",
    #     fix_hairline=True,
    # )
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    driver.get(url)
    # 将截图保存到本地
    time.sleep(5)
    driver.save_screenshot("../tmp/screenshot.png")
    print(driver.title)
    is_go = input("Continue? (y/n): ")
    if is_go == "n":
        raise Exception("User stop")
    driver.get(url)
    # 将截图保存到本地
    driver.save_screenshot("../tmp/screenshot.png")
    print(driver.title)
    is_go = input("Continue? (y/n): ")
    if is_go == "n":
        raise Exception("User stop")
except Exception as e:
    print(e)
finally:
    driver.quit()