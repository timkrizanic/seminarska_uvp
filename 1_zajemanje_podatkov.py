import lyricsgenius
import pandas as pd

GENIUS_TOKEN = "BbdyoSFW3Lu4jJ07ODyQxuJ3EY87W2rj0rAlmVg-09stkFl_xsz35TRqUXiSeOGC"

izvajalci_za_analizo = ["Grše", "Peki", "Baks", "BUNTAI", "KUKU$", "Miach", "High 5", "Sjena"]
stevilo_pesmi_na_izvajalca = 20
genius = lyricsgenius.Genius(GENIUS_TOKEN)
genius.remove_section_headers = True 
genius.skip_non_songs = True 
vse_zbrane_pesmi = []


for ime in izvajalci_za_analizo:
    print(f"\nIskanje izvajalca: {ime}")
    try:
        artist = genius.search_artist(ime, max_songs=stevilo_pesmi_na_izvajalca, sort="popularity")
        if artist:
            for song in artist.songs:
                cisto_besedilo = song.lyrics.split("Lyrics", 1)[-1] if "Lyrics" in song.lyrics else song.lyrics
                
                vse_zbrane_pesmi.append({
                    "Izvajalec": artist.name,
                    "Naslov_Pesmi": song.title,
                    "Besedilo": cisto_besedilo
                })
    except Exception as e:
        print(f"Napaka pri prenosu za izvajalca {ime}: {e}")


df = pd.DataFrame(vse_zbrane_pesmi)
df.to_csv("hrvaski_trap_podatki.csv", index=False, encoding="utf-8")
print(f"\nPrenesenih je {len(df)}  pesmi.")
print("Podatki so shranjeni v datoteko 'hrvaski_trap_podatki.csv'.")
