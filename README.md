# Python3_PyQt5

Для импорта функции async_timed из файла async_timer.py, расположенного в папке concurrency-in-python-with-asyncio/util, вам нужно добавить путь к папке concurrency-in-python-with-asyncio в переменную окружения PYTHONPATH в Linux. Это позволит Python найти модуль util.async_timer при выполнении сценария listing_2_18.py.
Вы можете добавить путь к PYTHONPATH перед запуском сценария следующим образом:
bash
	$ export PYTHONPATH=/полный/путь/к/concurrency-in-python-with-asyncio:$PYTHONPATH
	$python3 chapter_2/listing_2_18.py

Замените /полный/путь/к/concurrency-in-python-with-asyncio на фактический полный путь к папке concurrency-in-python-with-asyncio, где находится папка util.
После добавления пути к PYTHONPATH Python сможет корректно импортировать функцию async_timed из async_timer.py в вашем сценарии listing_2_18.py.
