import requests
import json
import csv

#Implementación para obtener los seguidores de una cuenta de Instagram de donde se obtendrán los datos para el proyecto.
#Por temas de privacidad, se omiten tanto los headers como el target_account. Si se desea probar el código, 
# se deben ingresar una cuenta de Instagram válida y los headers correspondientes a una sesión valida.

def get_user_id(username: str, headers: dict) -> str:
    profile_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    res = requests.get(profile_url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        try:
            return data['data']['user']['id']
        except KeyError:
            print("No se pudo extraer el ID del usuario.")
    else:
        print("Error al obtener el perfil:", res.status_code)
    return None

def get_followers_usernames(username: str, headers: dict, max_pages: int = 5) -> list:
    """
    Devuelve una lista de nombres de usuario de los seguidores de la cuenta indicada.
    """
    user_id = get_user_id(username, headers)
    if not user_id:
        return []

    # Query hash para obtener la lista de seguidores (sujeto a cambios)
    query_hash = "c76146de99bb02f6415203be841dd25a"
    
    variables = {
        "id": user_id,
        "include_reel": True,
        "first": 50,   # Número de seguidores por petición (ajusta según sea necesario)
        "after": None
    }
    
    followers_usernames = []
    
    for _ in range(max_pages):
        graphql_url = "https://www.instagram.com/graphql/query/"
        params = {
            "query_hash": query_hash,
            "variables": json.dumps(variables)
        }
        res = requests.get(graphql_url, params=params, headers=headers)
        if res.status_code != 200:
            print("Error en la consulta GraphQL:", res.status_code)
            break
        
        data = res.json()
        try:
            edges = data['data']['user']['edge_followed_by']['edges']
        except KeyError:
            print("No se encontró la información de los seguidores.")
            break
        
        for edge in edges:
            node = edge.get('node', {})
            if not node.get('is_private', True):
                follower_username = edge['node'].get('username')
                if follower_username:
                    followers_usernames.append(follower_username)
        
        page_info = data['data']['user']['edge_followed_by']['page_info']
        if page_info.get('has_next_page'):
            variables['after'] = page_info.get('end_cursor')
        else:
            break
    
    return followers_usernames

# Ejemplo de uso:
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "X-IG-App-ID": "936619743392459",
    "Cookie": "sessionid= ZZZZZZZZZZZZ; csrftoken=YYYYYYYYYYYY; datr=XXXXXXXXX; ig_did=ZZZZZZZZZZZZZZZZZZ; ds_user_id=YYYYYY; dpr=XXXX; mid=ZZZZZZ",  # Asegúrate de incluir ambos valores
    "X-CSRFToken": "y7hKZy1z6qeh6mSAjZZifzmwXN2a82vd",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Referer": "https://www.instagram.com/",
    "X-Requested-With": "XMLHttpRequest"
}


# Por ejemplo, para obtener los seguidores de una cuenta que sigues:
target_account = "cuenta_de_instagram"
followers = get_followers_usernames(target_account, headers, max_pages=20)
print(f"Se han obtenido {len(followers)} nombres de usuario de los seguidores:")
for username in followers:
    print(f"https://www.instagram.com/{username}/")
#for username in followers:
#    print(f"{username}")

with open("followers.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["username", "profile_url"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for username in followers:
        writer.writerow({
            "username": username,
            "profile_url": f"https://www.instagram.com/{username}/"
        })

print("Archivo followers.csv guardado con éxito.")

with open("followers.txt", "w", encoding="utf-8") as f:
    for username in followers:
        f.write(f"https://www.instagram.com/{username}/\n")

print("Archivo followers.txt guardado con éxito.")