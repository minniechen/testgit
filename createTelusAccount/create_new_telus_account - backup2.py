import sys

sys.path.append('D:\QA\createTelusAccount')
import telus_rest_api

def createNewTelusAccount(ENV, accountStatus, brandID, tierID, languageID, emailAddress, numberOfAssignedUsers, numberOfUnassignUsers, deviceID, DIDType):
    # Create telus account
    accountMailboxID = telus_rest_api.createTelusAccount(ENV, brandID, tierID, languageID, emailAddress)
    if accountStatus.lower() == 'activated':
        telus_rest_api.confirmAccount(ENV, accountMailboxID)
    else:
        telus_rest_api.unConfirmAccount(ENV, accountMailboxID)

    for i in range(1, int(numberOfAssignedUsers)+1):
        assignUserMailboxID = telus_rest_api.addAssignUser(ENV, accountMailboxID, emailAddress)
        if deviceID != 'none':
            telus_rest_api.addDeviceForAassignedUser(ENV, accountMailboxID, assignUserMailboxID, deviceID)
        if DIDType != 'none':
            telus_rest_api.addPhoneNumberForAassignedUser(ENV, brandID, accountMailboxID, assignUserMailboxID, DIDType)

    for j in range(1, int(numberOfUnassignUsers)+1):
        unassignUserIDs = telus_rest_api.addUnassignUser(ENV, accountMailboxID)
        if deviceID != 'none':
            telus_rest_api.addDeviceForUnaassignedUser(ENV, accountMailboxID, unassignUserIDs[0], deviceID)
        if DIDType != 'none':
            telus_rest_api.addPhoneNumberForUnassignedUser(ENV, brandID, accountMailboxID, unassignUserIDs[1], DIDType)


#createNewTelusAccount('http://fre01-p01-pas01:8080', 'activated', 7310,7316,1033,'tt@ringcentral.com',1,1,19,'local')
createNewTelusAccount(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])