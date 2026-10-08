SELECT SUM(prix * qte) AS chiffre_affaires_total FROM ventes;
SELECT produit, SUM(qte) AS quantite_vendue, SUM(prix * qte) AS chiffre_affaires FROM ventes GROUP BY produit ORDER BY chiffre_affaires DESC;
SELECT region, SUM(qte) AS quantite_vendue, SUM(prix * qte) AS chiffre_affaires FROM ventes;