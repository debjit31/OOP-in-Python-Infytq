def generate_firstIP(ip_bin, network_int):
    first_ip = ip_bin[:network_int]
    for i in range(network_int, 32):
       first_ip+='0'
    ##print(first_ip)
    createOctets(first_ip, 'First IP')
    

def generate_lastIP(ip_bin, network_int):
    last_ip = ip_bin[:network_int]
    for i in range(network_int, 32):
       last_ip+='1'
    ##print(last_ip)
    createOctets(last_ip, 'Last IP')
    

def createOctets(ip, name):
    tmp='0b'
    ip_addr =[]
    for i in range(0,32):
        if (i+1)%8!=0:
            tmp+=ip[i]
        else:
            tmp+=ip[i]
            ip_addr.append(tmp)
            tmp='0b'
    ##print(ip_addr)
    displayIP(ip_addr, name)


def displayIP(test, name):
    first_ip_dec = []
    for i in test:
        first_ip_dec.append(str(int(i,2)))
    ##print(first_ip_dec)
    first_ip_str = '.'.join(first_ip_dec)
    print(name , " :-",  first_ip_str)


if __name__ == "__main__":
    l = []
    l_net__ip = []
    ip = input()
    l = ip.split(sep='/')
    network_int = int(l[1])
    host_int = 32-network_int
    net_ip = l[0]
    ip_bin=""
    l_net__ip = net_ip.split(sep='.')
    ##print(l_net__ip)
    net_ip_bin = []
    for i in l_net__ip:
        x = int(i)
        bin_x = bin(x)
        bin_x=bin_x[2:]
        bin_x=bin_x.zfill(8)
        net_ip_bin.append(bin_x)
        ip_bin=ip_bin+bin_x
    ip_bin=ip_bin[:len(ip_bin)-1]
   ##print(net_ip_bin)
    generate_firstIP(ip_bin, network_int)
    generate_lastIP(ip_bin, network_int)
