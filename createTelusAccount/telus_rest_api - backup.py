import requests
import json
import time
import random
import sys

def getBrandToken(ENV, brandID):
    baseUrl = ENV + "/restapi/oauth/token"
    testKeyEndcode = 'Basic QUFDNTRhOGE5ZDRmYzIyNzQwQTdGMEIyZWYwQWYyMDc3ZGYzOWNlNDJGREFCOTAwZjM4ODAyNkI0MTJlYTg0RDpENWQwNkY2NEMwOGU5ODZiNDQxQUU0YjAxY2VjZDgzZWYxNjAzRTQ5MDVlMGM3N2Q0ZDdlYzUxOWZjQ0IxOEUw'
    stageKeyEndcode = 'Basic QUFDNTRhOGE5ZDRmYzIyNzQwQTdGMEIyZWYwQWYyMDc3ZGYzOWNlNDJGREFCOTAwZjM4ODAyNkI0MTJlYTg0RDpENWQwNkY2NEMwOGU5ODZiNDQxQUU0YjAxY2VjZDgzZWYxNjAzRTQ5MDVlMGM3N2Q0ZDdlYzUxOWZjQ0IxOEUw'
    proKeyEncode = 'Basic ZGYxNjZBRTM4MDliQzczN2ZlNTM1NzNkYjQzNDhiYTYwQkM5MTQ5N0REMTdEQkM2NWFkOTY1ZmI4MjRFMjYxNTozMTlkNzg2NjU2MjMwNTRiMTEzQzcwRTQ0ZjIzMGEzMUMyRTI5N0FFNjExMjM4NkUzRTY4RTExNUYzOTQ2RDZB'
    if ENV.lower().find('uat'):
        keyEndcode = stageKeyEndcode
    elif ENV.lower().find('api.ringcentral.com'):
        keyEndcode = proKeyEncode
    else:
        keyEndcode = testKeyEndcode

    payload = {'brand_id': brandID, 'grant_type': 'client_credentials', 'access_token_ttl': 7200}
    headers={'Authorization' : keyEndcode, 'Accept' : 'application/json'}
    # getBrandIDRequest = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
    getBrandTokenResponse = requests.post(baseUrl, data=payload, headers=headers)
    # print(getBrandTokenResponse.text)
    data = getBrandTokenResponse.json()
    if getBrandTokenResponse.ok:
        access_brand_token = data['token_type'] + ' ' + data['access_token']
        # print(access_brand_token)
    else:
        print('Failed to get brand access token, get brand token response: ' + str(data))
    return (access_brand_token)


def getAccountToken(ENV, accountMailboxID):
    baseUrl = ENV + "/restapi/oauth/token"
    testKeyEndcode = 'Basic QUFDNTRhOGE5ZDRmYzIyNzQwQTdGMEIyZWYwQWYyMDc3ZGYzOWNlNDJGREFCOTAwZjM4ODAyNkI0MTJlYTg0RDpENWQwNkY2NEMwOGU5ODZiNDQxQUU0YjAxY2VjZDgzZWYxNjAzRTQ5MDVlMGM3N2Q0ZDdlYzUxOWZjQ0IxOEUw'
    stageKeyEndcode = 'Basic QUFDNTRhOGE5ZDRmYzIyNzQwQTdGMEIyZWYwQWYyMDc3ZGYzOWNlNDJGREFCOTAwZjM4ODAyNkI0MTJlYTg0RDpENWQwNkY2NEMwOGU5ODZiNDQxQUU0YjAxY2VjZDgzZWYxNjAzRTQ5MDVlMGM3N2Q0ZDdlYzUxOWZjQ0IxOEUw'
    proKeyEncode = 'Basic ZGYxNjZBRTM4MDliQzczN2ZlNTM1NzNkYjQzNDhiYTYwQkM5MTQ5N0REMTdEQkM2NWFkOTY1ZmI4MjRFMjYxNTozMTlkNzg2NjU2MjMwNTRiMTEzQzcwRTQ0ZjIzMGEzMUMyRTI5N0FFNjExMjM4NkUzRTY4RTExNUYzOTQ2RDZB'
    if ENV.lower().find('uat'):
        keyEndcode = stageKeyEndcode
    elif ENV.lower().find('api.ringcentral.com'):
        keyEndcode = proKeyEncode
    else:
        keyEndcode = testKeyEndcode

    payload = {'account_id': accountMailboxID, 'grant_type': 'client_credentials', 'access_token_ttl': 7200}
    headers = {'Authorization': keyEndcode, 'Accept': 'application/json'}
    # getBrandIDRequest = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
    getBrandTokenResponse = requests.post(baseUrl, data=payload, headers=headers)
    # print(getBrandTokenResponse.text)
    data = getBrandTokenResponse.json()
    if getBrandTokenResponse.ok:
        access_account_token = data['token_type'] + ' ' + data['access_token']
        # print('get account token:' + access_account_token)
    else:
        print('Failed to get account access token, get Brand token response: ' + str(data))
    return (access_account_token)


