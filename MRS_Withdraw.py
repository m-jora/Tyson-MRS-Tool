import time, sys, threading
import csv, spin
from Comment import comment as add_comment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def Withdraw_requests(choice):

    sites = {
        "1": "http://workflow-train.tyson.com/MRS/Home/Inbox",
        "2": "http://workflow-test.tyson.com/MRS/Home/Inbox",
        "3": "http://workflow-dev.tyson.com/MRS/Home/Inbox",
        "4": "http://workflow-sbx.tyson.com/MRS/Home/Inbox",
        "5": "http://workflow.tyson.com/MRS/Home/Inbox"
    }

    options = webdriver.ChromeOptions()
    options.add_argument('-headless')
    options.add_argument('-no-sandbox')
    options.add_argument('-disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('chromedriver', options=options)

    driver.set_page_load_timeout(20)
    valid = False

    try:
        driver.get(sites[choice])
    except:
        print('MRS Failed to Load Please Restart Program')
        return

    while not valid:
        num_requests = input("Enter Number of Requests: ")
        try:
            num_requests = int(num_requests)
            valid = True
    
        except:
            print("Please Input a valid Number")
    num_remaining = num_requests

    valid = False
    while not valid:
        id = input ("Input Starting Position: ")
        try:
            id = int(id)
            if id < 1:
                print("Please Input A Valid Start Position")
            else:
                valid = True
        except:
            print("Please Input a Valid Number")



    valid = False
    while not valid:    
        comment = input("Enter Reason for Withdraw: ")
        if comment == '' or comment == None:
            print('Please input a Reason')
        else:
            valid = True

    spinner_thread = spin.SpinnerThread()
    spinner_thread.start()
    
    #id = 8
    error_count = 0
    error_ids = []

    while num_remaining > 0:
        
        if driver.current_url != sites[choice]:
            try:
                driver.get(sites[choice])
            except:
                pass


        try:
            requestid = f'//*[@id="Rows"]/tr[{id}]/td[1]/a'
            searchinput = driver.find_element(By.XPATH, requestid)
            current_request = searchinput.text
            searchinput.send_keys(Keys.ENTER)
        except:
            if driver.current_url == sites[choice]:
                print("Please ensure you don't have less requests than value input")

            else:
                driver.get(sites[choice])

        for i in range(3):
            try:
                time.sleep(1)
                driver.switch_to.alert.accept()

            except:
                pass

        try:
            request_action = '//*[@id="Withdrawn"]'
            driver.find_element(By.XPATH, request_action).click()
            
            proceed_button = '//*[@id="vm-cust-mass-update-form"]/form/div[3]/div/div/div/div/input'
            item = driver.find_element(By.XPATH, proceed_button)
            add_comment(driver, comment)
            item.click()

            if driver.current_url != sites[choice]:
                        error_count += 1
                        id += 1
                        num_remaining -= 1
                        error_ids.append(current_request)

        except:
            try:
                request_action = '//*[@id="rbWithdrawn"]'
                driver.find_element(By.XPATH, request_action).click()

                proceed_button = '//*[@id="btnRequestAction"]'
                item = driver.find_element(By.XPATH, proceed_button)
                add_comment(driver, comment)
                item.click()

                if driver.current_url != sites[choice]:
                        error_count += 1
                        id += 1
                        num_remaining -= 1
                        error_ids.append(current_request)

            except:
                try:
                    request_action = '//*[@id="Withdrawn"]'
                    driver.find_element(By.XPATH, request_action).click()
                    
                    proceed_button = '//*[@id="vm-override-partners-form"]/form/div[3]/div/div/div/div/input'
                    item = driver.find_element(By.XPATH, proceed_button)
                    add_comment(driver, comment)
                    item.click()
                    
                    if driver.current_url != sites[choice]:
                        error_count += 1
                        id += 1
                        num_remaining -= 1
                        error_ids.append(current_request)

                except:
                    id += 1
                    num_remaining -= 1
                    error_count += 1
                    error_ids.append(current_request)
     
        num_remaining -= 1
        if num_remaining <= error_count:
            time.sleep(5)


    spinner_thread.stop()
    print('\n')
    with open("Error_IDs.csv", 'w', newline = '') as fout:
        writer = csv.writer(fout)
        for ID in error_ids:
            writer.writerow([ID])
    print("Error Count:", error_count)
    print("List of IDS With Possible Errors:", error_ids)


def main(choice):
    task = threading.Thread(target = Withdraw_requests, args=(choice,))
    task.start()

    task.join()
    

if __name__ == '__main__':
    main('5')
