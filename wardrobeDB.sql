-- DROP DATABASE wardrobe_planner;
CREATE DATABASE wardrobe_planner;
USE wardrobe_planner;

CREATE TABLE users (
    user_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    user_password VARCHAR(50)

);

CREATE TABLE user_location (
    user_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    home_town VARCHAR(50),
    latitude FLOAT,
    longitude FLOAT

);

CREATE TABLE friends (
	user_ID INT NOT NULL,
	friend_ID INT NOT NULL,
    PRIMARY KEY (user_ID, friend_ID),
    FOREIGN KEY (user_ID) REFERENCES users(user_ID),
    FOREIGN KEY (friend_ID) REFERENCES users(user_ID)
);


CREATE TABLE ownership (
	item_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	owner_ID INT NOT NULL,
    FOREIGN KEY (owner_ID) REFERENCES users(user_ID)
);


CREATE TABLE clothes (
    item_ID INT NOT NULL PRIMARY KEY,
	item_type VARCHAR(50) NOT NULL,
    item_description VARCHAR(255) NOT NULL,
    weather_tag VARCHAR(50) NOT NULL,
    occasion_tag VARCHAR(50) NOT NULL,
    mood_tag VARCHAR(50) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES ownership(item_ID)
);

CREATE TABLE availability_status (
	item_ID INT NOT NULL PRIMARY KEY,
    item_status VARCHAR(50) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES clothes(item_ID)
);

INSERT INTO users (user_ID, user_name, user_password)
VALUES
 (1, 'Anna', 'MyPassword123'),
 (2, 'Maria', 'Diffi456'),
 (3, 'Jenny', 'SomE56'),
 (4, 'Lucy', 'ProT897')
;

INSERT INTO user_location (user_ID, home_town, latitude, longitude)
VALUES
 (1, 'Warsaw', 52.23, 21.01),
 (2, 'Cracow', 50.06, 19.94),
 (3, 'Gdansk', 54.37, 18.61),
 (4, 'Wroclaw', 51.11, 17.03)
;

INSERT INTO friends(user_ID, friend_ID)
VALUES
 (1, 1),
 (1, 2),
 (1, 3),
 (1, 4),
 (2, 2),
 (2, 1),
 (2, 3),
 (3, 1),
 (3, 2),
 (3, 3),
 (4, 2),
 (4, 3),
 (4, 4)
;


INSERT INTO ownership (item_ID, owner_ID)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 1),
(17, 1),
(18, 1),
(19, 1),
(20, 1),
(21, 1),
(22, 1),
(23, 1),
(24, 1),
(25, 1),
(26, 1),
(27, 1),
(28, 1),
(29, 1),
(30, 1),
(31, 1),
(32, 1),
(33, 1),
(34, 1),
(35, 1),
(36, 1),
(37, 1),
(38, 1),
(39, 1),
(40, 1),

(41, 2),
(42, 2),
(43, 2),
(44, 2),
(45, 2),
(46, 2),
(47, 2),
(48, 2),
(49, 2),
(50, 2),
(51, 2),
(52, 2),
(53, 2),
(54, 2),
(55, 2),
(56, 2),
(57, 2),
(58, 2),
(59, 2),
(60, 2),
(61, 2),
(62, 2),
(63, 2),
(64, 2),
(65, 2),
(66, 2),
(67, 2),
(68, 2),
(69, 2),
(70, 2),
(71, 2),
(72, 2),
(73, 2),
(74, 2),
(75, 2),
(76, 2),
(77, 2),
(78, 2),
(79, 2),
(80, 2),
(81, 2),
(82, 2),

(83, 3),
(84, 3),
(85, 3),
(86, 3),
(87, 3),
(88, 3),
(89, 3),
(90, 3),
(91, 3),
(92, 3),
(93, 3),
(94, 3),
(95, 3),
(96, 3),
(97, 3),
(98, 3),
(99, 3),
(100, 3),
(101, 3),
(102, 3),
(103, 3),
(104, 3),
(105, 3),
(106, 3),
(107, 3),
(108, 3),
(109, 3),
(110, 3),
(111, 3),
(112, 3),
(113, 3),
(114, 3),
(115, 3),
(116, 3),
(117, 3),
(118, 3),
(119, 3),
(120, 3),
(121, 3),
(122, 3),
(123, 3),
(124, 3),

