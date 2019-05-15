Бывает полезно оптимизировать вызовы "тяжёлых"функций с помощью кеширования. Кеширование – это сохранение результатов выполнения функций для предотвращения повторных вычислений. Перед вызовом функции проверяется есть ли уже вычисленный результат. Если есть – функция не вызывается, а возвращается сохранённое значение.
Реализуйте декоратор для Least Recently Used (LRU) Cache. Пользователь указывает размер кеша N, и в кеше сохраняются N последних вычислений. Другими словами, вытесняется из кеша сначало то, что использовалось давней всего.
Декоратор назовите @cache, он должен принимать один параметр – размер кеша. Поддержите как можно более широкий класс функций (функции многих аргументов, функции с именоваными параметрами, принимающие сложные типы итд). Декоратор должен вести себя порядочно, то есть не должен затирать документацию функции.