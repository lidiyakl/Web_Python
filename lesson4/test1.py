from testpage import OperationsHelper
import logging
import yaml
from time import sleep

with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)

def test_login_neg(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_login_pos(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("pswd"))
    testpage.click_login_button()
    assert "hello" in testpage.get_text().lower(), "test FAILED"

def test_contact_us(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name(testdata.get("name"))
    testpage.enter_email(testdata.get("email"))
    testpage.enter_content(testdata.get("content2"))
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == "Form successfully submitted", "test FAILED"

def test_create_post(browser):
    logging.info("Test create_post Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.add_title(testdata["title"])
    testpage.add_description(testdata["description"])
    testpage.add_content(testdata["content"])
    testpage.click_save_button()
    sleep(1)
    assert testpage.new_post_title() == f"{testdata['title']}", "test add post FAILED!"