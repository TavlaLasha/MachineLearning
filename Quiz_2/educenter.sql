-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 17, 2020 at 10:44 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `educenter`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) UNSIGNED NOT NULL,
  `pn` int(10) NOT NULL,
  `hours` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `pn`, `hours`) VALUES
(1, 588, 4.35),
(2, 588, 1.78),
(3, 588, 1.46),
(4, 588, 2.99),
(5, 588, 4.32),
(6, 588, 0.46),
(7, 588, 2.09),
(8, 884, 1.85),
(9, 884, 2.18),
(10, 884, 0.42),
(11, 884, 4.32),
(12, 884, 0.32),
(13, 884, 0.71),
(14, 884, 1.68),
(15, 796, 2.99),
(16, 796, 2.28),
(17, 796, 4.38),
(18, 796, 3.79),
(19, 796, 0.41),
(20, 796, 2.23),
(21, 796, 2.9),
(22, 727, 3.21),
(23, 727, 0.79),
(24, 727, 2.61),
(25, 727, 2.33),
(26, 727, 0.66),
(27, 727, 2.09),
(28, 727, 3.3),
(29, 976, 4.22),
(30, 976, 4.86),
(31, 976, 1.74),
(32, 976, 2.99),
(33, 976, 3.75),
(34, 976, 1.62),
(35, 976, 0.88),
(36, 302, 4.76),
(37, 302, 2.43),
(38, 302, 0.47),
(39, 302, 0.2),
(40, 302, 4.53),
(41, 302, 3.67),
(42, 302, 1.49),
(43, 267, 3.24),
(44, 267, 0.8),
(45, 267, 0.75),
(46, 267, 4.54),
(47, 267, 0.26),
(48, 267, 1.65),
(49, 267, 3.81),
(50, 596, 4.83),
(51, 596, 1.45),
(52, 596, 2.08),
(53, 596, 3.47),
(54, 596, 4.24),
(55, 596, 1.46),
(56, 596, 4.03),
(57, 905, 1.71),
(58, 905, 1.48),
(59, 905, 2.52),
(60, 905, 0.75),
(61, 905, 3.85),
(62, 905, 4.1),
(63, 905, 0.75),
(64, 757, 2.58),
(65, 757, 2.11),
(66, 757, 4.65),
(67, 757, 0.38),
(68, 757, 2.91),
(69, 757, 4),
(70, 757, 4.57),
(71, 538, 1.48),
(72, 538, 2.88),
(73, 538, 4.19),
(74, 538, 4.08),
(75, 538, 0.26),
(76, 538, 3.92),
(77, 538, 2.29),
(78, 879, 1.3),
(79, 879, 2.12),
(80, 879, 1.22),
(81, 879, 2.63),
(82, 879, 2.1),
(83, 879, 1.62),
(84, 879, 0.35),
(85, 941, 0.72),
(86, 941, 4.72),
(87, 941, 4.83),
(88, 941, 3.91),
(89, 941, 3.61),
(90, 941, 4.69),
(91, 941, 3.93),
(92, 686, 4.01),
(93, 686, 1.83),
(94, 686, 3.51),
(95, 686, 3.54),
(96, 686, 3.65),
(97, 686, 4.79),
(98, 686, 3.18),
(99, 177, 0.9),
(100, 177, 2.53),
(101, 177, 1.05),
(102, 177, 2.89),
(103, 177, 3.64),
(104, 177, 1.05),
(105, 177, 2.38),
(106, 955, 2.02),
(107, 955, 4.29),
(108, 955, 2.93),
(109, 955, 3.28),
(110, 955, 3.58),
(111, 955, 0.83),
(112, 955, 4.5),
(113, 747, 2.95),
(114, 747, 3.4),
(115, 747, 0.15),
(116, 747, 4.36),
(117, 747, 4.5),
(118, 747, 1.94),
(119, 747, 2),
(120, 885, 1.84),
(121, 885, 2.19),
(122, 885, 3.72),
(123, 885, 0.59),
(124, 885, 0.05),
(125, 885, 4.49),
(126, 885, 3.92),
(127, 268, 2.26),
(128, 268, 1.95),
(129, 268, 3.26),
(130, 268, 3.29),
(131, 268, 4.14),
(132, 268, 2.31),
(133, 268, 4.66),
(134, 947, 3.74),
(135, 947, 2.57),
(136, 947, 0.24),
(137, 947, 2.56),
(138, 947, 4.16),
(139, 947, 3.29),
(140, 947, 1.88),
(141, 261, 2.54),
(142, 261, 4.57),
(143, 261, 4.67),
(144, 261, 2.37),
(145, 261, 1.61),
(146, 261, 1.08),
(147, 261, 4.89),
(148, 219, 4.6),
(149, 219, 1.68),
(150, 219, 1.33),
(151, 219, 0.36),
(152, 219, 1.29),
(153, 219, 1.61),
(154, 219, 4.74),
(155, 190, 2.54),
(156, 190, 0.88),
(157, 190, 1.29),
(158, 190, 4.03),
(159, 190, 4.83),
(160, 190, 0.33),
(161, 190, 0.54),
(162, 809, 2.75),
(163, 809, 2.19),
(164, 809, 4.92),
(165, 809, 2.87),
(166, 809, 0.57),
(167, 809, 1.25),
(168, 809, 1.36),
(169, 998, 0.2),
(170, 998, 2.29),
(171, 998, 1.89),
(172, 998, 2.99),
(173, 998, 3.22),
(174, 998, 1.16),
(175, 998, 2.57),
(176, 883, 4),
(177, 883, 4.87),
(178, 883, 3.53),
(179, 883, 0.57),
(180, 883, 0.79),
(181, 883, 2.87),
(182, 883, 3.4),
(183, 111, 2.55),
(184, 111, 3.32),
(185, 111, 0.83),
(186, 111, 1.43),
(187, 111, 3.12),
(188, 111, 1.22),
(189, 111, 2.66),
(190, 784, 4.79),
(191, 784, 2.3),
(192, 784, 0.8),
(193, 784, 4.42),
(194, 784, 1.33),
(195, 784, 1.02),
(196, 784, 4.13),
(197, 700, 4.94),
(198, 700, 0.44),
(199, 700, 0.21),
(200, 700, 4.08),
(201, 700, 4.45),
(202, 700, 0.09),
(203, 700, 1.8),
(204, 468, 3.28),
(205, 468, 1.34),
(206, 468, 2.33),
(207, 468, 4.02),
(208, 468, 3.7),
(209, 468, 1.31),
(210, 468, 4.4),
(211, 441, 1.26),
(212, 441, 1.74),
(213, 441, 3.43),
(214, 441, 1.37),
(215, 441, 4.61),
(216, 441, 4.68),
(217, 441, 3.62),
(218, 230, 2.68),
(219, 230, 1.57),
(220, 230, 2.35),
(221, 230, 0.02),
(222, 230, 4.79),
(223, 230, 1.07),
(224, 230, 3.73),
(225, 140, 0.41),
(226, 140, 2.56),
(227, 140, 3.31),
(228, 140, 4.86),
(229, 140, 0.04),
(230, 140, 1.05),
(231, 140, 0.18),
(232, 247, 2.68),
(233, 247, 2.06),
(234, 247, 3.68),
(235, 247, 1.63),
(236, 247, 4.48),
(237, 247, 0.56),
(238, 247, 4.33),
(239, 910, 3.08),
(240, 910, 1.93),
(241, 910, 2.55),
(242, 910, 3.64),
(243, 910, 4.39),
(244, 910, 3.9),
(245, 910, 1.54),
(246, 776, 0.91),
(247, 776, 3.63),
(248, 776, 2.51),
(249, 776, 3.13),
(250, 776, 4.63),
(251, 776, 0.2),
(252, 776, 4.26),
(253, 984, 3.62),
(254, 984, 0.66),
(255, 984, 2.4),
(256, 984, 3.47),
(257, 984, 4.14),
(258, 984, 0.01),
(259, 984, 1.23),
(260, 857, 0.42),
(261, 857, 1.02),
(262, 857, 4.03),
(263, 857, 2.92),
(264, 857, 4.77),
(265, 857, 2.94),
(266, 857, 2.15),
(267, 725, 0.25),
(268, 725, 0.67),
(269, 725, 3.32),
(270, 725, 3.08),
(271, 725, 1.71),
(272, 725, 4.45),
(273, 725, 4.05),
(274, 193, 4.47),
(275, 193, 4.13),
(276, 193, 1.79),
(277, 193, 1),
(278, 193, 4.18),
(279, 193, 1.23),
(280, 193, 4.32),
(281, 840, 3.74),
(282, 840, 2.93),
(283, 840, 1.41),
(284, 840, 0.86),
(285, 840, 0.94),
(286, 840, 3.35),
(287, 840, 2.94),
(288, 824, 3.52),
(289, 824, 3.94),
(290, 824, 1.82),
(291, 824, 2.76),
(292, 824, 4.64),
(293, 824, 0.41),
(294, 824, 0.52),
(295, 677, 1.37),
(296, 677, 4.56),
(297, 677, 1.39),
(298, 677, 1.86),
(299, 677, 3.16),
(300, 677, 1.59),
(301, 677, 0.21),
(302, 292, 2.72),
(303, 292, 1.57),
(304, 292, 1.28),
(305, 292, 4.65),
(306, 292, 2.82),
(307, 292, 3.65),
(308, 292, 0.3),
(309, 620, 3.05),
(310, 620, 1.99),
(311, 620, 4.9),
(312, 620, 0.99),
(313, 620, 4.86),
(314, 620, 3.46),
(315, 620, 0.93),
(316, 313, 4.87),
(317, 313, 1.07),
(318, 313, 4.76),
(319, 313, 0.11),
(320, 313, 3.55),
(321, 313, 0.57),
(322, 313, 2.3),
(323, 327, 1.02),
(324, 327, 3.18),
(325, 327, 1.55),
(326, 327, 2.59),
(327, 327, 2.08),
(328, 327, 0.95),
(329, 327, 2.37),
(330, 285, 3.24),
(331, 285, 3.87),
(332, 285, 2.61),
(333, 285, 3.8),
(334, 285, 2.04),
(335, 285, 0.84),
(336, 285, 3.17),
(337, 791, 0.18),
(338, 791, 4.59),
(339, 791, 4.67),
(340, 791, 3.57),
(341, 791, 0.94),
(342, 791, 3.59),
(343, 791, 2.29),
(344, 690, 0.79),
(345, 690, 1.58),
(346, 690, 2.06),
(347, 690, 1.81),
(348, 690, 1.41),
(349, 690, 2.2),
(350, 690, 1.25),
(351, 207, 0.09),
(352, 207, 2.07),
(353, 207, 0.82),
(354, 207, 0.38),
(355, 207, 0.74),
(356, 207, 1.41),
(357, 207, 2.25),
(358, 253, 2.21),
(359, 253, 1.2),
(360, 253, 3.37),
(361, 253, 1.1),
(362, 253, 0.97),
(363, 253, 1.58),
(364, 253, 3.67),
(365, 403, 1.66),
(366, 403, 2.26),
(367, 403, 4.23),
(368, 403, 4.22),
(369, 403, 0.14),
(370, 403, 0.19),
(371, 403, 3.83),
(372, 369, 2.98),
(373, 369, 3.78),
(374, 369, 0.32),
(375, 369, 0.6),
(376, 369, 4.49),
(377, 369, 1.16),
(378, 369, 3.28),
(379, 303, 2.19),
(380, 303, 0.57),
(381, 303, 0.92),
(382, 303, 4.63),
(383, 303, 0.67),
(384, 303, 0.16),
(385, 303, 4.19),
(386, 485, 1.06),
(387, 485, 2.56),
(388, 485, 3.49),
(389, 485, 0.82),
(390, 485, 2.74),
(391, 485, 1.3),
(392, 485, 4.39),
(393, 467, 4.72),
(394, 467, 2.37),
(395, 467, 3.24),
(396, 467, 3.8),
(397, 467, 2.46),
(398, 467, 3.65),
(399, 467, 4.98),
(400, 975, 0.24),
(401, 975, 3.59),
(402, 975, 0.71),
(403, 975, 0.19),
(404, 975, 4.24),
(405, 975, 4.55),
(406, 975, 2.31),
(407, 649, 1.91),
(408, 649, 1.56),
(409, 649, 1.84),
(410, 649, 0.9),
(411, 649, 3.5),
(412, 649, 3.56),
(413, 649, 3.95),
(414, 626, 1.49),
(415, 626, 0.62),
(416, 626, 1.4),
(417, 626, 2.81),
(418, 626, 0.49),
(419, 626, 2.5),
(420, 626, 1.41),
(421, 411, 0.79),
(422, 411, 0.69),
(423, 411, 2.56),
(424, 411, 2.13),
(425, 411, 3.25),
(426, 411, 3.31),
(427, 411, 0.13),
(428, 373, 4.5),
(429, 373, 2.1),
(430, 373, 0.03),
(431, 373, 2.3),
(432, 373, 4.86),
(433, 373, 3.04),
(434, 373, 4.76),
(435, 402, 2.7),
(436, 402, 4.86),
(437, 402, 4.05),
(438, 402, 2.92),
(439, 402, 4.66),
(440, 402, 4.08),
(441, 402, 1.98),
(442, 720, 3.47),
(443, 720, 2.3),
(444, 720, 2.14),
(445, 720, 2.21),
(446, 720, 2.14),
(447, 720, 1.49),
(448, 720, 1.53),
(449, 363, 3.32),
(450, 363, 0.97),
(451, 363, 1.76),
(452, 363, 0.12),
(453, 363, 2.18),
(454, 363, 1.1),
(455, 363, 0.69),
(456, 636, 0.69),
(457, 636, 4.22),
(458, 636, 0.1),
(459, 636, 2.19),
(460, 636, 2.15),
(461, 636, 1.89),
(462, 636, 4.81),
(463, 315, 4.08),
(464, 315, 2.75),
(465, 315, 2.16),
(466, 315, 2.19),
(467, 315, 4.37),
(468, 315, 2.4),
(469, 315, 0),
(470, 715, 3.9),
(471, 715, 4.1),
(472, 715, 4.76),
(473, 715, 4.47),
(474, 715, 1.99),
(475, 715, 2.33),
(476, 715, 4.44),
(477, 674, 4.57),
(478, 674, 1.32),
(479, 674, 3.43),
(480, 674, 4.8),
(481, 674, 2.73),
(482, 674, 3.2),
(483, 674, 0.08),
(484, 383, 4.86),
(485, 383, 3.01),
(486, 383, 0.36),
(487, 383, 3.7),
(488, 383, 2.14),
(489, 383, 1.19),
(490, 383, 0.11),
(491, 993, 3.53),
(492, 993, 1.55),
(493, 993, 3.32),
(494, 993, 2.09),
(495, 993, 4.55),
(496, 993, 0.74),
(497, 993, 1.03),
(498, 338, 4.39),
(499, 338, 2.84),
(500, 338, 2.63),
(501, 338, 4.42),
(502, 338, 3.68),
(503, 338, 1.37),
(504, 338, 2.44),
(505, 718, 2.09),
(506, 718, 3.21),
(507, 718, 3.54),
(508, 718, 3.01),
(509, 718, 0.08),
(510, 718, 1.9),
(511, 718, 4.33),
(512, 787, 1.64),
(513, 787, 2.61),
(514, 787, 2.99),
(515, 787, 2.48),
(516, 787, 3.31),
(517, 787, 2.26),
(518, 787, 1.83),
(519, 159, 3.04),
(520, 159, 3.04),
(521, 159, 3.8),
(522, 159, 2.03),
(523, 159, 2),
(524, 159, 3.16),
(525, 159, 1.38),
(526, 828, 3.84),
(527, 828, 0.74),
(528, 828, 0.1),
(529, 828, 3.15),
(530, 828, 2.81),
(531, 828, 4.18),
(532, 828, 0.11),
(533, 539, 4.14),
(534, 539, 4.34),
(535, 539, 4.75),
(536, 539, 0.32),
(537, 539, 1.37),
(538, 539, 3.38),
(539, 539, 3.75),
(540, 739, 3.17),
(541, 739, 0.95),
(542, 739, 2.41),
(543, 739, 4.25),
(544, 739, 4.31),
(545, 739, 4.4),
(546, 739, 1.79),
(547, 180, 2.43),
(548, 180, 4.52),
(549, 180, 0.29),
(550, 180, 3.14),
(551, 180, 3.53),
(552, 180, 4.55),
(553, 180, 3.25),
(554, 716, 4.9),
(555, 716, 4.95),
(556, 716, 2.6),
(557, 716, 0.56),
(558, 716, 3.45),
(559, 716, 4.05),
(560, 716, 2.61),
(561, 258, 0.31),
(562, 258, 2.94),
(563, 258, 4.61),
(564, 258, 0.92),
(565, 258, 4.05),
(566, 258, 1.53),
(567, 258, 4.59),
(568, 934, 3.12),
(569, 934, 3.81),
(570, 934, 2.88),
(571, 934, 4.9),
(572, 934, 3.39),
(573, 934, 3.77),
(574, 934, 2.4),
(575, 605, 4.81),
(576, 605, 1.08),
(577, 605, 0.2),
(578, 605, 1.4),
(579, 605, 1.23),
(580, 605, 0.76),
(581, 605, 4.14),
(582, 705, 2.53),
(583, 705, 3.64),
(584, 705, 3.9),
(585, 705, 2.1),
(586, 705, 3.36),
(587, 705, 4.55),
(588, 705, 0),
(589, 389, 4.18),
(590, 389, 0.69),
(591, 389, 4.88),
(592, 389, 0.02),
(593, 389, 1.19),
(594, 389, 0.91),
(595, 389, 1.29),
(596, 587, 1.42),
(597, 587, 2.8),
(598, 587, 1.35),
(599, 587, 0.33),
(600, 587, 1.41),
(601, 587, 0.34),
(602, 587, 0.59),
(603, 112, 0.35),
(604, 112, 1.01),
(605, 112, 1.33),
(606, 112, 3.56),
(607, 112, 4.19),
(608, 112, 4.91),
(609, 112, 4.06),
(610, 348, 4.27),
(611, 348, 3.74),
(612, 348, 0.67),
(613, 348, 1.79),
(614, 348, 4.96),
(615, 348, 3.57),
(616, 348, 3.09),
(617, 869, 3.85),
(618, 869, 0.66),
(619, 869, 0.58),
(620, 869, 2.94),
(621, 869, 3.1),
(622, 869, 3.61),
(623, 869, 3.12),
(624, 818, 4.16),
(625, 818, 2.43),
(626, 818, 0.26),
(627, 818, 4.67),
(628, 818, 1),
(629, 818, 0.56),
(630, 818, 1.85),
(631, 472, 3.45),
(632, 472, 2.22),
(633, 472, 4.81),
(634, 472, 2.74),
(635, 472, 3.35),
(636, 472, 0.16),
(637, 472, 0.6),
(638, 949, 1.18),
(639, 949, 2.58),
(640, 949, 0.08),
(641, 949, 1.31),
(642, 949, 4.98),
(643, 949, 1.34),
(644, 949, 0.77),
(645, 372, 2.34),
(646, 372, 4.67),
(647, 372, 2.39),
(648, 372, 4.87),
(649, 372, 3.41),
(650, 372, 0.21),
(651, 372, 1.79),
(652, 886, 0.7),
(653, 886, 1.54),
(654, 886, 0.54),
(655, 886, 2.88),
(656, 886, 1.89),
(657, 886, 4.95),
(658, 886, 1.8),
(659, 729, 3.53),
(660, 729, 1.56),
(661, 729, 4.16),
(662, 729, 0.18),
(663, 729, 3.11),
(664, 729, 4),
(665, 729, 1.29),
(666, 817, 4.18),
(667, 817, 2.54),
(668, 817, 4.62),
(669, 817, 4.41),
(670, 817, 0),
(671, 817, 1.21),
(672, 817, 3.09),
(673, 707, 2.99),
(674, 707, 2.06),
(675, 707, 0.65),
(676, 707, 3.9),
(677, 707, 4.29),
(678, 707, 2.99),
(679, 707, 3.45),
(680, 440, 0.09),
(681, 440, 1.4),
(682, 440, 2.44),
(683, 440, 4.43),
(684, 440, 3.28),
(685, 440, 4.97),
(686, 440, 2.65),
(687, 161, 2.45),
(688, 161, 2.79),
(689, 161, 2.75),
(690, 161, 4.28),
(691, 161, 1.89),
(692, 161, 3.49),
(693, 161, 1.94),
(694, 174, 3.55),
(695, 174, 0.85),
(696, 174, 1.74),
(697, 174, 2),
(698, 174, 2.18),
(699, 174, 4.69),
(700, 174, 3.58);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=701;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;