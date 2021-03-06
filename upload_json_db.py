import MySQLdb as mysql
import json
import datetime as dt

import connect_db as con

def insert_recipe(recipe):
    r_id = recipe['id']
    title = recipe['title'].replace('"', "'").replace("'", "''")
    created_at = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if recipe['image_id'] == 'none':
        img_path = 'none'
    else:
        imgur_id = img_imgur[recipe['image_id']]
        img_path = 'https://i.imgur.com/{}.jpg'.format(imgur_id)

    sql = '''
        INSERT INTO `recipe` (`id`, `creator_id`, `title`, `created_at`, `avg_star`, `img_path`, `source_type`)
        VALUES ('{}', '17', "{}", '{}', 0, '{}', 'system')
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

    # === test for add user ===
    # cur.execute('''
    #     INSERT INTO `account` (`user_id`, `email`, `password`, `name`, `gender`, `pic_path`)
    #     VALUES (NULL, 'projectx@gmail.com', '', 'admin', 'none', '');
    # ''')

    # === insert recipe ===
    with open('./json/recipes_out.json') as json_f:
        recipes = json.loads(json_f.read())
    with open('./json/img_imgur.json') as json_f:
        img_imgur = json.loads(json_f.read())

    for rec in recipes:
        try:
            insert_recipe(rec)
        except:
            pass

    con.db.commit()
    con.db.close()