(125, 4),
(126, 4),
(127, 4),
(128, 4),
(129, 4),
(130, 4),
(131, 4),
(132, 4),
(133, 4),
(134, 4),
(135, 4),
(136, 4),
(137, 4),
(138, 4),
(139, 4),
(140, 4),
(141, 4),
(142, 4),
(143, 4),
(144, 4),
(145, 4),
(146, 4),
(147, 4),
(148, 4),
(149, 4),
(150, 4),
(151, 4),
(152, 4),
(153, 4),
(154, 4),
(155, 4),
(156, 4),
(157, 4),
(158, 4),
(159, 4),
(160, 4),
(161, 4),
(162, 4),
(163, 4),
(164, 4)
;

INSERT INTO clothes(item_ID, item_type, item_description, weather_tag, occasion_tag, mood_tag)
VALUES
(1, 'bottom', 'green denim trousers', 'freezing', 'home', 'neutral'),
(2, 'bottom', 'blue green trousers', 'cold', 'home', 'neutral'),
(3, 'bottom', 'pink denim trousers', 'mild', 'home', 'neutral'),
(4, 'bottom', 'grey suit pants', 'mild', 'work', 'neutral'),
(5, 'bottom', 'black suit pants', 'mild', 'work', 'serious'),
(6, 'bottom', 'red suit pants', 'cold', 'work', 'cheerful'),
(7, 'bottom', 'green suit pants', 'cold', 'work', 'neutral'),
(8, 'bottom', 'orange midi skirt', 'cold', 'work', 'cheerful'),
(9, 'bottom', 'black midi skirt', 'cold', 'work', 'serious'),
(10, 'bottom', 'black long skirt', 'freezing', 'work', 'neutral'),
(11, 'bottom', 'green long skirt', 'freezing', 'work', 'serious'),
(12, 'bottom', 'yellow mini skirt', 'warm', 'date', 'cheerful'),
(13, 'bottom', 'orange mini skirt', 'warm', 'date', 'neutral'),
(14, 'bottom', 'red mini skirt', 'warm', 'party', 'neutral'),
(15, 'bottom', 'pink mini skirt', 'hot', 'party', 'neutral'),
(16, 'bottom', 'flower midi skirt', 'mild', 'party', 'cheerful'),
(17, 'top', 'Printed T-shirt', 'mild', 'party', 'cheerful'),
(18, 'top', 'Black T-shirt', 'mild', 'date', 'cheerful'),
(19, 'top', 'Turquoise blouse', 'mild', 'work', 'neutral'),
(20, 'top', 'Red blouse', 'mild', 'date', 'neutral'),
(21, 'top', 'White T-shirt', 'mild', 'home', 'neutral'),
(22, 'top', 'Grey hoodie', 'cold', 'home', 'neutral'),
(23, 'top', 'Blue hoodie', 'cold', 'cleaning', 'neutral'),
(24, 'top', 'Grey wool cardigan', 'cold', 'work', 'neutral'),
(25, 'top', 'Yellow wool cardigan', 'freezing', 'work', 'neutral'),
(26, 'outer wear', 'Duck down jacket', 'freezing', 'date', 'romantic'),
(27, 'outer wear', 'Blue duck down jacket', 'freezing', 'party', 'neutral'),
(28, 'outer wear', 'Black wool coat', 'freezing', 'work', 'neutral'),
(29, 'outer wear', 'Black wool coat', 'freezing', 'work', 'neutral'),
(30, 'top', 'Dark grey hoodie', 'cold', 'sport', 'neutral'),
(31, 'top', 'Dark grey hoodie', 'cold', 'sport', 'neutral'),
(32, 'bottom', 'yoga pants', 'cold', 'sport', 'neutral'),
(33, 'bottom', 'yoga pants', 'cold', 'sport', 'neutral'),
(34, 'full body', 'brown wool dress', 'cold', 'date', 'neutral'),
(35, 'full body', 'green cotton dress', 'cold', 'work', 'neutral'),
(36, 'full body', 'green cotton dress', 'cold', 'work', 'neutral'),
(37, 'full body', 'blue poliester dress', 'mild', 'work', 'neutral'),
(38, 'full body', 'red silk dress', 'warm', 'date', 'romantic'),
(39, 'full body', 'silver sequin dress', 'warm', 'party', 'cheerful'),
(40, 'full body', 'navy blue jumpsuit', 'warm', 'party', 'neutral'),

