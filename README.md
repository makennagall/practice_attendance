# 🧗‍♀️practice_attendance 🪨
### Link to GitHub Repository: https://github.com/makennagall/practice_attendance. <br>
* You will need to generate an API credential and give it access to editing the spreadsheet. Here’s where you can manage your credentials: https://console.cloud.google.com/apis/credentials <br>
* After you generate your credentials, you will need to download them (a client and a key).  <br>
Save your key at the path specified in the line of code below (you can change this path to wherever you store your key, but standardize it among people who will run the code, and do not store it in the practice_attendence folder because it should not be in the GitHub)
client = pygsheets.authorize(service_account_file='../attendance/key_2024') 
The key will be a text document that looks like this: <br>
```
{
 "type": "service_account",
 "project_id": "attendance-",
 "private_key_id": "",
 "private_key": "-----BEGIN PRIVATE KEY-----




\n-----END PRIVATE KEY-----\n",
 "client_email": "gsheets@attendance.iam.gserviceaccount.com",
 "client_id": "###########",
 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
 "token_uri": "https://oauth2.googleapis.com/token",
 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
 "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gsheets%40attendance.iam.gserviceaccount.com",
 "universe_domain": "googleapis.com"
}
```


* Then update the access on the Google Sheets so the client email has editing access. My client email looks like this:<br>
gsheets@attendance-410803.iam.gserviceaccount.com, yours will be similar. <br>
* After this is set up, you should edit the attendance-names sheet of the practice attendance sheet and the Merch, Paid, and Trips sheets of the Dues spreadsheet. <br>
* You do not need to edit the Master sheet in Dues or the Totals or Dates sheets in the Attendance spreadsheet. Running the Python program will update these sheets. <br>
* To run the Python program, after downloading it from the GitHub, within the terminal on your computer you need go to the folder (cd stands for change directory):
<br>

    cd practice_attendance

 and run:<br>
 
    chmod +x run.py
  
chmod changes the permissions for this file so you can run the Python program. After the permissions are updated, you will not need to run this line again.<br>
After this is completed, if you navigated to the practice_attendance directory, run:

    ./run.py
  
this will run both the dues.py and attendance.py files. If you run into issues, you may need to run chmod +x for dues.py and attendance.py.
	
