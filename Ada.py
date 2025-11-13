#Adas kodeforslag oppgave 2 
#Variabler
def pause():
    input("\nTrykk Enter for å fortsette...")
#Bagrunnshistorie
print("Velkommen til Kontoret!" \
"\nDu er en i denne historien projektlederen Erling." \
"\nDu jober med et prosjet som heter 'Digital medborger portal'."
"\nDu er 6 uker inn i prosjektet og du merker at det begynner og oppstå koflikter i teamet.")
pause()
print ("\nDette er medlemmene i teamet ditt:" \
"\nSilje - Ekstern UX/UI-designer, fokusert på brukervennlighet og visuell kvalitet" \
"\nSivert - IT-rådgiver fra kommunens IT-avdeling, opptatt av teknisk sikkerhet og kostnadskontroll" \
"\nHamdi - Representant fra kulturavdelingen, ansvarlig for innbyggerdialog og kommunikasjon" \
"\nJabir - Brukerrepresentant fra en lokal innbyggerforening" \
"\nHallgeir - Politisk rådgiver, bindeledd til bystyret og prosjektets forankring" \
"\nNoa - Sikkerhetsekspert, innleid for å sikre databeskyttelse og personvern")
pause()

#Konflikt 1
print("\nDu møter Silje og Sivert på kontoret." \
"\nDe har en konflikt om designet og teknologivalget til protalen." \
"\nSilje mener løsningen til Sivert låser låser brukeropplevelsen og hinder utvikling." \
    "\nSivert mener Silje har utralistiske, usikre og dyre forslag til løsningen." )
print("\nHva gjør du?" \
      "\na) Tar konflikten i plenum med hele teamet." \
        "\nb) Snakker med Silje og Sivert hver for seg.")
konflikt_1= input("Skriv a eller b: ")

if konflikt_1== "a":
    print("\nDu velger å ta konflikten i plenum."
            "\nDu samler teamet og lar begge parter forklare sin side."
            "\nTeamet får høre begge sider, og det blir mer åpenhet."
            "\nDessver er spente stemning i teamet resten av dagen.")
elif konflikt_1== "b":
    print("\nDu velger å snakke med Silje og Sivert hver for seg."
            "\nDu får høre begge sider av konflikten og kan megle mellom dem."
            "\nBegge parter føler seg hørt, og du klarer å finne en mellomløsning."
            "\nStemningen i teamet bedrer seg de neste dagene.")
else:
    print("\nUgyldig valg. Vennligst start på nytt og velg a eller b.")
    konflikt_1= input("Skriv a eller b: ")
    if konflikt_1== "a":
        print("\nDu velger å ta konflikten i plenum."
                "\nDu samler teamet og lar begge parter forklare sin side."
                "\nTeamet får høre begge sider, og det blir mer åpenhet."
                "\nDessver er spente stemning i teamet resten av dagen.")
    elif konflikt_1== "b":
        print("\nDu velger å snakke med Silje og Sivert hver for seg."
                "\nDu får høre begge sider av konflikten og kan megle mellom dem."
                "\nBegge parter føler seg hørt, og du klarer å finne en mellomløsning."
                "\nStemningen i teamet bedrer seg de neste dagene.") 
    else:
        print("\nUgyldig valg igjen. Vennligst start på nytt senere.")
        exit()
pause()

#Konflikt 2
print("\nEt annet sted på kontoret møter du Hamdi og Jabir." \
      "\nHamdi ønsker å bruke kommunens allerede etablerte digitale plattform for portalen." \
      "\nJabir vil ha en mer åpn og fri løsning der innbygerene kan bidra mer spontant." \
        "\nDu merker at den lille diskusjonen begynner å eskalere.")
pause()
print("\nHva gjør du?" \
      "\na) Kaller begge inn til et møte for å diskutere fordeler og ulemper." \
      "\nb)Aventer situasjonen og håper de løser det selv.")
konflikt_2= input("Skriv a eller b: ")
if konflikt_2== "a":
    print("\nDu velger å kalle begge inn til et møte."
            "\nDu fasiliterer en diskusjon der begge parter kan legge frem sine synspunkter."
            "\nGjennom diskusjonen klarer dere å finne en løsning som kombinerer begge ideer."
            "\nDette styrker samarbeidet i teamet.")
elif konflikt_2== "b":
    print("\nDu velger å avvente situasjonen."
            "\nDiskusjonen mellom Hamdi og Jabir eskalerer, og det skaper en splittelse i teamet."
            "\nDette fører til redusert samarbeid og produktivitet i prosjektet.")
