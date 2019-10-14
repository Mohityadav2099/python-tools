from selenium import webdriver

def login(driver,email,password):
	url='https://www.facebook.com/'
	driver.get(url)
	username=driver.find_element_by_id('email')
	username.send_keys(email)
	password1=driver.find_element_by_id('pass')
	password1.send_keys(password)
	loginButton = driver.find_element_by_css_selector('[value="Log In"]')
	loginButton.click()

def main():
	driver=webdriver.Firefox()
	email='Your email ID here'
	password='Your password here'
	login(driver,email,password)
main()