(41, 'outer wear', 'Blue denim jacket', 'warm', 'date', 'neutral'),
(42, 'bottom', 'cotton', 'freezing', 'home', 'neutral'),
(43, 'bottom', 'blue trousers', 'cold', 'home', 'neutral'),
(44, 'bottom', 'pink cotton trousers', 'mild', 'home', 'neutral'),
(45, 'bottom', 'greyish suit pants', 'mild', 'work', 'neutral'),
(46, 'bottom', 'dark grey suit pants', 'mild', 'work', 'serious'),
(47, 'bottom', 'orange suit pants', 'cold', 'work', 'cheerful'),
(48, 'bottom', 'darnk green suit pants', 'cold', 'work', 'neutral'),
(49, 'bottom', 'red long skirt', 'cold', 'work', 'cheerful'),
(50, 'bottom', 'woolen midi skirt', 'freezing', 'work', 'serious'),
(51, 'bottom', 'brown long skirt', 'freezing', 'work', 'serious'),
(52, 'bottom', 'blue long skirt', 'cold', 'work', 'serious'),
(53, 'bottom', 'yellow skirt', 'hot', 'date', 'cheerful'),
(54, 'bottom', 'orange skirt', 'hot', 'date', 'romantic'),
(55, 'bottom', 'red mini skirt', 'hot', 'party', 'neutral'),
(56, 'bottom', 'pink mini skirt', 'warm', 'party', 'neutral'),
(57, 'bottom', 'printed midi skirt', 'mild', 'party', 'cheerful'),
(58, 'top', 'Animal print T-shirt', 'mild', 'party', 'cheerful'),
(59, 'top', 'White T-shirt', 'mild', 'date', 'cheerful'),
(60, 'top', 'Purple blouse', 'mild', 'work', 'neutral'),
(61, 'top', 'Red blouse', 'mild', 'date', 'romantic'),
(62, 'top', 'Golden T-shirt', 'mild', 'party', 'neutral'),
(63, 'top', 'White hoodie', 'cold', 'home', 'neutral'),
(64, 'top', 'Black hoodie', 'cold', 'cleaning', 'neutral'),
(65, 'top', 'Beige cardigan', 'cold', 'work', 'neutral'),
(66, 'top', 'White wool cardigan', 'freezing', 'work', 'neutral'),
(67, 'outer wear', 'Red jacket', 'freezing', 'date', 'romantic'),
(68, 'outer wear', 'Duck down jacket', 'freezing', 'party', 'neutral'),
(69, 'outer wear', 'Black coat', 'freezing', 'work', 'neutral'),
(70, 'outer wear', 'Blue wool coat', 'freezing', 'work', 'neutral'),
(71, 'top', 'Dark grey hoodie', 'cold', 'sport', 'cheerful'),
(72, 'top', 'Light blue hoodie', 'cold', 'sport', 'neutral'),
(73, 'bottom', 'yellow yoga pants', 'cold', 'sport', 'cheerful'),
(74, 'bottom', 'yoga pants', 'mild', 'sport', 'neutral'),
(75, 'full body', 'brown cotton dress', 'cold', 'date', 'neutral'),
(76, 'full body', 'green dress', 'mild', 'work', 'neutral'),
(77, 'full body', 'cotton dress', 'hot', 'work', 'neutral'),
(78, 'full body', 'poliester dress', 'mild', 'work', 'serious'),
(79, 'full body', 'silk dress', 'hot', 'date', 'romantic'),
(80, 'full body', 'sequin dress', 'hot', 'party', 'cheerful'),
(81, 'full body', 'golden jumpsuit', 'hot', 'party', 'neutral'),
(82, 'outer wear', 'Grey denim jacket', 'mild', 'date', 'neutral'),

