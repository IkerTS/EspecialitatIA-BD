# By Iker T.S IA&BD
import requests
# Extraccio de les dades
def get_data_from_api(url):
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error recuperant dades de l'api: {e}")
    return None

# Url's API
def get_categories_url(category_id = ''):
    return f"https://tienda.mercadona.es/api/categories/{category_id}"

def get_products_url(product_id):
    return f"https://tienda.mercadona.es/api/products/{product_id}"

# Obtenir tots els id's i noms de les subcategories de una categoria, o totes les categories i subcategories
def get_categories(category_id = ''):
    data = get_data_from_api(get_categories_url(category_id))
    if not category_id:
        categories = [
            {
                'name': category['name'],
                'subcategories': [
                    {'id': subcat['id'], 'name': subcat['name']}
                    for subcat in category.get('categories', [])
                ]
            }
            for category in data['results']
        ]
    else:
        categories = {
                'name': data['name'],
                'subcategories': [
                    {'id': subcat['id'], 'name': subcat['name']}
                    for subcat in data['categories']
                ]
            }
    return categories

#print(get_categories(112))
#for x in get_categories():
#    print(x)

# Obtenir del category_id, tots els seus productes
def get_category_and_products(category_id):
    data = get_data_from_api(get_categories_url(category_id))
    products = []
    products_new = []
    for value in data['categories']:
        for product in value.get("products", []):
            price_info = product.get('price_instructions', {})
            is_new = price_info.get('is_new')
            unit_price = price_info.get('unit_price', 'Unknown')
            product_info = {
                'category_id': value.get('id', 'Unknown'),
                'category_name': value.get('name', 'Unknown'),
                'id_product': product.get('id', 'Unknown'),
                'product': product.get('display_name', 'Unknown'), 
                'is_new': is_new, 
                'unit_price': unit_price
            }
            products.append(product_info)
            # Si un producte es nou, afegir-ho en una llista amb tots els productes nous
            products_new.append(product_info) if is_new else None
    return products, products_new

#products, products_new = get_category_and_products(112)
#for x in products:
#    print(x)
#for x in products_new:
#    print(x)

# Obtenir de TOTES les categories, els seus productes
def get_all_category_and_products():
    data = get_categories()
    all_products = []
    all_products_new = []
    categories_id = [
        subcat['id']
        for category in data
        for subcat in category['subcategories']
    ]
    for category_id in categories_id:
        product, product_new = get_category_and_products(category_id)
        for x in product:
            products = {
                'pri_category': category_id,
                **x
            }
            all_products.append(products)
        for x in product_new:
            products_new = {
                'pri_category': category_id,
                **x
            }
            all_products_new.append(products_new)
    return all_products, all_products_new

#all_products, all_products_new = get_all_category_and_products()
#for x in all_products:
#    print(x)
#for x in all_products_new:
#    print(x)

# Ordenar els productes d'una categoria de producte per el seu preu descendent, mostrar el 10 primers
def sort_price(category_id):
    products = get_category_and_products(category_id)[0]
    products.sort(key=lambda x: float(x['unit_price']), reverse=True)
    return products[:10]

#for x in sort_price(112):
#    print(x)