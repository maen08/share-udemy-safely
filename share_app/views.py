
from .models import ShareModel
from django.shortcuts import render,redirect
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from decouple import config



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
        email1 = request.POST.get('email')
        # password1 = request.POST.get('password')

        ShareModel.objects.create(
            email=email1,
            # password=password1
        )

        print(email1)
        # print(password1)
       
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver.maximize_window()
    
        if email1 == 'kabentolu':
                        # https://accounts.google.com/signin/v2/challenge/pwd?response_type=permission%20id_token%20code&scope=profile%20email&openid.realm&include_granted_scopes=true&redirect_uri=storagerelay%3A%2F%2Fhttps%2Fwww.udemy.com%3Fid%3Dauth686665&client_id=700206021005-bfren0qj1or8pp5spnn521hos9lm9ll9.apps.googleusercontent.com&ss_domain=https%3A%2F%2Fwww.udemy.com&gsiwebsdk=shim&access_type=offline&flowName=GeneralOAuthFlow&cid=1&navigationDirection=forward&TL=AM3QAYatKH4BHE4pwIz9Ms8zLPz-A_jM0YPDSad9Y1QgTOIX_r-65y_oWNg6eUA6
            driver.get('https://accounts.google.com/o/oauth2/auth/identifier?response_type=permission id_token code&scope=profile email&openid.realm&include_granted_scopes=true&redirect_uri=storagerelay%3A%2F%2Fhttps%2Fwww.udemy.com%3Fid%3Dauth686665&client_id=700206021005-bfren0qj1or8pp5spnn521hos9lm9ll9.apps.googleusercontent.com&ss_domain=https%3A%2F%2Fwww.udemy.com&gsiwebsdk=shim&access_type=offline&flowName=GeneralOAuthFlow')

            emails = driver.find_elements_by_name('identifier') #avoid 'WebElement' has no len() error
            for email in emails:
            
                EMAIL = config('EMAIL')

                email.send_keys(EMAIL)
                email.send_keys(Keys.RETURN)

                PASS = config('PASS')
                driver.implicitly_wait(15)
                passwords = driver.find_element_by_name('password')
              

                passwords.send_keys(PASS)
                passwords.send_keys(Keys.RETURN)

 

            
    return render(request, template_name='index.html')



