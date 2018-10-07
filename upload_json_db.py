import MySQLdb as mysql
import json
import datetime as dt

from connect_db import connect

def insert_recipe(data):
    r_id = data['id']
    cur.execute('''
        INSERT INTO `recipe` (`id`, `creator_id`, `title`, `created_at`, `avg_star`, `img_path`)
        VALUES ('{}', '3', "{}", '{}', 0, 'none')
    '''.format(r_id, data['title'], dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    for i, ingredient in enumerate(data['ingredients']):
        insert_ingredient(r_id, i, ingredient['text'])
    for i, ingredient in enumerate(data['instructions']):
        insert_instruction(r_id, i, ingredient['text'])

def insert_ingredient(r_id, step, text):
    cur.execute('''
        INSERT INTO `ingredient` (`id`, `recipe_id`, `text`, `step`)
        VALUES (NULL, '{}', '{}', {})
    '''.format(r_id, text, step))

def insert_instruction(r_id, step, text):
    cur.execute('''
        INSERT INTO `instruction` (`id`, `recipe_id`, `text`, `step`)
        VALUES (NULL, '{}', '{}', {})
    '''.format(r_id, text, step))

if __name__ == '__main__':
    connect()
    cur = db.cursor()

    # === test for add user ===
    # cur.execute('''
    #     INSERT INTO `account` (`user_id`, `email`, `password`, `name`, `gender`, `pic_path`)
    #     VALUES (NULL, 'projectx@gmail.com', '', 'admin', 'none', '');
    # ''')

    # === insert recipe ===
    with open('./json/recipes.json') as json_f:
        data = json.loads(json_f.read())
    for d in data:
        insert_recipe(d)

    db.commit()
    db.close()
