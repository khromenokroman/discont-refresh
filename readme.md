# 1с рарус ткпт

Скрипт обрабатывает файл выгрузки который предназначен для кассы, и заменяет значение в 29 параметре на 0 чтобы скидка по данному товару не проходила


У раруса с xpos3 есть проблемка при штатной выгрузке товар выгружается с признаком максимальная скидка включена и значение 100 тоесть скидка разрешена хотя документ запрет скидки есть и с фронтолом работает, так как база распределенная и просто так ничего не поменяешь а если поменяешь то потом при обновлениях самому нужно будет это все поддерживать поэтому быстренько написал парсер