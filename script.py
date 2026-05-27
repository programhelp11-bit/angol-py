import time

def indit_kviz():
    # Kérdések listája (10 alap + 10 nehezebb)
    kerdesek = [
        # --- Alap kérdések ---
        {"kerdes": "Hogy mondják angolul azt, hogy 'ceruza'?", "opciok": ["A) Pen", "B) Pencil", "C) Ruler", "D) Eraser"], "valasz": "B"},
        {"kerdes": "Melyik a helyes alak? 'I ___ a student.'", "opciok": ["A) is", "B) are", "C) am", "D) be"], "valasz": "C"},
        {"kerdes": "Mennyi: 'ten' + 'five'?", "opciok": ["A) Twelve", "B) Fifteen", "C) Fifty", "D) Twenty"], "valasz": "B"},
        {"kerdes": "Ki a 'brother'?", "opciok": ["A) Apa", "B) Nagypapa", "C) Fiútestvér", "D) Lánytestvér"], "valasz": "C"},
        {"kerdes": "Milyen színű a 'purple'?", "opciok": ["A) Lila", "B) Rózsaszín", "C) Kék", "D) Narancssárga"], "valasz": "A"},
        {"kerdes": "Melyik szó jelenti a hétfőt?", "opciok": ["A) Sunday", "B) Tuesday", "C) Monday", "D) Friday"], "valasz": "C"},
        {"kerdes": "Hogyan mondod: 'Neki (fiú) van egy kutyája'?", "opciok": ["A) He have got a dog.", "B) He has got a dog.", "C) He is a dog.", "D) He can a dog."], "valasz": "B"},
        {"kerdes": "Mit jelent a 'Can you swim?' kérdés?", "opciok": ["A) Szeretsz úszni?", "B) Szoktál úszni?", "C) Tudsz úszni?", "D) Akarsz úszni?"], "valasz": "C"},
        {"kerdes": "Hol találod a 'blackboard'-ot?", "opciok": ["A) Konyha", "B) Kert", "C) Tanterem", "D) Fürdőszoba"], "valasz": "C"},
        {"kerdes": "Hogy hívják az anyukád lánytestvérét?", "opciok": ["A) Uncle", "B) Aunt", "C) Cousin", "D) Grandmother"], "valasz": "B"},
        
        # --- Nehezebb kérdések (100 órás tanmenet haladóbb része) ---
        {
            "kerdes": "Hogy van az 'egerek' (többes szám) angolul?",
            "opciok": ["A) Mouses", "B) Mices", "C) Mice", "D) Mousees"],
            "valasz": "C"
        },
        {
            "kerdes": "Melyik a helyes tagadás? 'Éppen most nem nézek tévét.'",
            "opciok": ["A) I not watching TV.", "B) I don't watching TV.", "C) I am not watching TV.", "D) I'm no watching TV."],
            "valasz": "C"
        },
        {
            "kerdes": "Mit jelent ez az időpont: 'It's quarter to six'?",
            "opciok": ["A) Negyed hat", "B) Háromnegyed hat (5:45)", "C) Hat óra múlt 15 perccel", "D) Hat óra tíz perc"],
            "valasz": "B"
        },
        {
            "kerdes": "Melyik kérdőszó jelenti azt, hogy 'Kié'?",
            "opciok": ["A) Who", "B) Where", "C) Whose", "D) Why"],
            "valasz": "C"
        },
        {
            "kerdes": "Hogy mondjuk azt, hogy 'szemben valamivel'?",
            "opciok": ["A) Next to", "B) Opposite", "C) Between", "D) Under"],
            "valasz": "B"
        },
        {
            "kerdes": "Melyik szó jelenti a 'pincér' foglalkozást?",
            "opciok": ["A) Waiter", "B) Worker", "C) Teacher", "B) Driver"],
            "valasz": "A"
        },
        {
            "kerdes": "Egészítsd ki: 'There isn't ___ milk in the fridge.'",
            "opciok": ["A) some", "B) a", "C) any", "D) many"],
            "valasz": "C"
        },
        {
            "kerdes": "Hogy mondják a 'lábfejek' szót (többes számban)?",
            "opciok": ["A) Foots", "B) Feet", "C) Feets", "D) Footes"],
            "valasz": "B"
        },
        {
            "kerdes": "Melyik mondat helyes?",
            "opciok": ["A) I always am happy.", "B) Always I am happy.", "C) I am always happy.", "D) I am happy always."],
            "valasz": "C"
        },
        {
            "kerdes": "Hogyan kérdezed meg: 'Mit csinálsz most?'",
            "opciok": ["A) What do you do?", "B) What are you doing?", "C) What you doing?", "D) What are you do?"],
            "valasz": "B"
        }
    ]

    pontszam = 0
    osszes = len(kerdesek)

    print("--- BŐVÍTETT 5. OSZTÁLYOS ANGOL KVÍZ (20 KÉRDÉS) ---")
    print("Válaszolj a betűjelekkel (A, B, C vagy D)!\n")
    time.sleep(1)

    for i, k in enumerate(kerdesek):
        print(f"{i+1}. kérdés: {k['kerdes']}")
        for opcio in k['opciok']:
            print(opcio)
        
        valasz = input("Válaszod: ").strip().upper()

        if valasz == k['valasz']:
            print("Helyes! Great job! ✅")
            pontszam += 1
        else:
            print(f"Sajnos nem... A helyes válasz a {k['valasz']} volt. ❌")
        
        print("-" * 30)
        time.sleep(0.3)

    # Értékelés
    szazalek = (pontszam / osszes) * 100
    print(f"\nVége a kvíznek! Pontszámod: {pontszam}/{osszes} ({szazalek}%)")
    
    if szazalek == 100:
        print("Tökéletes! Te vagy az osztály legjobbja! 🏆")
    elif szazalek >= 80:
        print("Szuper teljesítmény! Nagyon jól megy az angol! 🌟")
    elif szazalek >= 60:
        print("Jó lett, de a nehezebb nyelvtant még nézd át! 📚")
    else:
        print("Gyakorolj még egy kicsit, menni fog az! 💪")

if __name__ == "__main__":
    indit_kviz()
