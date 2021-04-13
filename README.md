# cvs-vacs-checker
Check vaccine availability from CVS

## Prerequesites
This script uses a free Twilio account to send text messages

## Setup
1. Install the python package requirements:
```pip install -r requirements.txt```
1. Modify the settings variables in main.py:
    - to_num
    - from_num
    - account_sid
    - account_token
1. Modify state to search for: ```while not locate_vax("VT"):```

## Run
1. Run script: ```python main.py```
