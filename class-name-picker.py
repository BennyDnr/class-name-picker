import json
import os
import random
import pandas as pd
import streamlit as st

DATA_FILE = "schueler_daten_v2.json"

INITIAL_DATA = [
    # The Russians
    {
        "Name": "Alina",
        "Klasse": "8c",
        "Gruppe": "The Russians",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    {
        "Name": "Rafi",
        "Klasse": "8c",
        "Gruppe": "The Russians",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Flora",
        "Klasse": "8c",
        "Gruppe": "The Russians",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    {
        "Name": "Erik",
        "Klasse": "8c",
        "Gruppe": "The Russians",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Ilia",
        "Klasse": "8c",
        "Gruppe": "The Russians",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Jonah",
        "Klasse": "8c",
        "Gruppe": "The Russians",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Nico",
        "Klasse": "8c",
        "Gruppe": "The Russians",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Mia",
        "Klasse": "8c",
        "Gruppe": "The Russians",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    # Champions
    {
        "Name": "Lukas",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Levin",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Joni",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Noemi",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    {
        "Name": "Merle",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    {
        "Name": "Timo",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Darren",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Kilian",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Marie",
        "Klasse": "8c",
        "Gruppe": "Champions",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    # Forklift
    {
        "Name": "Maxi",
        "Klasse": "8c",
        "Gruppe": "Forklift",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Sofia",
        "Klasse": "8c",
        "Gruppe": "Forklift",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    {
        "Name": "Noah",
        "Klasse": "8c",
        "Gruppe": "Forklift",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Estelle",
        "Klasse": "8c",
        "Gruppe": "Forklift",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    {
        "Name": "Alicia",
        "Klasse": "8c",
        "Gruppe": "Forklift",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    {
        "Name": "Marlon",
        "Klasse": "8c",
        "Gruppe": "Forklift",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
    {
        "Name": "Selina",
        "Klasse": "8c",
        "Gruppe": "Forklift",
        "Geschlecht": "w",
        "Dran gewesen": False,
    },
    {
        "Name": "Cem",
        "Klasse": "8c",
        "Gruppe": "Forklift",
        "Geschlecht": "m",
        "Dran gewesen": False,
    },
]


def lade_daten():
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
      return pd.DataFrame(json.load(f))
  return pd.DataFrame(INITIAL_DATA)


def speichere_daten(df):
  df.to_json(DATA_FILE, orient="records", force_ascii=False, indent=4)


st.set_page_config(page_title="Mini Games & Paare", page_icon="🎮", layout="centered")
st.title("🎮 Schul-Tool: Mini Games & Paare")

df_schueler = lade_daten()

tab_minigames, tab_paare, tab_verwaltung = st.tabs(
    ["🎯 Mini Games", "👥 Paare", "⚙️ Klassen & Schüler verwalten"]
)

with tab_minigames:
  st.header("Mini Games – Team-Ziehung")

  if df_schueler.empty:
    st.warning("Keine Schüler vorhanden. Bitte unter Verwaltung anlegen.")
  else:
    klassen = sorted(df_schueler["Klasse"].unique().tolist())
    wahl_klasse = st.selectbox("Klasse für Mini Game wählen", klassen)

    df_klasse = df_schueler[df_schueler["Klasse"] == wahl_klasse]
    gruppen_in_klasse = sorted(df_klasse["Gruppe"].unique().tolist())

    st.info(
        f"Vorhandene Gruppen in dieser Klasse: {', '.join(gruppen_in_klasse)}"
    )

    anzahl_pro_gruppe = st.number_input(
        "Anzahl Spieler pro Gruppe, die antreten sollen",
        min_value=1,
        max_value=5,
        value=1,
    )

    if st.button("🎯 Spieler für Mini Game ziehen", type="primary"):
      st.subheader("Ausgeloste Spieler:")

      for grp in gruppen_in_klasse:
        df_grp = df_klasse[df_klasse["Gruppe"] == grp]
        offene_indices = df_grp[df_grp["Dran gewesen"] == False].index

        if len(offene_indices) < anzahl_pro_gruppe:
          df_schueler.loc[df_grp.index, "Dran gewesen"] = False
          offene_indices = df_grp.index
          st.toast(f"🔄 Lostopf für Gruppe '{grp}' wurde neu gemischt!")

        gezogene_indices = random.sample(
            list(offene_indices), min(anzahl_pro_gruppe, len(offene_indices))
        )
        df_schueler.loc[gezogene_indices, "Dran gewesen"] = True

        st.markdown(f"**Gruppe: {grp}**")
        for idx in gezogene_indices:
          name = df_schueler.loc[idx, "Name"]
          st.success(f"• {name}")

      speichere_daten(df_schueler)

    if st.button("Lostopf für diese Klasse komplett zurücksetzen"):
      df_schueler.loc[df_klasse.index, "Dran gewesen"] = False
      speichere_daten(df_schueler)
      st.success("Lostopf für die Klasse zurückgesetzt!")
      st.rerun()

with tab_paare:
  st.header("Paare bilden")

  klassen = sorted(df_schueler["Klasse"].unique().tolist())
  wahl_klasse_p = st.selectbox(
      "Klasse für Paare wählen", ["Alle Klassen"] + klassen
  )

  if wahl_klasse_p != "Alle Klassen":
    df_p = df_schueler[df_schueler["Klasse"] == wahl_klasse_p]
  else:
    df_p = df_schueler

  if st.button("Paare generieren", type="primary"):
    jungs = df_p[df_p["Geschlecht"].str.lower() == "m"]["Name"].tolist()
    maedchen = df_p[df_p["Geschlecht"].str.lower() == "w"]["Name"].tolist()

    random.shuffle(jungs)
    random.shuffle(maedchen)

    st.write(f"### Paare:")

    while jungs and maedchen:
      j = jungs.pop(0)
      m = maedchen.pop(0)
      st.markdown(f"* **{j}** & **{m}**")

    while len(jungs) >= 2:
      st.markdown(f"* **{jungs.pop(0)}** & **{jungs.pop(0)}**")
    if jungs:
      st.markdown(f"* **{jungs[0]}** *(bleibt übrig)*")

    while len(maedchen) >= 2:
      st.markdown(f"* **{maedchen.pop(0)}** & **{maedchen.pop(0)}**")
    if maedchen:
      st.markdown(f"* **{maedchen[0]}** *(bleibt übrig)*")

with tab_verwaltung:
  st.header("Klassen & Schüler verwalten")

  # --- EXPORT & IMPORT BEREICH ---
  col_exp, col_imp = st.columns(2)
  with col_exp:
    csv_bytes = df_schueler.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Alle Daten als CSV exportieren",
        data=csv_bytes,
        file_name="schueler_daten_export.csv",
        mime="text/csv",
    )

  with col_imp:
    with st.popover("📁 Daten per CSV importieren"):
      st.markdown("""
            **Struktur der CSV-Datei:**
            Die App unterstützt sowohl Dateien mit Kopfzeile als auch reine Datenzeilen (getrennt durch Komma oder Semikolon `;`).
            
            *Erwartete Spaltenreihenfolge (falls keine Kopfzeile da ist):*
            `Name`, `Klasse`, `Gruppe`, `Geschlecht`, `Dran gewesen (optional)`
            """)
      uploaded_csv = st.file_uploader("CSV-Datei auswählen", type=["csv"])
      if uploaded_csv is not None:
        try:
          # Versuche zu erkennen, ob eine Kopfzeile existiert
          first_line = uploaded_csv.readline().decode("utf-8")
          uploaded_csv.seek(0)
          
          has_header = any(col in first_line.lower() for col in ["name", "klasse", "geschlecht"])
          
          if has_header:
            df_imported = pd.read_csv(uploaded_csv, sep=None, engine="python")
          else:
            df_imported = pd.read_csv(uploaded_csv, sep=None, engine="python", header=None)
            # Spalten automatisch benennen
            if len(df_imported.columns) >= 4:
              df_imported.rename(columns={0: "Name", 1: "Klasse", 2: "Gruppe", 3: "Geschlecht"}, inplace=True)
              if len(df_imported.columns) >= 5:
                df_imported.rename(columns={4: "Dran gewesen"}, inplace=True)
            else:
              st.error("Die CSV-Datei hat zu wenige Spalten.")
              st.stop()

          # Pflichtspalten prüfen
          if "Name" in df_imported.columns and "Klasse" in df_imported.columns and "Geschlecht" in df_imported.columns:
            if "Gruppe" not in df_imported.columns:
              df_imported["Gruppe"] = "Standard"
            if "Dran gewesen" not in df_imported.columns:
              df_imported["Dran gewesen"] = False

            if st.button("Importierte Daten übernehmen"):
              df_schueler = pd.concat(
                  [df_schueler, df_imported], ignore_index=True
              )
              df_schueler = df_schueler.drop_duplicates(
                  subset=["Name", "Klasse"], keep="last"
              )
              speichere_daten(df_schueler)
              st.success("CSV erfolgreich importiert!")
              st.rerun()
          else:
            st.error("Fehler: Die Spalten konnten nicht automatisch zugeordnet werden.")
        except Exception as e:
          st.error(f"Fehler beim Lesen der Datei: {e}")

  st.divider()

  with st.expander("➕ Neue Klasse per Textfeld anlegen & aufteilen"):
    st.markdown("""
        Füge hier die Schüler ein. Pro Zeile ein Name, optional mit Komma und **m** oder **w**.
        Beispiel:
        ```text
        Flora, w
        Rafi, m
        Lukas
        ```
        """)
    neue_klasse_name = st.text_input("Name der neuen Klasse (z.B. 7b)")
    anzahl_gruppen = st.number_input(
        "Anzahl der Gruppen (z.B. 3)", min_value=1, max_value=10, value=3
    )
    rohtext = st.text_area("Schülerliste einfügen")

    if st.button("Klasse erstellen & Schüler aufteilen"):
      if not neue_klasse_name or not rohtext:
        st.error("Bitte Klassenname und Schülerliste angeben.")
      else:
        linien = rohtext.strip().split("\n")
        parsed_schueler = []

        for zeile in linien:
          parts = [p.strip() for p in zeile.split(",")]
          name = parts[0]
          geschlecht = ""
          if len(parts) > 1 and parts[1].lower() in ["m", "w"]:
            geschlecht = parts[1].lower()
          if name:
            parsed_schueler.append({"Name": name, "Geschlecht": geschlecht})

        random.shuffle(parsed_schueler)
        gruppen_namen = [f"Gruppe {i+1}" for i in range(int(anzahl_gruppen))]

        neue_eintraege = []
        for i, s in enumerate(parsed_schueler):
          zugewiesene_gruppe = gruppen_namen[i % len(gruppen_namen)]
          neue_eintraege.append({
              "Name": s["Name"],
              "Klasse": neue_klasse_name,
              "Gruppe": zugewiesene_gruppe,
              "Geschlecht": s["Geschlecht"],
              "Dran gewesen": False,
          })

        df_neu = pd.DataFrame(neue_eintraege)
        df_schueler = pd.concat([df_schueler, df_neu], ignore_index=True)
        speichere_daten(df_schueler)
        st.success(
            f"Klasse '{neue_klasse_name}' mit {len(neue_eintraege)} Schülern"
            " erfolgreich erstellt!"
        )
        st.rerun()

  st.divider()

  if df_schueler.empty:
    st.info("Keine Klassen vorhanden.")
  else:
    klassen = sorted(df_schueler["Klasse"].unique().tolist())
    klassen_tabs = st.tabs([f"Klasse: {k}" for k in klassen])

    for i, kl in enumerate(klassen):
      with klassen_tabs[i]:
        st.subheader(f"Verwaltung für Klasse: {kl}")

        df_kl = df_schueler[df_schueler["Klasse"] == kl]
        vorhandene_gruppen = sorted(df_kl["Gruppe"].unique().tolist())

        col_g1, col_g2 = st.columns(2)

        with col_g1:
          with st.expander("✏️ Gruppennamen bearbeiten"):
            altes_g = st.selectbox(
                "Welche Gruppe umbenennen?", vorhandene_gruppen, key=f"sel_{kl}"
            )
            neues_g = st.text_input(
                "Neuer Gruppenname", value=altes_g, key=f"txt_{kl}"
            )
            if st.button("Gruppe umbenennen", key=f"btn_g_{kl}"):
              if neues_g:
                df_schueler.loc[
                    (df_schueler["Klasse"] == kl)
                    & (df_schueler["Gruppe"] == altes_g),
                    "Gruppe",
                ] = neues_g
                speichere_daten(df_schueler)
                st.success(
                    f"Gruppe '{altes_g}' erfolgreich in '{neues_g}' umbenannt!"
                )
                st.rerun()

        with col_g2:
          with st.expander("🔀 Gruppen neu mischen"):
            st.markdown(
                "Teilt alle Schüler dieser Klasse zufällig auf eine Anzahl von"
                " Standard-Gruppen (Gruppe 1, Gruppe 2...) auf."
            )
            misch_anzahl = st.number_input(
                "Anzahl Zielgruppen",
                min_value=1,
                max_value=10,
                value=len(vorhandene_gruppen)
                if len(vorhandene_gruppen) > 0
                else 3,
                key=f"misch_anz_{kl}",
            )
            if st.button("Alle Schüler neu zuweisen", key=f"btn_misch_{kl}"):
              indices = df_schueler[df_schueler["Klasse"] == kl].index.tolist()
              random.shuffle(indices)
              neue_gruppen_namen = [
                  f"Gruppe {x+1}" for x in range(int(misch_anzahl))
              ]
              for idx_pos, idx in enumerate(indices):
                df_schueler.loc[idx, "Gruppe"] = neue_gruppen_namen[
                    idx_pos % len(neue_gruppen_namen)
                ]
              speichere_daten(df_schueler)
              st.success("Schüler wurden erfolgreich neu auf Gruppen gemischt!")
              st.rerun()

        st.markdown(
            "*(Tipp: Du kannst Zeilen direkt bearbeiten oder links in der"
            " Tabelle Zeilen ankreuzen und unten löschen)*"
        )

        edited_df_kl = st.data_editor(
            df_kl,
            num_rows="dynamic",
            use_container_width=True,
            key=f"editor_{kl}",
        )

        df_schueler = df_schueler[df_schueler["Klasse"] != kl]
        df_schueler = pd.concat(
            [df_schueler, edited_df_kl], ignore_index=True
        )

        col1, col2 = st.columns(2)
        with col1:
          if st.button(
              f"💾 Änderungen für Klasse {kl} speichern",
              key=f"save_{kl}",
              type="primary",
          ):
            speichere_daten(df_schueler)
            st.success(f"Änderungen für Klasse {kl} gespeichert!")
            st.rerun()

        with col2:
          if st.button(
              f"🗑️ Komplett gesamte Klasse {kl} löschen", key=f"del_{kl}"
          ):
            df_schueler = df_schueler[df_schueler["Klasse"] != kl]
            speichere_daten(df_schueler)
            st.warning(f"Klasse {kl} wurde gelöscht.")
            st.rerun()