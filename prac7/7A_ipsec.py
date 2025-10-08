class Policy:
    def __init__(self,local_subnet,remote_subnet,mode,pfs,esp):
        self.local_subnet=local_subnet
        self.remote_subnet=remote_subnet
        self.mode=mode
        self.pfs=pfs
        self.esp=esp

class Connection:
    def __init__(self,local_ip,remote_ip):
        self.local_ip=local_ip
        self.remote_ip=remote_ip
        self.policies=[]
        self.shared_secret=None

    def add_policy(self,policy):
        self.policies.append(policy)

    def add_psk(self,shared_secret):
        self.shared_secret=shared_secret

    def up(self):
        print("The Ipsec conection is start !!")
        print("\nThe Local ip :" , self.local_ip)
        print("The Remote ip :",self.remote_ip)
        for policy in self.policies:
            print("\n Policy")
            print("The Local subnet :",policy.local_subnet)
            print("The Remote subnet :",policy.remote_subnet)
            print("The mode :",policy.mode)
            print("The pfs  :",policy.pfs)
            print("The esp  :",policy.esp)
        print("\nThe Shared Secret is :",self.shared_secret)
        print("The connection is up !!")

if __name__=="__main__":
    local_ip="102.168.1.1"
    remote_ip="102.168.2.2"
    local_subnet="10.0.0.0/24"
    remote_subnet="10.0.0.1/24"
    shared_secret="India is the Best"

    mode="tunnel"
    pfs="group14"
    esp="aes128-sha256"

connection=Connection(local_ip,remote_ip)

outbound_policy=Policy(remote_subnet,local_subnet,mode,pfs,esp)
inbound_policy=Policy(local_subnet,remote_subnet,mode,pfs,esp)

connection.add_policy(outbound_policy)
connection.add_policy(inbound_policy)
connection.add_psk(shared_secret)
connection.up()