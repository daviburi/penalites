import random
p = 0.7 #probability of scoring a single shot
n = 30000 #number of penalty series
maxS = 5
nST = []

i = 1


while i<=n:
    nSA = 0
    nSB = 0
    gA = 0
    gB = 0

    #first 10 shots
    while (nSA<maxS): 
        if (gA+maxS-nSA>=gB): #should A team shoot
            nSA = nSA+1
            if random.random()<p:
                gA = gA+1
                #print ("A scored")
            #else:
                #print ("A didn't score")
        else:
            #print (nSA+nSB)
            break
        if (gB+maxS-nSB>=gA): #should B team shoot
            nSB = nSB+1
            if random.random()<p:
                gB = gB+1
                #print ("B scored")
            #else:
                #print ("B didn't score")
        else:
            #print (nSA+nSB)
            break
    while (gA==gB): #after 5 shots
        nSA = nSA+1
        if random.random()<p:
            gA = gA+1
        nSB = nSB+1
        if random.random()<p:
            gB = gB+1
            #print ("B scored")
        #else:
            #print ("B didn't score")
    nST.append(nSA+nSB)
    i = i+1
print (sum(nST)/n)
    