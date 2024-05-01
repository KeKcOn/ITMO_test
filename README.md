# Как запустить проект

1. Запускаем Docker Compose:

   ```bash
   docker compose up
   ```
2. Выполняем миграции:
   ```bash
   docker compose exec backend python manage.py migrate
   ```
3. Заполняем данными:
   ```bash
   docker compose exec backend python manage.py loaddata location_capital.json
   ```

## Примеры запросов к API

1. Добавление записи:

   ```bash
   POST api/capital/
   {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "properties": {
          "country": "Беларусь",
          "city": "Минск"
          },
          "geometry": {
            "coordinates": [
              27.56246513844343,
              53.90241012984757
              ],
            "type": "Point"
          },
          "id": 2
        }
      ]
   }
   ```

2. Вывод всех записей:

    ```bash
    GET api/capital/
    ```

Теперь ваш проект должен быть доступен по адресу http://localhost:8000/.
