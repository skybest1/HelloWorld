import urllib
import hashlib
import httplib
import json

def cal_token(params,private_key):
    data=""
    keys=params.keys()
    keys.sort()
    for key in keys:
        data=data+key
        data=data+str(params[key])
        #print key+":"+str(params[key])
    data=data+private_key
    hash_new=hashlib.sha1()
    hash_new.update(data)
    hash_value=hash_new.hexdigest()
    return hash_value

if __name__=="__main__":
    #calculate the params
    public_key="ucloudskybest1_zju@163.com13546925271030716530"
    private_key="90f02346530d9b8248584f6b886d4300ec414bbe"
    param={}
    param["public_key"]=public_key
    param["offset"]=0
    param["max_count"]=0
    param["format"]="json"
    param["access_token"]=cal_token(param,private_key)
    url_values=urllib.urlencode(param)
    print url_values
    #make http request
    httpconn=httplib.HTTPConnection("ucenter.ucloud.cn")
    url="/api/instances"+"?"+url_values
    httpconn.request("GET",url)
    data=httpconn.getresponse()
    #parse the json format
    rawdata=data.read()
    print rawdata
    
    result=json.loads(rawdata)
    vminfo=result["data"]
    for vm in vminfo:
        print vm["id"]
    
