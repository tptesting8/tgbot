from tg_bot import dispatcher

RUN_STRINGS = (
    "Куди ти зібрався?",
    "А? Шо? Вони пішли?"
    "ZZzzZZzz... А? Шо? о, знову тільки вони, нічого."
    "Повернися сюди.",
    "Не так швидко...",
    "Подивися на стіну!",
    "Не лишайте мене з ними!!",
    "Ти біжиш, ти помираєш.",
    "Ти пошкодуєщ...",
    "Ви можете спробувати /kickme, я чула, що це цікаво.",
    "Іди, потурбуй когось іншого, тут всім байдуже.",
    "Ти біжи, але тобі не сховатися.",
    "Це все, що в тебе є?",
    "Я стою позаду...",
    "У тебе є компанія!",
    "Ми можемо зробити це легким або складним шляхом.",
    "Ти просто не розумієщ цього, чи не так?",
    "Так, тобі краще тікати!",
    "Будь-ласка, нагадай мені, наскільки мені це важливо?",
    "На твоєму місці я б біжав швидше.",
    "Це точно той дроід, якого ми шукаємо.",
    "Най вдача буде на вашій стороні.",
    "Усім відомі останні слова.",
    "Вони зникли назавжди, щоб їх більше не бачили.",
    "\"О, подивись на мене! Я настільки крутий, що можу втікти від Бога! \"- це людина",
    "Так, так, просто натисніть /kickme уже.",
    "Ось, візьміть це кільце й держіть курс на Мордор, вам все одно по дорозі.",
    "За давніми легендами, вони ще біжать...",
    "На відміну від Гарі Потера, твоі батьки не зможуть захистити тебе від мене.",
    "Страх приводить до гніву. Гнів приводить до ненависті. Ненависть приводить до стражданнь. Якщо ви продовжите тікати в страху, ви можете "
    "стати наступним Вейдером.",
    "Кілька розрахунків після, я вирішив, що мій інтерес до ваших махінацій рівно 0.",
    "Продовжуйте, не впевнений, що ми хочемо, щоб ви тут лишались.",
    "Ти маг-ОЙ. Зажди. Ти не Гарі, продовжуйте рух.",
    "НЕ БІГАТИ ПО КОРИДОРАМ!",
    "Hasta la vista, дєтка.",
    "Хто випустив собаку?",
    "Це смішно тому, що всім пофіг.",
    "Ах, яка втрата. Він мені подобався.",
    "Чесно кажучи, моя дорогенька, мені байдуже.",
    "Ви не можете йти проти правди!",
    "Давним-давно, в далкекій-далекій галактиці... Комусь вони були потрібні. Але вже ні.",
    "Ех, подивись на них! Вони тікають від неминучого банхаммера... Мило.",
    "Хан стріляв першим. Я зроблю так, як він.",
    "Навіщо ти біжиш за білим кроликом?",
    "Як сказав би Доктор... Біжи!",
)

SLAP_TEMPLATES = (
    "{user1} {hits} {user2} {itemp}.",
    "{user1} {hits} в лице {user2} {itemp}.",
    "{user1} {throws} {itemr} в {user2}.",
    "{user1} бере {item} та {throws} їм в обличчя {user2}.",
    "{user1} запускає {itemr} в напрямку {user2}.",
    "{user1} розпочинає необразливо плескати {user2} {itemp}.",
    "{user1} притискає {user2} та кілька разів {hits} його {itemp}.",
    "{user1} хапає {itemr} та {hits} {user2}",
    "{user1} прив'язує {user2} до стільця й {throws} {itemr} у нього.",
    "{user1} по дружньому підштовхнув {user2}, щоб той швидше навчився плавати в лаві."
)

ITEMS =  (
    "чавунна сковорідка",
    "велика форель",
    "бейсбольна біта",
    "крикетна біта",
    "дерев'яна палиця",
    "ніготь",
    "принтер",
    "лопата",
    "ЕЛТ-монітор",
    "книжка з фізики ",
    "тостер",
    "портрет Річарда Столмана",
    "телевізор",
    "п'ятитонна машина",
    "рулон клейкої стрічки",
    "книга",
    "ноутбук",
    "старий телевізор",
    "мішок каменів",
    "форель",
    "гумове курчатко",
    "шипаста летюча миша",
    "вогнегасник",
    "важкий камінь",
    "шматок гімна",
    "вулик",
    "шматок гнилого м'яса",
    "ведмідь",
    "тонна цеглин",
)

