import time
def test(emailaddress):
    emailaddress = emailaddress.split('@')
    emailAddress = emailaddress[0] + '+' + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '@' + emailaddress[1]
test('tracy.wei@ringcentral.com')