(83, 'bottom', 'blue denim trousers', 'warm', 'party', 'neutral'),
(84, 'bottom', 'black denim trousers', 'cold', 'home', 'neutral'),
(85, 'top', 'black T-shirt', 'warm', 'home', 'neutral'),
(86, 'bottom', 'beige suit pants', 'mild', 'work', 'serious'),
(87, 'bottom', 'black suit pants', 'mild', 'work', 'serious'),
(88, 'top', 'black long sleeve shirt', 'mild', 'work', 'serious'),
(89, 'top', 'white long sleeve shirt', 'mild', 'work', 'serious'),
(90, 'top', 'navy long sleeve shirt', 'mild', 'work', 'serious'),
(91, 'bottom', 'navy denim trousers', 'cold', 'work', 'serious'),
(92, 'bottom', 'navy denim shorts', 'hot', 'party', 'cheerful'),
(93, 'bottom', 'black denim shorts', 'hot', 'party', 'neutral'),
(94, 'bottom', 'blue mini skirt', 'warm', 'date', 'neutral'),
(95, 'bottom', 'black mini skirt', 'warm', 'date', 'neutral'),
(96, 'bottom', 'grey long leggins', 'mild', 'sport', 'neutral'),
(97, 'bottom', 'black long leggins', 'mild', 'home', 'neutral'),
(98, 'bottom', 'black long skirt', 'mild', 'work', 'serious'),
(99, 'top', 'Printed T-shirt', 'warm', 'party', 'cheerful'),
(100, 'top', 'Black T-shirt', 'mild', 'date', 'cheerful'),
(101, 'top', 'black blouse', 'mild', 'work', 'neutral'),
(102, 'top', 'white blouse', 'mild', 'work', 'serious'),
(103, 'top', 'White T-shirt', 'mild', 'home', 'neutral'),
(104, 'outer wear', 'black hoodie', 'cold', 'home', 'neutral'),
(105, 'outer wear', 'blue hoodie', 'cold', 'home', 'neutral'),
(106, 'outer wear', 'black wool cardigan', 'freezing', 'work', 'neutral'),
(107, 'outer wear', 'grey wool cardigan', 'freezing', 'home', 'neutral'),
(108, 'outer wear', 'black jacket', 'freezing', 'party', 'neutral'),
(109, 'outer wear', 'blue denim jacket', 'mild', 'party', 'neutral'),
(110, 'outer wear', 'black wool coat', 'freezing', 'work', 'neutral'),
(111, 'outer wear', 'beige wool coat', 'freezing', 'work', 'neutral'),
(112, 'top', 'dark grey hoodie', 'cold', 'sport', 'neutral'),
(113, 'top', 'grey hoodie', 'cold', 'sport', 'neutral'),
(114, 'bottom', 'black yoga pants', 'mild', 'sport', 'neutral'),
(115, 'bottom', 'beige yoga pants', 'mild', 'sport', 'neutral'),
(116, 'full body', 'blue cotton dress', 'hot', 'party', 'cheerful'),
(117, 'full body', 'white cotton dress', 'hot', 'date', 'romantic'),
(118, 'full body', 'red cotton dress', 'mild', 'date', 'romantic'),
(119, 'full body', 'multicolor dress', 'hot', 'date', 'romantic'),
(120, 'full body', 'multicolor cotton dress', 'warm', 'date', 'romantic'),
(121, 'full body', 'black dress', 'warm', 'work', 'serious'),
(122, 'full body', 'navy dress', 'warm', 'party', 'neutral'),
(123, 'top', 'white T-shirt', 'mild', 'home', 'neutral'),
(124, 'top', 'multicolor blouse', 'mild', 'date', 'romantic'),