ITEMSP_UA =  (
    "чавунною сковорідкою",
    "великою фореллю",
    "бейсбольною бітою",
    "крикетною бітой",
    "дерев'яною палицею",
    "нігтем",
    "принтером",
    "лопатою",
    "ЕЛТ-монітором",
    "книжкою з фізики ",
    "тостером",
    "портретом Річарда Столмана",
    "телевізором",
    "пятитонною машиною",
    "рулоном скотча",
    "книгою",
    "ноутбуком",
    "старим телевізором",
    "мішком каменів",
    "фореллю",
    "гумовим курчатком",
    "шипастою летючею мишею",
    "вогнегасником",
    "важким каменем",
    "шматком гімна",
    "улеєм",
    "шматком гнилого м'яса",
    "ведмедем",
    "тонною цеглин",
    "гігантським пиріжком",
)

ITEMSR_UA =  (
    "чавунну сковорідку",
    "велику форель",
    "бейсбольну біту",
    "крикетну біту",
    "дерев'яну палицю",
    "ніготь",
    "принтер",
    "лопату",
    "ЕЛТ-монітор",
    "книжку з фізики",
    "тостер",
    "портрет Річарда Столмана",
    "телевізор",
    "п'ятитону машинк",
    "рулон скотчу",
    "книгу",
    "ноутбук",
    "старий телевізор",
    "мішок каменів",
    "форель",
    "гумове курча",
    "шипасту летучу мишу",
    "вогнегасник",
    "важкий камінь",
    "шматок гімна",
    "вулик",
    "шматок гнилого м'яса",
    "ведмедя",
    "тонну цеглин",
)


THROW =  (
    "кидає",
    "швиряє",
    "роняє",
)

HIT =  (
    "б'є",
    "молотить",
    "шльопає",
    "хлопає",
    "колотить",
    "царапає",
)

