
#1. Introduksjon: Kort bakgrunn om situasjonen i prosjektet og hvilke konflikter som
#ulmer.

#2. Beslutningspunkt 1: Hvordan håndterer Erling konflikten mellom Silje og Sivert?
#a. Alternativ A → konsekvens
#b. Alternativ B → konsekvens

#3. Beslutningspunkt 2: Hvordan håndterer han uenigheten mellom Hamdi og Jabir?
#a. Alternativ A → konsekvens
#b. Alternativ B → konsekvens

#4. Beslutningspunkt 3: Hvordan bevarer han motivasjonen i teamet?
#a. Alternativ A → konsekvens
#b. Alternativ B → konsekvens

#Variabler
key = True


def start():
    Start = input("\nTrykk enter for å starte spillet")

def fortsett():
    Fortsett = input("\nTrykk enter for å fortsette")

#Introduksjon
print("""\nVelkommen til beslutningsspillet om prosjektledelse!
Her skal du ta på deg rollen som prosjektleder Erling.  
Dine valg vil påvirke utfallet av prosjektet og teamets dynamikk. Lykke til!""")

start()

#Story bakgrunn
print("\n--- Introduksjon ---")


print ("""\nDet har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye
digitale medborgerportal, samlet sitt prosjektteam for første gang. Etter en inspirerende
oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver.
Teamet består av:
• Erling - prosjektleder, ansvarlig for fremdrift og relasjoner
• Sivert - IT-rådgiver fra kommunens IT-avdeling, opptatt av teknisk sikkerhet og
kostnadskontroll
• Silje - ekstern UX/UI-designer, fokusert på brukervennlighet og visuell kvalitet
• Hamdi - representant fra kulturavdelingen, ansvarlig for innbyggerdialog og
kommunikasjon
• Hallgeir - politisk rådgiver, bindeledd til bystyret og prosjektets forankring
• Noa - sikkerhetsekspert, innleid for å sikre databeskyttelse og personvern
• Jabir - brukerrepresentant fra en lokal innbyggerforening""")

fortsett()

print("""\nI starten var stemningen god. Gruppen opplevde høy motivasjon og fellesskap i målet
om å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen.
Men nå, etter seks uker, har prosjektet gått inn i den klassiske storming-fasen, der ulike
faglige perspektiver og personlige preferanser begynner å kollidere.""")

fortsett()

#Konflikt 1
print("\n---Konflikt 1: Silje og Sivert---")

print("""\nUenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til en
personkonflikt.
• Silje mener løsningen Sivert foreslår vil låse brukeropplevelsen og hindre
innovasjon.
• Sivert mener Siljes forslag er urealistisk, usikkert og for kostbart.""")

fortsett()

while True:
    print("""\nHvordan bør Erling håndtere konflikten mellom Silje og Sivert?
        Alternativ A: Snakke om det sammen i et felles møte
        Alternativ B: Ha separate samtaler med hver av dem""")  

    event1 = input("\nSkriv A eller B for å velge alternativ: ").upper()

    if event1 == "A":
        print("""\nErling velger å samle Silje og Sivert til et felles møte. Han legger vekt konflikt håndtering og samarbeid.
        Ting går bra tilslutt.""")

        fortsett()
        print ("\n Konflikten kommer til en løsning. Men...")
        event1_1 = input("\nSkiv A eller B å velge alternativ for å vinne: ").upper()

        if event1_1 == "A":
            print("\nWIN")
        elif event1_1 == "B":
            print("\nLOSE")
        
    elif event1 == "B":
        print("\nErling dør og erling kan ikke koflikthåndtere situasjonen.")
        break
    else: 
        print("\nUgyldig valg. Vennligst velg A eller B.")
        continue
    break

fortsett()
while True:
    #Konflikt 2
    print("\n---Konflikt 2: Hamdi og Jabir---") 


