import json

if __name__ == '__main__':
    with open('./json/recipes.json') as json_f:
        recipes = json.loads(json_f.read())

    with open('./json/recipe_images.json') as json_f:
        rec_imgs = json.loads(json_f.read())

    print(len(recipes))
    print(len(rec_imgs))

    img_ids = [rec['id'] for rec in rec_imgs]
    id_idxs = { id:idx for idx, id in enumerate(img_ids)}

    for rec in recipes:
        if rec['id'] in img_ids:
            id = rec['id']
            idx = id_idxs[id]
            rec['image_id'] = rec_imgs[idx]['images'][0]['id']
        else:
            rec['image_id'] = 'none'

    print('\n'.join([rec['image_id'] + ' ' + rec['partition'] for rec in recipes]))

    # write back
    with open('./json/recipes_out.json', 'w') as json_f:
        json_f.write(json.dumps(recipes, indent=2, separators=[',', ': ']))
