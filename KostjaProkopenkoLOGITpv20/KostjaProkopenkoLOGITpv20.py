def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
eng:list=loe_failist('eng.txt')

def lisamine(f):
    fail=open(f,'r')
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas



def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

rus:list=loe_failist("rus.txt")

def lisamine(f):
    fail=open(f,'r')
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas


