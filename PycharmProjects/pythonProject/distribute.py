import urllib.request
from base64 import encodebytes

ip = "192.168.253.130"
node_id = "openflow:52239919331"
table_id = "0"
flow_id = "d-d"
username = "admin"
password = "admin"
url = "http://" + ip + ":8181/restconf/config/opendaylight-inventory:nodes/node/" + node_id + "/flow-node-inventory:table/" + table_id + "/flow/" + flow_id
print(url)
flow = {
    "flow-node-inventory:flow": [
        {
            "id": "d-d",
            "priority": 2,
            "table_id": 0,
            "hard-timeout": 0,
            "match": {
                "in-port": "openflow:52239919331:3"
            },
            "cookie": 3098476543630901250,
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
flow["flow-node-inventory:flow"][0]["id"] = flow_id
print("please input priority of this flow:")
flow["flow-node-inventory:flow"][0]["priority"] = int(input())
print("please input hard-timeout of this flow:")
flow["flow-node-inventory:flow"][0]["hard-timeout"] = int(input())
print("please input idle-timeout of this flow:")
flow["flow-node-inventory:flow"][0]["idle-timeout"] = int(input())
print("please input in-port of this flow:")
flow["flow-node-inventory:flow"][0]["match"]["in-port"] = node_id + ":" + input()
print("please input output-port of this flow:")
flow["flow-node-inventory:flow"][0]["instructions"]["instruction"][0]["apply-actions"]["action"][0]["output-action"][
    "output-node-connector"] = input()

print("flow_id:" + str(flow["flow-node-inventory:flow"][0]["id"]))
print("priority:" + str(flow["flow-node-inventory:flow"][0]["priority"]))
print("hard-timeout:" + str(flow["flow-node-inventory:flow"][0]["hard-timeout"]))
print("idle-timeout:" + str(flow["flow-node-inventory:flow"][0]["idle-timeout"]))
print("in-port:" + flow["flow-node-inventory:flow"][0]["match"]["in-port"])
print("output-port:" +
      flow["flow-node-inventory:flow"][0]["instructions"]["instruction"][0]["apply-actions"]["action"][0][
          "output-action"]["output-node-connector"])
print(flow)
req = urllib.request.Request(url=url, data=bytes(str(flow), 'utf-8'), method="PUT")
b64str = encodebytes(bytes('%s:%s' % (username, password), 'utf-8'))[:-1]
req.add_header("Authorization", "Basic %s" % b64str.decode('utf-8'))
req.add_header("Accept", "application/json")
req.add_header("Content-Type", "application/json")
returnData = urllib.request.urlopen(req)
res_json = returnData.read().decode('utf-8')
print(res_json)
