CREATE DATABASE IF NOT EXISTS `data`;

CREATE TABLE IF NOT EXISTS `data`.`beers` (
	    `id` INTEGER(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	    `brewery` VARCHAR(255),
	    `style`    VARCHAR(255),
	    `price`    DECIMAL(13, 2),
	    `name` VARCHAR(255),
	    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
	);
	INSERT INTO `data`.`beers`
	    (brewery, style, price, name)
	VALUES
	    ('Dogfish Head', 'Strong Ale - American', 5.95, 'American Beauty'),
	    ('Dogfish Head', 'IPA - American', 6.95, '90 Minute IPA'),
	    ('Dogfish Head', 'Witbier', 5.95, 'Namaste'),
	    ('Carton Brewing Company', 'Other', 4.85, 'Boat Beer'),
	    ('Carton Brewing Company', 'IPA - Imperial / Double', 6.85, '077XX'),
	    ('Kane Brewing Company', 'IPA - American', 5.85, 'Head High'),
	    ('Tired Hands Brewing Company', 'IPA - American', 6.25, 'Alien Church'),
	    ('Tired Hands Brewing Company', 'Pale Ale - American', 5.99, 'HopHands'),
	    ('Maine Beer Company', 'Pale Ale - American', 5.50, 'Peeper Ale'),
	    ('Bell\'s Brewery', 'IPA - Imperial / Double', 6.50, 'Hopslam Ale (2017)'),
	    ('Bell\'s Brewery', 'IPA - American', 6.25, 'Two Hearted Ale'),
	    ('Fat Head\'s Brewery', 'IPA - Session / India Session Ale', 5.85, 'Sunshine Daydream Session IPA'),
	    ('Fat Head\'s Brewery', 'IPA - American', 5.85, 'Head Hunter IPA')
