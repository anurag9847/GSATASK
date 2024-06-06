from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import json
from datetime import datetime
from bson import json_util
from bson import ObjectId

# Create your views here.
def index(req):
    return HttpResponse('HI from API')

@csrf_exempt
def register(req):
    if req.method != 'POST':
        return JsonResponse({'err': 'invalid request'})

    try:
        prmsJsn = json.loads(req.body)

        name = prmsJsn.get('name')
        email = prmsJsn.get('email')
        mobile = prmsJsn.get('mobile')
        password = prmsJsn.get('password')

        if not name or not email or not mobile or not password:
            return JsonResponse({'err': 'All fields are required'}, status=400)

        # Connection to MongoDB
        dbCli = MongoClient('localhost', 27017) 
        dbDbs = dbCli['GSA']
        dbCll = dbDbs['users']

        now = datetime.now()

        dbCll.insert_one({'name': name, 'email': email, 'ts': now, 'mobile': mobile, 'password': password})

        dbCli.close()
        return JsonResponse({'status': 200, 'msg': 'Success'})
    except Exception as e:
        print(str(e))
        return JsonResponse({'err': str(e)}, status=500)

@csrf_exempt
def authentication(req):

    if req.method != 'POST':
        return JsonResponse({'err':'invalid request'})
    
    res = {}
    prmsJsn = json.loads(req.body)
    email = prmsJsn['email']
    try:

        dbCli = MongoClient('localhost',27017)
        dbDbs = dbCli['GSA']
        dbCll = dbDbs['users']
        fltr = {
            'email':  email
        }

        docs = dbCll.find(fltr)

        docs = json.loads(json_util.dumps(docs))
       

        if len(docs) == 0:
                res['status'] = 400
                res['message'] = 'User not found'

        for doc in docs:
            if doc['password'] != prmsJsn['password'] or doc['email'] != prmsJsn['email']:
                res['status'] = 400
                res['message'] = 'Invalid username or password'
            else:     
                res['status'] = 200
                res['message'] = 'Successfully authenticated'
                req.session['name'] = doc['name']

                return JsonResponse(res)

        dbCli.close()    
        return JsonResponse(res)
    except Exception as e:
       return JsonResponse({'err':'mongodb error','msg':str(e)})   

@csrf_exempt
def AddTask(req):

    if req.method != 'POST':
        return JsonResponse({'err':'invalid request'})
    
    
    prmsJsn = json.loads(req.body)

    ##get the Data from Req
    ## we have to add validation for it
    # for time being im skipping this part
    taskName = prmsJsn['taskName']
    Date = prmsJsn['date']
    Time = prmsJsn['time']
    AssignedBy = prmsJsn['assignedBy']
    Status = prmsJsn['status']

    ts = datetime.now()
    doc={
        'Task-Name':taskName,
        'Date':Date,
        'Time':Time,
        'Assigned-By':AssignedBy,
        'status':Status,
        'ts':ts
    }

    ##push the data to MongoDb
    try:
        dbCli = MongoClient('localhost', 27017) 
        dbDbs = dbCli['GSA']
        dbCll = dbDbs['Tasks']

        dbCll.insert_one(doc)

        return JsonResponse({'status':200})
        dbCll.close()
    except Exception as e:
        return JsonResponse({'err':str(e)})    

@csrf_exempt
def ViewTasks(req):

    out =[]
    res = {}

    if req.method != 'POST':
        return JsonResponse({'err':'invalid request'})

    try:
        dbCli = MongoClient('localhost', 27017) 
        dbDbs = dbCli['GSA']
        dbCll = dbDbs['Tasks']

        #any uilter we want means , add here
        fltr={}    

        docs = dbCll.find()

        for doc in docs:
            item = {}
            item['id'] = str(doc['_id'])
            item['task'] = doc['Task-Name']
            item['date'] = doc['Date']
            item['time'] = doc['Time']
            item['assigned'] = doc['Assigned-By']
            item['status'] = doc['status']
            out.append(item)

        res['items'] = items    
        
    except Exception as e:
        return JsonResponse({'err':str(e)})  
        
    finally:          
        return JsonResponse(out,safe=False)


    
    



