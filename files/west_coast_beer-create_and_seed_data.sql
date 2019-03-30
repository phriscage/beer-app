CREATE DATABASE IF NOT EXISTS `data`;

CREATE TABLE IF NOT EXISTS `data`.`beers` (
    `id` INTEGER(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `brewery` VARCHAR(255),
    `style`    VARCHAR(255),
    `price`    DECIMAL(13, 2),
    `name`    VARCHAR(255),
        `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO `data`.`beers`
    (brewery, style, price, name)
VALUES
    ('New Belgium Brewing', 'Red Ale - American Amber / Red', 4.50, 'Fat Tire'),
    ('Lagunitas Brewing Company', 'Pale Wheat Ale - American', 6.50, 'Little Sumpin\' Sumpin\' Ale'),
    ('Lagunitas Brewing Company', 'IPA - Imperical / Double', 6.90, 'Lagunitas Sucks'),
    ('Lagunitas Brewing Company', 'Strong Ale - American', 7.50, 'Undercover Investigation Shut-Down Ale'),
    ('Ballast Point Brewing Company', 'IPA - American', 6.95, 'Grapefruit Sculpin'),
    ('Ballast Point Brewing Company', 'IPA - American', 6.95, 'Pineapple Sculpin'),
    ('Russian River Brewing Company', 'IPA - Imperial / Double', 6.95, 'Pliny the Elder'),
    ('Stone Brewing', 'IPA - Session / India Session Ale', 5.95, 'Stone Go To IPA'),
    ('Firestone Walker Brewing Company', 'IPA - Session / India Session Ale', 5.95, 'Easy Jack')