def getLocalNumbers(ENV, brandID):
    baseUrl = ENV + '/restapi/v1.0/number-pool/lookup'
    npa = [780, 403, 587,236, 250, 604, 778, 204, 431, 506, 709, 902, 226, 418, 438, 450, 514, 579, 581, 819, 873]
    payload = {'brandId': brandID, 'paymentType': 'Local', 'countryId': 39, 'perPage': 10, 'npa': npa[0]}
    headers = {'Authorization': getBrandToken(ENV, brandID), 'Content-Type': 'application/json'}
    getLocalNumbersResponse = requests.post(baseUrl, params=payload, headers=headers)
    # print(getLocalNumbersResponse.text)
    data = getLocalNumbersResponse.json()
    # print("test npa: " + str(npa[1]))
    i = 1
    if getLocalNumbersResponse.ok:
        rows = data['records']
        isLocalExist = len(data['records'])
        # print('test records rows: ' + str(isLocalExist))
        while isLocalExist == 0:
            payload = {'brandId': brandID, 'paymentType': 'Local', 'countryId': 39, 'perPage': 10, 'npa': npa[i]}
            headers = {'Authorization': getBrandToken(ENV, brandID), 'Content-Type': 'application/json'}
            getLocalNumbersResponse = requests.post(baseUrl, params=payload, headers=headers)
            data = getLocalNumbersResponse.json()
            rows = data['records']
            i = i + 1
            isLocalExist = len(data['records'])
            if i>= len(npa):
                print("No found local number in number pool")
                break

            # print("test while cycle: " + str(isLocalExist))
        if i< len(npa):
            localNumbers = []
            for row in rows:
                phoneNumbers = row['phoneNumber']
                localNumbers.append(phoneNumbers)
            # print ('0:'+ localNumbers[0] + '    1:' + localNumbers[1] + '    2:' + localNumbers[2])
        else:
            print('Failed to get local number, get local number response: ' + str(data))
    return localNumbers


def getTFNumbers(ENV, brandID):
    baseUrl = ENV + '/restapi/v1.0/number-pool/lookup'
    npa = [800, 844, 855, 866, 877, 888]
    payload = {'brandId': brandID, 'paymentType': 'TollFree', 'countryId': 39, 'perPage': 10, 'npa': npa[0]}
    headers = {'Authorization': getBrandToken(ENV, brandID), 'Content-Type': 'application/json'}
    getLocalNumbersResponse = requests.post(baseUrl, params=payload, headers=headers)
    # print(getLocalNumbersResponse.text)
    data = getLocalNumbersResponse.json()
    i = 1
    if getLocalNumbersResponse.ok:
        rows = data['records']
        isLocalExist = len(data['records'])
        # print('test records rows: ' + str(isLocalExist))
        while isLocalExist == 0:
            payload = {'brandId': brandID, 'paymentType': 'TollFree', 'countryId': 39, 'perPage': 10, 'npa': npa[i]}
            headers = {'Authorization': getBrandToken(ENV, brandID), 'Content-Type': 'application/json'}
            getLocalNumbersResponse = requests.post(baseUrl, params=payload, headers=headers)
            data = getLocalNumbersResponse.json()
            rows = data['records']
            i = i + 1
            isLocalExist = len(data['records'])
            if i>= len(npa):
                print("No found toll free number in number pool")
                break
        if i < len(npa):
            rows = data['records']
            TFNumbers = []
            for row in rows:
                phoneNumbers = row['phoneNumber']
                TFNumbers.append(phoneNumbers)
            # print ('0:'+ TFNumbers[0] + '    1:' + TFNumbers[1] + '    2:' + TFNumbers[2])
        else:
            print('Failed to get toll free number, get toll free number response: ' + str(data))

    return TFNumbers

def getExtensionInfo(ENV, accountMailboxID, extensionMailboxID):
    baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID) + '/extension/'+ str(extensionMailboxID)
    # payload = {'extensionId': extensionMailboxID}
    headers = {'Authorization': getAccountToken(ENV, accountMailboxID)}
    getExtensionInfoResponse = requests.get(baseUrl, headers=headers)
    data = getExtensionInfoResponse.json()
    # print(getExtensionInfoResponse.text)
    if getExtensionInfoResponse.ok:
        extensionType = data['status']
        extensionPartnerID = data['partnerId']
        extensionInfo =[extensionPartnerID, extensionType]
        # print('get extension type: ' + extensionType)
    else:
        print('Failed to get account access token, get Brand token response: ' + str(data))
    return (extensionInfo)


