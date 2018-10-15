#-*- coding: UTF-8 -*-
import datetime
import pytz
import time
import json
import urllib.request
import uuid
from blog.until import errors
import hashlib
import urllib.parse

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

if (get_mac_address() == '00:16:3e:08:f3:70') :
    print(get_mac_address())
    MEDIAURL = 'https://ballgame.mobi/media/'
else:
    print(get_mac_address())
    MEDIAURL = 'http://127.0.0.1:8000/media/'

#微信小程序app-id/secret
WEICHAT_APPID='wxbb0350abfb3c20bf'
WEICHAT_SECRET= '8cc4562eb21cde20add802f93dd12e6a'



GENDER = (
        (1, '男'),
        (2, '女'),
        (0, '未知')
    )

UPDATA_USER_INFO = ['openid','avatar','city','country',
                    'nickname','gender','province'
                    ]

GET_USER_INFO = ['openid']

WE_CHAT_LOGIN = ['code']

CREATE_PHOTO = ['openid','game_subtitle','openid','ball_id','game_location','game_location_detail',
               'game_price','game_start_time','game_end_time','game_referee',
               'game_number','game_place_condition','number','lat','lng']

COMPTITIONS_PHOTO_LIST = ['openid','comptitions_id']

PHOTO_LIST = ['openid']

SEARCH_LIST = ['openid','name']

FILTER_LIST = ['openid']

PHOTO_COLLECT = ['openid','id','action']

PHOTO_LIKE = ['openid','id','action']

PHOTO_BUY = ['openid','id','action']
#时间戳转换
def timeStamp_to_date(timeStamp):
    dateArray = datetime.datetime.utcfromtimestamp(float(timeStamp))
    dateArray = dateArray + datetime.timedelta(hours=8)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime

def date_to_timeStamp(date):
    dtime = datetime.datetime.now()
    ans_time = time.mktime(dtime.timetuple())
    return ans_time

#请求返回数据整合
def response(status,code,msg = None,request_data = None):
    data = {}
    data['status'] = status
    data['code'] = code
    if msg is not None:
        data['message'] = msg
    if request_data is not None:
        data['data'] = request_data
    return data

def check_request_data(request_body,request_list):
    return

#请求验证是否成功
def request_verif(request_body,request_list):
    data = {}
    error = False
    data['errors'] = []
    if len(request_list) != 0:
        try:
            jsonData = json.loads(request_body.body.decode('utf-8'))
            print(jsonData)
            sign_data = sign(json.loads(request_body.body.decode('utf-8')))
            if 'sign' not in jsonData.keys():
                data['errors'].append({"参数错误": "Sign错误"})
                return None, data
            elif jsonData['sign'] != sign_data:
                data['errors'].append({"签名错误": "Sign错误"})
                return None, data
        except json.decoder.JSONDecodeError:
            error = True
            print("json 解析出错")
            data['errors'].append({"参数错误": "未传值"})
            return None,data
        except:
            print("出现错误")
            return  request_body.POST,None
    else:
        return request_body, None
    if request_body.method == 'POST':
        for p in request_list:
            if p not in jsonData:
                data['errors'].append({"参数错误":p+"未传值"})
                error = True
            else:
                if (jsonData[p] == None):
                    data['errors'].append({'error':errors.ERRORS[p]})
                    error = True
    elif request_body.method is 'GET':
        for p in request_list:
            if p not in request_body.GET:
                data['errors'].append({"参数错误":p+"未传值"})
                error = True
    if error:
        return None, data
    if request_body.method == 'POST':
        return json.loads(request_body.body.decode('utf-8')), None
    return request_body.GET, None

def sign(data):
    strs = ''
    for key in data.keys():
        if key != 'sign':
            strs = strs + str(key) + str(data[key])
    # 创建md5对象
    hl = hashlib.md5()
    hl.update((strs + WEICHAT_APPID).encode(encoding='utf-8'))
    print((strs + WEICHAT_APPID))
    print(hl.hexdigest())
    return hl.hexdigest()


def getaddress(address):
    address = urllib.request.quote(address)
    str = 'http://api.map.baidu.com/geocoder/v2/' \
          '?address='+ address +'&output=json&' \
          'ak=fBTBbXkPXNGR2jVxhLnGNpr94ZMw5zmc&callback=showLocation'
    data = urllib.request.urlopen(str)
    data1 = data.read()
    data2 = data1.decode("utf-8")
    data3 = data2.split(')')
    data4 = data3[0].split('(')
    JSON_DATA = json.loads(data4[1])
    return JSON_DATA['result']['location']


def getopenid(code):
    url = 'https://api.weixin.qq.com/sns/jscode2session?' \
          'appid='+WEICHAT_APPID+'&secret='+WEICHAT_SECRET+'&js_code='+code+'&grant_type=authorization_code'
    print(url)
    urllib.parse.quote(':')
    '%3A'
    data = urllib.request.urlopen(url)
    data1 = data.read()

    JSON_DATA = json.loads(str(data1).replace("'","").replace('b',""))
    return JSON_DATA['openid']
