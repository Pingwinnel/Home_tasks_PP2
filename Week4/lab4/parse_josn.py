import json
with open('json.json') as file:
    data=json.load(file)
print('''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')
for i in range(len(data["imdata"])):
    dn=data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    dnlen=len(dn)
    des=data["imdata"][i]["l1PhysIf"]["attributes"]["descr"]
    deslen=len(des)
    speed=data["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
    speedlen=len(speed)
    mtu=data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print(dn+" "*(49-dnlen)+des+" "*(24-deslen)+speed+" "*(8-speedlen),mtu)