def createTelusAccount(ENV, brandID, tierID, languageID, emailAddress):
    baseUrl = ENV + '/restapi/v1.0/account'
    mainNumber = getLocalNumbers(ENV, brandID)[0]
    dateTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    emailAddress = emailAddress.split('@')
    emailAddress = emailAddress[0] + '+' + dateTime + str(random.randint(1, 3)) + '@' + emailAddress[1]
    # print('time: ' + dateTime)
    headers = {'Authorization': getBrandToken(ENV, brandID), 'Content-Type': 'application/json'}
    payload ={
        "serviceInfo": {
            "brand": {
                "id": brandID
            },
            "targetServicePlan": {
                "id": tierID
            }
        },
        "mainNumber": mainNumber,
        "operator": {
            "regionalSettings": {
                "language": {
                    "id": languageID
                },
                "timezone": {
                    "id": "2"
                }
            },
            "contact": {
                "email": emailAddress,
                "firstName": "telus",
                "lastName": "tier-" + str(tierID) ,
                "businessPhone": "+16509240016",
                "businessAddress": {
                    "street": "546 Main St",
                    "city": "Arrakin",
                    "state": "CA",
                    "country": "US",
                    "zip": "97855"
                },
                "company": "The Great House of Atreides"
            },
            "type": "DigitalUser",
            "partnerId": "SID00"+dateTime
        },
        "partnerId": "BAN00"+dateTime
    }
    getCreateTelusAccountResponse = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
    print(getCreateTelusAccountResponse.text)
    data = getCreateTelusAccountResponse.json()
    if getCreateTelusAccountResponse.ok:
        mainNumberMailboxID = str(data['id'])
        mainNumber = str(data['mainNumber'])
        print('Telus account is created, main number: '+ mainNumber + '\r\n' + 'main number mailbox id: ' + mainNumberMailboxID)
        return mainNumberMailboxID
    else:
        print('Telus account is not created, Create Account API response:' + str(data))


def unConfirmAccount(ENV, brandID, accountMailboxID):
    baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID)
    headers = {'Authorization': getAccountToken(ENV,accountMailboxID), 'Content-Type': 'application/json'}
    payload ={
        "status": "Unconfirmed",
        "transition": {
            "sendConfirmationEmail": "true"
        }
    }
    getUnconfirmAccountResponse = requests.put(baseUrl, data=json.dumps(payload), headers=headers)
    print(getUnconfirmAccountResponse.text)
    data = getUnconfirmAccountResponse.json()
    if getUnconfirmAccountResponse.ok:
        mainNumber = str(data['mainNumber'])
        print('telus account has been activated but uncofirmed status: ' + mainNumber)
    else:
        print('Failed to activate telus account' + str(data))

def confirmAccount(ENV, accountMailboxID):
    baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID)
    headers = {'Authorization': getAccountToken(ENV,accountMailboxID), 'Content-Type': 'application/json'}
    payload ={
        "status":"Confirmed",
        "transition":{
            "sendConfirmationEmail":"true",
            "sendWelcomeEmail":"false",
            "shipDevices":"true"
        }
    }
    getConfirmAccountResponse = requests.put(baseUrl, data=json.dumps(payload), headers=headers)
    print(getConfirmAccountResponse.text)
    data = getConfirmAccountResponse.json()
    if getConfirmAccountResponse.ok:
        mainNumber = str(data['mainNumber'])
        print('telus account is created with active status: ' + mainNumber)
    else:
        print('Failed to active telus account' + str(data))


def addAssignUser(ENV, accountMailboxID, emailAddress):
    baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID) + '/extension'
    dateTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    emailAddress = emailAddress.split('@')
    emailAddress = emailAddress[0] + '+' + dateTime  + str(random.randint(1,3)) + '@' + emailAddress[1]
    # print('time: ' + dateTime)
    headers = {'Authorization': getAccountToken(ENV, accountMailboxID), 'Content-Type': 'application/json'}
    payload ={
        "partnerId":"SID" + dateTime,
        "type":"DigitalUser",
        "contact":{
            "email":emailAddress,
            "firstName":"firstname",
            "lastName":"ln" + str(dateTime),
            "businessAddress":{
                "street":"SPEERS RD",
                "city":"OAKVILLE",
                "state":"ON",
                "country":"CAN",
                "zip":"L6L 2X4"
            }
        }
    }
    getAssignUserResponse = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
    print(getAssignUserResponse.text)
    data = getAssignUserResponse.json()
    if getAssignUserResponse.ok:
        assignUserMailboxID = str(data['id'])
        assignUserExntesionNumber = str(data['extensionNumber'])
        print('New assign user is created, extension number: '+ assignUserExntesionNumber + '                 ' + 'assign user mailbox id: ' + assignUserMailboxID)
        return assignUserMailboxID
    else:
        print('New assign user is not created, new assign user extension API response:' + str(data))


