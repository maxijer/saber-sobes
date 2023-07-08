<h1> Как запускать</h1>
Для начала вам нужно загрузить все используемые библиотеки это можно сделать командой:

```pip install -r requirements.txt```

После чего вам нужно зайти в корень проекта и выполнить команду

```uvicorn main:app --reload```

<h1>Как тестировать</h1>
Можно перейти на <a>http://127.0.0.1:8000/docs</a> Там будет надпись default и чуть ниже зеленая кнопка на которой написано post.
Вам нужно нажать на нее. После чего появиться надпись Try it out. Нажмите на нее. У вас появится поле, туда нужно ввести json.
Пример:

```{"build":"forward_interest"}```

После чего нажмите execute. Вам вернется json в формате: 

```{
  {
  "ans": [
    "build_teal_leprechauns",
    "enable_yellow_centaurs",
    "bring_olive_centaurs",
    "coloring_white_centaurs",
    "create_teal_centaurs",
    "design_lime_centaurs",
    "train_purple_centaurs",
    "upgrade_navy_centaurs",
    "create_maroon_centaurs",
    "bring_blue_centaurs",
    "read_yellow_centaurs",
    "create_olive_centaurs",
    "coloring_aqua_centaurs",
    "coloring_aqua_golems",
    "coloring_navy_golems",
    "map_black_leprechauns",
    "upgrade_white_leprechauns",
    "map_olive_leprechauns",
    "enable_lime_leprechauns",
    "map_black_leprechauns",
    "upgrade_white_leprechauns",
    "map_olive_leprechauns",
    "enable_lime_leprechauns",
    "create_aqua_humans",
    "enable_olive_humans",
    "build_maroon_humans",
    "write_silver_humans",
    "write_white_humans",
    "create_purple_humans",
    "train_white_humans",
    "write_teal_humans",
    "enable_silver_humans",
    "bring_blue_ogres",
    "design_white_ogres",
    "train_green_ogres",
    "upgrade_aqua_ogres",
    "write_silver_ogres",
    "enable_fuchsia_ogres",
    "bring_green_ogres",
    "build_yellow_ogres",
    "create_maroon_ogres",
    "design_green_ogres",
    "upgrade_navy_ogres",
    "write_blue_ogres",
    "write_fuchsia_golems"
  ]
} 
```

Также есть альтернативный вариант тестирования. В файле ``req.py`` измените поле data_1 на тот словарь который 
вам нужен и запустите код файла ``req.py``.
