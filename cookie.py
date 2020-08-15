from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.add_cookie({'name':'BAIDUID','value':'5465766E9B4753274BE0195151461AAD:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'W0tLTVudk5vTnRSZ01MM3JzUHdWWk96cTJMMzNkLWpCcnh0YUJuUHNoeXJad0piQVFBQUFBJCQAAAAAAAAAAAEAAADdrXwgvL6x8s7kMTIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKva2lqr2tpaQ'})
sleep(3)
driver.refresh()
sleep(2)
driver.quit()

