/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - pola
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`pola` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pola`;

/*Table structure for table `address` */

DROP TABLE IF EXISTS `address`;

CREATE TABLE `address` (
  `userid` int(255) NOT NULL auto_increment,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address` longtext NOT NULL,
  `postcode` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  PRIMARY KEY  (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `address` */

insert  into `address`(`userid`,`username`,`email`,`address`,`postcode`,`mobile`) values (1,'a','a@gmail.com','ahgdfa','84654','987654321');

/*Table structure for table `categories` */

DROP TABLE IF EXISTS `categories`;

CREATE TABLE `categories` (
  `categoryId` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  UNIQUE KEY `categoryId` (`categoryId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `categories` */

insert  into `categories`(`categoryId`,`name`) values (1,'watch'),(2,'gajets'),(3,'TV'),(4,'Headphone'),(5,'Printers'),(6,'Accessories'),(7,'others');

/*Table structure for table `kart` */

DROP TABLE IF EXISTS `kart`;

CREATE TABLE `kart` (
  `userId` int(255) NOT NULL auto_increment,
  `username` varchar(255) NOT NULL,
  `productId` int(255) NOT NULL,
  PRIMARY KEY  (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `kart` */

insert  into `kart`(`userId`,`username`,`productId`) values (1,'a',0);

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `productId` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `image` longtext NOT NULL,
  `stock` varchar(255) NOT NULL,
  `categoryId` varchar(255) NOT NULL,
  UNIQUE KEY `productId` (`productId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`productId`,`name`,`price`,`description`,`image`,`stock`,`categoryId`) values ('1','SONY','1150','Resolution: HD Ready (1366x768) | Refresh Rate: 60 hertz\r\nConnectivity: 2 HDMI ports to connect set top box, Blu Ray players, gaming console | 2 USB ports to connect hard drives and other USB devices\r\nSound : 20 Watts Output | Open Baffle Speaker | ClearAudio+ technology | TV MusicBox\r\nSmart TV Features: Amazon Prime Video | Smart TV | Screen Mirroring | Netflix | HDR Gaming\r\nDisplay: HDR | X-Reality Pro | Motionflow XR 100\r\nWarranty Information: 1 year warranty provided by the manufacture from the date of purchase\r\nInstallation: Brand will contact for installation for this product once delivered. Contact Sony for assistance @ 18001037799 and provide product\'s model name and seller\'s details mentioned on your invoice. The service center will allot you a convenient slot for the service\r\nEasy returns: This product is eligible for replacement within 10 days of delivery in case of any product defects, damage or features not matching the description provided','sonyear.png','45','4'),('10','Onida 42 Inch','45000','Resolution : Full HD (1920x1080) | Refresh Rate: 60 hertz\r\nConnectivity: 3 HDMI ports to connect set top box, Blu-ray players, gaming console | 1 USB port to connect hard drives and other USB devices\r\nSound: 20 Watts Output | Dolby Digital Plus | DTS TruSurround\r\nSmart TV features : Dual band Wi-Fi | Built-in Fire TV OS | Alexa Voice Control | Display Mirroring for compatible devices | Voice Remote with Alexa | Live TV Tab | Apps: YouTube, Prime Video, Netflix, Hotstar, Zee5, SonyLiv and more\r\nWarranty Information: 1 Year warranty provided by Onida from date of purchase\r\nInstallation: For requesting installation/wall mounting/demo of this product once delivered, please directly call Onida support on 7490955555 and provide product\'s model name as well as seller\'s details mentioned on the invoice\r\nEasy returns: This product is eligible for replacement within 10 days of delivery in case of any product defects, damage or features not matching the description provided','onidatv.jpeg','148','3'),('11','One plus 22 Inch','22000','Resolution: HD Ready (1366x768) | Refresh Rate: 60 hertz\r\nConnectivity: 2 HDMI ports to connect set top box, Blu Ray players, gaming console | 2 USB ports to connect hard drives and other USB devices, Dimensions(TV With Stand) - 71.3cm*20cm*46.9cm, VESA Hole Pitch - 20cm*20cm\r\nSound : 20 Watts Output | Dolby Audio\r\nSmart TV Features: Android TV 9.0 | OnePlus Connect | Google Assistant | Play Store | Chromecast | Shared Album | Supported Apps : Netflix, YouTube, Prime video | Content Calendar | OxygenPlay\r\nDisplay : LED Panel | Noise Reduction | Colour Space Mapping |Dynamic Contrast | Anti-Aliasing | DCI-P3 93% colour gamut | Gamma Engine\r\nDesign: Bezel-less | Screen/Body Ratio = 91.4%\r\nWarranty Information: 1 year comprehensive warranty and additional 1 year on panel provided by the manufacturer from date of purchase','bpltv.jpg','357','3'),('12','HCL Keyboards','650','Hot keys function: volume, mute, play/pause, backward, forward. Illuminated Keys : No\r\nThe convenient multimedia keys let you easily access functions such as play, pause, rewind and fast-forward plus volume control\r\nWith a compact design that still features a full-sized keyboard and number pad, the Dell wired keyboard is ideal for home and office environments\r\nDell wired keyboard also has a palm rest that is available for separate purchase\r\nInterface: usb, device type: keyboard - wired, dimensions (wxdxh) 44. 2 Cm x 12. 7 Cm x 2. 44 Cm, weight: 503 g\r\n1 Year replacement warranty by dell as per dell\'s warranty & replacement policy','hclkey.jpg','316','6'),('13','MAC Keyboard','2550','Magic Keyboard delivers a remarkably comfortable and precise typing experience\r\nIt’s also wireless and rechargeable, with an incredibly long-lasting internal battery that’ll power your keyboard for about a month or more between charges\r\nIt pairs automatically with your Mac, so you can get to work straightaway\r\nAnd it includes a woven USB-C to Lightning Cable that lets you pair and charge by connecting to a USB-C port on your Mac.\r\nWhat\'s in the Box: Magic Keyboard, USB-C to Lightning Cable\r\nSystem Requirements: Mac with macOS 11.3 or later, iPad running iPadOS 14.5 or later, iPhone and iPod touch with iOS 14.5 or later','mackey.jpg','354','6'),('14','Keyboard Combo','4500','A set of three items','combo.jpg','468','6'),('15','OTG','70','Micro USB OTG For supported Phones & Tablets,\r\nPlease note that this OTG cable cable works only with OTG supported devices,\r\nCan be used for Pen Drive, Keyboard, Mouse,\r\nCompatibe with major new Android phone models,\r\nPack Contains 1 Shiny Black OTG Cable','otg.jpg','159','6'),('16','DELL LAPTOP','45000','Free upgrade to Windows 11 when available,\r\nDisclaimer-Upgrade rollout plan is being finalized and is scheduled to begin late in 2021 and continue into 2022,\r\nSpecific timing will vary by device i5-1135G7,\r\n8GB DDR4 | 512GB SSD | Win 10 + Office H&S 2019,\r\nINTEGRATED | Standard Keyboard,\r\n1 Year Onsite Hardware Service | NO ODD','dellLap.jpg','4895','7'),('17','Lenovo Laptop','7050','Processor: 11th Gen Intel Core i5-1135G7 processor, base speed 2.4 Ghz, max speed 4.2 Ghz, 4 Cores, 8 MB smart cache | Memory: 8GB DDR4 RAM 3200 MHz, upgradable up to 16 GB | Storage: 512GB SSD,\r\nOperating System: Preloaded Windows 10 Home with Lifetime Validity | Pre-installed software: Microsoft Office Home & Student 2019,\r\nDisplay: 15.6-inch screen with (1920x1080) FHD Antiglare display | TÜV Rheinland Low Blue Light Certified | Graphics: Intel UHD Graphics | Monitor Supports: Supports up to 2 independent displays,\r\nPorts: 1x USB 2.0 | 1x USB 3.2 Gen 1 | 1x USB-C 3.2 Gen 1 (support data transfer only) | 1x HDMI 1.4b | 1x Ethernet RJ-45 (LAN Port) | 1x Headphone / microphone combo jack (3.5mm),\r\nKeyboard: Spill Resistant Keyboard protects from accidental spills, Touchpad: Buttonless Mylar surface multi-touch touchpad, supports Precision TouchPad\r\n','samtab.jpg','128','7'),('18','ASUS Laptop','750','Full HD LED Backlit Anti-glare IPS Display (250 nits Brightness, 1:1000 Contrast Ratio, 45% NTSC Color Gamut, 67% sRGB, 50% Adobe, 170 Degree Viewing Angle, 144 Hz Refresh Rate),\r\nThis laptop comes with USB 3.2 Type-C with DisplayPort to give you fast transfers,\r\nBuilt-in Dual Speakers. Built-in Microphone,\r\nGraphic Processor: NVIDIA Geforce GTX 1650 Ti,\r\n','asus.jpg','167','7'),('19','Acer Laptop','3550','10 Generation Intel Core i7-10870H processor,\r\n1 TB SSD, PCIe Gen3, 8 Gb/s, NVMe,\r\n16 GB of DDR4 system memory, upgradable to 32 GB using two soDIMM modules,\r\nSupports up to 2 TB HDD 6.3 cm (2.5-inch) 5400 RPM,\r\nAlexa Built-in','acer.jpg','1687','7'),('2','JBL','1550','JBL Signature Sound,\r\n5 Hours of Playtime under optimum audio settings,\r\nWireless Bluetooth Streaming , Frequency response 180Hz – 20kHz,\r\nLong Press Play Button to Activate Google Assistant or Siri,\r\nNoise-cancelling Speakerphone, 600mAh, Battery charge time 1.5 hours,\r\nAudio Cable Input,\r\nWhat’s in the box: 1 x JBL GO, 1 x Micro USB cable for charging, 1 x Safety Sheet, 1 x Quick Start Guide, 1 x Warranty Card','jblear.jpg','515','4'),('20','DRONE','5000','Has 2.7K Camera,\r\n3-Axis Gimbal GPS 30min Flight Time,\r\nColour: White and black','123.png','6542','2'),('21','Smart watch','1250','A red color watch?Bluetooth Calling Watch?- Fire-Boltt Ring enables you to make and receive calls directly from your watch via the built-in speaker and microphone. This smartwatch features a dial pad, option to access recent calls & sync your phone’s contacts,\r\n?How to activate Bluetooth Calling?- To enable Bluetooth Calling Function, first connect it to the compatible app. Once connected, manually go to the phone\'s Bluetooth settings and pair this smartwatch (Bluetooth Name: BSW005). Upon pairing, you will get a notification: Connected for calls and audio.,\r\n?SPo2 & Heart Rate Tracking? - The Smartwatch tracks your real time Blood Oxygen Spo2 and has 24*7 Heart Rate Tracking. It also has Sleep and Fitness Tracking.,\r\n?1.7 inch HD Full Touch? - Industry Best Display of 1.7 Inches Size ?Full Metal Body with Changeable Strap? - Sleek & Fashionable Metal Body The one-click control mode and honey comb menu helps you quickly navigate ? Battery Life?- The watch can work for 24 Hours with Bluetooth Calling ( Normal Usage )*, 8 Days without Bluetooth Calling','e.png','357','1'),('22','Smart watch','1250','(SpO2) Blood-oxygen Level Measurement,\r\nStress Monitoring with Breathing Training,\r\nHeart Rate Monitoring and PAI Heath Assessment System,\r\n60+ Sports Modes and 5 ATM Water Resistance,\r\nSmart Notifications for Incoming Calls, Text Messages, Apps, and Calendars,\r\nCheck Out Our Store : Click on the blue Amazfit link below the Product title to explore our other models.','w.png','3579','1'),('23','Smart watch','1150','Monitors your heart rate, Blood pressure, Oxygen level in blood and sleep: The advanced technology perfectly syncs with your lifestyle and monitors your health all day, and night. This watch is a technological marvel,\r\nComes with 100+ Watch faces, Dynamic Display with full touch control: Pebble Pace has a full touch colorful dynamic display with haptic touch. Now feel every touch and add more color to your world. Now charge it and let your smart watch do the rest,\r\nInbuilt Speed pedometer and Multiple Workout mode: Pebble Pace has a highly accurate active step pedometer, and multiple workout modes that accurately monitors your workouts every day. Let nothing derail your fitness goals now.,\r\nUp to 14 days battery backup - The powerful 150 mAh battery along with the advanced smart sensors give the Pebble Pace a massive standby battery backup of 14 days and last 7 days of active use. Now charge it and let your smart watch do the rest.','r.png','187','1'),('24','Mi note Pro','7999','12MP+5MP dual rear camera | 20MP+2MP dual front camera,\r\n15.9004 centimeters (6.26-inch) multi-touch capacitive touchscreen with 2280 x 1080 pixels resolution,\r\nMemory, Storage & SIM: 6GB RAM | 64GB internal memory expandable up to 256GB | Dual SIM (micro+nano) dual-standby (4G+4G),\r\nAndroid Oreo v8.1 operating system with 1.8GHz Qualcomm Snapdragon 636 processor, Adreno 509,\r\n4000mAH lithium-ion battery','mi.png','59','2'),('25','Mi note 5 pro','16999','12MP+5MP dual rear camera | 20MP+2MP dual front camera,\r\n15.9004 centimeters (6.26-inch) multi-touch capacitive touchscreen with 2280 x 1080 pixels resolution,\r\nMemory, Storage & SIM: 6GB RAM | 64GB internal memory expandable up to 256GB | Dual SIM (micro+nano) dual-standby (4G+4G),\r\nAndroid Oreo v8.1 operating system with 1.8GHz Qualcomm Snapdragon 636 processor, Adreno 509,\r\n4000mAH lithium-ion battery','sd.png','4563','2'),('3','Samsung','500','12MP+5MP dual rear camera | 20MP+2MP dual front camera,\r\n15.9004 centimeters (6.26-inch) multi-touch capacitive touchscreen with 2280 x 1080 pixels resolution,\r\nMemory, Storage & SIM: 6GB RAM | 64GB internal memory expandable up to 256GB | Dual SIM (micro+nano) dual-standby (4G+4G),\r\nAndroid Oreo v8.1 operating system with 1.8GHz Qualcomm Snapdragon 636 processor, Adreno 509,\r\n4000mAH lithium-ion battery','samear.jpg','58','4'),('4','HP printer','7500','high branded printer with gud outut','hpprint.jpg','123','5'),('5','Godrej printers','11150','HIGHLY AFFORDABLE PRINTER FOR YOUR PRINT, SCAN AND COPY NEEDS,\r\nSIMPLE SET UP FROM YOUR PC: Use the HP Smart app to set up with USB in few easy steps. Automatic paper sensor : No,\r\nRELIABLE CONNECTIVITY : High-speed USB 2.0 Connectivity,\r\nCost-per-page: Rs 6 (Black), Rs 8 (Color), as per ISO standards,\r\nSAVE YOUR PRODUCTIVE TIME: High speed printing for Home needs; Black: Up to 7.5 ppm (ISO) ;Color: Up to 5.5 ppm (ISO),\r\nVERSATILE PRINT/MEDIA OPTIONS: Supports A4; B5; A6; DL envelope,\r\nPEACE OF MIND SERVICE SUPPORT: HP ON-SITE 1-YEAR WARRANTY (Use genuine HP 805 Black Original Ink Cartridge,HP 805 Tri-Colour Original Ink Cartridge)','godrejprint.jpg','45','5'),('6','HCL printers','12000','HIGHLY AFFORDABLE PRINTER FOR YOUR PRINT, SCAN AND COPY NEEDS,\r\nSIMPLE SET UP FROM YOUR PC: Use the HP Smart app to set up with USB in few easy steps. Automatic paper sensor : No,\r\nRELIABLE CONNECTIVITY : High-speed USB 2.0 Connectivity,\r\nCost-per-page: Rs 6 (Black), Rs 8 (Color), as per ISO standards,\r\nSAVE YOUR PRODUCTIVE TIME: High speed printing for Home needs; Black: Up to 7.5 ppm (ISO) ;Color: Up to 5.5 ppm (ISO),\r\nVERSATILE PRINT/MEDIA OPTIONS: Supports A4; B5; A6; DL envelope,\r\nPEACE OF MIND SERVICE SUPPORT: HP ON-SITE 1-YEAR WARRANTY (Use genuine HP 805 Black Original Ink Cartridge,HP 805 Tri-Colour Original Ink Cartridge)','HCLprint.jpg','146','5'),('7','EPSON Printers','15000','HIGHLY AFFORDABLE PRINTER FOR YOUR PRINT, SCAN AND COPY NEEDS,\r\nSIMPLE SET UP FROM YOUR PC: Use the HP Smart app to set up with USB in few easy steps. Automatic paper sensor : No,\r\nRELIABLE CONNECTIVITY : High-speed USB 2.0 Connectivity,\r\nCost-per-page: Rs 6 (Black), Rs 8 (Color), as per ISO standards,\r\nSAVE YOUR PRODUCTIVE TIME: High speed printing for Home needs; Black: Up to 7.5 ppm (ISO) ;Color: Up to 5.5 ppm (ISO),\r\nVERSATILE PRINT/MEDIA OPTIONS: Supports A4; B5; A6; DL envelope,\r\nPEACE OF MIND SERVICE SUPPORT: HP ON-SITE 1-YEAR WARRANTY (Use genuine HP 805 Black Original Ink Cartridge,HP 805 Tri-Colour Original Ink Cartridge)','epsonprint.jpg','8463','5'),('8','Panasonic 32','25000','Resolution: HD Ready (1366x768) | Refresh Rate: 60 hertz\r\nConnectivity: 2 HDMI ports to connect set top box, Blu Ray players, gaming console | 2 USB ports to connect hard drives and other USB devices, Dimensions(TV With Stand) - 71.3cm*20cm*46.9cm, VESA Hole Pitch - 20cm*20cm\r\nSound : 20 Watts Output | Dolby Audio\r\nSmart TV Features: Android TV 9.0 | OnePlus Connect | Google Assistant | Play Store | Chromecast | Shared Album | Supported Apps : Netflix, YouTube, Prime video | Content Calendar | OxygenPlay\r\nDisplay : LED Panel | Noise Reduction | Colour Space Mapping |Dynamic Contrast | Anti-Aliasing | DCI-P3 93% colour gamut | Gamma Engine\r\nDesign: Bezel-less | Screen/Body Ratio = 91.4%\r\nWarranty Information: 1 year comprehensive warranty and additional 1 year on panel provided by the manufacturer from date of purchase','panosonictv.jpg','612','3'),('9','Sony 3D','50000','Resolution : 4K Ultra HD (3840x2160) | Refresh Rate: 100 hertz\r\nConnectivity: 4 HDMI Ports To Connect Set Top Box, Blu Ray Players, Gaming Console | 3 Usb Ports To Connect Hard Drives and Other Usb Devices\r\nSound Output: Acoustic Surface Audio | Dolby Atmos | Sound Ambient Optimization | Voice Zoom | S Force Front Surround\r\nSmart TV Features: Android TV | Google Play | Google Assistant | Chromecast | Netflix Calibrated Mode | Calman Ready | Works With Apple Airplay | Works With Apple Homekit | Works With Alexa\r\nDisplay: X1 Ultimate Processor | Pixel Contrast Booster |X Motion Clarity | Ambient Optimization | HDMI 2.1\r\nWarranty Information: 2 year warranty provided by the manufacture from the date of purchase (Included Comprehensive and Additional warranty on Panel).\r\nInstallation: For installation/wall mounting/demo of this product once delivered, directly contact Sony at 18001037799 and provide product\'s model name and seller\'s details mentioned on your invoice. The service center will allot you a convenient slot for the service\r\nEasy returns: This product is eligible for replacement within 10 days of delivery in case of any product defects, damage or features not matching the description provided','sonytv.jpg','586','3');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(255) NOT NULL auto_increment,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`email`,`pass`) values (1,'a','a@gmail.com','a');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
