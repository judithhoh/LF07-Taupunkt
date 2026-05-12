from flask import Flask
from flask import request
from objekte import relay
from taupunkt_db import taupunkt_db_class
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return (" <!DOCTYPE html><html><head><title>Taupunktlüfter</title></head><body><h1>Projekt LF07 Taupunktlüfter</h1>"
            "<p>hier entsteht eine Seite mit den minimalen anforderungn für das Projekt. Diese Anforderungen sind, <br>"
            "das die Messdaten von 2 dht22 Sensoren und nachfolgenden Berechungnen in eine Datenbank geschreiben <br>"
            "werden soll. Diese Daten sollen über eine Webseite (diese Webseite) ausgelesn und angezeigt werden <br>"
             "(die neusten also refrashing möglich). neben dem kontrollieren von dem Lüftr über die berechungen soll <br>"
              "dies auch manuel möglich sein (Button oder so)</p>"
            "<form method='GET' action='/tabelle'>"
            "<button type='submit'>Datenbank Tabelle</button>"
            "</form>"
            "<form method='GET' action='/button'>"
            "<button type='submit'>Lüfter Steuerung</button>"
            "</form>"

            "</body></html> ")

@app.route("/tabelle")
def tabelle():
    datenbank = taupunkt_db_class()
    eintrag_top_50 =datenbank.datenbank_refrash()
    webseite = ("<!DOCTYPE html>"
    "<html>"

    "<head>"
    "<title>Taupunktlüfter_tabelle</title>"

    "<style>"
    "table, th, td {"
    "border:1px solid black;"
    "border-collapse: collapse;"
    "padding: 5px;"
    "}"
    "</style>"

    "</head>"

    "<body>"
    "<form method='GET' action='/'>"
    "<button type='submit'>zurück</button>"
    "</form>"
    "<h1>Taupunktlüfter Tabelle</h1>"
    "<table style=\"width:100%\">"
    "<tr>"
    "<th>Timestemp</th>"
    "<th>A_Temperatur</th>"
    "<th>I_Temperatur</th>"
    "<th>A_Luftfeuchtigkeit</th>"
    "<th>I_Luftfeuchtigkeit</th>"
    "<th>A_Taupunkt</th>"
    "<th>I_Taupunkt</th>"
    "<th>TaupunktDelta</th>"
    "<th>Lüfter_status</th>"
    "</tr>")
    for datensatz in eintrag_top_50:
        webseite += (
            "<tr>"
            f"<td>{datensatz[6]}</td>"
            f"<td>{datensatz[3]} °C</td>"
            f"<td>{datensatz[1]} °C</td>"
            f"<td>{datensatz[4]} %</td>"
            f"<td>{datensatz[2]} %</td>"
            f"<td>{datensatz[8]:.2f} °C</td>"
            f"<td>{datensatz[9]:.2f} °C</td>"
            f"<td>{datensatz[5]:.2f}</td>"
            f"<td>{datensatz[7]}</td>"
            "</tr>"
        )
    webseite += (
        "</table>"

        "<form method='GET' action='/tabelle'>"
        "<button type='submit'>Neueste Daten</button>"
        "</form>"

        "</body></html>"
    )

    return webseite


@app.route("/button")
def button():
    status = "AN" if relay.get_state() else "AUS"

    erfolg = request.args.get("ok")

    meldung = ""

    if erfolg == "1":
        meldung = "<p>Lüfter erfolgreich umgeschaltet!</p>"

    return (
            "<!DOCTYPE html>"
            "<html>"
            "<head><title>Taupunktlüfter_Button</title></head>"
            "<body>"
            "<form method='GET' action='/'>"
            "<button type='submit'>zurück</button>"
            "</form>"
            "<h1>Taupunktlüfter Lüfter kontrolle</h1>"

            f"<p>Lüfter Status: {status}</p>"

            + meldung +

            "<form method='POST' action='/luefter'>"
            "<button type='submit'>"
            "Lüfter umschalten"
            "</button>"
            "</form>"

            "</body></html>"
    )

@app.route("/luefter", methods=["POST"])
def luefter_schalten():
    state = relay.get_state()
    if state:
        relay.close()
    else:
        relay.open()
    return redirect(url_for("button"))
