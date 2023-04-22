from selenium import webdriver
from selenium.webdriver.common.keys import Keys

searches = ['source:"American Economic Review" OR source:"Journal of Finance" OR source:"Journal of Financial Economics" OR source:"Journal of Monetary Economics" OR source:"Journal of Political Economy" OR source:"Quarterly Journal of Economics"', 
            'source:"Review of Economic Studies" OR source:"American Political Science Review" OR source:"Economic Journal" OR source:"European Economic Review" OR source:"Games and Economic Behavior" OR source:"International Economic Review"', 
            'source:"International Organization" OR source:"Journal of Accounting and Economics" OR source:"Journal of Business" OR source:"Journal of Business and Economic Statistics" OR source:"Journal of Econometrics"', 
            'source:"Journal of Economic Theory" OR source:"Journal of International Economics" OR source:"Journal of Public Economics" OR source:"Journal of the American Statistical Association " OR source:"RAND Journal of Economics"']

while True:
   search_term = input("What to search for?: ")

   browser = webdriver.Chrome()
   for i in searches:
      search = f'{search_term} {i}'
      browser.execute_script("window.open('');")
      browser.switch_to.window(browser.window_handles[-1])
      browser.get('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + search)

   input("Press Enter to close all tabs and exit")
   browser.quit()
