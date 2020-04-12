Файлы для лабораторной работы №2.
Сделано на версии Python 3.8.2

Файлы с _Working - это модули, где реализованы классы (методы) для основных заданий.
Файлы с Test_ - тестовые модули, где в виде методов test_'метод' проверяется правильность работы
методов из соответствующих модулей _Working
Из дополнительных заданий реализован метакласс Singleton в модуле File_Working, который применяется
на класс File

Запускать тесты можно следующим образом:
На примере (Test_Cached)
1) Заходим в командную строку, переходим в директорию с тестовым модулем
2) С помощью интерпретатора python выполняем команду import Test_Cached
3) В той же директории появится папка __pycache__, в неё закидываем модуль Cached_Working
4) Открываем командую строку, переходим в папку __pycache__ и выполняем команду python Cached_Working.cpython-38.pyc

В итоге должен выполниться тестовый модуль и все тесты пройти успешно

! В тестовом модуле Test_File пути к тестируемому файлу с числами записаны мои, так что пути
необходимо заменить на свои, а именно:
Путь r"C:\Test_Modules\Nums.txt" это путь к файлу с числами, который тест должен отсортировать
В пути r"C:\Test_Modules\SORTED.txt" заменить ТОЛЬКО путь, имя SORTED.txt не трогать.(этот файл
создаётся после сортировки)
Путь r"C:\Test_Modules\File_for_check.txt" Создаёт временный файл для проверки других методов
работы с файлами, имя можно не менять, путь поменять на свой.
