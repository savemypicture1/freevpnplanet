# freevpnplanet tests

## Get started
1. Clone this repository `git clone https://github.com/savemypicture1/freevpnplanet.git`
2. Open the project folder `cd freevpnplanet`
3. Install the virtual environment:
- for windows `python -m venv venv`
- for macOS/linux `python3 -m venv venv`
4. Activate the virtual environment:
- for windows `venv\Scripts\activate`
- for macOS/linux `source venv/bin/activate`
5. [Install Allure](https://allurereport.org/docs/gettingstarted-installation/)
6. Installing dependencies `pip install -r requirements.txt`
7. Running autotests:
- for windows `python -m pytest --alluredir allure-results`
- for macOS/linux `python3 -m pytest --alluredir allure-results`
8. Generate a report `allure serve allure-results`