UkrainianStrings = {

#Connections
    "Disabled connections to this chat for users": "Від'єднані з'єднання в цьому чаті для користувачів",
    "Enabled connections to this chat for users": "Увімкнені з'єднання в цьому чаті для користувачів",
    "Please enter on/yes/off/no in group!": "Будь-ласка введіть on/yes/off/no в групу!",
    "Successfully connected to *{}*": "Успішно під'єднано до *{}*",
    "Connection failed!": "З'єднання не вдалось!",
    "Connections to this chat not allowed!": "Під'єднання до цього чату не дозволено!",
    "Write chat ID to connect!": "Напишіть ID чату для під'єднання",
    "Usage limited to PMs only!": "Використання лімітовано лише для особистих повідомлень!",

#Admin
    "How am I meant to promote someone that's already an admin?": "Як я можу призначити адміном того, хто вже ним являється?",
    "I can't promote myself! Get an admin to do it for me.": "Я не можу призначити себе! Отримайте адміністратора, щоб зробити це для мене.",
    "Successfully promoted in *{}*!": "Успішно призначений в *{}*!",

    "This person CREATED the chat, how would I demote them?": "Ця людина СТВОРИЛА чат, як я можу її знизити?",
    "Can't demote what wasn't promoted!": "Як я можу знизити того хто не є адміном?",
    "I can't demote myself!": "Я не можу знизити себе!",
    "Successfully demoted in *{}*!": "Успішно знизений в *{}*!",
    "Could not demote. I might not be admin, or the admin status was appointed by another user, so I can't act upon them!": 
    "Я не можу знизити. Можливо я не адмін, чи статус адміністратора був був призначений іншим користувачем, тому я не можу знизити його!",

    "I don't have access to the invite link, try changing my permissions!": "У мене немає доступу до запрошувального посилання, спробуйте змінити мої права!",
    "I can only give you invite links for supergroups and channels, sorry!": "Я можу надавати запрошувальні посилання для супергруп та каналів!",

    "Admins in": "Адміністратори в",
    "this chat": "цьому чаті",
    " (Creator)": " (Створювач)",

#Multi
    "Invalid Chat ID provided!": "ID чату не існує!", #Connections
    "You don't seem to be referring to a user.": "Здається, ви звертаєтесь не до користувача.", #Admin

#Misc
"RUNS-K": RUN_STRINGS,
"SLAP_TEMPLATES-K": SLAP_TEMPLATES,
"ITEMS-K": ITEMS,
"HIT-K": HIT,
"THROW-K": THROW,
"ITEMP-K": ITEMSP_UA,
"ITEMR-K": ITEMSR_UA,
"Today in {} is being {}, around {}°C.\n": "Сьогодні в {} {}, приблизно {}°C.\n",

#Multi
    "Invalid Chat ID provided!": "ID чату не існує!", #Connections

#__main__
    #Module names
        "Admin": "Адміністрування",
        "AFK": "Режим АФК",
        "AntiFlood": "Антифлуд",
        "Bans": "Бани",
        "Word Blacklists": "Чорні списки",
        "Filters": "Фільтри",
        "Command disabling": "Відключення команд",
        "Antispam security": "Антиспам захист",
        "Locks": "Блокування",
        "Log Channels": "Логування дій",
        "Misc": "Інше",
        "Purges": "Очистка",
        "Muting & Restricting": "Мути й заборони",
        "Notes": "Замітки",
        "Reporting": "Репорти",
        "RSS Feed": "RSS Лента",
        "Rules": "Правила",
        "Connections": "З'єднання",
        "Bios and Abouts": "Підпис людини",
        "Warnings": "Попередження",
        "Welcomes/Goodbyes": "Привітання/Прощання",

#Some main stuff
"Here is the help for the *{}* module:\n{}": "Допомога по модулю *{}*:\n{}",
"Back": "Назад",
"send-help": """Привіт усім! Моє ім'я *{}*. Я модульний бот з функцією управління групами з різними фановими фічами! 
Погляньте на наступні можливості, які я можу вам запропонувати:
Головні команди:
 - /start: коротка інфа про бота.
 - /help: Я напишу вам повідомлення.
 - /help <назва модуля>: Я раскажу вам про цей модуль.
 - /donate: Інформація про те як вдонатити в мене!
 - /lang: Змінити мову бота.
 - /settings: Показати поточні установки бота.
   {}
   """,


"\nAll commands can either be used with `/` or `!`.\n": "\nУсі команди можуть починатися з `/` або `!`\n",

#Module helps
"Admin_help": """ - /adminlist | /admins: Список адмінів чату.
*Тільки для адміністраторів:*
 - /pin: Тихо закріпити отримане повідомлення - додайте аргумент 'loud' або 'notify' щоб повідомити користувачів про закріплення.
 - /unpin: Відкріпити дане закріплене повідомлення.
 - /invitelink: Отримати посилання-запрошення.
 - /promote: Підвищити користівача.
 - /demote: Знизити користувача.""",

"AFK_help": """ - /afk <причина>: відмітити себе як АФК.
 - brb <причина>: теж саме як /afk - але не команда.
Якщо ви відмітили себе як АФК, на будь-яке згадування про вас буде відправлене повідомлення про вашу недоступність.""",

"AntiFlood_help": """- /flood: Отримати дані установки антифлуда.
*Тільки адміни:*
 - /setflood <число/`no`/`off`>: Увімкнути або вимкнути антифлуд захист.""",

"Antispam security_help":"""*Тільки адміни:*
 - /antispam <on/yes/off/no>: Вимкнути захист від небажаного спаму, або показати дані установки якщо немає аргумента. 
Антиспам використовується власниками ботів для бану спамерів у всіх групах. Це допомагає захистити \
вас та ваші групи, видаляючи спам флудерів як можна швидше. Це може бути відключене для вашої групи використовуючи \
`/antispam off`""",

"Locks_help": """ - /locktypes:  список можливих блокувань.
*Тільки адміни:*
 - /lock <тип>:  заблокувати елемент у цьому чаті.
 - /unlock <тип>: разблокувати елемент у цьому чаті.
 - /locks: Даний список блокувань у цьому чаті.
Блокування можна використовувати для обмеження користувачів групи. Наприклад:
Блокування URL-адрес буде автоматично видаляти всі повідомлення з URL-адресами, які не були в білому списці, блокування стикерів буде видаляти всі \
стикери и т. п.
Блокування ботів зупине не адміністраторів від додавання ботів у чат.""",

"Command disabling_help":""" - /cmds: Перевірка даного стану відключених команд.
*Тільки адміни:*
 - /enable <команда>: увімкнути цю команду.
 - /disable <команда>: вимкнути цю команду.
 - /listcmds: список усіх можливих команд для відключення.""", 

"Filters_help": """ - /filters: список усіх активних фільтрів у цьому чаті.
*Тільки адміни:*
 - /filter <ключове слово> <відповідне повідомлення>: Додати фільтр у цей чат. Бот буде відповідати на це повідомлення кожен раз, як "ключове слово" \
буде згадано. 
ДОДАТОК: усі фільтри не вразливі до регистру букв.
Якщо ви відповідаєте стикером з ключовим словом, то дайте відповідь на стикер повідленням `/filter 'ключове слово'`. 
Якщо ви хочете, щоб ваше ключове слово було реченням, використовуйте одинарні кавички. Наприклад: `/filter 'Привіт усім' Як ви?`
 - /stop <ключове слово>: Зувинти цей фільтр.""",

"Bans_help": """ - /kickme: Видаляє користувача написавшего це з групи. 
*Тільки адміни:*
 - /ban <користувач>: забанити користувача.
 - /tban <користувач> (m/h/d): Забанити користувача на X часу. m = хвилини, h = години, d = дні.
 - /unban <користувач>: Разбанити користувача. 
 - /kick <користувач>: видалити користувача.
ДОДАТОК: Замість конструкції `/команда <користувач>` можно відповісти командою на будь-яке повідомлення користувача.""",

"Connections_help":"""З'єднання можно використати для контролювання групи з ОП бота, це зручно щоб не спамити в чат.
Доступні дії з групами:
 • Перегляд та змінення нотаток
 • Перегляд та редагування фільтрів.
 • Перегляд та редагування нотаток.
 • Підвищувати/знижувати користувачів.
 • Перегляд списку адмінів, перегляд посилання для запрошення.
 • Вмикати/вимикати комманди в чаті
 • Більше в майбутньому!
 - /connection <chatid>: Підключитися до групи.
 - /disconnect: Відключитися від групи.
 - /allowconnect on/yes/off/no: Дозволити підключення користувачів(юзерів) до цієї групи.""",

"RSS Feed_help": """ - /addrss <посилання>: Додати посилання в підписку RSS.
 - /removerss <посилання>: Видалити посилання з підпису.
 - /rss <посилання>: Показати останню новину з RSS один раз.
 - /listrss: Показати підписки.
ДОДАТОК: В групі тільки адміни можуть додавати/видаляти RSS посилання""",

"Sed/Regex_help": """- s/<текст1>/<текст2>(/<прапор>): дайте відповідь на повідомлення з цією командою щоб замінити текст на ній, буде замінено \
'текст1' на 'текст2'. Прапор опціональний, '`i`' для ігнорування капсу, '`g`' для глобальної заміни. 
Розділювачі можуть бути  `/`, `_`, `|`, та `:`. Підтримується групування тексту. Результат не може бути більше ніж 4096 символів.
ДОДАТОК: Sed використовує деякі спеціальні символи, такі як: `+*.?\\`
Якщо ви хочете використовувати ці символи, переконайтесь, що ви їх екрануєте!
Приклад: `\\?`.""",

"Log Channels_help": """*Тільки адміни:*
- /logchannel: Отримати інформацію про даний лог канал
- /setlog: Встановити канал для логування.
- /unsetlog: Вимкнути канал для логування.
Налаштування канала для логування:
- Додавання бота в канал (Як адміна!)
- Відправлення `/setlog` в канал
- Пересилання відправленого повідомлення `/setlog` в групі
""", 

"Reporting_help": """ - /report <причина>: дайте відповідь на повідомлення щоб відправити його адмінам на перевірку.
 - @admin: теж саме що й /report, тільки без причини.
ДОДАТОК: Можливість репорта дозволена тільки користувачям, на адмінів не буде реакції
*Тільки адміни:*
 - /reports <on/off>: змінити установки репорта, або продивитися даний статус.
 - Якщо вивести в личку бота - змінити свої установки.
 - Якщо ввести в чат -  Змінити установки чата.""",

"Notes_help": """ - /get <назва нотатки>: Отримати нотатку з цим іменем.
 - #<назва нотатки>: ткж саме що й /get.
 - /notes або /saved: Показати усі нотатки в цій групі.
Якщо ви хочете отримати вміст нотатки без ніякого форматування, використайте `/get <назва нотатки> noformat`. Це \
корисно при оновленні існуючої нотатки.
*Тільки адміни:*
 - /save <назва нотатки> <данні нотатки>: Збарегти нотатку.
Кнопка може бути додана до нотатки з допомогою стандартного синтаксиса посилання на рохмітку - посилання повинне бути просто додано з допомогою \
`buttonurl:` приклад: `[Кнопка](buttonurl:example.com)`. Напишіть /markdownhelp Для отримання розширеної інформації.
 - /save <назва нотатки>: дайте відповідь на повідомлення щоб зберегти.
 - /clear <назва нотатки: видалити нотатку з цим іменем.""",

"Muting & Restricting_help": """*Тільки адміни:*
 - /mute <нік>: Замутити користувача. (Через нік або відповадь на повідомлення.)
 - /tmute <нік> Х(m/h/d): Замутити користувача на Х часу. (Через нік або відповідь на повідомлення.) m = хвилини, h = години, d = дні (приклад: `60m` або `1h`).
 - /unmute <нік>: Размутити користувача. (Через нік або відповідь на повідомлення.)
 - /restrict <нік>: Заборонити користувачу відправляти стікери, гіфки, посилання чи медіа.
 - /trestrict <нік> Х(m/h/d): Заборонити користувачу відправляти стікери, гіфки, посилання чи медіа на Х часу. (via handle, or reply). m = хвилини, h = години, d = дні (приклад: `60m` або `1h`).
 - /unrestrict <нік>: Дозволити користувачу відправляти стікери, гіфки, посилання чи медіа.""",

"Misc_help": """ - /id: Отримати ID групи. Якщо відповісти командою на повідомлення - ви отримаєте ID користувача.
 - /runs: Відповісти рандомною фразою.
 - /slap: Вдарити користувача.
 - /time <місце>: Виводить місцевий час.
 - /info: Отримати інфу про користувача.
 - /gdpr: Видаляє інфу про вас з бази данних бота.
 - /stickerid: Дайте відповідь на стікер щоб отримати його ID.
 - /getsticker: Дайте відповідь на стікер щоб отримати його як png.
 - /markdownhelp: Коротка інформація про те, як працює markdown в Telegram, - можна викликати тільки в личці.""",

"Bios and Abouts_help": """ - /setbio <текст>: При відповаіді, збереже біо іншого користувача. 
 - /bio: Виведе біо вашого чи іншого користувача.
 - /setme <текст>: Збереже вашу інформацію.
 - /me: Виведе інформацію про вас, чи про іншого користувача.""",

"Rules_help": """ - /rules: Вивести правила чата.
*Тільки адміни:*
 - /setrules <правила>: Встановити правила для чата.
 - /clearrules: Видалити правила для групи.""",

"Warnings_help": """ - /warns <нік>: Вивести дані варни цього користувача чи для себе.
 - /warnlist: Вивести список фільтрів для варнів.
*Тільки адміни:*
 - /warn <нік>: Попередити користувача. Після 3 попереджень  користувач буде заблокований у групі. Можна також використати як відповідь.
 - /resetwarn <нік>: Скинути попередження користувача. Можна також використати як відповідь.
 - /addwarn <ключове слово> <попередження>: Встановити фільтр попередження на ключове слово. Якщо ви хочете, щоб ваше ключове слово \
було реченням, виділіть його кавичками, наприклад: `/addwarn я розлючений 'Це злий  користувач'`.
 - /nowarn <ключове слово>: Вимкнути фільтр попереджень.
 - /warnlimit <число>: Встановити ліміт попереджень.
 - /strongwarn <on/yes/off/no>: Якщо увімкнено, то перевищення ліміту попереджень призведе до бану. Якщо вимкнено, користувач буде кікнутий.""",

"Welcomes/Goodbyes_help": """Повідомлення Привітання та Прощання можуть бути персоналізовані багатьма методами. 
Якщо ви хочете, щоб повідомлення були індивідуально сгенеровані, наприклад привітальне повідомлення за умовчанням, \
аи можете використовувати такі змінні:
 - `{{first}}`: Ім'я користувача. 
 - `{{last}}`: Прізвище користувача. Якщо нема прізвища, буде використано ім'я.
 - `{{fullname}}`: Повне ім'я користувача. Якщо нема повного імені, буде використано ім'я.
 - `{{username}}`: Нік користувача. Якщо нема повного імені, буде використано згадування.
 - `{{mention}}`: Згадує користувача з іменем.
 - `{{id}}`: ID користувача.
 - `{{count}}`: Лічильник користувачів у групі.
 - `{{chatname}}`: Ім'я групи.
Кожна змінна ПОВИННА бути виділена `{{}}` для зміни.
Повідомлення Привітання й Прощання також підтримують markdown, тому ви можете створювати будь-які елементи. \
Кнопки також підтримуються, тому ви можете створити свої привітання чудовими з лоромогою деяких кнопок з написом. \
Щоб створити кнопку, що ссилається на ваші правила, використовуйте це: `[Правила](buttonurl://t.me/{}?Start=group_id)`.\
Просто змініть `group_id` ID вашої групи, який можна отримати через /id. Зверніть увагу, що ID групи зазвичай зазвичай передує `-`, він потрібен, \
тому, будь-ласка, не видяляйте його. \
Ви можете також встановити зображення/гіфки/відео/голосові повідомлення в якості привітального повідомлення \
дайте відповідь на потрібний елемент та напишіть /setwelcome.
*Тільки адміни:*
 - /welcome <on/off>: Увімкнути/Вимкнути привітальні повідомлення.
 - /welcome: Показує даний статус привітальних повідомлень.
 - /welcome noformat: Показує данні установки привітання, без форматування - корисно при зміненні вашого привітального повідомлення!
 - /goodbye -> так само як і /welcome.
 - /setwelcome <текст>: Установка користувацького привітального повідомлення.
 - /setgoodbye <текст>: Установка користувацького прощального повідомлення.
 - /resetwelcome: Повернути привітальне повідомлення за умовчанням.
 - /resetgoodbye: Повернути прощальне повідомлення за умовчанням.
 - /cleanwelcome <on/off>: Видалення попереднього привітального повідомлення після відправлення нового, щоб уникнути спаму в групі.
 - /cleanservice <on/off/yes/no>: Видаляє всі службові повідомлення; Ці докучливі \"Х приєдналися до групи\", котрі ви бачите, коли люди приєднуються до групи.
 - /welcomesecurity <off/soft/hard>: soft - заборонити користувачу відправляти медіафайли протягом 24 годин, hard - заборонити користувачу віправляти повідомлення, поки він не натисне кнопку \"Я не бот\".""".format(dispatcher.bot.username),

"Word Blacklists_help":"""Чорні списки використовуються, щоб зупинити певні трігери в групі. Кожен раз, коли трігер буде згадано, \
повідомлення буде миттєво видалене. Це добре комбінується з фільтрами попереджень.
ДОДАТОК: чорні списки не діють на адмінів групи.
 - /blacklist: Перегляд поточних трігерів в групі.
*Тільки адміни:*
 - /addblacklist <трігер>: додайте трігер в чорний список. Кожна строка розпочиняється одним трігером, \
тому використання різних строк дозволить вам додавати кілька трігерів.
 - /unblacklist <трігер>: видалення трігера з чорного списку. Тут використовуєьбся така ж логіка нової строки, ви можете видалити \
кілька трігерів одночасно.
 - /rmblacklist <трігер>: теж саме, що й вище.""",

"Purges_help": """*Тільки адміни:*
 - /del: видалити повідомлення, на яке ви відповіли.
 - /purge: видаляє всі повідомлення між цим та тим на яке ви відповіли.
 - /purge <Число Х>: видаляє повідомлення на яке ви відповіли й наступні Х-повідомлень. """
}
