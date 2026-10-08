import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')


# Ventes (quantités) par produit
ventes_par_produit = données.groupby("produit", as_index=False)["qte"].sum()
fig_ventes = px.bar(
    ventes_par_produit,
    x="produit",
    y="qte",
    text="qte",
    title="Ventes par produit",
    labels={"produit": "Produit", "qte": "Quantité vendue"},
)
fig_ventes.write_html("ventes-par-produit.html")

# Chiffre d'affaires par produit
données["chiffre_affaires"] = données["prix"] * données["qte"]
ca_par_produit = données.groupby("produit", as_index=False)["chiffre_affaires"].sum()
fig_ca = px.bar(
    ca_par_produit,
    x="produit",
    y="chiffre_affaires",
    text="chiffre_affaires",
    title="Chiffre d'affaires par produit",
    labels={"produit": "Produit", "chiffre_affaires": "Chiffre d'affaires"},
)
fig_ca.write_html("ca-par-produit.html")

print('ventes-par-produit.html et ca-par-produit.html générés avec succès !')