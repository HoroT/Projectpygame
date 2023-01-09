def prov(self, login, parol, parol1):
    con = sqlite3.connect('reg.db')
    cur = con.cursor()
    result = cur.execute(
        f"""SELECT * FROM reg WHERE login = '{self.login}'""").fetchall()
    con.close()
    if len(login) < 4 or len(parol) < 4:
        self.label_2.setText('Длина должна быть более 4 символов')
    elif parol != parol1:
        self.label_2.setText('Пароли не совпадают!')
    elif parol.isalpha():
        self.label_2.setText('Неправильный ввод данных')
    elif len(result) != 0:
        self.label_2.setText('Этот логин уже занят')
    else:
        self.flag = 1
        self.reg()
        self.pushButton.setText('Завершить')
        self.label_2.setText('Вы успешно зарегестрированы')