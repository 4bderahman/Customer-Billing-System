clients = int(input("Le nombre des clients: "))
client = []
prixfinale = []

TVA = 0.15
remise = 0.02

for i in range(clients):
    client.append(input(f"Donner le nom et prenom du client {i + 1}: "))
    articles = int(input("Donner le nombre d'articles : "))
    somme = 0 
    for j in range(articles):
        prix_article = float(input(f"Donner le prix d'article {j + 1} : "))
        somme += prix_article
    
    TTC = somme + (somme * TVA)
    prix_final = TTC + (TTC * remise)
    prixfinale.append(prix_final)

print("FACTURE :")
for i in range(clients):
    print(f"Le total à payer pour le client {client[i]} : {prixfinale[i]} DHS")
