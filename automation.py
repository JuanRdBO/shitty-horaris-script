# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import keyboard
import platform

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import os

usernameStr = 'uxxxxx'
passwordStr = 'xxxxxx'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--incognito")

download_dir = "~/Desktop"
profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
options.add_experimental_option("prefs", profile)


driver = webdriver.Chrome('/Users/juanruizdebustillo/Scripts/Projects/horaris/chromedriver', chrome_options=options)
driver.get(('https://secretariavirtual.upf.edu/cosmos/Controlador/?apl=Uninavs&gu=a&idNav=identificacionCampus&aplDestino=PUBLI&NuevaSesionUsuario=true&idioma=ca&pais=ES&&NombreUsuarioAlumno=ALUMNO'))
delay = 3 # seconds

# fill in username and hit the next button
try:
	os.system("rm ~/Desktop/horaris.pdf")
except:
	pass

try:
    username = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'edit-name')))
    username.send_keys(usernameStr)
    password = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'edit-pass')))
    password.send_keys(passwordStr)
    signInButton = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'submit_ok')))
    signInButton.click()
    print ("Logged in!")
except TimeoutException:
    print( "Loading register page too much time!")

try:
    python_sign_in = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'sigBtnFreeHref')))
    #python_sign_in.click()

    action = ActionChains(driver)

    # First, go to your start point or Element
    action.move_to_element(python_sign_in)
    action.perform()

    # Then, move the mouse
    action.move_by_offset(0,100)
    action.pause(1)
    action.perform()

    action.move_by_offset(50,0)
    action.pause(1)
    action.perform()

    action.click()
    #action.context_click()
    action.perform()

    print ("Calendar page is being loaded!")
except TimeoutException:
    print( "Calendar page failed to load! Quitting...")


try:
    python_sign_in = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'botones')))
    python_sign_in.click()
    print ("Calender page is printing calendar...")
except TimeoutException:
    print( "Calender page failed to load! :-(")

driver.switch_to.window(driver.window_handles[0])    

try:
    python_sign_in = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'page-heading')))
    #python_sign_in.click()

    action = ActionChains(driver)

    # First, go to your start point or Element
    action.move_to_element(python_sign_in)
    action.perform()

    # Then, move the mouse
    action.move_by_offset(-450,80)
    action.pause(1)
    action.perform()

    action.click()
    #action.context_click()
    action.perform()

    print ("Calendar 'saving to pdf' page is ready!")
except TimeoutException:
    print( "Huh?! No button?! Quitting...")

sleep(2)
driver.switch_to.window(driver.window_handles[2])    

sleep(2)

keyboard.press_and_release('enter')
if platform.system() == 'Darwin':
    keyboard.press_and_release('cmd+d')
elif platform.system() == 'Linux':
    keyboard.press_and_release('alt+d')
elif platform.system() == 'Windows':
    keyboard.press_and_release('alt+d')
keyboard.write('HORARIS - printed with <3')
keyboard.press_and_release('enter')

# os.system("osascript ~/Scripts/Projects/horaris/applescript.scpt")
