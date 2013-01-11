import httplib
import urllib
import GetTest

public_key="ucloudskybest1_zju@163.com13546925271030716530"
private_key="90f02346530d9b8248584f6b886d4300ec414bbe"
param={}
param["instance_id"]="c5895458-2c00-0001-7d1b-ad43fd17117d"
param["public_key"]=public_key
param["format"]="json"
#param["access_token"]=GetTest.cal_token(param,private_key)
param["access_token"]=GetTest.cal_token(param,private_key)

body=urllib.urlencode(param)
print body
#
httpconn=httplib.HTTPConnection("ucenter.ucloud.cn")
url="/api/instance/shutdown"
headers={'User-Agent':"shoplug_platform/1.0","Connection":"close","Content-type":"application/x-www-form-urlencoded"}
httpconn.request("POST",url,body,headers)

data=httpconn.getresponse()
print data.read()
