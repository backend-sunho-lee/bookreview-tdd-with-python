from selenium import webdriver

#browser = webdriver.Firefox()
browser = webdriver.Firefox(executable_path="C:/Users/sssun/AppData/Local/Programs/Python/geckodriver.exe")
browser.get('http://localhost:8000')

#assert 'Django' in browser.title
assert 'TEST' in browser.title
