import requests
import time
import datetime
from twilio.rest import Client

# Settings Variables
to_num = "FILL THIS OUT"  # Phone number to text
from_num = "FILL THIS OUT"  # Phone number of your Twilio Account
account_sid = "FILL THIS OUT"  # Twilio Accound Id
account_token = "FILL THIS OUT"  # Twilio API Token

site_link = "https://www.cvs.com/immunizations/covid-19-vaccine"


def locate_vax(state="VT", test=False):
    if test:
        client = Client(account_sid, account_token)
        message = client.messages.create(
            to=f"+{to_num}", from_=f"+{from_num}", body="Testing the texting!"
        )
        return True
    try:
        getPage = requests.get(
            f"https://www.cvs.com/immunizations/covid-19-vaccine//immunizations/covid-19-vaccine.vaccine-status.{state}.json?vaccineinfo"
        )
        getPage.raise_for_status()
        vaccines = getPage.json()

        found = []

        for location in vaccines["responsePayloadData"]["data"][state]:
            if location["status"] != "Fully Booked":
                found.append(location)

        if found:
            print("Vaccines Found!")
            locations = [location["city"] for location in found]
            locations_list = ", ".join(locations)
            message = f"Vaccine(s) found: {locations_list}. Sign up: {site_link}"
            client = Client(account_sid, account_token)
            message = client.messages.create(
                to=f"+{to_num}", from_=f"+{from_num}", body=message
            )
            return True
        else:
            print("NO VACCINES FOR YOU :'(")
            return False
    except Exception as e:
        print(f"Some Error Happened: {e}")
        return False


def main():
    starttime = time.time()
    while not locate_vax("VT"):
        print(datetime.datetime.now())
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))


if __name__ == "__main__":
    main()
