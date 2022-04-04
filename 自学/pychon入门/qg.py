# -*- coding: utf-8 -*-
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import subprocess
import os
import logging
 
 
#  算法源码来源于大佬的github,详情参考  https://github.com/3b295/mosoteach_checkin
 
########  配置区  ########
# 登陆请求的返回JSON中可以找到
USER_ID = ''
ACCESS_SECRET = ''
 
# 签到请求的headers中可以找到
X_MSSVC_ACCESS_ID = ''
 
User_Agent=''
X_device_code=''
X_app_machine=''
# 建议默认即可
X_MSSVC_SEC_TS = '1537153727'
# 每次请求的延迟时间/秒,建议默认即可
sleepTime = '50'
 
# 日志的位置,默认即可
LOGGING_PATH = "./logging.txt"
 
# 经度
LNG = ''
# 纬度
LAT = ''
 
# 签到的课程号
CLAZZ_COURSE_ID = ''
# 签到的课程名
class_name=''
 
# server酱
server_chan_sckey = ''  # 申请地址http://sc.ftqq.com/3.version
server_chan = {
    'status': True,  # 如果关闭server酱功能，请改为False
    'url': 'https://sc.ftqq.com/{}.send'.format(server_chan_sckey)
}
 
####### end #########
 
class ResultCodeError(Exception):
    """http请求返回了未知的码"""
    pass
 
class Checkin:
 
    def __init__(self):
        self._logger = logging.Logger(__name__)
        console_hander = logging.StreamHandler()
        console_hander.setFormatter(logging.Formatter("%(asctime)s %(levelname)s:%(message)s"))
        console_hander.setLevel(logging.DEBUG)
        console_hander.addFilter(logging.Filter(__name__))
        self._logger.addHandler(console_hander)
 
        file_hander = logging.FileHandler(filename=LOGGING_PATH, mode='a', encoding='utf-8')
        file_hander.setFormatter(logging.Formatter("%(asctime)s %(levelname)s:%(message)s"))
        file_hander.setLevel(logging.INFO)
        self._logger.addHandler(file_hander)
 
    def checkin(self, checkin_id):
        self._logger.info('开始签到')
        today = datetime.today() - timedelta(seconds=60 * 60 * 8 + 10)
        date1 = today.strftime("%a, %d %b %Y %H:%M:%S GMT")
        date = today.strftime("%a, %d %b %Y %H:%M:%S GMT+00:00")
 
        url = "http://checkin.mosoteach.cn:19527/checkin"
 
        headers = {
            "Accept-Encoding": "gzip;q=0.7,*;q=0.7",
            "Connection":"close",
            "User-Agent": User_Agent,
            "Date": date1,
            "X-device-code": X_device_code,
            "X-mssvc-signature": self.get_checkin_signature(date),
            "X-mssvc-access-id": X_MSSVC_ACCESS_ID,
            "X-app-id": "MTANDROID",
            "X-app-version": "5.1.5",
            "X-dpr":"2.75",
            "X-app-machine":X_app_machine,
            "X-app-system-version":"9",
            "X-mssvc-sec-ts": X_MSSVC_SEC_TS,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": "52",
            "Host": "checkin.mosoteach.cn",
        }
 
        data = {
            "checkin_id": checkin_id,
            "report_pos_flag": "Y",
            "lat": LAT,
            "lng": LNG,
        }
 
        r = requests.post(url, headers=headers, data=data)
        resp = json.loads(r.text)
        if resp['result_code'] == 2409:
            self._logger.info("重复签到, 返回的值: {}".format(r.text))
            return False
        if resp['result_code'] == 0:
            self._logger.info("签到完毕, 返回的值: {}".format(r.text))
            self.server_chan_send('签到完毕',date)
            return True
        self._logger.info("签到失败, 返回的值: {}".format(r.text))
        return False
 
    def get_checkin_id(self):
        today = datetime.today() - timedelta(seconds=60 * 60 * 8 + 10)
        date1 = today.strftime("%a, %d %b %Y %H:%M:%S GMT")
        date = today.strftime("%a, %d %b %Y %H:%M:%S GMT+00:00")
 
        headers = {
            "Accept-Encoding": "gzip;q=0.7,*;q=0.7",
            "Connection": "close",
            "User-Agent": User_Agent,
            "Date": date1,
            "X-device-code": X_device_code,
            "X-mssvc-signature": self.get_current_open_signature(date),
            "X-mssvc-access-id": X_MSSVC_ACCESS_ID,
            "X-app-id": "MTANDROID",
            "X-app-version": "5.1.5",
            "X-dpr": "2.75",
            "X-app-machine": X_app_machine,
            "X-app-system-version": "9",
            "X-mssvc-sec-ts": X_MSSVC_SEC_TS,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": "52",
            "Host": "api.mosoteach.cn",
        }
 
        data = {
            "clazz_course_id": CLAZZ_COURSE_ID,
        }
 
        r = requests.post("http://api.mosoteach.cn/mssvc/index.php/checkin/current_open", headers=headers, data=data)
 
        resp = json.loads(r.text)
        if resp["result_code"] == 1001:
            self._logger.info("未签到")
            return -1
        elif resp["result_code"] == 0:
            self._logger.info("准备签到， 签到码: {}".format(resp['id']))
            return resp["id"]
        else:
            raise ResultCodeError("未知错误返回码: {}".format(resp))
 
    def monitor(self):
        self._logger.info("开始监听签到")
        while True:
            sleep(float(sleepTime))
            checkin_id = self.get_checkin_id()
            if checkin_id != -1:
                self.checkin(checkin_id)
                return
 
    def get_signature(self,type, datestr):
        cmd = r'java -cp {} com.Ak {} {}'.format('java_code', type, datestr)
        logging.debug(cmd)
 
        rst = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        rst = rst.communicate()[0].decode('ASCII')
        if os.linesep == '\n':  # linux
            return rst[:-1]
        else:  # windows
            return rst[:-2]
 
    def get_current_open_signature(self,date):
        datestr = ' '.join(
            map(lambda x: '"{}"'.format(x), [USER_ID, date, ACCESS_SECRET, CLAZZ_COURSE_ID]))
 
        return self.get_signature("current_open", datestr)
 
    def get_checkin_signature(self,date):
        datestr = ' '.join(map(lambda x: '"{}"'.format(x), [USER_ID, date, ACCESS_SECRET]))
        return self.get_signature("checkin", datestr)
 
    def server_chan_send(self,msg,date):
        """server酱将消息推送至微信"""
        desp = ''
        desp = '|  **课程名**  |   {}   |\r| :----------: | :---------- |\r'.format(class_name)
        desp += '| **签到时间** |   {}   |\r'.format(date)
        desp += '| **签到状态** |   {}   |\r'.format(msg)
        params = {
            'text': '您的网课签到消息来啦！！',
            'desp': desp
        }
        requests.get(server_chan['url'], params=params)
 
 
if __name__ == '__main__':
    ck=Checkin()
    ck.monitor()