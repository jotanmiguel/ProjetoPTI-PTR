CREATE TABLE `User` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `email` varchar(255),
  `password` varchar(255),
  `address` adressObject,
  `nif` int,
  `phone` varchar(255),
  `role` varchar(255)
);

CREATE TABLE `Customer` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `firstName` varchar(255),
  `lastName` varchar(255),
  `shippingAdress` adressObject,
  `billingAdress` adressObject
);

CREATE TABLE `Supplier` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `name` varchar(255)
);

CREATE TABLE `ProductionUnit` (
  `id` int PRIMARY KEY,
  `supplier_id` int,
  `name` varchar(255),
  `address` adressObject
);

CREATE TABLE `Category` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `atributeIds` array,
  `parent_category_id` int
);

CREATE TABLE `Attribute` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `data_type` varchar(255)
);

CREATE TABLE `Product` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `description` varchar(255),
  `category_id` int,
  `supplier_id` int,
  `production_unit_id` int,
  `price` decimal
);

CREATE TABLE `ProductAttribute` (
  `id` int PRIMARY KEY,
  `product_id` int,
  `attribute_id` int,
  `value` varchar(255)
);

CREATE TABLE `Order` (
  `id` int PRIMARY KEY,
  `customer_id` int,
  `date` datetime,
  `status` varchar(255),
  `payment` Payment,
  `delivery` datetime,
  `productIds` array,
  `shippingAdress` adressObject
);

CREATE TABLE `OrderProduct` (
  `id` int PRIMARY KEY,
  `order_id` int,
  `product_id` int,
  `quantity` int
);

CREATE TABLE `Stock` (
  `id` int PRIMARY KEY,
  `product_id` int,
  `production_unit_id` int,
  `quantity` int
);

ALTER TABLE `Customer` ADD FOREIGN KEY (`user_id`) REFERENCES `User` (`id`);

ALTER TABLE `Supplier` ADD FOREIGN KEY (`user_id`) REFERENCES `User` (`id`);

ALTER TABLE `ProductionUnit` ADD FOREIGN KEY (`supplier_id`) REFERENCES `Supplier` (`id`);

ALTER TABLE `Category` ADD FOREIGN KEY (`atributeIds`) REFERENCES `Attribute` (`id`);

ALTER TABLE `Category` ADD FOREIGN KEY (`parent_category_id`) REFERENCES `Category` (`id`);

ALTER TABLE `Product` ADD FOREIGN KEY (`category_id`) REFERENCES `Category` (`id`);

ALTER TABLE `Product` ADD FOREIGN KEY (`supplier_id`) REFERENCES `Supplier` (`id`);

ALTER TABLE `Product` ADD FOREIGN KEY (`production_unit_id`) REFERENCES `ProductionUnit` (`id`);

ALTER TABLE `ProductAttribute` ADD FOREIGN KEY (`product_id`) REFERENCES `Product` (`id`);

ALTER TABLE `ProductAttribute` ADD FOREIGN KEY (`attribute_id`) REFERENCES `Attribute` (`id`);

ALTER TABLE `Order` ADD FOREIGN KEY (`customer_id`) REFERENCES `Customer` (`id`);

ALTER TABLE `OrderProduct` ADD FOREIGN KEY (`order_id`) REFERENCES `Order` (`id`);

ALTER TABLE `OrderProduct` ADD FOREIGN KEY (`product_id`) REFERENCES `Product` (`id`);

ALTER TABLE `Stock` ADD FOREIGN KEY (`product_id`) REFERENCES `Product` (`id`);

ALTER TABLE `Stock` ADD FOREIGN KEY (`production_unit_id`) REFERENCES `ProductionUnit` (`id`);
