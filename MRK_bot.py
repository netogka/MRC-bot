import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import telebot
from telebot import types
bot = telebot.TeleBot("ТОКЕН")
english = None

@bot.message_handler(commands=["start"])
def start(message):
    on = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Вопросы📜")
    button2 = types.KeyboardButton("Проходные баллы 2021📊")
    button3 = types.KeyboardButton("Список документов📚")
    button4 = types.KeyboardButton("Общежитие🏢")
    button5 = types.KeyboardButton("Иностранным гражданам🌎")
    button6 = types.KeyboardButton("Стоимость обучения💰")
    button7 = types.KeyboardButton("Стоимость общежития💵")
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Наш сайт', url='https://www.mrk-bsuir.by/ru')
    english1 =types.InlineKeyboardButton(text="English",callback_data="1")
    russia1 = types.InlineKeyboardButton(text ="Русский",callback_data="2")
    markup.add(btn,english1,russia1)
    on.add(button1,button2,button3,button4,button5,button6,button7)
    bot.send_message(message.from_user.id, "Привет,{0.first_name}, я помогу ответить на все твои вопросы по поводу поступления в Минский Радиотехнический Колледж.".format(message.from_user),reply_markup=on)
    bot.send_message(message.from_user.id, "{0.first_name}, воспользуйся подсказками снизу, чтобы узнать больше о поступлении в МРК.".format(message.from_user),reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    english = False
    if call.data == "1":
        english = True
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Questions📜")
        button2 = types.KeyboardButton("Passing points 2021📊")
        button3 = types.KeyboardButton("List of documents📚")
        button4 = types.KeyboardButton("Dormitory🏢")
        button5 = types.KeyboardButton("Foreign citizens🌎")
        button6 = types.KeyboardButton("Tuition fees💰")
        button7 = types.KeyboardButton("The cost of a dormitory💵")
        on.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(call.message.chat.id, "You have switched to english",reply_markup=on)
    elif call.data =="2":
        english = False
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Вопросы📜")
        button2 = types.KeyboardButton("Проходные баллы 2021📊")
        button3 = types.KeyboardButton("Список документов📚")
        button4 = types.KeyboardButton("Информация об общежитии🏢")
        button5 = types.KeyboardButton("Иностранным гражданам🌎")
        button6 = types.KeyboardButton("Стоимость обучения💰")
        button7 = types.KeyboardButton("Стоимость общежития💵")
        on.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(call.message.chat.id, "Вы перешли на русский язык",reply_markup=on)
    return english

@bot.message_handler(content_types=['text', 'document', 'audio'])
def text_message(message):
    if message.text == "Проходные баллы 2021📊" or message.text == "Passing points 2021📊":
        f = open(r'passpoints.pdf', 'rb')
        bot.send_document(message.chat.id, f, timeout=150)
    elif message.text == "/reference":
        bot.send_message(message.chat.id, "Я бот, предназначенный для помощи абитуриентам МРК в вопросах поступления.")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Используй активные кнопки внизу для получения необходимой информации.")
    elif message.text == "Стоимость общежития💵" or message.text == "The cost of a dormitory💵":
        f = open(r'costdormitory.pdf', 'rb')
        bot.send_document(message.chat.id, f)
    elif message.text == "Стоимость обучения💰" or message.text == "Tuition fees💰":
        f = open(r'tuitionfees.pdf', 'rb')
        bot.send_document(message.chat.id, f)
    elif message.text == "Список документов📚" or message.text == "List of documents📚":
        f = open(r'documents.pdf', 'rb')
        bot.send_document(message.chat.id, f)
    elif message.text == "Иностранным гражданам🌎" or message.text == "Foreign citizens🌎":
        f = open(r'foreign.pdf', 'rb')
        bot.send_document(message.chat.id, f)
    elif message.text == "Общежитие🏢" or message.text == "Dormitory🏢":
        f = open(r'dormitory.pdf', 'rb')
        bot.send_document(message.chat.id, f)
    elif message.text == "Вопросы📜":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1️⃣")
        button2 = types.KeyboardButton("2️⃣")
        button3 = types.KeyboardButton("3️⃣")
        button4 = types.KeyboardButton("4️⃣")
        button5 = types.KeyboardButton("5️⃣")
        button6 = types.KeyboardButton("6️⃣")
        button7 = types.KeyboardButton("7️⃣")
        button8 = types.KeyboardButton("8️⃣")
        button9 = types.KeyboardButton("9️⃣")
        button10 = types.KeyboardButton("1️⃣0️⃣")
        button11 = types.KeyboardButton("1️⃣1️⃣")
        button12 = types.KeyboardButton("1️⃣2️⃣")
        button13 = types.KeyboardButton("1️⃣3️⃣")
        button14 = types.KeyboardButton("1️⃣4️⃣")
        button15 = types.KeyboardButton("1️⃣5️⃣")
        button16 = types.KeyboardButton("Задать вопрос❔")
        back = types.KeyboardButton("Назад↩")
        on.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, back)
        bot.send_message(message.chat.id,
                     text = "1.Чем отличается \"филиал БГУИР\" от простого колледжа?\n2.В случае нехватки баллов будет ли возможность перевести документы на другую специальность?\n3.Как правильно подсчитать проходной балл?\n4.Какие документы нужно предоставить на льготы?\n5.Можно ли при подаче документов на одну специальность параллельно подать документы на другую?\n"
                     "6.Можно ли поступить в колледж после 10 класса?\n7.Когда можно узнать проходные баллы?\n8.По каким прредметам считается проходной балл?\n9.Возможно ли перевестись с одного направления на другое в течение обучения?\n10.В каких числах можно подавать документы?\n"
                     "11.Есть ли возможность и на каких условиях продолжить обучение в УО БГУИР после окончания колледжа?\n12.Могут ли родители подать документы без присутствия ребенка?\n13.Каким образом происходит округление балла?\n14.Есть ли возможность при обучении в колледже перевестись на другую специальность?\n15.Работая на каких должностях присутсвует возможность поступить на заочное бюджетное обучение?",
                     reply_markup=on)
    elif message.text == "Questions📜":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1️⃣❔")
        button2 = types.KeyboardButton("2️⃣❔")
        button3 = types.KeyboardButton("3️⃣❔")
        button4 = types.KeyboardButton("4️⃣❔")
        button5 = types.KeyboardButton("5️⃣❔")
        button6 = types.KeyboardButton("6️⃣❔")
        button7 = types.KeyboardButton("7️⃣❔")
        button8 = types.KeyboardButton("8️⃣❔")
        button9 = types.KeyboardButton("9️⃣❔")
        button10 = types.KeyboardButton("1️⃣0️⃣❔")
        button11 = types.KeyboardButton("1️⃣1️⃣❔")
        button12 = types.KeyboardButton("1️⃣2️⃣❔")
        button13 = types.KeyboardButton("1️⃣3️⃣❔")
        button14 = types.KeyboardButton("1️⃣4️⃣❔")
        button15 = types.KeyboardButton("1️⃣5️⃣❔")
        button16 = types.KeyboardButton("Ask a question❔")
        back = types.KeyboardButton("Back↩")
        on.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, back)
        bot.send_message(message.chat.id, "1. What is the difference between \"BSUIR branch\" and a simple college?\n2.In case of a shortage of points, will it be possible to transfer documents to another specialty?\n3.How to calculate the passing score correctly?\n4.What documents do I need to provide for benefits?\n5.Is it possible, when applying for one specialty, to apply for another in parallel?\n6.Is it possible to go to college after the 10th grade?\n7.When can I find out the passing scores?\n8.By what criteria is a passing score considered?\n9.Is it possible to transfer from one direction to another during the training?\n10.In what numbers can I submit documents?\n11.Is there an opportunity and under what conditions to continue studying at the UO BSUIR after graduating from college?\n12.Can parents submit documents without the presence of a child?\n 13.How does the rounding of the score occur?\n14.Is there an opportunity to transfer to another specialty while studying at college?\n15.Working in what positions is there an opportunity to enroll in correspondence budget training?", reply_markup=on)
    else:
        answer(message)

