# Создание API-сервиса для ветеринарной клиники | Автор: Синецкий Андрей

1. Создан и оформлен гитхаб
2. Реализован путь /: - [https://dog-api-vggc.onrender.com/](https://dog-api-vggc.onrender.com/)
3. Реализован путь: POST https://dog-api-vggc.onrender.com/post 
4. Реализована запись собак:

   Можно протестировать POST https://dog-api-vggc.onrender.com/dogs/

Body 
{
    "name": "Druzhok",
    "pk": 8,
    "kind": "bulldog"
}

5. Реализовано получение списка собак: GET [https://dog-api-vggc.onrender.com/dogs/](https://dog-api-vggc.onrender.com/dogs/)
6. Реализовано получение собаки по id: GET [https://dog-api-vggc.onrender.com/dogs/1](https://dog-api-vggc.onrender.com/dogs/1) | [https://dog-api-vggc.onrender.com/dogs/2](https://dog-api-vggc.onrender.com/dogs/2)
7. Реализовано получение собак по типу: GET [https://dog-api-vggc.onrender.com/dogs/?type=terrier](https://dog-api-vggc.onrender.com/dogs/?type=terrier)
8. Реализовано обновление собаки по id:

PATCH https://dog-api-vggc.onrender.com/dogs/1

Body 
{
    "name": "Updated Name",
    "pk": 1,
    "kind": "bulldog"
}


9. Сервис открывается по ссылке: [https://dog-api-vggc.onrender.com/](https://dog-api-vggc.onrender.com/)  (Надеюсь правильно понял задание, в чате уточнял.)

10. Документация совпадает с заданием:

- Создан публичный репозиторий на GitHub ✅
- Указаны лицензии и создан .gitignore ✅
- Добавлены в коллабораторы необходимые пользователи ✅
- Заполнен README с кратким описанием того, что было сделано и ссылками на результат ✅
- Добавлен в репозиторий файл main.py с реализованной логикой ✅
- Сервис развернут на публичном хостинге render.com ✅
- Прислал в AnyTask две ссылки: на репозиторий и на поднятый веб-сервис ✅




