from Labbar import labb3språk


def språkmeny():
    kör = True
    while kör:
        try:
            val = int(input('''Vilket språk önskas?
                        1 Visk 2 Rövar 3 Bebis
                        4 All 5 Fikon 6 Avsluta programmet'''))
            if 1 <= val <= 5:
                while True:
                    try:
                        mening = input('Din mening: ')
                        l = [labb3språk.viskspråket, labb3språk.rövarspråket, labb3språk.bebisspråket,
                             labb3språk.allspråket, labb3språk.fikonspråket]
                        l[val - 1](mening)
                        break

                    except:
                        print('Vänligen skriv in en mening för översättning')
            elif val == 6:
                print('Hejdå!')
                kör = False
            else:
                print('Välj en siffra från menyn ovan!')
        except:
            print('Välj en siffra från menyn ovan!')
språkmeny()