(125, 'top', 'white cotton shirt', 'mild', 'work', 'neutral'),
(126, 'top', 'white t-shirt', 'mild', 'home', 'neutral'),
(127, 'top', 'printed t-shirt', 'warm', 'date', 'cheerful'),
(128, 'top', 'black hoodie', 'cold', 'cleaning', 'neutral'),
(129, 'top', 'white top', 'hot', 'party', 'neutral'),
(130, 'top', 'black top', 'hot', 'party', 'neutral'),
(131, 'outer wear', 'black cardigan', 'freezing', 'work', 'neutral'),
(132, 'outer wear', 'black duck down jacket', 'freezing', 'party', 'neutral'),
(133, 'outer wear', 'black leather jacket', 'mild', 'party', 'neutral'),
(134, 'outer wear', 'blue denim jacket', 'mild', 'date', 'cheerful'),
(135, 'top', 'navy hoodie', 'cold', 'sport', 'neutral'),
(136, 'top', 'grey hoodie', 'cold', 'sport', 'neutral'),
(137, 'bottom', 'yoga pants', 'cold', 'sport', 'neutral'),
(138, 'bottom', 'yoga pants', 'cold', 'sport', 'neutral'),
(139, 'full body', 'beige jersey long dress', 'warm', 'date', 'neutral'),
(140, 'full body', 'white linen dress', 'hot', 'work', 'neutral'),
(141, 'full body', 'black shirt dress', 'cold', 'work', 'neutral'),
(142, 'full body', 'black denim platsuit', 'hot', 'party', 'neutral'),
(143, 'full body', 'blue denim dungarees', 'mild', 'home', 'neutral'),
(144, 'full body', 'pink jersey jumpsuit', 'warm', 'party', 'cheerful'),
(145, 'full body', 'red satin jumpsuit', 'warm', 'date', 'romantic'),
(146, 'top', 'black t-shirt', 'warm', 'home', 'neutral'),
(147, 'top', 'blue top', 'hot', 'party', 'cheerful'),
(148, 'top', 'red blouse', 'mild', 'date', 'neutral'),
(149, 'top', 'white t-shirt', 'mild', 'home', 'neutral'),
(150, 'top', 'red t-shirt', 'warm', 'home', 'cheerful'),
(151, 'top', 'red hoodie', 'cold', 'home', 'neutral'),
(152, 'top', 'pink blouse', 'mild', 'date', 'romantic'),
(153, 'top', 'printed t-shirt', 'warm', 'home', 'neutral'),
(154, 'outer wear', 'beige blazer', 'mild', 'work', 'neutral'),
(155, 'outer wear', 'black blazer', 'mild', 'work', 'serious'),
(156, 'outer wear', 'black wool coat', 'freezing', 'work', 'neutral'),
(157, 'outer wear', 'orange blazer', 'mild', 'work', 'cheerful'),
(158, 'top', 'beige sweater', 'cold', 'work', 'neutral'),
(159, 'top', 'black sweater', 'cold', 'work', 'neutral'),
(160, 'bottom', 'beige skirt', 'warm', 'date', 'neutral'),
(161, 'bottom', 'navy midi skirt', 'mild', 'work', 'neutral'),
(162, 'full body', 'black long dress', 'mild', 'date', 'neutral'),
(163, 'full body', 'multicolor cotton dress', 'hot', 'work', 'cheerful'),
(164, 'full body', 'pink cotton dress', 'warm', 'date', 'romantic')
;

INSERT INTO availability_status (item_ID, item_status)
VALUES
(1, 'available'),
(2, 'available'),
(3, 'available'),
(4, 'available'),
(5, 'available'),
(6, 'available'),
(7, 'available'),
(8, 'available'),
(9, 'available'),
(10, 'dirty'),
(11, 'dirty'),
(12, 'available'),
(13, 'available'),
(14, 'available'),
(15, 'available'),
(16, 'available'),
(17, 'available'),
(18, 'available'),
(19, 'available'),
(20, 'available'),
(21, 'available'),
(22, 'available'),
(23, 'available'),
(24, 'available'),
(25, 'available'),
(26, 'available'),
(27, 'available'),
(28, 'available'),
(29, 'available'),
(30, 'dirty'),
(31, 'available'),
(32, 'available'),
(33, 'available'),
(34, 'available'),
(35, 'available'),
(36, 'available'),
(37, 'available'),
(38, 'available'),
(39, 'available'),
(40, 'available'),