def addUnassignUser(ENV, accountMailboxID):
    baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID) + '/extension'
    dateTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    # print('time: ' + dateTime)
    headers = {'Authorization': getAccountToken(ENV,accountMailboxID), 'Content-Type': 'application/json'}
    payload ={
        "type": "DigitalUser",
        "status": "Unassigned",
        "partnerId": "b" + dateTime + str(random.randint(5, 10))
    }
    getUnassignUserResponse = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
    print(getUnassignUserResponse.text)
    data = getUnassignUserResponse.json()
    if getUnassignUserResponse.ok:
        unassignUserMailboxID = str(data['id'])
        unassignUserParterID = str(data['partnerId'])
        print('New unassign user is created, mailbox id: ' + unassignUserMailboxID)
        print('New unassign user is created, partner id: ' + unassignUserParterID)
        return (unassignUserMailboxID, unassignUserParterID)
    else:
        print('New assign user is not created, unassign user API response:' + str(data))


def addPhoneNumberForAassignedUser(ENV, brandID, accountMailboxID, extensionMailboxID, DIDType):
    baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID) + '/phone-number'
    dateTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    # print('time: ' + dateTime)
    if DIDType.lower() == 'tollfree' or DIDType == 'tf':
        phoneNumber = getTFNumbers(ENV, brandID)[0]
    else:
        phoneNumber = getLocalNumbers(ENV, brandID)[0]

    headers = {'Authorization': getAccountToken(ENV, accountMailboxID), 'Content-Type': 'application/json'}
    payload ={
        "phoneNumber": phoneNumber,
        "type":"VoiceFax",
        "extension":{
            "id":extensionMailboxID
        }
    }
    getAddPhoneNumberForAassignedUser = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
    print(getAddPhoneNumberForAassignedUser.text)
    data = getAddPhoneNumberForAassignedUser.json()
    if getAddPhoneNumberForAassignedUser.ok:
        phoneNumber = str(data['phoneNumber'])
        print('Assign phone number:   '+ phoneNumber + '   to user mailbox id = ' + str(extensionMailboxID))
    else:
        print('Failed to add phone number for the user mailbox id = '+ extensionMailboxID)


def addPhoneNumberForUnassignedUser(ENV, brandID, accountMailboxID, partnerId, DIDType):
    baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID) + '/phone-number'
    if DIDType.lower() == 'tollfree' or DIDType.lower() == 'tf':
        phoneNumber = getTFNumbers(ENV, brandID)[0]
    else:
        phoneNumber = getLocalNumbers(ENV, brandID)[0]

    headers = {'Authorization': getAccountToken(ENV, accountMailboxID), 'Content-Type': 'application/json'}
    payload ={
        "phoneNumber": phoneNumber,
        "type": "VoiceFax",
        "extension": {
            "partnerId": partnerId
        }
    }
    getAddPhoneNumberForUnassignedUser = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
    print(getAddPhoneNumberForUnassignedUser.text)
    data = getAddPhoneNumberForUnassignedUser.json()
    if getAddPhoneNumberForUnassignedUser.ok:
        phoneNumber = str(data['phoneNumber'])
        print('Assign phone number:   '+ phoneNumber + '   to unassign user partnerid='+ str(partnerId))
    else:
        print('Failed to add phone number for unassign user parterId = '+ str(partnerId))


