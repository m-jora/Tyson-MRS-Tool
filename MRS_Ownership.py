import time, sys, threading
import xlrd, spin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def Force_Ownership(choice):
    options = webdriver.ChromeOptions()
    #options.add_argument('-headless')
    options.add_argument('-no-sandbox')
    options.add_argument('-disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('chromedriver', options = options)

    sites = {
        "1": "http://workflow-train.tyson.com/MRS/Admin/DataSpecialistAdmin/ManageAgents",
        "2": "http://workflow-test.tyson.com/MRS/Admin/DataSpecialistAdmin/ManageAgents",
        "3": "http://workflow-dev.tyson.com/MRS/Admin/DataSpecialistAdmin/ManageAgents",
        "4": "http://workflow-sbx.tyson.com/MRS/Admin/DataSpecialistAdmin/ManageAgents",
        "5": "http://workflow.tyson.com/MRS/Admin/DataSpecialistAdmin/ManageAgents"
    }

    driver.set_page_load_timeout(20)
    try:
        driver.get(sites[choice])
    except:
        print('MRS Failed to Load Please Restart Program')
        return

    ids = []
    try:
        with open('IDs.xlsx', 'r') as f:
            pass

    except:
        print("Please create a Spreadsheet named IDs and save it in the same location as this program\n")
        return

    spinner_thread = spin.SpinnerThread()
    spinner_thread.start()

    wb = xlrd.open_workbook('IDs.xlsx')
    sheet = wb.sheet_by_index(0)
    for cell in sheet.col(0):
        ids.append(str(cell.value)[:-2])

    time.sleep(2)
    for x in ids:
        try:
            id_box = '//*[@id="vm-agent-mgr"]/div[1]/table/tbody/tr[2]/td[2]/input[1]'
            searchinput = driver.find_element(By.XPATH, id_box)
            searchinput.clear()
            searchinput.send_keys(x)

            force_button = '//*[@id="vm-agent-mgr"]/div[1]/table/tbody/tr[2]/td[2]/input[3]'
            searchinput = driver.find_element(By.XPATH, force_button)
            searchinput.click()

            time.sleep(2)
        except:
            try:
                time.sleep(2)
                driver.switch_to.alert.accept()
            except:
                pass

    spinner_thread.stop()
    print()
    print()
    print("Gained Ownership of all", len(ids), "requests")


def main(choice):
    task = threading.Thread(target = Force_Ownership, args = (choice,))
    task.start()

    task.join()


if __name__ == '__main__':
    main('5')