(41, 'available'),
(42, 'dirty'),
(43, 'available'),
(44, 'available'),
(45, 'available'),
(46, 'available'),
(47, 'available'),
(48, 'available'),
(49, 'available'),
(50, 'available'),
(51, 'available'),
(52, 'available'),
(53, 'available'),
(54, 'available'),
(55, 'available'),
(56, 'available'),
(57, 'available'),
(58, 'available'),
(59, 'available'),
(60, 'available'),
(61, 'available'),
(62, 'available'),
(63, 'available'),
(64, 'available'),
(65, 'available'),
(66, 'available'),
(67, 'available'),
(68, 'available'),
(69, 'available'),
(70, 'dirty'),
(71, 'available'),
(72, 'available'),
(73, 'available'),
(74, 'available'),
(75, 'available'),
(76, 'available'),
(77, 'available'),
(78, 'available'),
(79, 'available'),
(80, 'available'),
(81, 'available'),
(82, 'available'),
(83, 'available'),
(84, 'available'),
(85, 'available'),
(86, 'available'),
(87, 'available'),
(88, 'available'),
(89, 'available'),
(90, 'dirty'),
(91, 'available'),
(92, 'available'),
(93, 'available'),
(94, 'available'),
(95, 'available'),
(96, 'available'),
(97, 'available'),
(98, 'available'),
(99, 'available'),
(100, 'available'),
(101, 'dirty'),
(102, 'available'),
(103, 'available'),
(104, 'available'),
(105, 'available'),
(106, 'dirty'),
(107, 'available'),
(108, 'available'),
(109, 'available'),
(110, 'available'),
(111, 'available'),
(112, 'available'),
(113, 'available'),
(114, 'available'),
(115, 'dirty'),
(116, 'available'),
(117, 'available'),
(118, 'available'),
(119, 'available'),
(120, 'available'),
(121, 'available'),
(122, 'available'),
(123, 'available'),
(124, 'dirty'),
(125, 'available'),
(126, 'available'),
(127, 'available'),
(128, 'available'),
(129, 'dirty'),
(130, 'available'),
(131, 'available'),
(132, 'available'),
(133, 'available'),
(134, 'available'),
(135, 'available'),
(136, 'available'),
(137, 'available'),
(138, 'dirty'),
(139, 'available'),
(140, 'available'),
(141, 'available'),
(142, 'available'),
(143, 'available'),
(144, 'available'),
(145, 'available'),
(146, 'available'),
(147, 'available'),
(148, 'available'),
(149, 'available'),
(150, 'available'),
(151, 'available'),
(152, 'available'),
(153, 'available'),
(154, 'dirty'),
(155, 'available'),
(156, 'available'),
(157, 'available'),
(158, 'available'),
(159, 'available'),
(160, 'available'),
(161, 'available'),
(162, 'available'),
(163, 'available'),
(164, 'available')
;



-- adding new users. uder_id should be created automatically sice we put it as AUTO_INCREMENT
-- INSERT INTO users (user_name, user_password)
-- VALUES ;

-- adding to user_location
-- INSERT INTO user_location (user_ID, home_town, latitude, longitude)
-- VALUES ;
--
--


-- next step is to show all users with their user_id to enable input for the next step:
-- SELECT user_name, user_ID  FROM users;

-- aftrewards we will ask for assigning friends to new user's_id:
-- INSERT INTO friends (user_ID, friend_ID)
-- VALUES ;


-- Deleting clothes
-- DELETE FROM clothes
-- WHERE item_ID = " " ;

-- Adding new clothes. item_id is auto incremented so we do not have to ask for input
-- INSERT INTO clothes (item_type, item_description, weather_tag, occasion_tag, mood_tag)
-- VALUES ;


-- next step is to show all clothes to enable input for the next step:
-- SELECT item_ID, item_description, user_ID, user_name FROM ownership;


-- assigning clothes ownership
-- INSERT INTO ownership (item_ID, owner_ID)
-- VALUES ;


