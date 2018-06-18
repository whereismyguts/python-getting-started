from django.shortcuts import render
from django.http import HttpResponse

import pymongo

image = "iVBORw0KGgoAAAANSUhEUgAAAJUAAABwCAMAAAAg9cJMAAAAMFBMVEXu7u7W1tbv7+/AwMDV1dXn5+fk5OTh4eHZ2dnPz8/q6urDw8PMzMzd3d3IyMjS0tKs2+sWAAAEFUlEQVR4nMWbi3KsIAyGhXJVkfd/24Nc1d2eIiTATKcdy5KvyU+I0S7Lt2GYoF9/ATuoZLLejmHkzfTmIV/YoQ6KEHxvOU+ddiqxPBQ+VoAixMqq6TzMRsZKUIysdfM5GYBVoGqFhY+VPEWqoU4s5CC2QOF7qwkKGYu+1tQArLbwJSwkbfVA4XmrOXyIWH2eQsLqh3JrrMBYEFDw3gKBAsYqnuKdiwFiwYQvrgWlLUgoOG+BQgFhwWkKEAs2fEBYGFDdWDhQnVjwmgLAwvJUFxYmVDMWLlQjVoZi0JoqWK+LZmxPBayX3iqewoN6jYWXEjqwRoTvicXpX0OSQVAOS+j98IPI/w8Wpu27WPAbdGr/iWMn7PdB8jTNFK6snKcYUbZg/ToKu/VbEJVq8RYrsBLUvnohKtS2YdS6/sSKcXtA/azUN38ZIpQP4Bcsh6OkFFIa4sEu4XNb0WCeN54qZ6CCpRgzJUusklyEbokS+H3yQnXBMi5KlymLvAvdfwL1ocKFKmPtj+BQYbcClVQ3ikrpaPqumXMK2x5Q46iCt2wSjVdVfgyy3aFGUjksHWxyugpppFiXuEnZdoMaSkVU/G5jviI6JTBxmzeWKuYvt+n0CXjmqcNDrNSwSVROT75o9plAk/jDRnzpspJJVGTxtXxMETolz8PXU3dnjaNi5rRERcxOP0dKnjJcn0QlgvWcylM95WnvIRxI5Ysmqsrhk9JqIFBTqMJDUMrIDcvmAuEqrHFUKlw7r+grVArtbKpST/kEMZUqRtBeKs+AFSI4iSqr/b4JNbFhspmzB/kvmUFNzQwhW8pEk+lCduVzsqiXOxUpgDaWge4g5BNPHN9qOM+VLW2+W3V6DeDQ01nFw+4IUL5o3mLGkrMqmVL17dbfyriq74hXJlZ9eyrOXWVslBtyTRo/9CwqJ/ONBX2dNxPhq1Snc6hS5fm48zq9dYS8NYEqJoTt2Yh1WEc5EwdT5TLB3lt5dOG5kaRHU+limSmxxFtUN7hhpYTIWGO6H3e7jBnB+cq5iK2iDyzcTlG8Rfi0GlsvyZXPCahdtVgI6I8IfYzSLQo7EfcpgGFfPPUnFvrLp6YO6s6O/0asObYwrPr/sHHepvCfAqRj9+9dVe6ekR8CvLM0CuulnTFYr62MwMo26jN1w0daod784djeyrvv3fq4WM2xwMTqEAgeVtfKWFiNmsLF6t7fGFgASQceC2RFaCyg9WCxyotEnasVLIBXa+EOMjhvdaYEHCzgIx8GC0xTn1gd/woAXxz1ewtUU1BY4OGDwEKC6tMFYq3WvjSKpnqx0MLXg4UM1aatAfeW702gaqoZCzt8DyzGq+anf/Ab8JKntyPqpgcs7KZTxKpuTvrXzdChop365qSbPgDKe+s71D9eSi2hAs7HLgAAAABJRU5ErkJggg=="
uri = "mongodb://user:admin123@ds115352.mlab.com:15352/sorokin_sad"

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    data =  {
                "_id": {
                    "$oid": "5991af7343a1437a102f133a"
                },
                "Name": "Item title",
                "Description": "Some description.",
                "Tags": "one, two, free",
                "Price": 800,
                "Images": [
                    "<Binary Data>",
                    "<Binary Data>",
                    "<Binary Data>",
                    "<Binary Data>"
                ]
            }


    return render(request, 'index.html', data)


def db(request):

    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

    thingies = db['Thingies']
    first = thingies.find_one()
    import json
    import base64
    for image in first["Images"]:
        dataStr = json.dumps(data)
        base64EncodedStr = base64.b64encode(dataStr)
        first["Images"].append(base64EncodedStr)
    # data = {
    #         'greetings': [
    #             {"test": first['Description']}, 
    #             {"test": first['Name']}
    #         ]
    #     }
    return render(request, 'index.html', first )


