import urllib
from base64 import encodebytes

from django.shortcuts import render
import requests
import socket
from myapp.models import Information

flow = {
    "flow-node-inventory:flow": [
        {
            "id": "666",
            "priority": 2,
            "table_id": 0,
            "hard-timeout": 0,
            "match": {
                "in-port": "openflow:52239919331:3"
            },
            "cookie": 11111111111111,
            "instructions": {
                "instruction": [
                    {
                        "order": 0,
                        "apply-actions": {
                            "action": [
                                {
                                    "order": 0,
                                    "output-action": {
                                        "max-length": 65535,
                                        "output-node-connector": "2"
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "idle-timeout": 0
        }
    ]
}


def index(request):
    return render(request, 'index.html')


def Distribute(request):
    global flow
    information = Information()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    information.ip = ip = s.getsockname()[0]
    information.node_id = node_id = request.POST.get("node_id")
    information.table_id = table_id = 0
    information.flow_id = flow_id = request.POST.get("flow_id")
    information.username = username = "admin"
    information.password = password = "admin"
    flow["flow-node-inventory:flow"][0]["id"] = flow_id
    information.priority = flow["flow-node-inventory:flow"][0]["priority"] = request.POST.get("priority")
    information.hard_timeout = flow["flow-node-inventory:flow"][0]["hard-timeout"] = request.POST.get("hard_timeout")
    information.idle_timeout = flow["flow-node-inventory:flow"][0]["idle-timeout"] = request.POST.get("idle_timeout")
    information.in_port = flow["flow-node-inventory:flow"][0]["match"]["in-port"] = node_id + ":" + request.POST.get("in_port")
    information.output_port = flow["flow-node-inventory:flow"][0]["instructions"]["instruction"][0]["apply-actions"]["action"][0]["output-action"]["output-node-connector"] = request.POST.get("output_port")
    information.url = url = "http://" + str(ip) + ":8181/restconf/config/opendaylight-inventory:nodes/node/" + str(node_id) + "/flow-node-inventory:table/" + str(table_id) + "/flow/" + str(flow_id)
    information.save()
    req = urllib.request.Request(url=url, data=bytes(str(flow), 'utf-8'), method="PUT")
    b64str = encodebytes(bytes('%s:%s' % (username, password), 'utf-8'))[:-1]
    req.add_header("Authorization", "Basic %s" % b64str.decode('utf-8'))
    req.add_header("Accept", "application/json")
    req.add_header("Content-Type", "application/json")
    returnData = urllib.request.urlopen(req)
    res_json = returnData.read().decode('utf-8')
    return render(request, 'index.html')