def answer(message):
    if message.text == "1️⃣":
        bot.send_message(message.chat.id, "До 2015 года наш колледж являлся учреждением высшего образования, в котором учащиеся после получения среднего специального образования имели возможность получить и высшее образование. С 2015 года мы стали филиалом БГУИР. С этого времени в колледже ребята получают только среднее специальное образования, потом в сокращенные сроки в БГУИРе получают высшее образование.")
    elif message.text == "2️⃣":
        bot.send_message(message.chat.id, "Да, можно будет. Только в отведенные сроки приема документов. Следите за датами приема документов.")
    elif message.text == "3️⃣":
        bot.send_message(message.chat.id, "Результаты двух ЦТ (язык и математика) со 100-балльной шкалы переводятся в 10-балльную. Плюс к этому добавляется средний балл Вашего документа об образовании. При поступлении в колледж принимаются сертификаты от 1 до 100 баллов. Так называемые пороги по набранным баллам на ЦТ для учреждений среднего специального образования не существуют. Главное пройти по конкурсу - у кого общее количество баллов выше, тот и поступит (суммируются баллы по двум сертификатам + средний балл документа об образовании).")
    elif message.text == "4️⃣":
        bot.send_message(message.chat.id, "Необходимо предоставить документы подтверждающие Ваше право на льготы (удостоверение многодетной семьи).")
    elif message.text == "5️⃣":
        bot.send_message(message.chat.id, "Нет. Если Вы видите, что не проходите по баллам, Вам необходимо явиться в приемную комиссию и подать в установленные сроки документы на другую специальность (переписать заявление, переоформить договор с указанием новой специальности).")
    elif message.text == "6️⃣":
        bot.send_message(message.chat.id, "Да, на специальности на базе 9 кл. При поступлении на базе 9 кл. будет учитываться  документ об образовании за 9 кл., соответственно, отметки за 10 кл. не учитываются.")
    elif message.text == "7️⃣":
        bot.send_message(message.chat.id, "Проходные баллы можно узнать только после окончания приема документов на обучение. Вступительные испытания – конкурс среднего балла документа об образовании.")
    elif message.text == "8️⃣":
        bot.send_message(message.chat.id, "Средний балл выводится из общей суммы баллов всех предметов, отмеченных в документе об образовании.")
    elif message.text == "9️⃣":
        bot.send_message(message.chat.id, "Перевестись сложно, для этого необходимо, чтобы освободилось место. Перевод возможен только после первого курса при наличии вакантных мест.")
    elif message.text == "1️⃣0️⃣":
        bot.send_message(message.chat.id, "С 20 июля.")
    elif message.text == "1️⃣1️⃣":
        bot.send_message(message.chat.id, "После окончания колледжа возможно обучение в сокращенные сроки (3 года) в БГУИРе. Для этого необходимо в БГУИРе сдать два внутренних экзамена в письменной форме и пройти конкурс или по результатам ЦТ поступить на полный срок. Уточняйте все нюансы поступления в приемной комиссии БГУИР (2 корпус, 310 каб.).")
    elif message.text == "1️⃣2️⃣":
        bot.send_message(message.chat.id, "В случае подачи документов от имени абитуриента его законным представителем предъявляются документы, удостоверяющие личность и статус законного представителя, и копия документа, удостоверяющего личность и статус абитуриента. В случае подачи документов от имени абитуриента его представителем, действующим на основании доверенности, предъявляются документ, удостоверяющий личность представителя, копия документа, удостоверяющего личность абитуриента, и доверенность, заверенная нотариально или уполномоченным должностным лицом.")
    elif message.text == "1️⃣3️⃣":
        bot.send_message(message.chat.id, "Существует правило округления, суть которого в следующем: если число округляют до какого-нибудь разряда, то все следующие за этим разрядом цифры заменяют нулями, а если они стоят после запятой, то их отбрасывают. Если первая отброшенная или замененная нулем цифра равна 5 и выше, то стоящую перед ней цифру увеличивают на 1. Если первая отброшенная или замененная нулем цифра меньше 5, то стоящую перед ней цифру оставляют без изменения.")
    elif message.text == "1️⃣4️⃣":
        bot.send_message(message.chat.id, "Перевод на вакантные места лиц, зачисленных по иным специальностям (направлениям специальностей), или зачисление на указанные места лиц, не прошедших по конкурсу или отчисленных с иных специальностей (направлений специальностей), не допускается.")
    elif message.text == "1️⃣5️⃣":
        bot.send_message(message.chat.id, "Тестировщик программного обеспечения, техник по защите информации, техник вычислительного (информационно-вычислительного) центра,оператор электронно-вычислительных машин, другие должности, связанные с обслуживанием, администрированием информационно-компьютерных сетей; лица, имеющие профессионально-техническое образование с общим средним образованием по следующим специальностям: документоведение, информационное и организационное обслуживание, техническое обслуживание и ремонт электронно-вычислительной техники, эксплуатация электронно-вычислительных машин.")
    elif message.text == "Назад↩":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Вопросы📜")
        button2 = types.KeyboardButton("Проходные баллы 2021📊")
        button3 = types.KeyboardButton("Список документов📚")
        button4 = types.KeyboardButton("Общежитие🏢")
        button5 = types.KeyboardButton("Иностранным гражданам🌎")
        button6 = types.KeyboardButton("Стоимость обучения💰")
        button7 = types.KeyboardButton("Стоимость общежития💵")
        on.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, text="Вы вернулись в меню", reply_markup=on)
    elif message.text == "1️⃣❔":
        bot.send_message(message.chat.id, "Until 2015, our college was an institution of higher education, in which students after receiving secondary special education had the opportunity to receive higher education. Since 2015, we have become a branch of BSUIR. Since that time, the students receive only secondary specialized education in college, then they receive higher education in a shortened period in BSUIR.")
    elif message.text == "2️⃣❔":
        bot.send_message(message.chat.id, "Yes, it will be possible. Only within the allotted time for receiving documents. Keep track of the dates of receipt of documents.")
    elif message.text == "3️⃣❔":
        bot.send_message(message.chat.id, "The results of two CT (language and mathematics) are translated from a 100-point scale to a 10-point scale. Plus, the average score of your education document is added to this. Certificates from 1 to 100 points are accepted for admission to the college. The so-called thresholds for points scored on the CT for institutions of secondary special education do not exist. The main thing is to pass the competition - whoever has the total number of points higher, he will enter (the points for two certificates are summed up + the average score of the education document).")
    elif message.text == "4️⃣❔":
        bot.send_message(message.chat.id, "It is necessary to provide documents confirming your right to benefits (certificate of a large family).")
    elif message.text == "5️⃣❔":
        bot.send_message(message.chat.id, "No. If you see that you do not pass the points, you need to appear at the admissions committee and submit documents for another specialty within the prescribed time (rewrite the application, reissue the contract indicating the new specialty).")
    elif message.text == "6️⃣❔":
        bot.send_message(message.chat.id, "Yes, on a specialty based on 9 cl. When enrolling on the basis of the 9th grade, the education document for the 9th grade will be taken into account, respectively, marks for the 10th grade are not taken into account.")
    elif message.text == "7️⃣❔":
        bot.send_message(message.chat.id, "Passing points can be found out only after the end of accepting documents for training. Entrance tests - competition of the average score of the document on education.")
    elif message.text == "8️⃣❔":
        bot.send_message(message.chat.id, "The average score is derived from the total score of all subjects marked in the education document.")
    elif message.text == "9️⃣❔":
        bot.send_message(message.chat.id, "It is difficult to transfer, for this it is necessary to free up space. Transfer is possible only after the first year, if there are vacancies.")
    elif message.text == "1️⃣0️⃣❔":
        bot.send_message(message.chat.id, "Since July 20th.")
    elif message.text == "1️⃣1️⃣❔":
        bot.send_message(message.chat.id, "After graduating from college, it is possible to study in a shortened period (3 years) in BSUIR. To do this, it is necessary to pass two internal exams in writing at the BSUIR and pass a competition or, according to the results of the CT, enroll for a full term. Clarify all the nuances of admission in the admissions committee of BSUIR (2nd building, 310 kab.).")
    elif message.text == "1️⃣2️⃣❔":
        bot.send_message(message.chat.id, "In case of submission of documents on behalf of the applicant, his legal representative presents documents certifying the identity and status of the legal representative, and a copy of the document certifying the identity and status of the applicant. If documents are submitted on behalf of the applicant by his representative acting on the basis of a power of attorney, a representative's identity document, a copy of the applicant's identity document, and a power of attorney certified by a notary or an authorized official are presented.")
    elif message.text == "1️⃣3️⃣❔":
        bot.send_message(message.chat.id,"There is a rounding rule, the essence of which is as follows: if a number is rounded to some digit, then all the digits following this digit are replaced with zeros, and if they are after the decimal point, they are discarded. If the first discarded or zero-replaced digit is 5 and higher, then the digit in front of it is increased by 1. If the first discarded or zero-replaced digit is less than 5, then the digit in front of it is left unchanged.")
    elif message.text == "1️⃣4️⃣❔":
        bot.send_message(message.chat.id, "Transfer to vacant places of persons enrolled in other specialties (areas of specialties), or enrollment in these places of persons who did not pass the competition or expelled from other specialties (areas of specialties) is not allowed.")
    elif message.text == "1️⃣5️⃣❔":
        bot.send_message(message.chat.id, "Software tester, information security technician, technician of computing (information and computing) center, operator of electronic computers, other positions related to maintenance, administration of information and computer networks; persons with vocational and technical education with general secondary education in the following specialties: documentation, information and organizational maintenance, maintenance and repair of electronic computing equipment, operation of electronic computers.")
    elif message.text == "Back↩":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Questions📜")
        button2 = types.KeyboardButton("Passing points 2021📊")
        button3 = types.KeyboardButton("List of documents📚")
        button4 = types.KeyboardButton("Dormitory🏢")
        button5 = types.KeyboardButton("Foreign citizens🌎")
        button6 = types.KeyboardButton("Tuition fees💰")
        button7 = types.KeyboardButton("The cost of a dormitory💵")
        on.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, "You are back in the menu", reply_markup=on)
    elif message.text == "Задать вопрос❔":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Назад⬅")
        on.add(button1)
        bot.send_message(message.chat.id, "Задайте вопрос, которого нет в списке выше.", reply_markup=on)
        bot.register_next_step_handler(message, questionsru)
    elif message.text == "Ask a question❔":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Back⬅")
        on.add(button1)
        bot.send_message(message.chat.id, "Ask a question that is not in the list above.", reply_markup=on)
        bot.register_next_step_handler(message, questionsen)
    elif message.text == "Назад⬅":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1️⃣")
        button2 = types.KeyboardButton("2️⃣")
        button3 = types.KeyboardButton("3️⃣")
        button4 = types.KeyboardButton("4️⃣")
        button5 = types.KeyboardButton("5️⃣")
        button6 = types.KeyboardButton("6️⃣")
        button7 = types.KeyboardButton("7️⃣")
        button8 = types.KeyboardButton("8️⃣")
        button9 = types.KeyboardButton("9️⃣")
        button10 = types.KeyboardButton("1️⃣0️⃣")
        button11 = types.KeyboardButton("1️⃣1️⃣")
        button12 = types.KeyboardButton("1️⃣2️⃣")
        button13 = types.KeyboardButton("1️⃣3️⃣")
        button14 = types.KeyboardButton("1️⃣4️⃣")
        button15 = types.KeyboardButton("1️⃣5️⃣")
        button16 = types.KeyboardButton("Задать вопрос❔")
        back = types.KeyboardButton("Назад↩")
        on.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, back)
        bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=on)
    elif message.text == "Back⬅":
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("1️⃣❔")
        button2 = types.KeyboardButton("2️⃣❔")
        button3 = types.KeyboardButton("3️⃣❔")
        button4 = types.KeyboardButton("4️⃣❔")
        button5 = types.KeyboardButton("5️⃣❔")
        button6 = types.KeyboardButton("6️⃣❔")
        button7 = types.KeyboardButton("7️⃣❔")
        button8 = types.KeyboardButton("8️⃣❔")
        button9 = types.KeyboardButton("9️⃣❔")
        button10 = types.KeyboardButton("1️⃣0️⃣❔")
        button11 = types.KeyboardButton("1️⃣1️⃣❔")
        button12 = types.KeyboardButton("1️⃣2️⃣❔")
        button13 = types.KeyboardButton("1️⃣3️⃣❔")
        button14 = types.KeyboardButton("1️⃣4️⃣❔")
        button15 = types.KeyboardButton("1️⃣5️⃣❔")
        button16 = types.KeyboardButton("Ask a question❔")
        back = types.KeyboardButton("Back↩")
        on.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, back)
        bot.send_message(message.chat.id, "You came back", reply_markup=on)
    else:
        bot.send_message(message.chat.id, text="Увы, я такое не умею")

