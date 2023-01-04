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
    ${response}=  DELETE On Session  mysession  /binaryFile_delete/1  headers=${headers}
    Status Should Be  200  ${response}

Test update bin file
    Create Session  mysession  ${base_url}
    ${header}  create dictionary  Content-Type=application/json
    ${response}=  PUT On Session  mysession  /binaryFile_move/2  data={"father":"robotdir"}  headers=${header}
    Status Should Be  200  ${response}

Test buf file page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /bufFile
    Status Should Be  200  ${response}
    should be equal as strings  ${response.content}  This is buf files pages
Test all buf page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /bufFiles
    Status Should Be  200  ${response}
    #log to console  ${response.content}
    ${file_name}=  Get Value From Json  ${response.json()}  bufFiles
    log to console  ${file_name}


Test get buf file
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /bufFile_read/1
    Status Should Be  200  ${response}

Test create buf file
    ${header}  create dictionary  Content-Type=${CONTENT_TYPE}
    Create Session  mysession  ${base_url}
    ${response}=  POST On Session  mysession  /bufFile_create/bufFiles  data={"fileName":"testro"}  headers=${header}
    Status Should Be  201  ${response}
    ${getHeaderValue}=  Get From Dictionary  ${response.headers}  Content-Type
    Should be equal  ${getHeaderValue}  application/json

Test delete buf file
    Create Session  mysession  ${base_url}
    ${headers}  create dictionary  Content-Type=application/json
    ${response}=  DELETE On Session  mysession  /bufFile_delete/1  headers=${headers}
    Status Should Be  302  ${response}

Test move buf file
    Create Session  mysession  ${base_url}
    ${header}  create dictionary  Content-Type=application/json
    ${response}=  PUT On Session  mysession  /bufFile_move/2  data={"father":"robotdirbuf"}  headers=${header}
    Status Should Be  200  ${response}

Test consume and push buf file
    Create Session  mysession  ${base_url}
    ${header}  create dictionary  Content-Type=application/json
    ${response}=  PUT On Session  mysession  /bufFile_push/2  data={"maxSize":"22"}  headers=${header}
    Status Should Be  200  ${response}

Test log file page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /logFile
    Status Should Be  200  ${response}
    should be equal as strings  ${response.content}  This is log files pages

Test all log page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /logFiles
    Status Should Be  200  ${response}
    #log to console  ${response.content}
    ${file_name}=  Get Value From Json  ${response.json()}  logFiles
    log to console  ${file_name}


Test get log file
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /logFile_read/1
    Status Should Be  200  ${response}

Test create log file
    ${header}  create dictionary  Content-Type=${CONTENT_TYPE}
    Create Session  mysession  ${base_url}
    ${response}=  POST On Session  mysession  /logFile_create/logFiles  data={"fileName":"testro"}  headers=${header}
    Status Should Be  201  ${response}
    ${getHeaderValue}=  Get From Dictionary  ${response.headers}  Content-Type
    Should be equal  ${getHeaderValue}  application/json

Test delete log file
    Create Session  mysession  ${base_url}
    ${headers}  create dictionary  Content-Type=application/json
    ${response}=  DELETE On Session  mysession  /logFile_delete/1  headers=${headers}
    Status Should Be  200  ${response}

Test move log file
    Create Session  mysession  ${base_url}
    ${header}  create dictionary  Content-Type=application/json
    ${response}=  PUT On Session  mysession  /logFile_move/2  data={"father":"robotdirlog"}  headers=${header}
    Status Should Be  200  ${response}

Test append log file
    Create Session  mysession  ${base_url}
    ${header}  create dictionary  Content-Type=application/json
    ${response}=  PUT On Session  mysession  /logFile_append/2  data={"info":"infor"}  headers=${header}
    Status Should Be  200  ${response}

Test dir page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /directory
    Status Should Be  200  ${response}
    should be equal as strings  ${response.content}  This is directory pages

Test all dir page
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /directories
    Status Should Be  200  ${response}
    #log to console  ${response.content}
    ${file_name}=  Get Value From Json  ${response.json()}  directories
    log to console  ${file_name}


Test get dir
    Create Session  mysession  ${base_url}
    ${response}=  GET On Session  mysession  /dir_read/1
    Status Should Be  200  ${response}

Test create dir
    ${header}  create dictionary  Content-Type=${CONTENT_TYPE}
    Create Session  mysession  ${base_url}
    ${response}=  POST On Session  mysession  /dir_create/directories  data={"dirName":"testro"}  headers=${header}
    Status Should Be  201  ${response}
    ${getHeaderValue}=  Get From Dictionary  ${response.headers}  Content-Type
    Should be equal  ${getHeaderValue}  application/json

Test delete dir
    Create Session  mysession  ${base_url}
    ${headers}  create dictionary  Content-Type=application/json
    ${response}=  DELETE On Session  mysession  /dir_delete/1  headers=${headers}
    Status Should Be  200  ${response}

Test move dir
    Create Session  mysession  ${base_url}
    ${header}  create dictionary  Content-Type=application/json
    ${response}=  PUT On Session  mysession  /dir_move/2  data={"father":"robotdir"}  headers=${header}
    Status Should Be  200  ${response}




*** Keywords ***
