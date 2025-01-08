# Jednostavni kalkulator
def kalkulator():
    print("Dobrodošao u kalkulator!")
    print("Izaberi operaciju:")
    print("1. Sabiranje")
    print("2. Oduzimanje")
    print("3. Množenje")
    print("4. Deljenje")
    
    # Unos korisničkog izbora
    izbor = input("Unesi broj operacije (1/2/3/4): ")
    
    # Provera da li je unos validan
    if izbor in ['1', '2', '3', '4']:
        try:
            # Unos brojeva
            broj1 = float(input("Unesi prvi broj: "))
            broj2 = float(input("Unesi drugi broj: "))
            
            # Izvršavanje izabrane operacije
            if izbor == '1':
                rezultat = broj1 + broj2
                print(f"Rezultat: {broj1} + {broj2} = {rezultat}")
            elif izbor == '2':
                rezultat = broj1 - broj2
                print(f"Rezultat: {broj1} - {broj2} = {rezultat}")
            elif izbor == '3':
                rezultat = broj1 * broj2
                print(f"Rezultat: {broj1} * {broj2} = {rezultat}")
            elif izbor == '4':
                if broj2 != 0:
                    rezultat = broj1 / broj2
                    print(f"Rezultat: {broj1} / {broj2} = {rezultat}")
                else:
                    print("Greška: Deljenje nulom nije dozvoljeno!")
        except ValueError:
            print("Greška: Unos mora biti broj.")
    else:
        print("Greška: Pogrešan izbor operacije.")

# Poziv funkcije kalkulator
kalkulator()
