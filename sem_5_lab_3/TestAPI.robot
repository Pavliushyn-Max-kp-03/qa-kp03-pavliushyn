*** Settings ***
Library  SeleniumLibrary
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Library  json

*** Variables ***
${base_url}  http://127.0.0.1:5000
${CONTENT_TYPE}  application/json

*** Test Cases ***
Test_main_page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /
    Status Should Be  200  ${response}  #Check Status as 200
    log to console  ${response.content}
    should be equal as strings  ${response.content}  This is lab2
Test_bin_page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /binaryFile
    Status Should Be  200  ${response}
    should be equal as strings  ${response.content}  This is binary files pages
Test all bin page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /binaryFiles
    Status Should Be  200  ${response}
    #log to console  ${response.content}
    ${file_name}=  Get Value From Json  ${response.json()}  binFiles
    log to console  ${file_name}
    #should be equal as strings  ${file_name}  [[{'father': None, 'fileName': 'binFile1', 'id': 1, 'info': 'info1'}, {'father': 'root', 'fileName': 'binFile2', 'id': 2, 'info': 'info2'}]]


Test get bin file
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /binaryFile_read/1
    Status Should Be  302  ${response}

Test create bin file
    ${header}  create dictionary  Content-Type=${CONTENT_TYPE}
    Create Session  mysession  ${base_url}
    ${response}=  POST On Session  mysession  /binaryFile_create/binaryFiles  data={"fileName":"testro"}  headers=${header}
    Status Should Be  201  ${response}
    ${getHeaderValue}=  Get From Dictionary  ${response.headers}  Content-Type
    Should be equal  ${getHeaderValue}  application/json

Test delete bin file
    Create Session  mysession  ${base_url}
    ${headers}  create dictionary  Content-Type=application/json
    ${response}=  DELETE On Session  mysession  /binaryFile_delete/4  headers=${headers}
    Status Should Be  200  ${response}

*** Keywords ***
