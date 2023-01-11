-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 11, 2023 at 05:42 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pothole`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_pothole`
--

CREATE TABLE `account_pothole` (
  `p_id` int(11) NOT NULL,
  `address` varchar(500) NOT NULL,
  `remarks` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `img` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account_pothole`
--

INSERT INTO `account_pothole` (`p_id`, `address`, `remarks`, `date`, `img`) VALUES
(24, 'qewrw', 'rweqt', '2023-01-01', ''),
(25, 'fsssaf', 'fdsaf', '2023-01-04', ''),
(26, 'wewe', 'wewe', '2023-01-04', ''),
(27, 'wewe', 'wewe', '2023-01-04', ''),
(28, 'zzzzz', 'zzzzzzzzz', '2023-01-03', ''),
(29, 'zzzzz', 'zzzzzzzzz', '2023-01-03', ''),
(30, 'zzzz', 'aaaaa', '2023-01-03', ''),
(31, 'adas', 'fda', '2023-01-03', ''),
(32, 'wwwwwwww', 'qqqqqq', '2023-01-02', ''),
(33, 'zzc', 'czx', '2023-01-03', ''),
(34, 'zzc', 'czx', '2023-01-03', ''),
(35, 'aaa', 'ssss', '2023-01-04', 'images/beans.jpg'),
(36, 'owiru', 'oiherq', '2023-01-03', ''),
(37, 'asag', 'aewagw', '2023-01-02', 'images/Brinjal.jpg'),
(38, 'wow this worked', 'finallyyyy', '2023-01-03', 'images/Tomato_je.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `account_user`
--

CREATE TABLE `account_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_contractor` tinyint(1) NOT NULL,
  `is_corporator` tinyint(1) NOT NULL,
  `is_section_officer` tinyint(1) NOT NULL,
  `is_user` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account_user`
--

INSERT INTO `account_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_admin`, `is_contractor`, `is_corporator`, `is_section_officer`, `is_user`) VALUES
(1, 'pbkdf2_sha256$390000$I1RlRMt0FeLJFQ0aJReEqa$bSHGDRJdKl10eqoJnwnyEUafvjlWLQyv3G8J/ZoS4Sk=', '2023-01-09 15:47:15.957823', 0, 'Hari', '', '', 'hari@gmail.com', 0, 1, '2023-01-04 15:55:02.119037', 0, 0, 0, 0, 1),
(5, 'pbkdf2_sha256$390000$Z7QlKtN37UPjvRBL3Tw9Jd$ZzRNodHscBaEIDdSYIUn9DY2kSGilg+Z5fvIaFxAliw=', '2023-01-08 12:25:22.646792', 1, 'vhbj', '', '', 'vhbj@gmail.com', 1, 1, '2023-01-08 12:24:51.072555', 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `account_user_groups`
--

CREATE TABLE `account_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `account_user_user_permissions`
--

CREATE TABLE `account_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add pothole', 7, 'add_pothole'),
(26, 'Can change pothole', 7, 'change_pothole'),
(27, 'Can delete pothole', 7, 'delete_pothole'),
(28, 'Can view pothole', 7, 'view_pothole');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-01-08 12:25:39.743348', '35', 'Pothole object (35)', 2, '[{\"changed\": {\"fields\": [\"Img\"]}}]', 7, 5);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'account', 'pothole'),
(6, 'account', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-01-04 15:37:00.843051'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-01-04 15:37:01.014852'),
(3, 'auth', '0001_initial', '2023-01-04 15:37:03.518964'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-01-04 15:37:03.690764'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-01-04 15:37:03.690764'),
(6, 'auth', '0004_alter_user_username_opts', '2023-01-04 15:37:03.706531'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-01-04 15:37:03.737628'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-01-04 15:37:03.737628'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-01-04 15:37:03.753379'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-01-04 15:37:03.768999'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-01-04 15:37:03.784631'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-01-04 15:37:03.831491'),
(13, 'auth', '0011_update_proxy_permissions', '2023-01-04 15:37:03.862597'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-01-04 15:37:03.925082'),
(15, 'account', '0001_initial', '2023-01-04 15:37:07.710065'),
(16, 'account', '0002_remove_user_is_customer_remove_user_is_employee_and_more', '2023-01-04 15:37:07.913108'),
(17, 'admin', '0001_initial', '2023-01-04 15:37:08.897288'),
(18, 'admin', '0002_logentry_remove_auto_add', '2023-01-04 15:37:08.912873'),
(19, 'admin', '0003_logentry_add_action_flag_choices', '2023-01-04 15:37:08.928615'),
(20, 'sessions', '0001_initial', '2023-01-04 15:37:09.053464'),
(21, 'account', '0003_pothole', '2023-01-08 06:14:30.584216'),
(22, 'account', '0004_pothole_img', '2023-01-08 08:47:32.320541'),
(23, 'account', '0005_alter_pothole_img', '2023-01-08 08:52:30.380256'),
(24, 'account', '0006_alter_pothole_img', '2023-01-08 09:00:45.798790'),
(25, 'account', '0007_alter_pothole_img', '2023-01-08 09:05:12.456656'),
(26, 'account', '0008_alter_pothole_img', '2023-01-08 09:09:19.061962'),
(27, 'account', '0009_alter_pothole_img', '2023-01-08 09:14:25.688633'),
(28, 'account', '0010_alter_pothole_img', '2023-01-08 11:44:19.589103'),
(29, 'account', '0011_alter_pothole_img', '2023-01-08 12:09:49.713765'),
(30, 'account', '0012_alter_pothole_img', '2023-01-08 12:19:31.773722');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('c1rzo0cut2m14n6velwkck5jtdzfsasg', '.eJxVjDsOwjAQBe_iGln-O0tJzxksf3ZxANlSnFSIu0OkFNC-mXkvFuK21rANXMJc2JlJdvrdUswPbDso99hunefe1mVOfFf4QQe_9oLPy-H-HdQ46rdWJBPZKYHPKJzTykoAoUG5MmnjFGWK1khpABMS6GQVekSbhY9ERrP3B81gN7U:1pEuMl:bcgmx_nqDzSIJ1zeQXqTPJi40n0hVm0pliGdzxrtujU', '2023-01-23 15:47:15.967058'),
('h1qmsp73gv6az4i87596973czume6s5d', '.eJxVjDsOwyAQBe9CHSE-BkPK9D4DYhc2OIlAMnYV5e6xJRdJOzPvvVmI21rC1vMS5sSuzLDLL4OIz1wPkR6x3hvHVtdlBn4k_LSdTy3l1-1s_w5K7GVfi5zRShsVZUpIRozaj1rDoKQZyCtSCFokAEHCKSOd0DuMWqK36AjY5wvwfjf4:1pEUjq:-AhbzbEBJpd6oEFEjZKcO6x2PukRoRuHmg4rko5THhE', '2023-01-22 12:25:22.656150'),
('j53xo9vfpkzvbf9wfnjf2riz6oj7ab8v', '.eJxVjDsOwjAQBe_iGln-O0tJzxksf3ZxANlSnFSIu0OkFNC-mXkvFuK21rANXMJc2JlJdvrdUswPbDso99hunefe1mVOfFf4QQe_9oLPy-H-HdQ46rdWJBPZKYHPKJzTykoAoUG5MmnjFGWK1khpABMS6GQVekSbhY9ERrP3B81gN7U:1pD66h:uE5OavIxJu9ELU_QfXSRTIwlTWuRpEkPBYR2CtVUel0', '2023-01-18 15:55:11.378498'),
('ndakfuvf60vqcpkiyzrc0avxakdqx61f', '.eJxVjDsOwjAQBe_iGln-O0tJzxksf3ZxANlSnFSIu0OkFNC-mXkvFuK21rANXMJc2JlJdvrdUswPbDso99hunefe1mVOfFf4QQe_9oLPy-H-HdQ46rdWJBPZKYHPKJzTykoAoUG5MmnjFGWK1khpABMS6GQVekSbhY9ERrP3B81gN7U:1pDqhi:GM-b6IpluLY5Lft4CdS-pozGFeK2UgT5DuJh66Q2Vrs', '2023-01-20 17:40:30.189114'),
('og5xk16xj36noqz8so8ckd3eg8o5dod3', '.eJxVjDsOwjAQBe_iGln-O0tJzxksf3ZxANlSnFSIu0OkFNC-mXkvFuK21rANXMJc2JlJdvrdUswPbDso99hunefe1mVOfFf4QQe_9oLPy-H-HdQ46rdWJBPZKYHPKJzTykoAoUG5MmnjFGWK1khpABMS6GQVekSbhY9ERrP3B81gN7U:1pERod:vHpVgRMZAtl3kELSrf9TiOWjNG4HM0gTk-eEs6mNIs0', '2023-01-22 09:18:07.603036'),
('pgmwkjhege97ckaficzhx4wh95anqgps', '.eJxVjDsOwjAQBe_iGln-O0tJzxksf3ZxANlSnFSIu0OkFNC-mXkvFuK21rANXMJc2JlJdvrdUswPbDso99hunefe1mVOfFf4QQe_9oLPy-H-HdQ46rdWJBPZKYHPKJzTykoAoUG5MmnjFGWK1khpABMS6GQVekSbhY9ERrP3B81gN7U:1pD7e9:NAnifJ8PPLK4BT7UcRHkRCkD0N0KCq3C8QoUxH_ufIA', '2023-01-18 17:33:49.984422'),
('rlus76e2zf0pc1c4i7f05866wxq9plfq', 'e30:1pDqEE:LY8qXPiANKEsdiXSFpDi0TQPvgq5UVTn_eQfdiJ-CVw', '2023-01-20 17:10:02.931636');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_pothole`
--
ALTER TABLE `account_pothole`
  ADD PRIMARY KEY (`p_id`);

--
-- Indexes for table `account_user`
--
ALTER TABLE `account_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `account_user_groups`
--
ALTER TABLE `account_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_user_groups_user_id_group_id_4d09af3e_uniq` (`user_id`,`group_id`),
  ADD KEY `account_user_groups_group_id_6c71f749_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `account_user_user_permissions`
--
ALTER TABLE `account_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_user_user_permis_user_id_permission_id_48bdd28b_uniq` (`user_id`,`permission_id`),
  ADD KEY `account_user_user_pe_permission_id_66c44191_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_account_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_pothole`
--
ALTER TABLE `account_pothole`
  MODIFY `p_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `account_user`
--
ALTER TABLE `account_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `account_user_groups`
--
ALTER TABLE `account_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `account_user_user_permissions`
--
ALTER TABLE `account_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_user_groups`
--
ALTER TABLE `account_user_groups`
  ADD CONSTRAINT `account_user_groups_group_id_6c71f749_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `account_user_groups_user_id_14345e7b_fk_account_user_id` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`);

--
-- Constraints for table `account_user_user_permissions`
--
ALTER TABLE `account_user_user_permissions`
  ADD CONSTRAINT `account_user_user_pe_permission_id_66c44191_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `account_user_user_pe_user_id_cc42d270_fk_account_u` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_account_user_id` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
