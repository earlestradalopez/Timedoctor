## Requirements for Automation
### Applications:
* Latest Python (3.8)
* Chrome browser
* Chromedriver

### Python packages:
* pip install robotframework
* pip install robotframework-selenium2library
* pip install keyboard
* pip install pyautogui
* pip install configparser
* pip install requests
* pip install pywin32

## Setup Configuration
* Input the correct user directory in main.robot file under ${user_path} Variables

![user path](https://github.com/earlestradalopez/Timedoctor/blob/master/images/config.png)

## How to Run the automation
* Run command line as Administrator 
* Go to the Timedoctor automation directory - e.g. cd <Timedoctor automation directory>
* Run for Silent mode: `robot Test_Cases\Silent-mode.robot`
* Run for Active mode: `robot Test_Cases\timedoctor.robot`
  
![cmd image](https://github.com/earlestradalopez/Timedoctor/blob/master/images/cmd.png) 
  
## Output
### Report log file = report.html under current directory

![report image](https://github.com/earlestradalopez/Timedoctor/blob/master/images/report.png)

### Detailed log file = log.html under current directory

![log image](https://github.com/earlestradalopez/Timedoctor/blob/master/images/log.png)
