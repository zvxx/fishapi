from flask import *
import requests
' تم تصليح'
import requests,time
def cokadada():
    cokANDdata=requests.get('https://login.aol.com/account/create',headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0','accept-language': 'en-US,en;q=0.9',})
    AS=cokANDdata.cookies.get_dict()['AS']
    A1=cokANDdata.cookies.get_dict()['A1']
    A3=cokANDdata.cookies.get_dict()['A3']
    A1S=cokANDdata.cookies.get_dict()['A1S']
    specData=cokANDdata.text.split('''name="attrSetIndex">
        <input type="hidden" value="''')[1].split(f'" name="specData">')[0]
    specId=cokANDdata.text.split('''name="browser-fp-data" id="browser-fp-data" value="" />
        <input type="hidden" value="''')[1].split(f'" name="specId">')[0]
    crumb=cokANDdata.text.split('''name="cacheStored">
        <input type="hidden" value="''')[1].split(f'" name="crumb">')[0]
    sessionIndex=cokANDdata.text.split('''"acrumb">
        <input type="hidden" value="''')[1].split(f'" name="sessionIndex">')[0]
    acrumb=cokANDdata.text.split('''name="crumb">
        <input type="hidden" value="''')[1].split(f'" name="acrumb">')[0]
    return AS,A1,A3,A1S,specData,specId,crumb,acrumb,sessionIndex
Qredes='قريديس'

app = Flask(__name__)
@app.route('/Qredes/email=<email>')

def checkaolav(email):
        if '@' in email:email=email.split('@')[0]
        tm1=str(time.time()).split('.')[0]
        AS,A1,A3,A1S,specData,specId,crumb,acrumb,sessionIndex=cokadada()
        cookies = {
    'gpp': 'DBAA',
    'gpp_sid': '-1',
    'A1':A1,
    'A3':A3,
    'A1S':A1S,
    '__gads': 'ID=c0M0fd00676f0ea1:T='+tm1+':RT='+tm1+':S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
    '__gpi': 'UID=00000cf0e8904e94:T='+tm1+':RT='+tm1+':S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
    'cmp': 't='+str(time.time()).split('.')[0]+'&j=0&u=1---',
    'AS': AS,
};headers = {
    'authority': 'login.aol.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://login.aol.com',
    'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}
        params = {
    'validateField': 'userId',
};data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=&lastName=&userid-domain=yahoo&userId={email}&password=&mm=&dd=&yyyy=&signup='



        response = requests.post('https://login.aol.com/account/module/create', params=params,  headers=headers, data=data,cookies=cookies).text
        if '{"errors":[{"name":"firstName","error":"FIELD_EMPTY"},{"name":"lastName","error":"FIELD_EMPTY"},{"name":"birthDate","error":"INVALID_BIRTHDATE"},{"name":"password","error":"FIELD_EMPTY"}]}' in response:return {'s':'good','by':'@Qredes','email':email+'@aol.com'}
        elif 'IDENTIFIER_NOT_AVAILABLE' or 'LENGTH_TOO_SHORT' or 'CANNOT_START_WITH_SPECIAL_CHARACTER_OR_NUMBER' or 'CANNOT_END_WITH_SPECIAL_CHARACTER' or 'SOME_SPECIAL_CHARACTERS_NOT_ALLOWED' in response:return {'s':'bad','by':'@Qredes','email':email+'@aol.com'}
        else:checkaolav(email)
