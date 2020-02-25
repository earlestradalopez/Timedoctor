*** Settings ***
Resource	${EXECDIR}/main.robot

*** Test Cases ***
Test Case 1
	[Documentation]	Evaluation Task test case
	I create a new silent company
	I download Timedoctor application
	I install the Timedoctor application
	I log in to Timedoctor application
	I navigate page	https://www.theverge.com
	I put OS into sleep mode for  60 seconds
	I wait for  60 seconds
	I open new tab and navigate to  https://www.facebook.com
	I wait for  60 seconds
	I open the application  calc.exe
	I wait for  60 seconds
	# Lock and Unlock code here
	I put OS into sleep mode for  180 seconds
	I disable the network connection	
	I wait for  120 seconds
	I restore the network connection
	I close the browser
	I uninstall the Timedoctor application	
	I verify the Activity Timeuse
