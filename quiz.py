print('\n\n\nWelkom bij de gigantische Webdevelopers Quiz 2023')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=10
 
if antwoord.lower()=='ja':

    print('\n\nMooi. Dan gaat de gigantische Webdevelopers Quiz 2023 beginnen!\nDe quiz bestaat uit meerkeuzevragen. Kies bij elke vraag uit één van de drie antwoorden.\n\n')

    antwoord=input('Vraag 1: In welk jaar kwam de Compact Disc op de markt? \n\n A: 1980 \n B: 1981 \n C: 1982 ')
    if antwoord.lower()=='c' or antwoord.lower()=='1982':
        punten += 1
        print('Dit is het juiste antwoord! ')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: C ')
 
    antwoord=input('Vraag 2: De Compact Disc is onstaan uit een samenwerking tussen welke twee fabrikanten? \n\n A: Philips en Sony \n B: Toshiba en Panasonic \n C: Nakamichi en Denon ')
    if antwoord.lower()=='a' or antwoord.lower()=='philips en sony':
        punten += 1
        print('Dit is het juiste antwoord! ')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: A ')

    antwoord=input('Vraag 3: Wat was het eerste album dat werd uitgebracht op Compact Disc? \n\n A: ABBA - The Visitors \n B: Bruce Springsteen - Born In The USA \n C: Billy Joel - 52nd Street ')
    if antwoord.lower()=='a' or antwoord.lower()=='abba - the visitors':
        punten += 1
        print('Dit is het juiste antwoord!')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: A ')

    antwoord=input('Vraag 4: Wat was het eerste model Compact Disc-speler dat op de markt kwam? \n\n A: Philips CD200 \n B: Panasonic SL-P10 \n C: Sony CDP101 ')
    if antwoord.lower()=='c' or antwoord.lower()=='sony cdp101':
        punten += 1
        print('Dit is het juiste antwoord!')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: C' )

    antwoord=input('Vraag 5: Hoe hoog is de sampling rate van de Compact Disc? \n\n A: 48 kHz \n B: 44.1 kHz \n C: 96 kHz ')
    if antwoord.lower()=='b' or antwoord.lower()=='44.1 khz':
        punten += 1
        print('Dit is het juiste antwoord!')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: B' )

    antwoord=input('Vraag 6: Van welk soort plastic is de Compact Disc gemaakt? \n\n A: PVC (Polyvinylchloride) \n B: Polycarbonaat \n C: Celluoide  ')
    if antwoord.lower()=='b' or antwoord.lower()=='polycarbonaat':
        punten += 1
        print('Dit is het juiste antwoord!')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: B ')

    antwoord=input('Vraag 7: Hoeveel minuten aan muziek passen er maximaal op de Compact Disc? \n\n A: 60 minuten \n B: 74 minuten \n C: 90 minuten  ')
    if antwoord.lower()=='b' or antwoord.lower()=='74 minuten':
        punten += 1
        print('Dit is het juiste antwoord!')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: B ')

    antwoord=input('Vraag 8: Wat is de diameter van de Compact Disc? \n\n A: 10 centimeter \n B: 11,5 centimeter \n C: 12 centimeter  ')
    if antwoord.lower()=='c' or antwoord.lower()=='12 centimeter':
        punten += 1
        print('Dit is het juiste antwoord!')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: C ')

    antwoord=input('Vraag 9: Wat was het eerste nieuwe volledig digitaal opgenomen album dat werd uitgebracht op Compact Disc? \n\n A: Peter Gabriel - Peter Gabriel (1982) \n B: Lionel Richie - Cant Slow Down \n C: Christopher Cross - Another Page ')
    if antwoord.lower()=='a' or antwoord.lower()=='peter gabriel - peter gabriel (1982)':
        punten += 1
        print('Dit is het juiste antwoord!')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: A ')

    antwoord=input('Vraag 10: Hoeveel MB aan data past er op een Compact Disc? \n\n A: 567 MB \n B: 734 MB \n C: 986 MB  ')
    if antwoord.lower()=='b' or antwoord.lower()=='734 mb':
        punten += 1
        print('Dit is het juiste antwoord!')
    else:
        print('Helaas, het juiste antwoord had moeten zijn: B ')    

    print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 6: print('Goed bezig!')
    else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')

elif antwoord.lower()=='nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')
