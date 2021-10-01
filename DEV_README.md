1. Download chrome.exe and run the commands below:
    - unzip chromedriver_linux64.zip -d ~/
    - rm chromedriver_linux64.zip
    - sudo mv -f ~/chromedriver /usr/local/share
    - sudo chmod +x /usr/local/share/chromedriver
    - sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

2. Add environment variable 
   1. Getting LI_AT
Navigate to www.linkedin.com and log in
Open browser developer tools (Ctrl-Shift-I or right click -> inspect element)
Select the appropriate tab for your browser (Application on Chrome, Storage on Firefox)
Click the Cookies dropdown on the left-hand menu, and select the www.linkedin.com option
Find and copy the li_at value.
   2. Set the LI_AT environment variable
3. Server will run on http://127.0.0.1:5000/ 


       
