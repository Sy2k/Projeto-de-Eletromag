# ----------- Importando bibliotecas -----------
import math

# ----------- Algumas variaveis para os calculos futuros-----------
mhi_ar = 4*math.pi*1e-7
mhi_min = mhi_ar*1000
mhi_max = mhi_ar*20000

aream = 2268*1e-6
area1 = 1146.6*1e-6
area2 = 1096*1e-6
areae = (63*17.6*1e-6)

lgm = 2.2*1e-3
lg1 = 1e-3
lg2 = 1e-3

l1 = (8.75+54.5+52.9)*1e-3
l2 = (8.75+54.5+52.9)*1e-3
l3 = (8.75+54.5)*1e-3
le = (-17.4/2)+(105.8/2)*1e-3

fluxo = 0.9116*(aream)
i_max = 0.4
i_min = 0.35

# ----------- Calculando as relutancias do gap -----------
rgm = lgm/(mhi_ar * aream)
rg1 = lg1/(mhi_ar * area1)
rg2 = lg2/(mhi_ar * area2)

# ----------- Calculando as relutancias maximas -----------
rf1_max = l1/(mhi_max * area1)
rf2_max = l2/(mhi_max * area2)
rf3_max = l3/(mhi_max * aream)
rfe_max = le/(mhi_max * areae)

# ----------- Calculando as relutancias minimas -----------
rf1_min = l1/(mhi_min * area1)
rf2_min = l2/(mhi_min * area2)
rf3_min = l3/(mhi_min * aream)
rfe_min = le/(mhi_min * areae)
 
# ----------- Calculando as req equivalente minimo e maximo -----------
req1_max = rf1_max + rg1 + rfe_max
req2_max = rf2_max + rg2 + rfe_max
req3_max = rgm + rf3_max

req1_min = rf1_min + rg1 + rfe_min
req2_min = rf2_min + rg2 + rfe_min
req3_min = rgm + rf3_min

req_max = ((req2_max*req1_max)/(req2_max+req1_max)) + req3_max
req_min = ((req2_max*req1_min)/(req2_max+req1_min)) + req3_min

# ----------- Calculando numero de volta maximo e minimo -----------
n1 = (fluxo*req_max)/i_max
n2 = (fluxo*req_min)/i_min

print("Numero de voltas 1:",n1)
print("Numero de voltas 2:",n2)

# print(rf1_min)

# ----------- Valores minimos para comparar -----------
# rgm = 771915.51
# rg1 = 694929.928
# rg2 = 725939.35

# rf1 = 80611.58
# rf2 = 84100.007
# rf3 = 22191.57
# rfe = 31721.9
