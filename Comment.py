from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def comment(driver, comment):
    commentsection = '//*[@id="SupportSection"]/ul/li[3]/a'
    driver.find_element(By.XPATH, commentsection).send_keys(Keys.ENTER)


    comment_box = '//*[@id="RequestSupportViewModel_NewComment"]'
    driver.find_element(By.XPATH, comment_box).send_keys(comment)


    comment_submit = '//*[@id="btnAddComment"]'
    driver.find_element(By.XPATH, comment_submit).send_keys(Keys.ENTER)
    