import csv
import jsonlines
from io import StringIO

from google.cloud import storage
import googleapiclient.discovery

def list_sub_directories(bucket_name, prefix):
    """Returns a list of sub-directories within the given bucket."""
    service = googleapiclient.discovery.build('storage', 'v1')

    req = service.objects().list(bucket=bucket_name, prefix=prefix, delimiter='/')
    res = req.execute()
    return res['prefixes']

trained_models = list_sub_directories(bucket_name='north-t5x', prefix='finetuned/scandeval/')

storage_client = storage.Client()
bucket = storage_client.get_bucket('north-t5x')
    
for tm in trained_models:
    v = tm[-2]
    m = tm.replace("finetuned/scandeval/scandinavian_large_","")[:-4] 
    metric_file =(tm+'inference_eval/'+m+'-metrics.jsonl')
    
    try:
        blob = bucket.blob(metric_file)
        blob = blob.download_as_string()
        blob = blob.decode('utf-8')
        blob = StringIO(blob)  #tranform bytes to string herei

        reader = jsonlines.Reader(blob)
        result = m+"\t"+v+"\t"
        for obj in reader:
            result += str(obj['f1_macro'])+"\t"

        print(result)
    except:
        print("Errors reading "+metric_file)
