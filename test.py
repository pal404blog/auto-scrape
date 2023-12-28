from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import openpyxl



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
wb = openpyxl.Workbook()
ws = wb.active
data = (("ID","Name","CGPA", "SGPA"))
ws.append(data)
for x in range(181):
    driver.get('https://charusat.edu.in:912/UniExamResult/frmUniversityResult.aspx') # Open Quora website

    a1 = driver.find_element('xpath','//*[@id="ddlInst"]') # HTML tag element for email field
    drop = Select(a1)
    drop.select_by_visible_text('CSPIT')

    a2 = driver.find_element('xpath','//*[@id="ddlDegree"]') # HTML tag element for password field
    drop = Select(a2)
    drop.select_by_visible_text('BTECH(CE)') # Login password

    a3 = driver.find_element('xpath','//*[@id="ddlSem"]') # HTML tag element for password field
    drop = Select(a3)
    drop.select_by_visible_text('5')

    a4 = driver.find_element('xpath','//*[@id="ddlScheduleExam"]') # HTML tag element for password field
    drop = Select(a4)
    drop.select_by_visible_text('NOVEMBER 2023')

    a5 = driver.find_element('xpath','//*[@id="txtEnrNo"]') # HTML tag element for password field
    
    if x< 154:
        if x < 100:
            if x < 10:
                a5.send_keys('21CE00'+ str(x+1) )
            else:
                a5.send_keys('21CE0'+ str(x+1) )
        
        else :
            a5.send_keys('21CE'+ str(x+1) )
    else:
        a5.send_keys('D22CE'+ str(x+1) )
    # Diploma rolls

    

    button = driver.find_element('xpath','//*[@id="btnSearch"]') # HTML tag element for button

    button.click()
    WebDriverWait(driver, timeout=100)
    try:
        # driver.wait(button.get_attribute("Processing.."))
        b1 = driver.find_element('xpath','/html/body/form/div[3]/div/div/table[3]/tbody/tr[1]/td[1]')
        name = driver.find_element('xpath','//*[@id="uclGrd1_lblStudentName"]')
        idno = driver.find_element('xpath','//*[@id="uclGrd1_lblExamNo"]')
        # b3 = driver.find_element('xpath','/html/body/form/div[3]/div/div/table[4]/tbody/tr[1]/td[4]')
        # b4 = driver.find_element('xpath','//*[@id="uclGrd1_lblSGPA"]')
        # b5 = driver.find_element('xpath','/html/body/form/div[3]/div/div/table[3]/tbody/tr[1]/td[4]')
        # b6 = driver.find_element('xpath','//*[@id="uclGrd1_lblExamNo"]')
        # b7 = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl02_lblSubjectName"]')
        # sgp = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl02_lblGrade"]')
        # javat = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl03_lblGrade"]')
        # javap = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl04_lblGrade"]')
        # det = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl05_lblGrade"]')
        # dep = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl06_lblGrade"]')
        # dcnt = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl07_lblGrade"]')
        # dcnp= driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl08_lblGrade"]')
        # art = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl09_lblGrade"]')
        # creative = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl10_lblGrade"]')
        # math = driver.find_element('xpath', '//*[@id="uclGrd1_grdResult_ctl11_lblGrade"]')
        cgpa = driver.find_element('xpath', '//*[@id="uclGrd1_tblCumulative"]/tbody/tr[2]/td[3]')
        sgpa = driver.find_element('xpath', '//*[@id="form1"]/div[3]/div/div/table[4]/tbody/tr[2]/td[3]')





        data1 = ((idno.text,name.text,cgpa.text , sgpa.text))
        ws.append(data1)
        wb.save("result2024.xlsx")
        # f = open("results.txt", "a")
        # f.write(b1.text + ":" + name.text + "\n" + b5.text + ":" + b6.text + "\n" + b3.text + ":" + b4.text +"\n \n")
        # f.close()

    except:
        print("Id not found " + str(x+1))