else:
    print("\nUgyldig valg. Vennligst start på nytt og velg a eller b.")
    konflikt_2= input("Skriv a eller b: ")
    if konflikt_2== "a":
        print("\nDu velger å kalle begge inn til et møte."
                "\nDu fasiliterer en diskusjon der begge parter kan legge frem sine synspunkter."
                "\nGjennom diskusjonen klarer dere å finne en løsning som kombinerer begge ideer."
                "\nDette styrker samarbeidet i teamet.")
    elif konflikt_2== "b":
        print("\nDu velger å avvente situasjonen."
                "\nDiskusjonen mellom Hamdi og Jabir eskalerer, og det skaper en splittelse i teamet."
                "\nDette fører til redusert samarbeid og produktivitet i prosjektet.")
    else:
        print("\nUgyldig valg igjen. Vennligst start på nytt senere.")
        exit()
pause()

#Konflikt 3 
print("\nSenere på dagen merker du at teamet virker skutebt etter at konfliktene tidligere." \
      "\nFolk trekker seg tilbake, og stemningen er lavere enn før." \
        "\nDu må bestemme hva du skal prioritere nå.")
print("\nHva gjør du?" \
      "\na)Setter av tid til en team-building aktivitet for å styrke samholdet." \
      "\nb)Fortsetter å fokusere på prosjektets fremdrift og mål.")
konflikt_3= input("Skriv a eller b: ")
if konflikt_3== "a":
    print("\nDu velger å sette av tid til en team-building aktivitet."
            "\nAktiviteten hjelper teamet med å gjenoppbygge tillit og forbedre kommunikasjonen."
            "\nStemningen i teamet bedrer seg, og folk føler seg mer engasjert i prosjektet.")
elif konflikt_3== "b":
    print("\nDu velger å fokusere på prosjektets fremdrift."
            "\nTeamet fortsetter å jobbe.")
else:
    print("\nUgyldig valg. Vennligst start på nytt og velg a eller b.")
    konflikt_3= input("Skriv a eller b: ")
    if konflikt_3== "a":
        print("\nDu velger å sette av tid til en team-building aktivitet."
                "\nAktiviteten hjelper teamet med å gjenoppbygge tillit og forbedre kommunikasjonen."
                "\nStemningen i teamet bedrer seg, og folk føler seg mer engasjert i prosjektet.")
    elif konflikt_3== "b":
        print("\nDu velger å fokusere på prosjektets fremdrift."
                "\nTeamet fortsetter å jobbe.")
    else:
        print("\nUgyldig valg igjen. Vennligst start på nytt senere.")
        exit()
pause()

#Oppsummering
print("\n==================================" \
      "\nProsjet status:" \
        "\n==================================")

if konflikt_1== "a" and konflikt_2== "a" and konflikt_3== "a": #1
    print("\nTeamet finner tilbake til hverandre." \
          "\nÅpen dialog og relasjonsbygging gjør at dere går videre til norming-fasen." \
            "\nProsjektet ligger godt an.")
elif konflikt_1== "a" and konflikt_2== "a" and konflikt_3== "b": #2
    print("\nKonflikten er håndtert ryddig, men presset på leveransen gjør teamet sårbart." \
          "\nProsjektet ligger godt an")
elif konflikt_1== "a" and konflikt_2== "b" and konflikt_3== "a": #3
    print("\nDesign/IT-konflikten er ryddet opp i, og motivasjonen styrkes, men den ulmende uenigheten mellom Hamdi og Jabir følger dere videre." \
    "\nProsjektet går fremover, men med noen skjulte spenninger.")
elif konflikt_1== "a" and konflikt_2== "b" and konflikt_3== "b": #4
    print("\nProsjektet går videre, men uenigheten mellom Hamdi og Jabir vokser i bakgrunnen, og teamet føler seg slitne." \
        "\nDere leverer, men samarbeidet er ikke sterkt.")
elif konflikt_1== "b" and konflikt_2== "a" and konflikt_3== "a": #5
    print("\nGjenom megling, dialog og team-building får du samlet teamet igjen." \
          "\nDere jobber mer koordinert og prosjektet har god fremdrift og solid fundament.")
elif konflikt_1== "b" and konflikt_2== "a" and konflikt_3== "b": #6
    print("\nKonfliktene er ryddet ioo i, men fokuset på tempo svekker motivasjonen." \
          "\nProsjekte går videre, teamet er litt slitene og litt distansert.")
elif konflikt_1== "b" and konflikt_2== "b" and konflikt_3== "a": #7
    print("\nDu har dempet konfliktene, men ikke løst dem helt." \
        "\nMotivasjonen reddes litt mot slutten, og prosjektet går videre med noen spenninger.")
elif konflikt_1== "b" and konflikt_2== "b" and konflikt_3== "b": #8
    print("\nProsjektet henger sammen med gaffateip." \
        "\nKonfliktene er delvis skjult, motivasjonen lav, og ingen føler seg helt med.")
else:
    print("\nNoe gikk galt med valgene dine. Vennligst start på nytt.")
pause()

print("\nTakk for at du spilte! Ha en fin dag på kontoret.")