def addDeviceForAassignedUser(ENV, accountMailboxID, extensionMailboxID, deviceID):
    baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID) + '/order'
    dateTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    # print('time: ' + dateTime)
    headers = {'Authorization': getAccountToken(ENV, accountMailboxID), 'Content-Type': 'application/json'}
    if deviceID == -1:
        payload ={
           "devices":[
              {
                 "type":"SoftPhone",
                 "name":"John Smith's SoftPhone",
                 "extension":{
                    "id":extensionMailboxID
                 },
                 "emergencyServiceAddress":{
                    "street":"546 Main Elm St, #320",
                    "city":"Arrakin",
                    "state":"CA",
                    "country":"US",
                    "zip":"97855",
                    "customerName":"John Smith"
                 },
                 "shipping":{
                    "method":{
                       "id":"1"
                    }
                 }
              }
           ]
        }
    elif deviceID == 0:
        payload ={
            "devices": [
                {
                    "type": "OtherPhone",
                    "name": "Existing phone",
                    "extension": {
                        "id": extensionMailboxID
                    },
                    "emergencyServiceAddress": {
                        "street": "546 Main Elm St, #322",
                        "city": "Arrakin",
                        "state": "CA",
                        "country": "US",
                        "zip": "97855",
                        "customerName": "Helen Star"
                    },
                    "shipping": {
                        "method": {
                            "id": "1"
                        }
                    }
                }
            ]
        }
    else:
        payload = {
            "devices": [
                {
                    "type": "HardPhone",
                    "model": {
                        "id": deviceID
                    },
                    "name": "deviceID" + str(deviceID),
                    "extension": {
                        "id": extensionMailboxID
                    },
                    "emergencyServiceAddress": {
                        "street": "546 Main Elm St, #320",
                        "city": "Arrakin",
                        "state": "CA",
                        "country": "US",
                        "zip": "97855",
                        "customerName": "John Smith"
                    },
                    "shipping": {
                        "address": {
                            "street": "5120 Broadway ave",
                            "city": "Redwood City",
                            "state": "CA",
                            "country": "US",
                            "zip": "95302",
                            "customerName": "Acme Inc."
                        },
                        "method": {
                            "id": "2"
                        }
                    }
                }
            ]
        }

    getAddDeviceForAassignedUser = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
    print(getAddDeviceForAassignedUser.text)
    data = getAddDeviceForAassignedUser.json()
    if getAddDeviceForAassignedUser.ok:
        # phoneName = str(data['devices']['model'])
        print('Device is added user mailbox id = ' + str(extensionMailboxID))
    else:
        print('Failed to add device for the user mailbox id = '+ str(extensionMailboxID))

def addDeviceForUnaassignedUser(ENV, accountMailboxID, extensionMailboxID, deviceID):
        baseUrl = ENV + '/restapi/v1.0/account/' + str(accountMailboxID) + '/order'
        headers = {'Authorization': getAccountToken(ENV, accountMailboxID), 'Content-Type': 'application/json'}
        if deviceID == -1:
            payload ={
               "devices":[
                  {
                     "type":"SoftPhone",
                     "name":"SoftPhone test",
                     "extension":{
                        "id":extensionMailboxID
                     },
                     "shipping":{
                        "method":{
                           "id":"1"
                        }
                     }
                  }
               ]
            }
        elif deviceID == 0:
            payload ={
                "devices": [
                    {
                        "type": "OtherPhone",
                        "name": "Existing phone test",
                        "extension": {
                            "id": extensionMailboxID
                        },
                        "shipping": {
                            "method": {
                                "id": "1"
                            }
                        }
                    }
                ]
            }
        else:
            payload = {"devices":[
                    {
                        "type":"HardPhone",
                        "model":{
                            "id":deviceID
                        },
                        "name":"device id: " + str(deviceID),
                        "extension":{
                            "id":extensionMailboxID
                        },
                        "shipping":{
                            "address":{
                                "street":"5120 Broadway ave",
                                "city":"Redwood City",
                                "state":"CA",
                                "country":"US",
                                "zip":"95302",
                                "customerName":"Acme Inc."
                            },
                            "method":{
                                "id":"2"
                            }
                        }
                    }
                ]
            }
        getAddDeviceForUnaassignedUser = requests.post(baseUrl, data=json.dumps(payload), headers=headers)
        print(getAddDeviceForUnaassignedUser.text)
        # data = getAddDeviceForUnaassignedUser.json()
        if getAddDeviceForUnaassignedUser.ok:
            # phoneName = str(data['devices']['model'])
            print('Device is added unassign user mailbox id = ' + str(extensionMailboxID))
        else:
            print('Failed to add device for unasign user mailbox id = ' + str(extensionMailboxID))


# addPhoneNumberForUnassignedUser(sys.argv[1], 284990004, addUnassignUser(sys.argv[1], 284990004))
# addDeviceForAassignedUser(sys.argv[1], 284990004, 284990004)
# activateAccount(sys.argv[1], 280305005)
# getExtensionInfo('http://fre01-p01-pas01:8080', 7310, 326293003, 326295003)
# getAccountToken('http://fre01-p01-pas01:8080', 326293003)