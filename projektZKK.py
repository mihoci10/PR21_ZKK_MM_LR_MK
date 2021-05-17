from csv import DictReader
from datetime import datetime
import numpy as np
import seaborn as sn
from matplotlib import pyplot as plt
from scipy.stats import beta
from numpy.polynomial.polynomial import polyfit


reader = DictReader(open('pn2020/pn2020.csv', 'rt'))
vsehMoskih=0
vsehZensk=0
tip=[]
stanjeP=[]
stanjeV=[]
varnostniPas=[]
alko=[]
spol=[]
klasN=[]

for row in reader:
    stanjeP.append(row["StanjePrometa"])
    stanjeV.append(row["StanjeVozisca"])
    tip.append(row["TipNesrece"])
    varnostniPas.append(row["UporabaVarnostnegaPasu"])
    alko.append(row["VrednostAlkotesta"])
    spol.append(row["Spol"])
    klasN.append(row["KlasifikacijaNesrece"])

tipVp={}
for i in tip:
    if i in tipVp:
        tipVp[i]+=1
    else:
        tipVp[i]=0

skupaj=sum(tipVp.values())

print("Tipi nesreč in njihov delež: \n")

for i in tipVp:
    print(str(i) + ": " + str(tipVp[i]/skupaj))

plt.pie(tipVp.values(), labels=tipVp.keys())
plt.show()

print("\n#############################################\n")
############################################################

print("Delež neuporabe varnostnega pasu pri različnih tipih nesreč:\n")

tipiPas={}

for i in range(len(tip)):
    if tip[i] in tipiPas:
        if(varnostniPas[i]=="NE"):
            tipiPas[tip[i]]+=1
    else:
        if(varnostniPas[i]=="NE"):
            tipiPas[tip[i]]=1
        else:
            tipiPas[tip[i]]=0
        
tipiNesrecE=[]
delezTipovE=[]
for i in tipiPas:
    tipiNesrecE.append(i)
    delezTipovE.append(tipiPas[i]/tipVp[i])
    print(str(i) + ": " + str(tipiPas[i]/tipVp[i]))

fig = plt.figure(figsize = (18, 5))
plt.bar(tipiNesrecE, delezTipovE, width=0.5, color='maroon')
plt.xticks(fontsize=6)
plt.title("Delež neuporabe varnostnega pasu pri različnih tipih nesreč")
plt.xlabel("Tipi nesreč")
plt.ylabel("Delež nepripetih pasov")
plt.show()

print("\n#############################################\n")
############################################################


ct=0
ctP=0
ctPZ=0
ctPM=0

ctZ=0
ctM=0

for i in range(len(alko)):
    ct+=1
    if(spol[i]=='ŽENSKI'):
        ctZ+=1
        
    if(spol[i]=='MOŠKI'):
        ctM+=1

    if(alko[i]!=None):    
        if(float(alko[i])>0):
            ctP+=1
            if(spol[i]=='ŽENSKI'):
                ctPZ+=1
            elif(spol[i]=='MOŠKI'):
                ctPM+=1
        

print("Delež voznikov pod vplivom alkohola (2020): " + str(ctP/ct))
print("Delež žensk, ki so vozile pod vplivom alkohola (2020): " + str(ctPZ/ctZ))
print("Delež moških, ki so vozili pod vplivom alkohola (2020): " + str(ctPM/ctM))

plt.bar(["Ženske","Moški","Skupaj"], [float(ctPZ/ctZ),float(ctPM/ctM),float(ctP/ct)], color=["maroon","blue","grey"])
plt.show()

print("\n#############################################\n")
############################################################



ct=0
ctS=0
ctM=0
ctL=0
ctH=0

for i in klasN:
    ct+=1
    if(i=='S SMRTNIM IZIDOM'):
        ctS+=1
    if(i=='Z MATERIALNO ŠKODO'):
        ctM+=1
    if(i=='Z LAŽJO TELESNO POŠKODBO'):
        ctL+=1
    if(i=='S HUDO TELESNO POŠKODBO'):
        ctH+=1


