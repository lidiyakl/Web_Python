import yaml
# from module import Site
import pytest
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
# site = Site(testdata["address"])


def test_step1(site, selector_login, selector_password, selector_button, selector_error):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys("test")
    
    input2 = site.find_element("xpath", selector_password)
    input2.send_keys("test")
    
    btn = site.find_element("css", selector_button)
    btn.click()
    
    err_label = site.find_element("xpath", selector_error)
    assert err_label.text == "401"

def test_step2(site, selector_login, selector_password, selector_button, selector_home):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("login"))
    
    input2 = site.find_element("xpath", selector_password)
    input2.send_keys(testdata.get("pswd"))
    
    btn = site.find_element("css", selector_button)
    btn.click()
    
    home_path = site.find_element("xpath", selector_home)
    assert home_path.text == "Home", "test failed"

# Дом. задание

def test_step3(site, selector_login, selector_password, selector_button, create_post,
                add_title, add_description, add_content, save_post, check_title, title_name):

    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("login"))
    
    input2 = site.find_element("xpath", selector_password)
    input2.send_keys(testdata.get("pswd"))
    
    btn = site.find_element("css", selector_button)
    btn.click()

    time.sleep(testdata["sleep_time"])

    btn_post = site.find_element("xpath", create_post)
    btn_post.click()

    input3 = site.find_element("xpath", add_title)
    input3.clear()
    input3.send_keys(testdata["title"])

    input4 = site.find_element("xpath", add_description)
    input4.clear()
    input4.send_keys(testdata["description"])

    input5 = site.find_element("xpath", add_content)
    input5.clear()
    input5.send_keys(testdata["content"])

    btn = site.find_element("xpath", save_post)
    btn.click()

    time.sleep(testdata["sleep_time"])

    code_label = site.find_element("xpath", check_title).text
    assert code_label == title_name, "test FAIL"
    
    site.driver.close()
    

if __name__=="__main__":
    pytest.main([-vv])

# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))

# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath, "color"))