@bot.message_handler(content_types=['text'])
def questionsru(message):
    try:
        username = "{0.username}".format(message.from_user, bot.get_me())
        fromaddr = "abiturientmrk@gmail.com"
        mypass = "rrprgvbepmxhognl"
        toaddr = "zam_ur@mrk-bsuir.by"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Отправитель: " #+ str(message.chat.id)
        if message.text != "Назад⬅":
            on = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Назад⬅")
            on.add(button1)
            body = message.text
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, mypass)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            bot.reply_to(message, "Спасибо, Ваше сообщение отправлено📨.", reply_markup=on)
        else:
            on = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("1️⃣")
            button2 = types.KeyboardButton("2️⃣")
            button3 = types.KeyboardButton("3️⃣")
            button4 = types.KeyboardButton("4️⃣")
            button5 = types.KeyboardButton("5️⃣")
            button6 = types.KeyboardButton("6️⃣")
            button7 = types.KeyboardButton("7️⃣")
            button8 = types.KeyboardButton("8️⃣")
            button9 = types.KeyboardButton("9️⃣")
            button10 = types.KeyboardButton("1️⃣0️⃣")
            button11 = types.KeyboardButton("1️⃣1️⃣")
            button12 = types.KeyboardButton("1️⃣2️⃣")
            button13 = types.KeyboardButton("1️⃣3️⃣")
            button14 = types.KeyboardButton("1️⃣4️⃣")
            button15 = types.KeyboardButton("1️⃣5️⃣")
            button16 = types.KeyboardButton("Задать вопрос❔")
            back = types.KeyboardButton("Назад↩")
            on.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
                   button12, button13, button14, button15, button16, back)
            bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=on)
    except Exception:
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Back⬅")
        on.add(button1)
        bot.reply_to(message, "Произошла ошибка отправки⛔Попробуйте позже.", reply_markup=on)

