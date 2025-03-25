from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main_html():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion_image')
def promote():
    return f'''<!doctype html>
    <html lang="en">
        <head>
            <title>Колонизация</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='styles/style.css')}">
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            
            <img src=https://static.tildacdn.com/tild3432-3939-4763-b237-393664633666/1.png 
            alt="здесь должна была быть картинка, но не нашлась">
            
            <h2 class=black>Человечеству мала одна планета.</h2>
            <h2 class="green">Человечество вырастает из детства.</h2>
            <h2 class="grey">Мы сделаем обитаемыми безжизненные пока планеты.</h2>
            <h2 class="yellow">И начнем с Марса!</h2>
            <h2 class="red">Присоединяйся!</h2>
        </body>
    </html>
    '''


@app.route('/foo')
def foo():
    names = ['Аня', 'Маша', 'Есения', 'Дина', 'Алина', 'Инга']
    s = ''
    for i, name in enumerate(names):
        s += f'<h{i + 1}>{name}</h{i + 1}>'
    return s


@app.route('/image_mars')
def image():
    return f''' <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src=https://static.tildacdn.com/tild3432-3939-4763-b237-393664633666/1.png 
    alt="здесь должна была быть картинка, но не нашлась">
    <p>Вот она такая, красная планета.</p>'''


@app.route('/css')
def css_sample():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='styles/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='styles/table.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>На участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <style>
                                        li {'{ list-style-type: none;}'}
                                        ul {'{ margin-left: 0; padding-left: 0;}'}
                                    </style>
                                    <ul>
                                        <li>
                                        <input type="checkbox" class="form-check-input" id="profession_1" name="accept">
                                        <label class="form-check-label" for="profession_1">Инженер-исследователь</label>
                                        </li>
                                        
                                        <li>
                                        <input type="checkbox" class="form-check-input" id="profession_2" name="accept">
                                        <label class="form-check-label" for="profession_2">Инженер-строитель</label>
                                        </li>
                                        
                                        <li>
                                        <input type="checkbox" class="form-check-input" id="profession_3" name="accept">
                                        <label class="form-check-label" for="profession_3">Пилот</label>
                                        </li>
                                        
                                        <li>
                                        <input type="checkbox" class="form-check-input" id="profession_4" name="accept">
                                        <label class="form-check-label" for="profession_4">Метеоролог</label>
                                        </li>
                                        
                                        <li>
                                        <input type="checkbox" class="form-check-input" id="profession_5" name="accept">
                                        <label class="form-check-label" for="profession_5">Инженер по жизнеобеспечению</label>
                                        </li>
                                        
                                        <li>
                                        <input type="checkbox" class="form-check-input" id="profession_6" name="accept">
                                        <label class="form-check-label" for="profession_6">Инженер по радиационной защите</label>
                                        </li>
                                        
                                        <li>
                                        <input type="checkbox" class="form-check-input" id="profession_7" name="accept">
                                        <label class="form-check-label" for="profession_7">Врач</label>
                                        </li>
                                        
                                        <li>
                                        <input type="checkbox" class="form-check-input" id="profession_8" name="accept">
                                        <label class="form-check-label" for="profession_8">Экзобиолог</label>
                                        </li>
                                    </ul>
                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите участвовать в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                        <input type="checkbox" class="form-check-input" id="accept" name="accept">
                                        <label class="form-check-label" for="profession_3">Готовы остаться на Марсе?</label>
                                    <div class="form-group">
                                        
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

@app.route('/two_params/<planet>')
def planet():
    return f''' <!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='styles/table.css')}" />
                    <title>Планета</title>
                  </head>
            '''
if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
