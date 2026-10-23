# Seminarska naloga: Analiza podatkov

Za seminarsko nalogo pri predmetu uvod v pogramiranje sem se odločil analizirati besedila pesmi iz spletne strani genious.com. Natančneje, analiziral sem le pesmi zvrsti hrvaškega trapa, kjer sem si izbral nekaj izvajalcev ter probal najti čim več lastnosti njihovih besedil. Za to nalogo sem se odločil, ker sam veliko poslušam to zvrst glasbe, tako da sem zvedel nekaj novega o mojih interesih.

## Struktura projekta

README.md - opis seminarske naloge in navodila za zagon kode

1_zajemanje_podatkov.py - datoteka s kodo, ki prenese naslove, imena avtorjev in besedila pesmi iz Genious.com in jih shrani v datoteko hrvaski_trap_podatki.csv

2_analiza_in_grafi.py - datoteka s kodo, ki požene iskanje po besedilih in izriše grafe ter tabele z dobljenimi rezultati

hrvaski_trap_podatki.csv - datoteka z besedili pesmi, pridobljenimi z 1_zajemanje_podatkov.py

seminarska_naloga-ipynb - datoteka s jupyter notebookom, kjer je koda ter analiza podatkov in rezultatov, predstavljenih z grafi in tabelami.

## Navodila za pogon kode:

Odprite terminal na svojem računalniku in vnesite:
git clone https://github.com/timkrizanic/seminarska_uvp.git

Pred prvim zagonom morate v terminalu namestiti tri knjižnice. Odprite terminal in zaženite:
pip install lyricsgenius pandas matplotlib ipykernel

Odprite program VS Code, izberite File -> Open Folder in odprite to mapo. Kliknite na datoteko seminarska_naloga.ipynb. Zgoraj desno izberite svoj Kernel in kliknite gumb Run All.

## Težave, s katerimi sem se soočal

Prva težava je bila trajanje zajema podatkov. Ker besedila vsebujejo veliko podatkov, zajemanje podatkov traja več minut, tako da je pri spreminjanju kode trajalo več časa. Ker je bilo  to kdaj za program, se je pri analizi nekaterih izvajalcev program znal sesuti. Probleme sem imel tudi s iskanjem izbranih besed po besedilu, saj se sklanjatve v hrvaškem jeziku pri nekaterih besedah razlikujejo, tako da je bilo težko zajeti vse ponovitve nekaterih izrazov.

## Zaključek

Pri delanju seminarske naloge sem pridobil veliko novih izkušenj pri programiranju, še posebaj pri analizi podatkov, oz. prenosu in obdelavi podatkov iz spleta. V prihodnosti želim sestaviti podoben program, ki vzame veliko večjo bazo podatkov, da bi bilu rezultati širši in bolj natančni.