def questionsen(message):
    try:
        username = "{0.username}".format(message.from_user, bot.get_me())
        fromaddr = "abiturientmrk@gmail.com"
        mypass = "rrprgvbepmxhognl"
        toaddr = "zam_ur@mrk-bsuir.by"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Отправитель: " #+ str(message.chat.id)
        if message.text != "Back⬅":
            on = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Back⬅")
            on.add(button1)
            body = message.text
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, mypass)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            bot.reply_to(message, "Thank you, your message has been sent📨.", reply_markup=on)
        else:
            on = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("1️⃣❔")
            button2 = types.KeyboardButton("2️⃣❔")
            button3 = types.KeyboardButton("3️⃣❔")
            button4 = types.KeyboardButton("4️⃣❔")
            button5 = types.KeyboardButton("5️⃣❔")
            button6 = types.KeyboardButton("6️⃣❔")
            button7 = types.KeyboardButton("7️⃣❔")
            button8 = types.KeyboardButton("8️⃣❔")
            button9 = types.KeyboardButton("9️⃣❔")
            button10 = types.KeyboardButton("1️⃣0️⃣❔")
            button11 = types.KeyboardButton("1️⃣1️⃣❔")
            button12 = types.KeyboardButton("1️⃣2️⃣❔")
            button13 = types.KeyboardButton("1️⃣3️⃣❔")
            button14 = types.KeyboardButton("1️⃣4️⃣❔")
            button15 = types.KeyboardButton("1️⃣5️⃣❔")
            button16 = types.KeyboardButton("Ask a question❔")
            back = types.KeyboardButton("Back↩")
            on.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
                   button12, button13, button14, button15, button16, back)
            bot.send_message(message.chat.id, "You came back", reply_markup=on)
    except Exception:
        on = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Back⬅")
        on.add(button1)
        bot.reply_to(message, "A sending error has occurred⛔Try again later.")
bot.polling(none_stop=True, interval=0)