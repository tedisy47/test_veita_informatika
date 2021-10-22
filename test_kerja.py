import urllib.request
import json



def application(env, start_response):
    start_response('200 OK', [('Content-Type','application/json')])
    url = 'https://mocki.io/v1/8e889d1f-77cc-4838-9caf-97d3a421b95c'
    response = urllib.request.urlopen(url).read()

    jsonResponse = json.loads(response.decode('utf-8'))
   
    datajson = jsonResponse['features'][0]

    
    geometry_array = []
    for geometry in datajson['geometry']['coordinates'][0]:
        koordinat = str(geometry[1])+','+str(geometry[0])
        geometry_array.append(koordinat)


    data ={'geometry_locs' : geometry_array}


    result =  json.dumps(data)
    result = result.encode('utf-8')
    return [result]