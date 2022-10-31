from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import cv2 as cv
import time

numImages = 50
saveDir = "cao"
query = ["dog",'cachorro','cao']
savePath = 'C:\\Users\\Pcpastre_\\Documents\\GitHub\\googleImageDownlaod\\download'
try:
	os.mkdir(savePath)
except:
	pass


try:
	os.mkdir(savePath +'/' + saveDir)
except:
	pass


# Creating a webdriver instance
driver = webdriver.Chrome()


def scroll_to_bottom():

	driver.execute_script('\
		window.scrollTo(0,document.body.scrollHeight)')

	last_height = driver.execute_script('\
	return document.body.scrollHeight')

	while True:
		driver.execute_script('\
		window.scrollTo(0,document.body.scrollHeight)')

		time.sleep(3)

		new_height = driver.execute_script('\
		return document.body.scrollHeight')

		# click on "Show more results" (if exists)
		try:
			driver.find_element_by_css_selector(".YstHxe input").click()
			time.sleep(3)

		except:
			pass

		# checking if we have reached the bottom of the page
		if new_height == last_height:
			break

		last_height = new_height

def saveImg(saveDir, query):
	count = 0
	for j in query:
		# Maximize the screen
		driver.maximize_window()

		# Open Google Images in the browser
		url = 'https://www.google.com/search?q='+ j+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-0oOYuID7AhXBrJUCHS9PANAQ_AUoAXoECAMQAw&biw=1280&bih=648&dpr=1.5'
		driver.get(url)
		"""
		# Finding the search box
		box = driver.find_element(By.XPATH, ('//*[@id="yDmH0d"]'))

		# Type the search query in the search box
		box.send_keys(j)

		# Pressing enter
		box.send_keys(Keys.ENTER)
		"""
		scroll_to_bottom()

		# Loop to capture and save each image
		for i in range(1, numImages):

			# range(1, numImages) will capture images 1 to X of the search results
			# You can change the range as per your need.
			
				
			try:

			# XPath of each image
				img = driver.find_element(By.XPATH,('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img'))

				# Enter the location of folder in which
				# the images will be saved
				img.screenshot(savePath + '/' + saveDir +'/'+ 
							saveDir + '_(' + str(i+count*numImages) + ').png')
				# Each new screenshot will automatically
				# have its name updated

				# Just to avoid unwanted errors
				time.sleep(0.2)

			except:
				print("XPATH ERROR")
				# if we can't find the XPath of an image,
				# we skip to the next image
				continue
		count = count + 1

saveImg(saveDir, query)

driver.close()
