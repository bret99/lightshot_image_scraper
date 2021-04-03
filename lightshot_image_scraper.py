import urllib.request
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pytesseract
from PIL import Image
import random
import string
import os
import sys

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

secrets_list = []
positive_answers = ['Y', 'y', 'Yes', 'YES', 'yes']
negative_answers = ['N', 'n', 'No', 'NO', 'no']
lang_list = ['eng', 'rus']
links_list = []


def generate_alphanum_random_string():
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 6)).lower()
    return rand_string


def user_input_secrets():
    while 1:
        user_input_secrets = input(
            '\nEnter the \033[1;91msecrets\033[1;00m to find: ')
        secrets_list.append(user_input_secrets)
        user_input_exit = input(
                'Would you like to enter more \033[1;91msecrets\033[1;00m (y/n)? ')
        if user_input_exit in positive_answers or user_input_exit == '':
            pass
        elif user_input_exit in negative_answers:
            print('Your secrets to find => \033[1;92m')
            print(secrets_list, '\033[1;00m')
            break
        else:
            sys.exit('\033[1;91m\nWrong input!!!\nExiting..\033[1;00m\n')


def main():
    try:
        user_input_count = int(
            input(
                'Enter the links amount to scrape "\033[1;94mhttps://prnt.sc\033[1;00m" site: '
            ))
    except:
        sys.exit('\033[1;91m\nWrong input!\nExiting..\033[1;00m\n')

    count = 0

    while count < user_input_count:
        links_list.append(generate_alphanum_random_string())
        count = count + 1

    for link in links_list:
        try:
            driver.get('https://prnt.sc/' + link)
            image = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/img')
            download = image.get_attribute('src')
        except NoSuchElementException:
            print("Element not found")
        try:
            urllib.request.urlretrieve(download, 'image.png')
        except urllib.error.HTTPError:
            pass
        scan_result = pytesseract.image_to_string(Image.open(
            '{}/image.png'.format(os.getcwd())),
                                                  lang=user_input_lang)
        print(scan_result)
        for secret in secrets_list:
            if secret in scan_result:
                print(
                    "\033[1;91mSecret FOUND on \033[1;92m'https://prnt.sc/{0}'\033[1;91m! It is \033[1;92m{1}\033[1;00m"
                    .format(link, secret))
                os.system(
                    "echo '[] Secret FOUND on https://prnt.sc/{0}! It is {1}' >> lightshot_scan_results.txt"
                    .format(link, secret))
        print(
            "\n=================================================================================================================\n"
        )

    if os.path.isfile('{}/image.png'.format(os.getcwd())):
        os.remove('{}/image.png'.format(os.getcwd()))
    else:
        pass


user_input_lang = input(
    'Enter the language to find secrets (\033[1;94mrus\033[1;00m/\033[1;94meng\033[1;00m): '
).lower()

if user_input_lang not in lang_list:
    sys.exit('\033[1;91m\nWrong input!\nExiting..\033[1;00m\n')
else:
    user_input_secrets()
    main()
    
driver.quit()    

print('Your links are:\n')

for link in links_list:
    print('\033[1;93mhttps://prnt.sc/{}\033[1;00m'.format(link))

print(
    '\nIf SUCCESSFUL you will find scan results in \033[1;94mlightshot_scan_results.txt\033[1;00m\n'
)