print("Delež nesreč z materialno škodo: " + str(ctM/ct))
print("Delež nesreč z lažjo telesno poškodbo: " + str(ctL/ct))
print("Delež nesreč s hudo telesno poškodbo: " + str(ctH/ct))
print("Delež nesreč s smrtnim izidom: " + str(ctS/ct))

print("\n#############################################\n")
############################################################

ctPasInSmrt=0
ctBrezpasuInSmrt=0

ctPas=0
ctBrezpasu=0

for i in range(len(varnostniPas)):
    if(varnostniPas[i]=='NE'):
        ctBrezpasu+=1
    elif(varnostniPas[i]=='DA'):
        ctPas+=1



for i in range(len(varnostniPas)):
    if(varnostniPas[i]=='NE' and klasN[i]=='S SMRTNIM IZIDOM'):
        ctBrezpasuInSmrt+=1
    if(varnostniPas[i]=='DA' and klasN[i]=='S SMRTNIM IZIDOM'):
        ctPasInSmrt+=1    

print("Možnost preživetja če imamo pripet varnostni pas v prometni nesreči: " + str(1-(ctPasInSmrt/ctPas)))
print("Možnost preživetja če nimamo pripetega varnostnega pasu v prometni nesreči: " + str(1-(ctBrezpasuInSmrt/ctBrezpasu)))


print("\n#############################################\n")
############################################################


ctAlkoInSmrt=0
ctBrezalkoInSmrt=0

ctAlko=0
ctBrezalko=0

for i in range(len(alko)):
    if(float(alko[i])>0):
        ctAlko+=1
    else:
        ctBrezalko+=1



for i in range(len(alko)):
    if(float(alko[i])<=0 and klasN[i]=='S SMRTNIM IZIDOM'):
        ctBrezalkoInSmrt+=1
    if(float(alko[i])>0 and klasN[i]=='S SMRTNIM IZIDOM'):
        ctAlkoInSmrt+=1    

print("Možnost preživetja če smo bili udeleženi v prometni nesreči pod vplivom alkohola: " + str(1-(ctAlkoInSmrt/ctAlko)))
print("Možnost preživetja če smo bili udeleženi v prometni nesreči brez vpliva alkohola: " + str(1-(ctBrezalkoInSmrt/ctBrezalko)))

print("\n#############################################\n")
############################################################

reader = DictReader(open('pn2010/pn2010.csv', 'rt'))
vsehMoskihS=0
vsehZenskS=0
tipS=[]
stanjePS=[]
stanjeVS=[]
varnostniPasS=[]
alkoS=[]
spolS=[]
klasNS=[]

