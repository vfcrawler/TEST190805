import requests

# 格式要求严格 去空格换行....
str_cookies = '_zap=54fd98ed-eeb3-4962-a477-1dd8fd8257d6;_xsrf=0bb67ad9-9527-4749-a8a4-b3a7f662e66d;d_c0="AICjv_Mc7w-PTg_iIc_Q5TRn62SL6L_hsSc=|1566524645";l_n_c=1;l_cap_id="MjUzNjAxMjNjZDA4NGYxYWJiODRiYzg1ZTk2OGRkY2M=|1566525858|e1f34af7d1a0f88263214b4deb27c656e15e49a1";r_cap_id="NzU2NzFiNjU4MWZhNDFmZGEwY2MyN2MzMzBiMmVlNWM=|1566525858|b2e0b64441160d933bb87ff8b4b62ee350848196";cap_id="MWMzYzIxM2Q5MTFkNDNmOTg0YTc3NzNjNmJjNGNmMTI=|1566525858|7f154244b89fabb9fad9756730b91be4c620f123";n_c=1;capsion_ticket="2|1:0|10:1566540910|14:capsion_ticket|44:MWNkNjNlYzAzMGQxNDY3NThhZmYyMGY4NTQ5ODcyZjk=|ca2c00f03042cdcacaacd137505ad60e71330a9170d76428ff627ff04fefec05";z_c0="2|1:0|10:1566540938|4:z_c0|92:Mi4xalFXSEJBQUFBQUFBZ0tPXzh4enZEeVlBQUFCZ0FsVk5pdEpNWGdDVi04U0FfWERpdXh2SmlMNDhUOWZRNlU3M3F3|be1a86fb4f507e95796d73e5641e24651fd11be1b63f8ba03abad2d2f5b2d7eb";unlock_ticket="AGBClzRtgwsmAAAAYAJVTZKLX10OvapKNjDZD1-ZRBuKVWE3VmvWXQ==";tst=r'

headers = {
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookies': str_cookies
}

res = requests.get('https://www.zhihu.com',headers=headers,verify=False)

print(res.text)


