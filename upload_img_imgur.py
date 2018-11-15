import base64, requests
import json, time

def openIMG(f_name):
    with open(f_name, 'rb') as img_f:
        raw_str = img_f.read()
        base64_str = base64.b64encode(raw_str)
    return base64_str

def uploadIMG(img_id):
    upload_url = 'https://api.imgur.com/3/image'
    head = {'Authorization': 'Client-ID b454dd1ee56691e',
            'Authorization': 'Bearer 24dc7968030e2e64f23494e759655c32de8e480c'}

    img_base64 = openIMG('./img/{}'.format(img_id))
    data = {
        'image': img_base64,
        'album': '4PbT8jC', # peojct-recipe
        'type': 'base64',
        'name': img_id,
        'title': img_id,
        'description': img_id
    }

    res = requests.post(upload_url, headers=head, data=data)
    res = res.json()
    print(res)

    time.sleep(2)

    return res['data']['id']

def show_albums():
    upload_url = 'https://api.imgur.com/3/account/teacher144123/albums'
    head = {'Authorization': 'Client-ID b454dd1ee56691e',
            'Authorization': 'Bearer 24dc7968030e2e64f23494e759655c32de8e480c'}

    res = requests.get(upload_url, headers=head)
    # print(res.text)
    data = res.json()
    print(data)

if __name__ == '__main__':
    with open('./json/recipes_out.json') as json_f:
        recipes = json.loads(json_f.read())
    with open('./json/img_imgur.json') as json_f:
        img_imgur = json.loads(json_f.read())

    for i, rec in enumerate(recipes):
        img_id = rec['image_id']
        if img_id != 'none' and img_id not in img_imgur:
            print('{} / {}'.format(i, len(recipes)), img_id)
            imgur_id = uploadIMG(img_id)
            img_imgur[img_id] = imgur_id

    with open('./json/img_imgur.json', 'w') as json_f:
        json_f.write(json.dumps(img_imgur, indent=2))
