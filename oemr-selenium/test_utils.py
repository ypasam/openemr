import json

from selenium.webdriver.common.by import By


def read_configurations_from_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    configurations = []

    for server, user_data in data["SERVERS"].items():
        url_value = user_data['url']
        users = user_data['users']

        for user in users:
            username = user['username']
            password = user['password']
            configurations.append((url_value, username, password))

    return configurations


def read_urls_from_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    # Adjusted to access the "SERVERS" key directly
    servers_data = data.get("SERVERS", {})
    urls = [server_data['url'] for server_data in servers_data.values()]

    return urls


# Added this function to access the url after logging in from secret.json
# to replace the hard coded value
def get_expected_url_after_login(file_path='secret.json'):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data.get('expected_url_after_login', '')


def login(browser, username, password, login_url):
    expected_url_after_login = get_expected_url_after_login()

    browser.get(login_url)
    browser.find_element(By.ID, 'authUser').send_keys(username)
    browser.find_element(By.ID, "clearPass").send_keys(password)
    browser.find_element(By.ID, "login-button").submit()

    tabs_to_close = browser.find_elements(By.CSS_SELECTOR, 'span[class="fa fa-fw fa-xs fa-times"]')
    for tab_close in tabs_to_close:
        tab_close.click()

    return expected_url_after_login in browser.current_url


def read_admin_configurations_from_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    first_user_configurations = []

    # Iterate over each server in the "SERVERS" dictionary
    for server, user_data in data["SERVERS"].items():
        url_value = user_data['url']

        # Check if there are users defined for the server and it's not an empty list
        if user_data['users']:
            first_user = user_data['users'][0]  # Get the first user
            username = first_user['username']
            password = first_user['password']

            first_user_configurations.append((url_value, username, password))

    return first_user_configurations
