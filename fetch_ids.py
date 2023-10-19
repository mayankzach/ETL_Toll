import requests
import re

def fetch_id():
    cookies = {
    '_ga': 'GA1.1.1666050177.1697398760',
    '_ga_T9160NXX5D': 'GS1.1.1697398760.1.1.1697398775.0.0.0',
    'ASP.NET_SessionId': 'pboqwja12ksycyme2l2rrecj',}

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.1666050177.1697398760; _ga_T9160NXX5D=GS1.1.1697398760.1.1.1697398775.0.0.0; ASP.NET_SessionId=pboqwja12ksycyme2l2rrecj',
        'Origin': 'https://tis.nhai.gov.in',
        'Referer': 'https://tis.nhai.gov.in/tollplazasataglance.aspx?language=en',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',}

    data = "{'TollName':''}"

    response = requests.post('https://tis.nhai.gov.in/TollPlazaService.asmx/GetTollPlazaInfoGrid',
        cookies=cookies,
        headers=headers,
        data=data,)
    l=re.findall('javascript:TollPlazaPopup\(\d+\)',response.text)
    print(l)
    ids=[int(re.findall('\d+',s)[0]) for s in l]
    return ids

if __name__=="__main__":
    print(fetch_id())