-- assigning availability status for the new item
-- INSERT INTO availability_status (item_ID, item_status)
-- VALUES ;


-- running 'laundry' function to clean the clothes, e.g.
-- UPDATE availability_status AS a
-- SET a.item_status = 'available'
-- WHERE a.item_status = 'dirty'
-- AND a.item_id IN (
--   SELECT o.item_id
--   FROM ownership AS o
--   WHERE o.owner_id = 1
-- );




-- changing the item status from 'available' to 'taken' after it was selected by a user
-- UPDATE availability_status AS a
-- SET a.item_status = 'taken'
-- WHERE a.item_id in (1,2,3);

-- changing the item status 'dirty' after user puts it away
-- UPDATE availability_status AS a
-- SET a.item_status = 'dirty'
-- WHERE a.item_id in (1,2,3);


-- overview of the wardrobes of your own and friends that YOU SHARE your wardrobe with
-- SELECT u1.user_id, u1.user_name, u2.user_id AS friend_id, u2.user_name AS friend_name
-- FROM users AS u1
-- INNER JOIN friends AS f ON u1.user_id = f.user_id
-- INNER JOIN users AS u2 ON f.friend_id = u2.user_id
-- WHERE u1.user_id in (2)
-- ORDER BY u1.user_id;


-- overview of users who put you as their friend to SHARE clothes WITH YOU:
-- SELECT u1.user_id, u1.user_name
-- FROM users AS u1
-- INNER JOIN friends AS f ON u1.user_id = f.user_id
-- INNER JOIN users AS u2 ON f.friend_id = u2.user_id
-- WHERE u2.user_id in (1)
-- AND u1.user_id <> 1
-- ORDER BY u2.user_id;


-- count of items with status 'available' for a certain user (user 1):
-- SELECT COUNT(*) AS count_available_items
-- FROM availability_status AS a
-- JOIN ownership AS o ON a.item_id = o.item_id
-- WHERE a.item_status = 'available' AND o.owner_id = 1;


-- count of items with status 'dirty' for a certain user (user 1):
-- SELECT COUNT(*) AS count_available_items
-- FROM availability_status AS a
-- JOIN ownership AS o ON a.item_id = o.item_id
-- WHERE a.item_status = 'dirty' AND o.owner_id = 1;



-- running a search based on certain tags:

-- SELECT c.item_description, c.item_id, o.owner_id
-- FROM clothes AS c
-- -- JOIN with availability_status TABLE
-- INNER JOIN
-- 	(SELECT item_id
-- 	FROM availability_status
-- 	WHERE item_status = 'available') AS a
-- ON c.item_ID = a.item_ID

-- -- JOIN with ownership TABLE
-- INNER JOIN ownership AS o
-- ON o.item_ID = c.item_ID

-- -- JOIN with friends TABLE
-- INNER JOIN
-- 	(SELECT user_ID
--     FROM friends
--     WHERE friend_ID = 1
--     ) AS f
-- ON f.user_ID = o.owner_ID

-- AND c.item_id IN (
--     SELECT c.item_ID
--     FROM clothes AS c
--     WHERE c.weather_tag = 'mild'
--     AND c.occasion_tag = 'work'
--     AND c.mood_tag = 'neutral' );





-- alternative code for performing the same search:

-- SELECT c.item_description, c.item_ID, o.owner_ID
-- FROM clothes AS c
-- INNER JOIN availability_status AS a ON c.item_ID = a.item_ID
-- INNER JOIN ownership AS o ON c.item_id = o.item_id
-- WHERE a.item_status = 'available'
-- AND c.item_id IN (
--     SELECT c.item_id
--     FROM clothes AS c
--     WHERE c.weather_tag = 'mild'
--     AND c.occasion_tag = 'work'
--     AND c.mood_tag = 'neutral'
-- )
-- AND c.item_id IN (
--     SELECT o.item_id
--     FROM ownership AS o
-- 	WHERE o.owner_id IN (
-- 		SELECT f.user_ID
-- 		FROM friends AS f
--         WHERE f.friend_ID = 1)
--         );