# 022 paro
IPREM=600; ip=IPREM*7/6
print('022 IPREM+1/6',ip,'tope175',ip*1.75,'200',ip*2,'225',ip*2.25,'min80',ip*.8)
bruto=2000; base=bruto*14/12; print('base reg',base,'70%',base*.7,'60%',base*.6)
print('pierdes al mes vs 2333',base-ip*1.75, 'vs nomina 2000', 2000-1225)
print('indemn 33d/año, 5 años:', bruto*14/365*33*5)
# 023 multa
m=200; print('023',m*.5,m*1.2, m*1.2-m*.5)
# 024 jubilacion 63
for pen in (1500,1577.6):
  for c in (.21,.19,.17,.13):
    r=pen*(1-c); print('024',pen,c,round(r,2),round(pen-r,2),'año',round((pen-r)*14,2),'20 años',round((pen-r)*14*20))
# 025 FGD
print('025', 150000-100000, 'pareja 200k cuenta conjunta ->', 100000*2)
# 026 renta tarde (plazo fin 30-jun-2026; 19-nov -> meses completos jul,ago,sep,oct = 4)
d=1000; rec=d*(0.01+0.01*4); print('026 recargo',rec,'con 25% red',rec*.75,'sancion leve 50%',d*.5,'15% >12m',d*.15)
# 027 hipoteca 180000, tipo 3.189 (TAE ref BdE sep) usamos 3.1 nominal escenario? usamos 3 %
def cuota(P,r,n): i=r/12; return P*i/(1-(1+i)**-n)
P=180000
for r in (0.03,):
  for a in (20,25,30,35):
    c=cuota(P,r,a*12); print('027',r,a,round(c,2),'intereses',round(c*a*12-P))
# 028 billete 50 de ene-2002 -> oct-2026 +79.9%
f=1.799; print('028', 50/f, 50*f, 100/f, 1-1/f)
