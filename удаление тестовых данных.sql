/*
Удаляет только тестовые данные, которые были внесены файлом для заполнения тестовых данных
*/

DELETE FROM blog_post WHERE id > '1000';
DELETE FROM guide_news WHERE id > '1000';
DELETE FROM guide_about WHERE id > '1000';
DELETE FROM guide_usertowns WHERE id > '1000';
DELETE FROM guide_towns WHERE name = 'Полоцк';
DELETE FROM guide_towns WHERE name = 'Новополоцк';
DELETE FROM guide_towns WHERE name = 'Минск';
DELETE FROM guide_towns WHERE name = 'Молодечно';
DELETE FROM guide_towns WHERE name = 'Жодино';
DELETE FROM guide_towns WHERE name = 'Вилейка';
DELETE FROM guide_towns WHERE name = 'Витебск';
DELETE FROM guide_districts WHERE name = 'Минская область';
DELETE FROM guide_districts WHERE name = 'Витебская область';