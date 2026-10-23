import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hrvaski_trap_podatki.csv")
print(f"Število pesmi: {len(df)}")

# 1. Povprečno število besed v pesmi

def prestej_vse_besede(besedilo):
    if isinstance(besedilo, str):
        return len(besedilo.split())
    return 0

df["Vse_Besede"] = df["Besedilo"].apply(prestej_vse_besede)

# tabela
statistika_dolzine = df.groupby("Izvajalec")["Vse_Besede"].describe().round(2)
display(statistika_dolzine)

# graf
plt.figure(figsize=(10, 4))
df.groupby("Izvajalec")["Vse_Besede"].mean().sort_values(ascending=False).plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("1. Povprečno število besed v pesmih")
plt.xlabel("Izvajalec")
plt.ylabel("Število besed")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Povprečna dolžina naslovov pesmi

def dolzina_naslova(naslov):
    if isinstance(naslov, str):
        return len(naslov)
    return 0

stolpec_naslov = "Naslov" if "Naslov" in df.columns else "Naslov_Pesmi"
df["Dolzina_Naslova"] = df[stolpec_naslov].apply(dolzina_naslova)
naslov_povprecje = df.groupby("Izvajalec")["Dolzina_Naslova"].mean().sort_values(ascending=False)

print("\n 2. Povprečna dolžina naslovov pesmi")
print(naslov_povprecje.round(2))

# graf
plt.figure(figsize=(10, 4))
naslov_povprecje.plot(kind="bar", color="gold", edgecolor="black")
plt.title("2. Povprečna dolžina naslovov pesmi")
plt.xlabel("Izvajalec")
plt.ylabel("Število znakov")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Uporaba trap slenga

skupne_ponovitve_besed = {"pare": 0, "lova": 0, "keš": 0, "euro": 0, "klub": 0, "brat": 0, "noć": 0}

def analiziraj_trap_sleng(besedilo):
    if not isinstance(besedilo, str):
        return 0
    besedilo_lower = besedilo.lower()
    
    p_pare = besedilo_lower.count("pare")
    p_lova = besedilo_lower.count("lova")
    p_kes = besedilo_lower.count("keš") or besedilo_lower.count("kes")
    p_euro = besedilo_lower.count("euro") or besedilo_lower.count("evro")
    p_klub = besedilo_lower.count("klub")
    p_brat = besedilo_lower.count("brat")
    p_noc = besedilo_lower.count("noć") or besedilo_lower.count("noc")
    
    skupne_ponovitve_besed["pare"] += p_pare
    skupne_ponovitve_besed["lova"] += p_lova
    skupne_ponovitve_besed["keš"] += p_kes
    skupne_ponovitve_besed["euro"] += p_euro
    skupne_ponovitve_besed["klub"] += p_klub
    skupne_ponovitve_besed["brat"] += p_brat
    skupne_ponovitve_besed["noć"] += p_noc
    
    return p_pare + p_lova + p_kes + p_euro + p_klub + p_brat + p_noc

df["Trap_Sleng_Skupaj"] = df["Besedilo"].apply(analiziraj_trap_sleng)

# tabela
tabela_slenga = df.groupby("Izvajalec")["Trap_Sleng_Skupaj"].agg(Skupaj='sum', Povprečno='mean').round(2)
display(tabela_slenga)

# graf
plt.figure(figsize=(10, 4))
df.groupby("Izvajalec")["Trap_Sleng_Skupaj"].mean().sort_values(ascending=False).plot(kind="bar", color="lightgreen", edgecolor="black")
plt.title("3. Uporaba trap slenga (povprečno ponovitev na pesem)")
plt.xlabel("Izvajalec")
plt.ylabel("Povprečno ponovitev")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# 4. Uporaba kletvic

def prestej_kletvice(besedilo):
    if not isinstance(besedilo, str):
        return 0
    besedilo_lower = besedilo.lower()
    
    kurva = besedilo_lower.count("kurv")
    sranje = besedilo_lower.count("sranj")
    jebi = besedilo_lower.count("jeb")
    kurac = besedilo_lower.count("kurac") + besedilo_lower.count("kurc")
    boga = besedilo_lower.count("boga")
    mater = besedilo_lower.count("mater")
    kmica = besedilo_lower.count("kmic")
    
    return kurva + sranje + jebi + kurac + boga + mater + kmica

df["Kletvice_Skupaj"] = df["Besedilo"].apply(prestej_kletvice)

# tabela
tabela_kletvic = df.groupby("Izvajalec")["Kletvice_Skupaj"].agg(Skupaj='sum', Povprečno='mean').round(2)
display(tabela_kletvic)

# graf
plt.figure(figsize=(10, 4))
df.groupby("Izvajalec")["Kletvice_Skupaj"].mean().sort_values(ascending=False).plot(kind="bar", color="tomato", edgecolor="black")
plt.title("4. Povprečna uporaba kletvic")
plt.xlabel("Izvajalec")
plt.ylabel("Povprečno ponovitev")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Pogostost izbranih besed

print("\nSKUPNA POGOSTOST IZBRANIH BESED")

df_besede = pd.DataFrame(list(skupne_ponovitve_besed.items()), columns=['Ključna beseda', 'Število ponovitev'])
df_besede = df_besede.sort_values(by='Število ponovitev', ascending=False).reset_index(drop=True)
display(df_besede)