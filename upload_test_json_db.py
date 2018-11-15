import MySQLdb as mysql
import json
import datetime as dt

import connect_db as con

def update_recipe(recipe):
    r_id = recipe['id']

    img_path = 'none'
    if recipe.get('images'):
        img = recipe['images'][0]['id']

        data_path = 'media/data/images/test/'
        img = '/'.join(list(img.replace('.jpg',''))[0:4]) + '/' + img
        img_path = '/' + data_path + img

    sql = '''
        UPDATE `recipe` SET img_path = '{}'
        WHERE id = '{}'
    '''.format(img_path, r_id)
    cur.execute(sql)

def insert_recipe(recipe):
    r_id = recipe['id']
    title = recipe['title'].replace('"', "'").replace("'", "''")
    created_at = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    img_path = 'none'
    if recipe.get('images'):
        img_path = recipe['images'][0]['id']


    sql = '''
        INSERT INTO `recipe` (`id`, `creator_id`, `title`, `created_at`, `avg_star`, `img_path`, `source_type`)
        VALUES ('{}', '17', "{}", '{}', 0, '{}', 'temp')
    '''.format(r_id, title, created_at, img_path)
    cur.execute(sql)

    for i, ingredient in enumerate(recipe['ingredients']):
        insert_ingredient(r_id, i, ingredient['text'])
    for i, ingredient in enumerate(recipe['instructions']):
        insert_instruction(r_id, i, ingredient['text'])

def insert_ingredient(r_id, step, text):
    text = text.replace('"', "'").replace("'", "''")
    sql = '''
        INSERT INTO `ingredient` (`id`, `recipe_id`, `text`, `step`)
        VALUES (NULL, '{}', "{}", {})
    '''.format(r_id, text, step)
    cur.execute(sql)

def insert_instruction(r_id, step, text):
    text = text.replace('"', "'").replace("'", "''")
    sql = '''
        INSERT INTO `instruction` (`id`, `recipe_id`, `text`, `step`)
        VALUES (NULL, '{}', "{}", {})
    '''.format(r_id, text, step)
    cur.execute(sql)

if __name__ == '__main__':
    con.connect()
    cur = con.db.cursor()

    # === insert recipe ===
    with open('./json/test_all.json') as json_f:
        recipes = json.loads(json_f.read())

    for i, rec in enumerate(recipes):
        if i % 5000 == 0:
            print(i, len(recipes))
            con.db.commit()
        try:
            # insert_recipe(rec)
            update_recipe(rec)
        except Exception as e:
            # print(e)
            pass

    # for rec in recipes:
    #     insert_recipe(rec)

    con.db.commit()
    con.db.close()
