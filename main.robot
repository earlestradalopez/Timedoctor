*** Settings ***
Library     Selenium2Library
Library     String
Library     ${CURDIR}${/}modules${/}functions.py
 
*** Variables ***
${Browser}      Chrome
${f_exist}      False
${Email}        qa_test@test.com
${TokenId}      empty
${user_path}    C:/Users/test
${app_delay}    15s

*** Keywords ***
I create a new silent company
    ${Email} =              signup
    Should Not Be Empty     ${Email}

I verify the Activity Timeuse
    ${TokenId} =            getAuthorizationDetails
    Sleep                   360s # wait for 3 mins to get the activity timeuse logs
    ${f_exist} =            getActivityTimeuse      ${TokenId}
    Should Be True          ${f_exist}

I login to Timedoctor page
    Input Text      //*[@id="mat-input-0"]       ${Email}
    Input Password  //*[@id="mat-input-1"]       123456
    Click Button    LOGIN

I install the Timedoctor application
    runFile                 installer/timedoctor2-setup-3.0.52-windows.exe
    Sleep                   ${app_delay}
    window_activate         Setup TkTopLevel
    sendKeys                enter 2
    sendKeys                enter 1
    ${f_exist} =            check_file_exist    ${user_path}/Time Doctor 2/timedoctor2.exe
    Should Be True          ${f_exist}
    ${f_exist} =            check_file_exist    ${user_path}/Time Doctor 2/uninstall.exe
    Should Be True          ${f_exist}
    sendKeys                enter 1

I uninstall the Timedoctor application
    runFile                 ${user_path}/Time Doctor 2/uninstall.exe
    Sleep                   ${app_delay}
    window_activate         Question
    sendKeys                enter 1
    ${f_exist} =            check_file_not_exist    ${user_path}/Time Doctor 2/timedoctor2.exe
    Should Be True          ${f_exist}
    sendKeys                enter 1

I log in to Timedoctor application
    runFile                 ${user_path}/Time Doctor 2/timedoctor2.exe
    Sleep                   ${app_delay}
    window_activate         Time Doctor 2
    mouse_move              135 55 1
    mouse_click             1
    mouse_move              155 75 1
    mouse_click             1
    sendKeys                y 30
    window_activate         Time Doctor 2
    ${Email} =              get_set_config      DEFAULT email
    key_write               ${Email}    
    Sleep                   1s
    sendKeys                tab 1
    key_write               123456
    Sleep                   1s
    sendKeys                enter 5
    sendKeys                tab 1
    sendKeys                tab 1
    sendKeys                tab 1
    sendKeys                tab 1
    sendKeys                tab 1           
    sendKeys                enter 1    

I download Timedoctor application
    downloadFile    https://s3.amazonaws.com/sfproc-downloads/3.0.52/windows/bitrock/timedoctor2-setup-3.0.52-windows.exe    installer/timedoctor2-setup-3.0.52-windows.exe

I put OS into sleep mode for
    [Arguments]     ${args}
    osSleep         ${args}

I wait for
    [Arguments]     ${args}
    Sleep           ${args}

I open new tab and navigate to
    [Arguments]     ${args}
    Execute Javascript   window.open('${args}');

I open the application  
    [Arguments]     ${args}
    runFile         ${args}

I disable the network connection
    runFileWait         ipconfig /release
    I navigate page     https://api2.timedoctor.com
    Page Should Contain  This site can’t be reached
    Close Browser

I restore the network connection
    runFileWait     ipconfig /renew

I navigate page
    [Arguments]     ${args}
    Open Browser    ${args}    ${Browser}

I close the browser
    Close Browser
