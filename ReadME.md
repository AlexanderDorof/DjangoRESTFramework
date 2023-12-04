1. Создан проект (django_rest) и приложение (drf) содержащее логику взаимодействия с Django REST Framework.
2. Админка настоена, логин/пароль root/root
3. Создана модель Wonder (Чудеса света) c 5 полями: 'title', 'creator', 'created', 'place', 'current_status'.
4. Создан кастомный сериализатор, наследуемый от класса Serializer, модуля serializers. Соедржит методы create и update.
5. Класс представления модуля View включает методы get, post, put, delete для соответсвующих http-методов.
6. get/post доступны по url api/wonders/. А put/delete требуют передачи ключа записи - api/wonders/<strong>int</strong>
7. Реализован поиск по произвольному полю: api/wonders/<strong>field</strong>/?q=tower в классе SearchView.
