DELETE FROM blog_post WHERE id BETWEEN '1000' AND '1002';
DELETE FROM guide_news WHERE id BETWEEN '1000' AND '1002';
DELETE FROM guide_about WHERE id BETWEEN '1000' AND '1002';
DELETE FROM guide_usertowns WHERE id BETWEEN '1000' AND '1003';
DELETE FROM guide_towns WHERE name IN ('Полоцк', 'Новополоцк', 'Минск', 'Молодечно', 'Жодино', 'Вилейка', 'Витебск');
DELETE FROM guide_districts WHERE name IN ('Минская область', 'Витебская область');
