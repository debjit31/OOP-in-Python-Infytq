m = int(input())
data = input()
n = int(input())
div = input()
def xor(a, b):
    xor_res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            xor_res += '0'
        else:
            xor_res += '1'
    return xor_res
    
def calcCrc(data, div):
    tmp = data[0:len(div)]
    res = xor(tmp, div)
    res = res[1:]
    #print(res)
    for i in range(len(div)-1, len(data)-1):
        res += data[i+1]
        #print(res)
        if res[0] == '0':
            zero_div = ""
            for i in range(len(div)):
                zero_div += '0'
            #print(zero_div)
            res = xor(res, zero_div)
            res = res[1:]
        elif res[0] == '1':
            res = xor(res, div)
            res = res[1:]
    
    return res        
        

for i in range(len(div)-1):
    data += '0'
crc = calcCrc(data, div)
print(crc)