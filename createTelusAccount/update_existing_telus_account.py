import sys

sys.path.append('D:\QA\createTelusAccount')
import telus_rest_api

def updateExistingTelusAccount(ENV, brandID, accountID, userMailboxID, emailAddress, numberOfAssignedUsers, numberOfUnassignUsers, deviceID, DIDType):
    if accountID != '':
        # assign device or phone number for existing user
        # print('test mailbobx id: ' + str(userMailboxID))
        if int(userMailboxID) != 0  and deviceID != 'none':
            if telus_rest_api.getExtensionInfo(ENV, accountID, userMailboxID)[1] == 'Unassigned':
                telus_rest_api.addDeviceForUnaassignedUser(ENV, accountID, userMailboxID, int(deviceID))
            else:
                telus_rest_api.addDeviceForAassignedUser(ENV, accountID, userMailboxID, int(deviceID))
            # print('assign device type=' + str(deviceID) + ' for user mailboxid = ' + str(userMailboxID))
        if  int(userMailboxID) != 0  and (DIDType != 'none'):
            if telus_rest_api.getExtensionInfo(ENV, accountID, userMailboxID)[1] == 'Unassigned':
                telus_rest_api.addPhoneNumberForUnassignedUser(ENV, brandID, accountID, telus_rest_api.getExtensionInfo(ENV, accountID, userMailboxID)[0], DIDType)
            else:
                telus_rest_api.addPhoneNumberForAassignedUser(ENV, brandID, accountID, userMailboxID, DIDType)
            # print('assign phone number for user mailboxid = ' + str(userMailboxID))
        # add assign user or unassign user for account
        for i in range(1, int(numberOfAssignedUsers)+1):
            assignUserMailboxID = telus_rest_api.addAssignUser(ENV, accountID, emailAddress)
            if deviceID != 'none':
                telus_rest_api.addDeviceForAassignedUser(ENV, accountID, assignUserMailboxID, int(deviceID))
            if DIDType != 'none':
                telus_rest_api.addPhoneNumberForAassignedUser(ENV, brandID, accountID, assignUserMailboxID,DIDType)
        for j in range(1, int(numberOfUnassignUsers)+1):
            unassignUserIDs = telus_rest_api.addUnassignUser(ENV, accountID)
            if deviceID != 'none':
                telus_rest_api.addDeviceForUnaassignedUser(ENV, accountID, unassignUserIDs[0], int(deviceID))
            if DIDType != 'none':
                telus_rest_api.addPhoneNumberForUnassignedUser(ENV, brandID, accountID, unassignUserIDs[1],DIDType)
				
updateExistingTelusAccount(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])