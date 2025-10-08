import random,time
from datetime import datetime

traffic_data=[{'source':'192.168.1.1','destination':'10.0.0.1','port':'22','payload':'india','protocol':'TCP'},
              {'source':'192.168.1.2','destination':'10.0.0.3','port':'25','payload':'mandavi','protocol':'TCP'},
              {'source':'10.0.0.1','destination':'168.127.1.2','port':'20','payload':'USA','protocol':'TCP'},
              {'source':'20.0.0.1','destination':'192.168.1.1','port':'80','payload':'AMERICA','protocol':'TCP'},
              {'source':'unknown','destination':'30.0.0.2','port':'22','payload':'krishit','protocol':'TCP'},
              {'source':'192.168.3.1','destination':'unknown','port':'10','payload':'china','protocol':'TCP'}]

def is_suspicious(packet):
    suspicious_source=['unknown','192.168.3.1']
    suspicious_port=['10','80']
    return packet['source'] in suspicious_source or packet['port'] in suspicious_port

def generate_alert(packet,is_suspicious):
    status="suspicious" if is_suspicious else "non-suspicious"
    msg=f'{status} packet is detected  '
    msg+=f"Time :{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    for key,value in packet.items():
        msg+=f'{key} : {value} \n'
    
    return msg

def alert_log(msg):
    with open('alerts.log','a') as f:
        f.write(msg+ "\n")

for packet in traffic_data:
    suspicious=is_suspicious(packet)
    alert_msg=generate_alert(packet,suspicious)
    print(alert_msg)
    alert_log(alert_msg)