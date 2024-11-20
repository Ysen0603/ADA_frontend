import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# Connexion à la base de données MongoDB
client = MongoClient('mongodb+srv://yassineennaya2264:Q8jChRXcaBcuwtB@cluster0.kxill.mongodb.net/Project?retryWrites=true&w=majority')
db = client['Project']  

# Collections MongoDB
products_collection = db['products']
sales_collection = db['sales']

# Charger les données des fichiers CSV
products_df = pd.read_csv('products.csv', encoding='Windows-1252')
sales_df = pd.read_csv('sales.csv', encoding='Windows-1252')



# Insérer les produits dans la collection products
products_data = products_df.to_dict(orient='records')
products_collection.insert_many(products_data)

# Formater la date et insérer les ventes dans la collection sales
def convert_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')


sales_df['Date'] = sales_df['Date'].apply(convert_date)
sales_data = sales_df.to_dict(orient='records')
sales_collection.insert_many(sales_data)

print("Données insérées avec succès dans MongoDB !")
