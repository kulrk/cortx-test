*** Settings ***
Documentation  This is the common resources file containing common keywords
Library  SeleniumLibrary    screenshot_root_directory=reports/screenshots
Library  String
Library  DateTime
Library    Collections
Variables  common_variables.py
Variables  element_locators.py


*** Keywords ***
Log To Console And Report
    [Documentation]  This Keyword is for logging the same string to console and report.
    [Arguments]  ${log_message}
    log  ${log_message}
    Log To Console  ${\n}${log_message}

Navigate To Page
    [Documentation]  This Keyword is for naviagting to certain page
    [Arguments]  ${page_name}  ${sub_page}=False
    log to console and report  Navigating to ${page_name}
    Click Element  ${${page_name}}
    Sleep  1s
    ${value}=  Convert To Boolean  ${sub_page}
    Run Keyword If  ${value}
    ...  Click Element  ${${sub_page}}

Read Table Data
    [Documentation]  This Keyword is for reading the data from the html table and it returns the data in list format.
    [Arguments]  ${table_element}
    @{table_data}=    Create List
    @{table_elements}=  Get WebElements  ${table_element}
    sleep  2s
    FOR  ${elements}  IN  @{table_elements}
            ${text}=    Get Text    ${elements}
            Append To List  ${table_data}  ${text}
    END
    Log To Console And Report   ${table_data}
    [Return]   @{table_data}

Action On The Table Element
    [Documentation]  This Keyword is for performing actions like edit/delete on perticualr user/element in html table.
    [Arguments]  ${Element_for_action}  ${USER_NAME}
    sleep  2s
    Log To Console And Report   ${Element_for_action}
    ${Action_element} =  Format String  ${Element_for_action}  ${USER_NAME}
    Log To Console And Report   ${Action_element}
    ${table_elements}=  Get WebElement  ${Action_element}
    sleep  2s
    click element   ${table_elements}
    sleep  2s

Generate New User Name
    [Documentation]  Functionlity to generate new user name
    ${str}=  Get Current Date
    ${str}=  Replace String  ${str}  :  ${EMPTY}
    ${str}=  Replace String  ${str}  .  ${EMPTY}
    ${str}=  Replace String  ${str}  -  ${EMPTY}
    ${str}=  Replace String  ${str}  ${space}  ${EMPTY}
    ${str}=  catenate  SEPARATOR=  testuser  ${str}
    [Return]  ${str}

Generate New User Email
    [Documentation]  Functionlity to generate new user email
    ${name}=  Generate New User Name
    ${email}=  catenate  SEPARATOR=  ${name}  @seagate.com
    [Return]  ${email}

Generate New Password
    [Documentation]  Functionlity to generate valid password
    ${upper_case}=  Generate Random String  2  [UPPER]
    ${lower_case}=  Generate Random String  2  [LOWER]
    ${numbers}=  Generate Random String  2  [NUMBERS]
    ${special_char}=  Generate random string    2    !@#$%^&*()
    ${password}=  Catenate  SEPARATOR=  ${upper_case}  ${lower_case}  ${numbers}  ${special_char}
    Log To Console And Report  ${password}
    [Return]  ${password}

Verify message
    [Documentation]  This keyword verifies error messages for provided element with expected message.
    [Arguments]  ${element_locator}  ${message_to_verify}
    wait until element is visible  ${${element_locator}}  timeout=10
    ${msg_from_gui}=  get text  ${${element_locator}}
    Log To Console And Report  message from guI is ${msg_from_gui}
    should be equal  ${msg_from_gui}  ${message_to_verify}