for row in reader:
    stanjePS.append(row["StanjePrometa"])
    stanjeVS.append(row["StanjeVozisca"])
    tipS.append(row["TipNesrece"])
    varnostniPasS.append(row["UporabaVarnostnegaPasu"])
    alkoS.append(row["VrednostAlkotesta"])
    spolS.append(row["Spol"])
    klasNS.append(row["KlasifikacijaNesrece"])
    #tipNesrece=(row['ZaporednaStevilkaPN;KlasifikacijaNesrece;UpravnaEnotaStoritve;DatumPN;UraPN;VNaselju;Lokacija;VrstaCesteNaselja;SifraCesteNaselja;TekstCesteNaselja;SifraOdsekaUlice;TekstOdsekaUlice;StacionazaDogodka;OpisKraja;VzrokNesrece;TipNesrece;VremenskeOkoliscine;StanjePrometa;StanjeVozisca;VrstaVozisca;GeoKoordinataX;GeoKoordinataY;ZaporednaStevilkaOsebeVPN;Povzrocitelj;Starost;Spol;UEStalnegaPrebivalisca;Drzavljanstvo;PoskodbaUdelezenca;VrstaUdelezenca;UporabaVarnostnegaPasu;VozniskiStazVLetih;VozniskiStazVMesecih;VrednostAlkotesta;VrednostStrokovnegaPregleda'].split(";")[9])
    #stanjePrometa=(row['ZaporednaStevilkaPN;KlasifikacijaNesrece;UpravnaEnotaStoritve;DatumPN;UraPN;VNaselju;Lokacija;VrstaCesteNaselja;SifraCesteNaselja;TekstCesteNaselja;SifraOdsekaUlice;TekstOdsekaUlice;StacionazaDogodka;OpisKraja;VzrokNesrece;TipNesrece;VremenskeOkoliscine;StanjePrometa;StanjeVozisca;VrstaVozisca;GeoKoordinataX;GeoKoordinataY;ZaporednaStevilkaOsebeVPN;Povzrocitelj;Starost;Spol;UEStalnegaPrebivalisca;Drzavljanstvo;PoskodbaUdelezenca;VrstaUdelezenca;UporabaVarnostnegaPasu;VozniskiStazVLetih;VozniskiStazVMesecih;VrednostAlkotesta;VrednostStrokovnegaPregleda'].split(";")[1])
    #stanjeVozisca=(row['ZaporednaStevilkaPN;KlasifikacijaNesrece;UpravnaEnotaStoritve;DatumPN;UraPN;VNaselju;Lokacija;VrstaCesteNaselja;SifraCesteNaselja;TekstCesteNaselja;SifraOdsekaUlice;TekstOdsekaUlice;StacionazaDogodka;OpisKraja;VzrokNesrece;TipNesrece;VremenskeOkoliscine;StanjePrometa;StanjeVozisca;VrstaVozisca;GeoKoordinataX;GeoKoordinataY;ZaporednaStevilkaOsebeVPN;Povzrocitelj;Starost;Spol;UEStalnegaPrebivalisca;Drzavljanstvo;PoskodbaUdelezenca;VrstaUdelezenca;UporabaVarnostnegaPasu;VozniskiStazVLetih;VozniskiStazVMesecih;VrednostAlkotesta;VrednostStrokovnegaPregleda'].split(";")[17])

    #tip.append(tipNesrece)
    #stanjeP.append(stanjePrometa)
    #stanjeV.append(stanjeVozisca)

tipVpS={}
for i in range(len(tipS)):
    if tipS[i] in tipVpS:
        tipVpS[tipS[i]]+=1
    else:
        if(tipS[i]=="PREVRNITEV VOZILA" or tipS[i]=="TRČENJE V OBJEKT" or tipS[i]=="TRČENJE V STOJEČE / PARKIRANO VOZILO" or tipS[i]=="BOČNO TRČENJE" or tipS[i]=="NALETNO TRČENJE" or tipS[i]=="OSTALO" or tipS[i]=="POVOŽENJE ŽIVALI" or tipS[i]=="OPLAŽENJE" or tipS[i]=="POVOŽENJE PEŠCA" or tipS[i]=="ČELNO TRČENJE"):
            tipVpS[tipS[i]]=0
        else:
            tipS[i]="OSTALO"
            if("OSTALO" in tipVpS):
                tipVpS["OSTALO"]+=1
            else:
                tipVpS["OSTALO"]=0

print("############################  ")

skupajS=sum(tipVpS.values())

print("Tipi nesreč in njihov delež: \n")

for i in tipVpS:
    print(str(i) + ": " + str(tipVpS[i]/skupajS))

plt.pie(tipVpS.values(), labels=tipVpS.keys())
plt.show()

print("\n#############################################\n")
############################################################

ctS=0
ctPS=0
ctPZS=0
ctPMS=0

ctZS=0
ctMS=0

