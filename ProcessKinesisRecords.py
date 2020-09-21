from __future__ import print_function
import json
import base64
import boto3
import os

s3 = boto3.client('s3', endpoint_url='http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME'], aws_access_key_id='temp', aws_secret_access_key='temp')
def lambda_handler(event, context):
    temp = []
    keys = ['remote','host', 'user', 'time', 'method', 'path', 'protocol', 'code', 'size', 'referer', 'agent', 'http_x_forwarded_for']

    for record in event['Records']:
        payload = base64.b64decode(record["kinesis"]["data"])
        
        val = str(payload).replace(' +','+').split()
        data = dict(zip(keys,val))
        data['code'] = int(data['code'])

        temp.append(data)

    bucket = 'test'
    lambda_path = '/log/access_log/'
    tmp_path = '/tmp/tmp.json'
    
    file_name =  temp[0]['time'].split(':')[0].replace('[','').replace('/','_')
    file_name += '.json'

    path = temp[0]['time'].split(':')[0].replace('[','').split("/")
    bucket_path = 'yy='+path[2]+'/mm='+path[1]+'/dd='+path[0] +'/'+ file_name
    lambda_path += bucket_path 

    with open(tmp_path, 'w', encoding='utf-8') as file:
        json.dump(temp,file,indent=2)
    
    s3.upload_file(tmp_path, bucket, lambda_path)
    return {"result" : 200 }
        

