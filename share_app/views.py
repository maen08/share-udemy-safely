
from .models import ShareModel
from django.shortcuts import render,redirect
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
# GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')




# driver.quit()



def index(request):
    if request.method == 'POST':
        email = request.POST.get('email-input')
        password = request.POST.get('password-input')
        obj = Search()
        obj.word = word
        print(word)
        # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        # driver.get('https: // accounts.google.com/o/oauth2/auth/identifier?response_type = permission id_token code & scope = profile email & openid.realm & include_granted_scopes = true & redirect_uri = storagerelay % 3A % 2F % 2Fhttps % 2Fwww.udemy.com % 3Fid % 3Dauth218179 & client_id = 700206021005-bfren0qj1or8pp5spnn521hos9lm9ll9.apps.googleusercontent.com & ss_domain = https % 3A % 2F % 2Fwww.udemy.com & gsiwebsdk = shim & access_type = offline & flowName = GeneralOAuthFlow')
        driver.get('https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F')



        email = driver.find_element_by_name('email')
        password = driver.find_element_by_name('password')
        email.send_keys(email)
        # search.send_keys(Keys.RETURN)


        # result_links = driver.find_elements_by_css_selector("[class='question-hyperlink']")
        # for link in result_links:
        #     link.send_keys(Keys.CONTROL + 't', Keys.RETURN)
            
    return render(request, template_name='index.html')