for i in range(len(alkoS)):
    ctS+=1
    if(spolS[i]=='ŽENSKI'):
        ctZS+=1
        
    if(spolS[i]=='MOŠKI'):
        ctMS+=1

    if(alkoS[i]!="None"):
        if(float(alkoS[i])>0):
            ctPS+=1
            if(spolS[i]=='ŽENSKI'):
                ctPZS+=1
            elif(spolS[i]=='MOŠKI'):
                ctPMS+=1
        

print("Delež voznikov pod vplivom alkohola (2010): " + str(ctPS/ctS))
print("Delež žensk, ki so vozile pod vplivom alkohola (2010): " + str(ctPZS/ctZS))
print("Delež moških, ki so vozili pod vplivom alkohola (2010): " + str(ctPMS/ctMS))

plt.bar(["Ženske","Moški","Skupaj"], [float(ctPZS/ctZS),float(ctPMS/ctMS),float(ctPS/ctS)], color=["maroon","blue","grey"])
plt.show()

print("\n#############################################\n")
############################################################

print("Delež neuporabe varnostnega pasu pri različnih tipih nesreč (2010):\n")

tipiPasS={}

for i in range(len(tipS)):
    if tipS[i] in tipiPasS:
        if(varnostniPasS[i]=="NE"):
            tipiPasS[tipS[i]]+=1
    else:
        if(varnostniPasS[i]=="NE"):
            tipiPasS[tipS[i]]=1
        else:
            tipiPasS[tipS[i]]=0
        
tipiNesrecES=[]
delezTipovES=[]
for i in tipiPasS:
    tipiNesrecES.append(i)
    
    delezTipovES.append(tipiPasS[i]/tipVpS[i])
    print(str(i) + ": " + str(tipiPasS[i]/tipVpS[i]))

fig = plt.figure(figsize = (18, 5))
plt.bar(tipiNesrecES, delezTipovES, width=0.5, color='maroon')
plt.xticks(fontsize=6)
plt.title("Delež neuporabe varnostnega pasu pri različnih tipih nesreč (2010)")
plt.xlabel("Tipi nesreč")
plt.ylabel("Delež nepripetih pasov")
plt.show()


print("\n#############################################\n")
############################################################



ctS=0
ctSS=0
ctMS=0
ctLS=0
ctHS=0

for i in klasNS:
    ctS+=1
    if(i=='S SMRTNIM IZIDOM'):
        ctSS+=1
    if(i=='Z MATERIALNO ŠKODO'):
        ctMS+=1
    if(i=='Z LAŽJO TELESNO POŠKODBO'):
        ctLS+=1
    if(i=='S HUDO TELESNO POŠKODBO'):
        ctHS+=1


print("Delež nesreč z materialno škodo (2010): " + str(ctMS/ctS))
print("Delež nesreč z lažjo telesno poškodbo (2010): " + str(ctLS/ctS))
print("Delež nesreč s hudo telesno poškodbo (2010): " + str(ctHS/ctS))
print("Delež nesreč s smrtnim izidom (2010): " + str(ctSS/ctS))

print("\n#############################################\n")
############################################################

ctPasInSmrtS=0
ctBrezpasuInSmrtS=0

ctPasS=0
ctBrezpasuS=0

for i in range(len(varnostniPasS)):
    if(varnostniPasS[i]=='NE'):
        ctBrezpasuS+=1
    elif(varnostniPasS[i]=='DA'):
        ctPasS+=1



for i in range(len(varnostniPasS)):
    if(varnostniPasS[i]=='NE' and klasNS[i]=='S SMRTNIM IZIDOM'):
        ctBrezpasuInSmrtS+=1
    if(varnostniPasS[i]=='DA' and klasNS[i]=='S SMRTNIM IZIDOM'):
        ctPasInSmrtS+=1    

print("Možnost preživetja če imamo pripet varnostni pas v prometni nesreči (2010): " + str(1-(ctPasInSmrtS/ctPasS)))
print("Možnost preživetja če nimamo pripetega varnostnega pasu v prometni nesreči (2010): " + str(1-(ctBrezpasuInSmrtS/ctBrezpasuS)))


    
