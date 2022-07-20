from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from urllib.parse import unquote
import server.database.database as db
import sys
import os





# #twilio creds- need to remove before leaving on git

@extend_schema(
        examples=[
                    OpenApiExample(
                        name='health',
                        value='{ \"status\": \"UP\" }'
                    ),
                ],
        description='Get health of application',
        responses=OpenApiTypes.OBJECT,
     )
@api_view(['GET','POST'])
@csrf_exempt


def printt(thing):
    resp = thing

def parse_req(req):
    dict = {}
    for item in req.split("&")[1:]:
        split = item.split("=")
        dict[split[0]] = split[1]
    return dict

def sms(request):
    resp = ""
    req = parse_req(str(request))
    incoming_og = unquote(req['Body']) #unquotes undoes percent encoding
    to_number = "+" + req['From'][3:]  #saving incoming phone number
    #response = requests.request("GET", url).json()
    incoming = ''
    for c, i in zip(incoming_og, range(len(incoming_og))):
        if c == incoming_og[i-1] == incoming_og[i+1] == "+":
            incoming += c
        elif c == "+" and incoming_og[i-1].isnumeric() and incoming_og[i+1].isnumeric():
            incoming += c
        elif c == "+":
            incoming += ' '
        else:
            incoming += c

    print(1, incoming)
    #resp = "here"
    client = Client('$$$$$$$$$$$$$$$$$$$$$$', '$$$$$$$$$$$$$$$$$$$$$$$$')
    if incoming[0] == ">" or incoming[0] == "<":
        file = open('output.txt', 'w')
        sys.stdout = file
        code = incoming[1:]
        exec(code)
        file.close()
        file = open('output.txt', 'r')
        for line in file.readlines():
            client.messages.create(body=line, from_='+19894761292', to=to_number)
        os.remove("output.txt")
    print("got through that")

    message = client.messages.create(
        body='Hi there',
        from_='+19894761292',
        to=to_number
    )

    print(message.sid)
    print("done")

    return HttpResponse('')


######################DJANGO/IBM ADDED FUNCTIONS#############################
def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def index(request):
    return render(request, 'index.html')


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def retrieveData():
    conn=db.dataseconnectToDB2()
    return(db.fetchData(conn))
