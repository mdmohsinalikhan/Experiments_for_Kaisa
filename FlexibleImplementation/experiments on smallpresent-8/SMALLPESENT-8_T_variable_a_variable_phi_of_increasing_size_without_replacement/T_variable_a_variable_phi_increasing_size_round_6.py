import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


#Creating the list. Logorithm of sample size. Will be plotted in x-axis
t_0 = [math.log(272.000000,2),math.log(232.000000,2),math.log(276.000000,2),math.log(280.000000,2),math.log(238.000000,2),math.log(277.000000,2),math.log(288.000000,2),math.log(264.250000,2),math.log(240.187500,2),math.log(296.187500,2),math.log(303.187500,2),math.log(233.265625,2),math.log(249.261719,2),math.log(267.257812,2),math.log(308.066406,2),math.log(418.075195,2),math.log(560.386963,2),math.log(772.011719,2),math.log(1353.184387,2),math.log(2532.894073,2)]
t_1 = [math.log(224.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(244.000000,2),math.log(209.000000,2),math.log(220.000000,2),math.log(241.750000,2),math.log(229.375000,2),math.log(231.562500,2),math.log(240.437500,2),math.log(278.218750,2),math.log(263.007812,2),math.log(265.316406,2),math.log(240.029297,2),math.log(268.448242,2),math.log(288.879883,2),math.log(469.595215,2),math.log(545.500366,2),math.log(861.235718,2),math.log(1407.206329,2)]
t_2 = [math.log(256.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(274.000000,2),math.log(237.000000,2),math.log(273.000000,2),math.log(315.750000,2),math.log(272.375000,2),math.log(261.812500,2),math.log(274.281250,2),math.log(254.703125,2),math.log(274.406250,2),math.log(242.175781,2),math.log(236.273438,2),math.log(268.094727,2),math.log(325.903320,2),math.log(461.666748,2),math.log(635.067749,2),math.log(1025.351440,2),math.log(1673.350342,2)]
t_3 = [math.log(240.000000,2),math.log(272.000000,2),math.log(280.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(267.000000,2),math.log(255.500000,2),math.log(230.625000,2),math.log(243.125000,2),math.log(247.125000,2),math.log(235.078125,2),math.log(212.921875,2),math.log(264.472656,2),math.log(298.980469,2),math.log(349.461914,2),math.log(442.787598,2),math.log(543.487305,2),math.log(819.697510,2),math.log(1464.518860,2),math.log(2764.994629,2)]
t_4 = [math.log(256.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(242.000000,2),math.log(260.000000,2),math.log(275.000000,2),math.log(257.250000,2),math.log(211.062500,2),math.log(242.343750,2),math.log(248.390625,2),math.log(273.046875,2),math.log(319.531250,2),math.log(354.660156,2),math.log(349.389648,2),math.log(364.740723,2),math.log(435.023193,2),math.log(582.510376,2),math.log(858.821106,2),math.log(1406.127441,2)]
t_5 = [math.log(288.000000,2),math.log(296.000000,2),math.log(264.000000,2),math.log(290.000000,2),math.log(249.000000,2),math.log(223.500000,2),math.log(266.000000,2),math.log(198.125000,2),math.log(242.875000,2),math.log(245.968750,2),math.log(234.250000,2),math.log(254.914062,2),math.log(264.378906,2),math.log(312.347656,2),math.log(345.875977,2),math.log(417.139648,2),math.log(557.433594,2),math.log(930.583984,2),math.log(1584.823120,2),math.log(2818.139893,2)]
t_6 = [math.log(256.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(246.000000,2),math.log(272.000000,2),math.log(257.500000,2),math.log(273.750000,2),math.log(272.250000,2),math.log(263.625000,2),math.log(275.718750,2),math.log(276.046875,2),math.log(252.734375,2),math.log(246.285156,2),math.log(298.662109,2),math.log(337.179688,2),math.log(435.469238,2),math.log(526.443115,2),math.log(701.637573,2),math.log(1101.059937,2),math.log(1828.312225,2)]
t_7 = [math.log(288.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(270.000000,2),math.log(269.000000,2),math.log(270.000000,2),math.log(279.000000,2),math.log(267.750000,2),math.log(272.687500,2),math.log(295.968750,2),math.log(278.312500,2),math.log(308.882812,2),math.log(280.398438,2),math.log(261.027344,2),math.log(310.182617,2),math.log(415.442871,2),math.log(560.577881,2),math.log(955.718384,2),math.log(1600.344482,2),math.log(3095.078979,2)]
t_8 = [math.log(240.000000,2),math.log(216.000000,2),math.log(232.000000,2),math.log(222.000000,2),math.log(240.000000,2),math.log(257.500000,2),math.log(250.500000,2),math.log(254.625000,2),math.log(262.687500,2),math.log(226.468750,2),math.log(233.937500,2),math.log(251.054688,2),math.log(234.859375,2),math.log(252.484375,2),math.log(324.210938,2),math.log(388.531738,2),math.log(631.602051,2),math.log(909.988403,2),math.log(1452.429810,2),math.log(2528.108276,2)]
t_9 = [math.log(256.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(236.000000,2),math.log(240.000000,2),math.log(300.000000,2),math.log(274.000000,2),math.log(259.125000,2),math.log(241.625000,2),math.log(258.593750,2),math.log(241.265625,2),math.log(254.960938,2),math.log(287.972656,2),math.log(268.667969,2),math.log(313.432617,2),math.log(391.229492,2),math.log(568.122314,2),math.log(932.680054,2),math.log(1682.608032,2),math.log(2995.075043,2)]
t_10 = [math.log(256.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(246.000000,2),math.log(247.000000,2),math.log(246.500000,2),math.log(252.000000,2),math.log(211.875000,2),math.log(249.312500,2),math.log(264.781250,2),math.log(269.781250,2),math.log(282.304688,2),math.log(343.968750,2),math.log(464.294922,2),math.log(753.000000,2),math.log(1192.698242,2),math.log(2133.114014,2),math.log(4061.334717,2),math.log(7685.821960,2),math.log(14916.574554,2)]
t_11 = [math.log(224.000000,2),math.log(216.000000,2),math.log(208.000000,2),math.log(256.000000,2),math.log(245.000000,2),math.log(233.000000,2),math.log(246.000000,2),math.log(212.125000,2),math.log(238.937500,2),math.log(247.093750,2),math.log(261.734375,2),math.log(271.554688,2),math.log(286.183594,2),math.log(320.375000,2),math.log(415.406250,2),math.log(446.018555,2),math.log(685.044434,2),math.log(1129.609741,2),math.log(1956.056641,2),math.log(3742.999420,2)]
t_12 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(274.000000,2),math.log(248.000000,2),math.log(280.500000,2),math.log(243.250000,2),math.log(248.625000,2),math.log(264.687500,2),math.log(269.812500,2),math.log(248.937500,2),math.log(279.539062,2),math.log(263.324219,2),math.log(306.117188,2),math.log(342.338867,2),math.log(420.045410,2),math.log(593.038818,2),math.log(911.583862,2),math.log(1467.417725,2),math.log(2735.487457,2)]
t_13 = [math.log(256.000000,2),math.log(288.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(265.000000,2),math.log(260.000000,2),math.log(286.000000,2),math.log(270.375000,2),math.log(267.062500,2),math.log(259.187500,2),math.log(258.953125,2),math.log(269.335938,2),math.log(291.156250,2),math.log(310.345703,2),math.log(401.369141,2),math.log(671.866211,2),math.log(1027.422363,2),math.log(1671.482300,2),math.log(2967.823730,2),math.log(5615.709839,2)]
t_14 = [math.log(256.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(200.000000,2),math.log(211.000000,2),math.log(219.000000,2),math.log(229.750000,2),math.log(240.000000,2),math.log(239.875000,2),math.log(241.625000,2),math.log(242.000000,2),math.log(257.882812,2),math.log(314.898438,2),math.log(386.832031,2),math.log(437.354492,2),math.log(573.412598,2),math.log(881.248779,2),math.log(1465.505249,2),math.log(2384.179626,2),math.log(4565.714050,2)]
t_15 = [math.log(240.000000,2),math.log(240.000000,2),math.log(220.000000,2),math.log(246.000000,2),math.log(260.000000,2),math.log(240.500000,2),math.log(278.750000,2),math.log(253.625000,2),math.log(233.187500,2),math.log(296.781250,2),math.log(283.625000,2),math.log(244.734375,2),math.log(291.792969,2),math.log(345.259766,2),math.log(442.280273,2),math.log(539.514160,2),math.log(794.684570,2),math.log(1265.271851,2),math.log(2363.936035,2),math.log(4487.131714,2)]
t_16 = [math.log(256.000000,2),math.log(280.000000,2),math.log(308.000000,2),math.log(278.000000,2),math.log(275.000000,2),math.log(268.000000,2),math.log(275.000000,2),math.log(300.875000,2),math.log(256.000000,2),math.log(276.906250,2),math.log(266.609375,2),math.log(292.257812,2),math.log(287.292969,2),math.log(261.521484,2),math.log(290.748047,2),math.log(307.240234,2),math.log(418.479248,2),math.log(623.937744,2),math.log(1013.571472,2),math.log(1705.846680,2)]
t_17 = [math.log(256.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(284.000000,2),math.log(255.000000,2),math.log(282.000000,2),math.log(244.000000,2),math.log(223.750000,2),math.log(259.250000,2),math.log(268.937500,2),math.log(255.671875,2),math.log(243.476562,2),math.log(240.367188,2),math.log(295.458984,2),math.log(339.060547,2),math.log(360.972656,2),math.log(453.104736,2),math.log(643.175537,2),math.log(1002.666809,2),math.log(1691.557495,2)]
t_18 = [math.log(240.000000,2),math.log(232.000000,2),math.log(212.000000,2),math.log(260.000000,2),math.log(274.000000,2),math.log(261.000000,2),math.log(242.500000,2),math.log(262.375000,2),math.log(293.625000,2),math.log(294.375000,2),math.log(293.375000,2),math.log(261.265625,2),math.log(309.507812,2),math.log(328.275391,2),math.log(381.227539,2),math.log(463.755371,2),math.log(631.130615,2),math.log(915.557983,2),math.log(1628.796387,2),math.log(2928.472534,2)]
t_19 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(296.000000,2),math.log(314.000000,2),math.log(244.250000,2),math.log(251.125000,2),math.log(282.812500,2),math.log(315.750000,2),math.log(290.218750,2),math.log(269.390625,2),math.log(284.675781,2),math.log(313.781250,2),math.log(316.972656,2),math.log(359.390625,2),math.log(427.479004,2),math.log(583.743164,2),math.log(907.896912,2),math.log(1602.945587,2)]
t_20 = [math.log(240.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(270.000000,2),math.log(293.000000,2),math.log(296.500000,2),math.log(280.500000,2),math.log(254.000000,2),math.log(261.187500,2),math.log(262.062500,2),math.log(225.546875,2),math.log(249.507812,2),math.log(292.085938,2),math.log(278.273438,2),math.log(338.171875,2),math.log(458.759277,2),math.log(609.801270,2),math.log(789.262573,2),math.log(1414.242371,2),math.log(2650.739990,2)]
t_21 = [math.log(272.000000,2),math.log(264.000000,2),math.log(216.000000,2),math.log(210.000000,2),math.log(243.000000,2),math.log(258.500000,2),math.log(263.750000,2),math.log(261.250000,2),math.log(269.437500,2),math.log(252.781250,2),math.log(252.640625,2),math.log(246.656250,2),math.log(239.050781,2),math.log(297.937500,2),math.log(277.313477,2),math.log(407.255371,2),math.log(543.166992,2),math.log(752.102295,2),math.log(1277.372314,2),math.log(2309.796753,2)]
t_22 = [math.log(256.000000,2),math.log(264.000000,2),math.log(316.000000,2),math.log(322.000000,2),math.log(282.000000,2),math.log(247.500000,2),math.log(299.000000,2),math.log(257.500000,2),math.log(271.875000,2),math.log(268.125000,2),math.log(283.187500,2),math.log(252.109375,2),math.log(243.304688,2),math.log(293.007812,2),math.log(370.806641,2),math.log(473.314453,2),math.log(659.596680,2),math.log(1058.914062,2),math.log(1984.812866,2),math.log(3502.107391,2)]
t_23 = [math.log(256.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(286.000000,2),math.log(252.000000,2),math.log(237.500000,2),math.log(252.750000,2),math.log(256.000000,2),math.log(256.875000,2),math.log(245.875000,2),math.log(231.531250,2),math.log(234.000000,2),math.log(246.007812,2),math.log(254.322266,2),math.log(306.854492,2),math.log(401.831543,2),math.log(530.687012,2),math.log(896.391113,2),math.log(1596.520081,2),math.log(2922.550507,2)]
t_24 = [math.log(288.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(250.000000,2),math.log(261.000000,2),math.log(221.500000,2),math.log(236.500000,2),math.log(227.000000,2),math.log(228.687500,2),math.log(249.343750,2),math.log(238.968750,2),math.log(248.710938,2),math.log(258.441406,2),math.log(277.886719,2),math.log(306.990234,2),math.log(376.735352,2),math.log(460.644775,2),math.log(612.647827,2),math.log(1082.157715,2),math.log(1879.638611,2)]
t_25 = [math.log(256.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(254.000000,2),math.log(268.000000,2),math.log(212.000000,2),math.log(230.500000,2),math.log(243.375000,2),math.log(233.437500,2),math.log(274.562500,2),math.log(289.968750,2),math.log(327.726562,2),math.log(316.566406,2),math.log(354.875000,2),math.log(370.679688,2),math.log(437.042480,2),math.log(552.434570,2),math.log(715.136230,2),math.log(1125.449158,2),math.log(2171.972229,2)]
t_26 = [math.log(288.000000,2),math.log(280.000000,2),math.log(260.000000,2),math.log(262.000000,2),math.log(286.000000,2),math.log(275.000000,2),math.log(266.500000,2),math.log(260.750000,2),math.log(243.500000,2),math.log(237.937500,2),math.log(279.531250,2),math.log(302.140625,2),math.log(329.507812,2),math.log(396.250000,2),math.log(495.721680,2),math.log(692.943359,2),math.log(1114.107422,2),math.log(1989.758301,2),math.log(3651.163635,2),math.log(7124.812317,2)]
t_27 = [math.log(272.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(230.000000,2),math.log(242.500000,2),math.log(260.250000,2),math.log(251.250000,2),math.log(256.125000,2),math.log(232.406250,2),math.log(248.359375,2),math.log(251.171875,2),math.log(246.144531,2),math.log(304.826172,2),math.log(357.358398,2),math.log(423.479492,2),math.log(548.812988,2),math.log(846.824707,2),math.log(1364.199097,2),math.log(2525.927551,2)]
t_28 = [math.log(256.000000,2),math.log(224.000000,2),math.log(284.000000,2),math.log(282.000000,2),math.log(223.000000,2),math.log(221.000000,2),math.log(238.250000,2),math.log(216.750000,2),math.log(233.687500,2),math.log(246.468750,2),math.log(235.062500,2),math.log(244.890625,2),math.log(268.316406,2),math.log(269.980469,2),math.log(306.418945,2),math.log(370.455078,2),math.log(516.131592,2),math.log(869.696533,2),math.log(1562.843079,2),math.log(2880.642029,2)]
t_29 = [math.log(288.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(244.000000,2),math.log(246.000000,2),math.log(247.000000,2),math.log(270.000000,2),math.log(294.000000,2),math.log(281.062500,2),math.log(245.437500,2),math.log(244.531250,2),math.log(233.984375,2),math.log(286.304688,2),math.log(338.664062,2),math.log(373.250977,2),math.log(483.375488,2),math.log(742.076660,2),math.log(1217.890381,2),math.log(2275.588867,2),math.log(4642.891602,2)]
t_30 = [math.log(256.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(260.000000,2),math.log(241.000000,2),math.log(231.000000,2),math.log(264.000000,2),math.log(277.250000,2),math.log(282.062500,2),math.log(245.093750,2),math.log(248.093750,2),math.log(262.546875,2),math.log(331.351562,2),math.log(399.613281,2),math.log(492.262695,2),math.log(729.544434,2),math.log(1132.052002,2),math.log(1870.463867,2),math.log(3546.613647,2),math.log(6972.251678,2)]
t_31 = [math.log(240.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(270.000000,2),math.log(305.000000,2),math.log(242.500000,2),math.log(220.000000,2),math.log(246.250000,2),math.log(260.125000,2),math.log(224.750000,2),math.log(236.546875,2),math.log(226.703125,2),math.log(262.402344,2),math.log(290.548828,2),math.log(304.938477,2),math.log(377.955566,2),math.log(557.592041,2),math.log(883.767578,2),math.log(1558.995667,2),math.log(2874.430267,2)]
t_32 = [math.log(288.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(222.000000,2),math.log(247.000000,2),math.log(252.000000,2),math.log(272.250000,2),math.log(262.500000,2),math.log(290.375000,2),math.log(325.781250,2),math.log(299.640625,2),math.log(295.257812,2),math.log(273.023438,2),math.log(277.835938,2),math.log(310.697266,2),math.log(402.155762,2),math.log(513.611328,2),math.log(877.712769,2),math.log(1449.623291,2),math.log(2498.960236,2)]
t_33 = [math.log(224.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(262.000000,2),math.log(239.000000,2),math.log(240.500000,2),math.log(221.500000,2),math.log(223.625000,2),math.log(213.000000,2),math.log(225.156250,2),math.log(257.125000,2),math.log(265.468750,2),math.log(298.566406,2),math.log(327.615234,2),math.log(353.296875,2),math.log(439.768555,2),math.log(597.310547,2),math.log(897.119263,2),math.log(1574.230103,2),math.log(2926.169250,2)]
t_34 = [math.log(256.000000,2),math.log(288.000000,2),math.log(248.000000,2),math.log(254.000000,2),math.log(284.000000,2),math.log(291.500000,2),math.log(247.500000,2),math.log(262.625000,2),math.log(266.187500,2),math.log(260.750000,2),math.log(251.500000,2),math.log(271.695312,2),math.log(285.843750,2),math.log(277.435547,2),math.log(329.018555,2),math.log(424.043945,2),math.log(595.082275,2),math.log(927.718506,2),math.log(1607.612549,2),math.log(2982.188324,2)]
t_35 = [math.log(288.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(258.000000,2),math.log(299.000000,2),math.log(275.500000,2),math.log(287.500000,2),math.log(244.875000,2),math.log(245.875000,2),math.log(282.093750,2),math.log(252.875000,2),math.log(246.765625,2),math.log(277.445312,2),math.log(261.337891,2),math.log(299.875977,2),math.log(343.431152,2),math.log(488.872559,2),math.log(796.407349,2),math.log(1371.100708,2),math.log(2412.188660,2)]
t_36 = [math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(230.000000,2),math.log(233.000000,2),math.log(266.000000,2),math.log(285.750000,2),math.log(234.750000,2),math.log(257.687500,2),math.log(299.593750,2),math.log(275.875000,2),math.log(265.593750,2),math.log(295.183594,2),math.log(292.294922,2),math.log(334.633789,2),math.log(444.805664,2),math.log(608.343994,2),math.log(853.883911,2),math.log(1446.490051,2),math.log(2684.123047,2)]
t_37 = [math.log(256.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(254.000000,2),math.log(291.000000,2),math.log(234.500000,2),math.log(244.500000,2),math.log(249.750000,2),math.log(245.625000,2),math.log(254.906250,2),math.log(263.156250,2),math.log(272.132812,2),math.log(303.218750,2),math.log(306.890625,2),math.log(335.784180,2),math.log(365.959961,2),math.log(473.859619,2),math.log(704.921631,2),math.log(1138.961853,2),math.log(1870.557800,2)]
t_38 = [math.log(288.000000,2),math.log(272.000000,2),math.log(292.000000,2),math.log(256.000000,2),math.log(258.000000,2),math.log(241.000000,2),math.log(275.750000,2),math.log(264.875000,2),math.log(275.750000,2),math.log(272.218750,2),math.log(249.046875,2),math.log(259.875000,2),math.log(275.105469,2),math.log(294.949219,2),math.log(322.686523,2),math.log(430.314941,2),math.log(555.981934,2),math.log(852.090576,2),math.log(1561.278015,2),math.log(2924.022644,2)]
t_39 = [math.log(224.000000,2),math.log(272.000000,2),math.log(296.000000,2),math.log(242.000000,2),math.log(271.000000,2),math.log(251.500000,2),math.log(274.000000,2),math.log(250.875000,2),math.log(287.250000,2),math.log(281.906250,2),math.log(240.359375,2),math.log(210.554688,2),math.log(261.312500,2),math.log(303.589844,2),math.log(384.283203,2),math.log(492.331543,2),math.log(813.519775,2),math.log(1314.667114,2),math.log(2463.813904,2),math.log(4443.504517,2)]
t_40 = [math.log(240.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(246.000000,2),math.log(273.000000,2),math.log(242.000000,2),math.log(203.750000,2),math.log(225.000000,2),math.log(256.937500,2),math.log(243.125000,2),math.log(262.312500,2),math.log(214.898438,2),math.log(228.710938,2),math.log(255.294922,2),math.log(317.054688,2),math.log(383.915039,2),math.log(491.256104,2),math.log(677.480469,2),math.log(1045.341919,2),math.log(1909.716278,2)]
t_41 = [math.log(240.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(262.000000,2),math.log(253.000000,2),math.log(234.500000,2),math.log(229.500000,2),math.log(216.125000,2),math.log(246.125000,2),math.log(272.281250,2),math.log(271.562500,2),math.log(299.992188,2),math.log(248.519531,2),math.log(246.603516,2),math.log(301.394531,2),math.log(366.222656,2),math.log(530.475586,2),math.log(802.253784,2),math.log(1370.964722,2),math.log(2634.117798,2)]
t_42 = [math.log(256.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(290.000000,2),math.log(319.000000,2),math.log(296.500000,2),math.log(265.500000,2),math.log(263.625000,2),math.log(289.500000,2),math.log(278.500000,2),math.log(303.000000,2),math.log(360.695312,2),math.log(366.714844,2),math.log(412.861328,2),math.log(583.277344,2),math.log(814.233887,2),math.log(1271.588867,2),math.log(2292.418579,2),math.log(4328.480591,2),math.log(8576.429596,2)]
t_43 = [math.log(272.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(276.000000,2),math.log(236.000000,2),math.log(238.500000,2),math.log(252.750000,2),math.log(259.250000,2),math.log(250.500000,2),math.log(264.812500,2),math.log(276.156250,2),math.log(272.976562,2),math.log(297.492188,2),math.log(314.048828,2),math.log(393.989258,2),math.log(491.371582,2),math.log(763.028320,2),math.log(1141.024536,2),math.log(1842.655457,2),math.log(3361.065857,2)]
t_44 = [math.log(272.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(224.000000,2),math.log(245.000000,2),math.log(259.000000,2),math.log(244.250000,2),math.log(228.375000,2),math.log(219.812500,2),math.log(233.625000,2),math.log(256.937500,2),math.log(281.109375,2),math.log(261.808594,2),math.log(322.667969,2),math.log(396.135742,2),math.log(510.819824,2),math.log(655.529297,2),math.log(989.936768,2),math.log(1707.620544,2),math.log(3128.307709,2)]
t_45 = [math.log(256.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(236.000000,2),math.log(244.000000,2),math.log(232.500000,2),math.log(237.250000,2),math.log(281.000000,2),math.log(275.312500,2),math.log(282.093750,2),math.log(275.937500,2),math.log(298.414062,2),math.log(348.390625,2),math.log(354.164062,2),math.log(449.603516,2),math.log(700.334961,2),math.log(1154.422363,2),math.log(2100.770020,2),math.log(3783.128845,2),math.log(7282.329102,2)]
t_46 = [math.log(272.000000,2),math.log(296.000000,2),math.log(284.000000,2),math.log(272.000000,2),math.log(239.000000,2),math.log(261.000000,2),math.log(263.750000,2),math.log(271.000000,2),math.log(297.437500,2),math.log(262.000000,2),math.log(260.468750,2),math.log(279.156250,2),math.log(284.859375,2),math.log(371.681641,2),math.log(450.847656,2),math.log(715.894043,2),math.log(1119.187500,2),math.log(1935.389038,2),math.log(3482.918091,2),math.log(6545.151123,2)]
t_47 = [math.log(256.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(266.000000,2),math.log(267.000000,2),math.log(306.500000,2),math.log(276.750000,2),math.log(257.000000,2),math.log(263.437500,2),math.log(248.375000,2),math.log(291.859375,2),math.log(263.273438,2),math.log(261.187500,2),math.log(271.529297,2),math.log(274.740234,2),math.log(354.239746,2),math.log(446.344727,2),math.log(752.086548,2),math.log(1218.660583,2),math.log(2497.842712,2)]
t_48 = [math.log(304.000000,2),math.log(296.000000,2),math.log(260.000000,2),math.log(246.000000,2),math.log(259.000000,2),math.log(256.000000,2),math.log(316.250000,2),math.log(282.500000,2),math.log(278.937500,2),math.log(239.312500,2),math.log(235.921875,2),math.log(284.601562,2),math.log(254.492188,2),math.log(267.771484,2),math.log(309.437500,2),math.log(328.655762,2),math.log(481.700928,2),math.log(760.552856,2),math.log(1218.274231,2),math.log(2144.193665,2)]
t_49 = [math.log(224.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(238.000000,2),math.log(277.000000,2),math.log(273.500000,2),math.log(303.250000,2),math.log(286.125000,2),math.log(241.562500,2),math.log(281.656250,2),math.log(285.484375,2),math.log(260.210938,2),math.log(287.230469,2),math.log(335.722656,2),math.log(336.964844,2),math.log(449.413574,2),math.log(477.469482,2),math.log(714.911743,2),math.log(1154.450317,2),math.log(2099.755676,2)]
t_50 = [math.log(240.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(275.000000,2),math.log(255.000000,2),math.log(226.250000,2),math.log(241.000000,2),math.log(245.562500,2),math.log(279.218750,2),math.log(232.390625,2),math.log(244.656250,2),math.log(247.472656,2),math.log(280.091797,2),math.log(307.928711,2),math.log(380.398926,2),math.log(533.966309,2),math.log(749.532471,2),math.log(1258.340942,2),math.log(2218.325134,2)]
t_51 = [math.log(240.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(296.000000,2),math.log(278.000000,2),math.log(266.000000,2),math.log(247.250000,2),math.log(303.250000,2),math.log(321.000000,2),math.log(321.625000,2),math.log(269.015625,2),math.log(287.171875,2),math.log(266.402344,2),math.log(302.222656,2),math.log(351.375977,2),math.log(392.541504,2),math.log(556.293945,2),math.log(869.587280,2),math.log(1536.090881,2),math.log(2662.194641,2)]
t_52 = [math.log(256.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(258.000000,2),math.log(272.000000,2),math.log(251.000000,2),math.log(256.750000,2),math.log(255.000000,2),math.log(248.250000,2),math.log(255.656250,2),math.log(248.140625,2),math.log(265.156250,2),math.log(275.105469,2),math.log(277.054688,2),math.log(306.313477,2),math.log(353.678223,2),math.log(513.046387,2),math.log(783.830933,2),math.log(1289.979065,2),math.log(2131.039642,2)]
t_53 = [math.log(224.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(246.000000,2),math.log(263.000000,2),math.log(260.500000,2),math.log(269.250000,2),math.log(282.375000,2),math.log(294.812500,2),math.log(320.781250,2),math.log(287.906250,2),math.log(298.679688,2),math.log(265.207031,2),math.log(282.033203,2),math.log(304.538086,2),math.log(403.184082,2),math.log(529.017822,2),math.log(800.886963,2),math.log(1337.684814,2),math.log(2365.215881,2)]
t_54 = [math.log(256.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(250.000000,2),math.log(275.000000,2),math.log(255.000000,2),math.log(235.500000,2),math.log(279.250000,2),math.log(257.312500,2),math.log(258.531250,2),math.log(230.562500,2),math.log(236.125000,2),math.log(264.320312,2),math.log(287.037109,2),math.log(305.023438,2),math.log(405.334473,2),math.log(562.959961,2),math.log(892.735352,2),math.log(1667.461487,2),math.log(3275.391327,2)]
t_55 = [math.log(272.000000,2),math.log(272.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(266.000000,2),math.log(244.000000,2),math.log(228.000000,2),math.log(240.875000,2),math.log(280.000000,2),math.log(302.125000,2),math.log(325.062500,2),math.log(262.507812,2),math.log(274.226562,2),math.log(319.517578,2),math.log(365.547852,2),math.log(438.433105,2),math.log(623.412109,2),math.log(966.285522,2),math.log(1720.863953,2),math.log(3235.005463,2)]
t_56 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(268.000000,2),math.log(276.000000,2),math.log(270.500000,2),math.log(285.250000,2),math.log(271.875000,2),math.log(251.812500,2),math.log(239.156250,2),math.log(265.515625,2),math.log(240.601562,2),math.log(252.941406,2),math.log(297.583984,2),math.log(354.718750,2),math.log(462.492188,2),math.log(709.409424,2),math.log(1232.516235,2),math.log(2016.727051,2),math.log(3730.146912,2)]
t_57 = [math.log(256.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(262.000000,2),math.log(277.000000,2),math.log(275.000000,2),math.log(273.250000,2),math.log(242.000000,2),math.log(227.937500,2),math.log(253.562500,2),math.log(281.109375,2),math.log(246.601562,2),math.log(280.792969,2),math.log(290.906250,2),math.log(382.197266,2),math.log(511.388672,2),math.log(729.870361,2),math.log(1175.717529,2),math.log(2145.195251,2),math.log(3905.416382,2)]
t_58 = [math.log(256.000000,2),math.log(248.000000,2),math.log(212.000000,2),math.log(214.000000,2),math.log(240.000000,2),math.log(208.000000,2),math.log(208.500000,2),math.log(244.000000,2),math.log(237.250000,2),math.log(217.187500,2),math.log(281.687500,2),math.log(294.429688,2),math.log(291.093750,2),math.log(360.400391,2),math.log(569.862305,2),math.log(922.338867,2),math.log(1531.880127,2),math.log(2971.049194,2),math.log(6046.203674,2),math.log(12418.245636,2)]
t_59 = [math.log(272.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(286.000000,2),math.log(260.000000,2),math.log(276.000000,2),math.log(279.500000,2),math.log(274.625000,2),math.log(278.687500,2),math.log(265.875000,2),math.log(240.437500,2),math.log(263.484375,2),math.log(277.609375,2),math.log(297.460938,2),math.log(383.243164,2),math.log(558.592773,2),math.log(758.832275,2),math.log(1367.328003,2),math.log(2533.470520,2),math.log(4771.768524,2)]
t_60 = [math.log(256.000000,2),math.log(264.000000,2),math.log(276.000000,2),math.log(244.000000,2),math.log(239.000000,2),math.log(271.500000,2),math.log(269.250000,2),math.log(273.750000,2),math.log(281.062500,2),math.log(264.812500,2),math.log(274.328125,2),math.log(287.773438,2),math.log(299.609375,2),math.log(303.623047,2),math.log(362.386719,2),math.log(440.371094,2),math.log(565.509033,2),math.log(799.230103,2),math.log(1414.766113,2),math.log(2667.824402,2)]
t_61 = [math.log(288.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(278.000000,2),math.log(276.000000,2),math.log(272.000000,2),math.log(293.250000,2),math.log(277.000000,2),math.log(301.250000,2),math.log(264.937500,2),math.log(239.718750,2),math.log(267.054688,2),math.log(267.082031,2),math.log(350.091797,2),math.log(472.242188,2),math.log(646.965332,2),math.log(1138.240967,2),math.log(2012.232300,2),math.log(3861.914307,2),math.log(7255.610229,2)]
t_62 = [math.log(272.000000,2),math.log(296.000000,2),math.log(248.000000,2),math.log(254.000000,2),math.log(249.000000,2),math.log(237.000000,2),math.log(257.250000,2),math.log(272.875000,2),math.log(276.125000,2),math.log(270.781250,2),math.log(268.046875,2),math.log(269.632812,2),math.log(281.484375,2),math.log(285.822266,2),math.log(395.762695,2),math.log(606.536621,2),math.log(952.913574,2),math.log(1757.326050,2),math.log(3464.571167,2),math.log(6587.973175,2)]
t_63 = [math.log(272.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(228.000000,2),math.log(278.000000,2),math.log(266.500000,2),math.log(264.000000,2),math.log(268.375000,2),math.log(268.375000,2),math.log(287.062500,2),math.log(264.187500,2),math.log(282.015625,2),math.log(318.175781,2),math.log(357.792969,2),math.log(398.610352,2),math.log(485.944336,2),math.log(802.846680,2),math.log(1417.905640,2),math.log(2538.199585,2),math.log(4592.859436,2)]
t_64 = [math.log(256.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(238.000000,2),math.log(251.000000,2),math.log(265.500000,2),math.log(258.750000,2),math.log(254.250000,2),math.log(269.187500,2),math.log(250.125000,2),math.log(261.671875,2),math.log(266.125000,2),math.log(261.507812,2),math.log(267.927734,2),math.log(299.906250,2),math.log(364.170410,2),math.log(527.602783,2),math.log(790.691040,2),math.log(1236.594360,2),math.log(2340.755951,2)]
t_65 = [math.log(272.000000,2),math.log(240.000000,2),math.log(216.000000,2),math.log(228.000000,2),math.log(219.000000,2),math.log(236.500000,2),math.log(267.250000,2),math.log(259.125000,2),math.log(276.125000,2),math.log(253.656250,2),math.log(267.828125,2),math.log(240.007812,2),math.log(258.425781,2),math.log(301.318359,2),math.log(310.327148,2),math.log(339.142090,2),math.log(418.693115,2),math.log(567.880249,2),math.log(849.162292,2),math.log(1473.399445,2)]
t_66 = [math.log(256.000000,2),math.log(304.000000,2),math.log(260.000000,2),math.log(292.000000,2),math.log(294.000000,2),math.log(256.500000,2),math.log(262.000000,2),math.log(222.875000,2),math.log(248.750000,2),math.log(231.125000,2),math.log(221.515625,2),math.log(261.226562,2),math.log(281.324219,2),math.log(331.148438,2),math.log(350.460938,2),math.log(457.952148,2),math.log(676.441650,2),math.log(1015.469727,2),math.log(1811.484985,2),math.log(3322.194824,2)]
t_67 = [math.log(240.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(258.000000,2),math.log(221.000000,2),math.log(224.500000,2),math.log(250.500000,2),math.log(257.500000,2),math.log(288.562500,2),math.log(272.093750,2),math.log(240.453125,2),math.log(273.367188,2),math.log(301.808594,2),math.log(327.273438,2),math.log(362.563477,2),math.log(456.989258,2),math.log(599.284668,2),math.log(996.252075,2),math.log(1741.678528,2),math.log(3286.979126,2)]
t_68 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(244.000000,2),math.log(237.000000,2),math.log(248.000000,2),math.log(259.250000,2),math.log(253.625000,2),math.log(248.812500,2),math.log(237.250000,2),math.log(246.718750,2),math.log(240.671875,2),math.log(254.097656,2),math.log(301.474609,2),math.log(346.448242,2),math.log(352.719727,2),math.log(469.018066,2),math.log(729.477295,2),math.log(1284.629395,2),math.log(2256.332245,2)]
t_69 = [math.log(240.000000,2),math.log(248.000000,2),math.log(284.000000,2),math.log(266.000000,2),math.log(278.000000,2),math.log(269.000000,2),math.log(259.750000,2),math.log(285.250000,2),math.log(237.812500,2),math.log(241.250000,2),math.log(227.375000,2),math.log(248.460938,2),math.log(259.667969,2),math.log(294.376953,2),math.log(371.989258,2),math.log(478.740723,2),math.log(663.964355,2),math.log(1062.183838,2),math.log(1795.838257,2),math.log(3248.067352,2)]
t_70 = [math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(230.000000,2),math.log(245.000000,2),math.log(246.500000,2),math.log(260.000000,2),math.log(231.000000,2),math.log(257.562500,2),math.log(259.125000,2),math.log(280.031250,2),math.log(281.859375,2),math.log(279.117188,2),math.log(299.462891,2),math.log(338.698242,2),math.log(434.060547,2),math.log(622.415527,2),math.log(907.608276,2),math.log(1662.085510,2),math.log(2998.645782,2)]
t_71 = [math.log(256.000000,2),math.log(272.000000,2),math.log(276.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(218.000000,2),math.log(245.750000,2),math.log(269.625000,2),math.log(257.687500,2),math.log(246.750000,2),math.log(234.734375,2),math.log(218.968750,2),math.log(266.078125,2),math.log(342.923828,2),math.log(386.790039,2),math.log(504.125977,2),math.log(734.589600,2),math.log(1208.172729,2),math.log(2156.203369,2),math.log(4050.208740,2)]
t_72 = [math.log(240.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(254.000000,2),math.log(286.000000,2),math.log(292.000000,2),math.log(272.250000,2),math.log(255.000000,2),math.log(255.812500,2),math.log(294.312500,2),math.log(256.250000,2),math.log(254.062500,2),math.log(270.027344,2),math.log(313.792969,2),math.log(363.791992,2),math.log(491.456055,2),math.log(718.937988,2),math.log(1177.403931,2),math.log(2151.507568,2),math.log(3974.660278,2)]
t_73 = [math.log(256.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(260.000000,2),math.log(233.000000,2),math.log(233.500000,2),math.log(250.750000,2),math.log(277.000000,2),math.log(250.312500,2),math.log(275.093750,2),math.log(289.531250,2),math.log(251.664062,2),math.log(282.324219,2),math.log(337.464844,2),math.log(349.477539,2),math.log(442.795898,2),math.log(644.907227,2),math.log(1009.532227,2),math.log(1755.763733,2),math.log(3236.973694,2)]
t_74 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(274.000000,2),math.log(254.000000,2),math.log(265.500000,2),math.log(260.250000,2),math.log(252.875000,2),math.log(249.562500,2),math.log(234.125000,2),math.log(255.328125,2),math.log(268.257812,2),math.log(301.820312,2),math.log(383.318359,2),math.log(546.303711,2),math.log(895.570312,2),math.log(1495.127930,2),math.log(3072.839478,2),math.log(5829.728516,2),math.log(11404.979767,2)]
t_75 = [math.log(272.000000,2),math.log(256.000000,2),math.log(244.000000,2),math.log(242.000000,2),math.log(247.000000,2),math.log(243.500000,2),math.log(232.750000,2),math.log(248.000000,2),math.log(254.625000,2),math.log(259.875000,2),math.log(270.718750,2),math.log(296.226562,2),math.log(293.007812,2),math.log(343.937500,2),math.log(380.165039,2),math.log(561.305176,2),math.log(882.227295,2),math.log(1450.252319,2),math.log(2650.385071,2),math.log(5180.603333,2)]
t_76 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(249.000000,2),math.log(224.000000,2),math.log(250.250000,2),math.log(246.625000,2),math.log(236.875000,2),math.log(251.531250,2),math.log(256.093750,2),math.log(280.000000,2),math.log(314.199219,2),math.log(254.876953,2),math.log(270.448242,2),math.log(364.683105,2),math.log(446.321777,2),math.log(709.129395,2),math.log(1176.891602,2),math.log(2054.864807,2)]
t_77 = [math.log(240.000000,2),math.log(248.000000,2),math.log(284.000000,2),math.log(292.000000,2),math.log(255.000000,2),math.log(262.500000,2),math.log(276.750000,2),math.log(261.875000,2),math.log(245.750000,2),math.log(275.906250,2),math.log(246.890625,2),math.log(262.414062,2),math.log(286.910156,2),math.log(314.785156,2),math.log(413.831055,2),math.log(507.099609,2),math.log(796.734131,2),math.log(1247.322876,2),math.log(2300.383362,2),math.log(4135.837799,2)]
t_78 = [math.log(272.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(246.000000,2),math.log(248.000000,2),math.log(243.500000,2),math.log(241.000000,2),math.log(262.875000,2),math.log(275.625000,2),math.log(287.281250,2),math.log(291.953125,2),math.log(275.468750,2),math.log(314.484375,2),math.log(358.216797,2),math.log(451.888672,2),math.log(613.210938,2),math.log(891.319092,2),math.log(1380.997803,2),math.log(2639.387024,2),math.log(5036.865753,2)]
t_79 = [math.log(224.000000,2),math.log(224.000000,2),math.log(256.000000,2),math.log(266.000000,2),math.log(246.000000,2),math.log(242.000000,2),math.log(234.000000,2),math.log(227.250000,2),math.log(218.250000,2),math.log(242.968750,2),math.log(279.562500,2),math.log(297.257812,2),math.log(302.640625,2),math.log(314.132812,2),math.log(439.556641,2),math.log(687.362793,2),math.log(961.104736,2),math.log(1443.907593,2),math.log(2629.041077,2),math.log(4974.373993,2)]
t_80 = [math.log(240.000000,2),math.log(288.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(237.000000,2),math.log(239.500000,2),math.log(199.750000,2),math.log(208.000000,2),math.log(226.187500,2),math.log(251.906250,2),math.log(223.093750,2),math.log(213.296875,2),math.log(231.539062,2),math.log(241.511719,2),math.log(291.830078,2),math.log(381.183105,2),math.log(549.568604,2),math.log(961.986084,2),math.log(1527.725769,2),math.log(2856.280212,2)]
t_81 = [math.log(272.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(244.000000,2),math.log(204.000000,2),math.log(244.000000,2),math.log(271.250000,2),math.log(264.625000,2),math.log(244.687500,2),math.log(268.625000,2),math.log(249.203125,2),math.log(241.703125,2),math.log(287.738281,2),math.log(291.486328,2),math.log(335.738281,2),math.log(413.301758,2),math.log(549.011963,2),math.log(829.448486,2),math.log(1466.939636,2),math.log(2555.363068,2)]
t_82 = [math.log(272.000000,2),math.log(264.000000,2),math.log(236.000000,2),math.log(258.000000,2),math.log(262.000000,2),math.log(251.000000,2),math.log(266.250000,2),math.log(281.500000,2),math.log(265.312500,2),math.log(286.187500,2),math.log(259.953125,2),math.log(274.890625,2),math.log(293.468750,2),math.log(269.183594,2),math.log(342.512695,2),math.log(408.885254,2),math.log(630.346191,2),math.log(966.637329,2),math.log(1569.920227,2),math.log(2885.177429,2)]
t_83 = [math.log(224.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(224.000000,2),math.log(230.000000,2),math.log(212.500000,2),math.log(259.250000,2),math.log(252.250000,2),math.log(269.250000,2),math.log(227.031250,2),math.log(207.500000,2),math.log(272.929688,2),math.log(281.566406,2),math.log(290.560547,2),math.log(354.605469,2),math.log(506.521484,2),math.log(787.336426,2),math.log(1233.588989,2),math.log(2216.240356,2),math.log(4239.377380,2)]
t_84 = [math.log(256.000000,2),math.log(256.000000,2),math.log(292.000000,2),math.log(268.000000,2),math.log(268.000000,2),math.log(270.500000,2),math.log(278.750000,2),math.log(258.000000,2),math.log(285.500000,2),math.log(242.656250,2),math.log(255.750000,2),math.log(255.562500,2),math.log(244.187500,2),math.log(274.943359,2),math.log(311.506836,2),math.log(375.569336,2),math.log(532.760742,2),math.log(839.066406,2),math.log(1585.594116,2),math.log(2846.997009,2)]
t_85 = [math.log(224.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(274.000000,2),math.log(245.000000,2),math.log(261.500000,2),math.log(257.500000,2),math.log(274.750000,2),math.log(276.062500,2),math.log(254.125000,2),math.log(274.250000,2),math.log(246.867188,2),math.log(254.425781,2),math.log(296.054688,2),math.log(338.434570,2),math.log(415.895020,2),math.log(572.142090,2),math.log(894.203979,2),math.log(1665.922791,2),math.log(2971.286957,2)]
t_86 = [math.log(224.000000,2),math.log(208.000000,2),math.log(224.000000,2),math.log(250.000000,2),math.log(236.000000,2),math.log(256.500000,2),math.log(227.000000,2),math.log(205.125000,2),math.log(192.812500,2),math.log(226.218750,2),math.log(236.843750,2),math.log(232.367188,2),math.log(296.140625,2),math.log(277.158203,2),math.log(301.768555,2),math.log(381.041016,2),math.log(516.505615,2),math.log(773.625244,2),math.log(1173.093079,2),math.log(2111.680023,2)]
t_87 = [math.log(240.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(250.000000,2),math.log(237.000000,2),math.log(260.000000,2),math.log(307.000000,2),math.log(286.250000,2),math.log(280.937500,2),math.log(268.031250,2),math.log(250.531250,2),math.log(245.218750,2),math.log(349.832031,2),math.log(379.132812,2),math.log(425.855469,2),math.log(600.887695,2),math.log(976.877686,2),math.log(1603.351929,2),math.log(3087.179932,2),math.log(5869.437317,2)]
t_88 = [math.log(272.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(242.000000,2),math.log(266.000000,2),math.log(264.500000,2),math.log(236.750000,2),math.log(240.500000,2),math.log(245.687500,2),math.log(243.375000,2),math.log(251.015625,2),math.log(258.546875,2),math.log(239.832031,2),math.log(216.626953,2),math.log(265.815430,2),math.log(323.139160,2),math.log(423.845215,2),math.log(594.607422,2),math.log(1020.876099,2),math.log(1815.339752,2)]
t_89 = [math.log(272.000000,2),math.log(296.000000,2),math.log(264.000000,2),math.log(250.000000,2),math.log(298.000000,2),math.log(257.500000,2),math.log(225.000000,2),math.log(240.250000,2),math.log(221.375000,2),math.log(252.843750,2),math.log(242.078125,2),math.log(262.632812,2),math.log(258.566406,2),math.log(271.296875,2),math.log(311.608398,2),math.log(363.796875,2),math.log(448.560303,2),math.log(659.081055,2),math.log(1165.328796,2),math.log(2070.318390,2)]
t_90 = [math.log(240.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(274.000000,2),math.log(279.500000,2),math.log(239.250000,2),math.log(253.750000,2),math.log(254.000000,2),math.log(281.218750,2),math.log(305.062500,2),math.log(323.062500,2),math.log(357.304688,2),math.log(433.367188,2),math.log(524.974609,2),math.log(824.958008,2),math.log(1412.006836,2),math.log(2719.380615,2),math.log(5137.978027,2),math.log(10014.106262,2)]
t_91 = [math.log(272.000000,2),math.log(224.000000,2),math.log(240.000000,2),math.log(250.000000,2),math.log(236.000000,2),math.log(228.500000,2),math.log(236.500000,2),math.log(258.375000,2),math.log(280.125000,2),math.log(267.250000,2),math.log(234.671875,2),math.log(259.546875,2),math.log(300.343750,2),math.log(377.035156,2),math.log(453.765625,2),math.log(545.104980,2),math.log(736.997070,2),math.log(1418.246094,2),math.log(2559.576599,2),math.log(4932.887299,2)]
t_92 = [math.log(288.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(239.000000,2),math.log(240.000000,2),math.log(229.250000,2),math.log(250.375000,2),math.log(263.625000,2),math.log(218.937500,2),math.log(228.796875,2),math.log(245.890625,2),math.log(262.160156,2),math.log(313.064453,2),math.log(396.778320,2),math.log(518.059082,2),math.log(859.125488,2),math.log(1424.434570,2),math.log(2527.748840,2),math.log(4679.483673,2)]
t_93 = [math.log(272.000000,2),math.log(248.000000,2),math.log(276.000000,2),math.log(274.000000,2),math.log(228.000000,2),math.log(236.500000,2),math.log(212.750000,2),math.log(230.250000,2),math.log(249.812500,2),math.log(251.656250,2),math.log(288.515625,2),math.log(313.554688,2),math.log(323.605469,2),math.log(384.421875,2),math.log(516.305664,2),math.log(729.286621,2),math.log(1205.856934,2),math.log(2080.590332,2),math.log(4043.407837,2),math.log(7872.354187,2)]
t_94 = [math.log(240.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(256.000000,2),math.log(265.000000,2),math.log(241.500000,2),math.log(249.250000,2),math.log(227.000000,2),math.log(242.500000,2),math.log(224.906250,2),math.log(251.984375,2),math.log(264.789062,2),math.log(341.843750,2),math.log(417.697266,2),math.log(539.509766,2),math.log(816.867676,2),math.log(1317.634033,2),math.log(2297.253540,2),math.log(4441.813965,2),math.log(8717.681641,2)]
t_95 = [math.log(240.000000,2),math.log(248.000000,2),math.log(236.000000,2),math.log(250.000000,2),math.log(272.000000,2),math.log(264.500000,2),math.log(277.750000,2),math.log(308.625000,2),math.log(278.937500,2),math.log(266.968750,2),math.log(268.531250,2),math.log(285.023438,2),math.log(297.273438,2),math.log(350.093750,2),math.log(419.690430,2),math.log(583.881836,2),math.log(860.677734,2),math.log(1505.690430,2),math.log(2807.351868,2),math.log(5332.481812,2)]
t_96 = [math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(257.000000,2),math.log(283.500000,2),math.log(276.250000,2),math.log(268.500000,2),math.log(287.562500,2),math.log(305.062500,2),math.log(269.406250,2),math.log(261.484375,2),math.log(233.175781,2),math.log(286.257812,2),math.log(331.197266,2),math.log(431.740723,2),math.log(510.378906,2),math.log(797.812866,2),math.log(1409.282593,2),math.log(2542.202057,2)]
t_97 = [math.log(224.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(228.000000,2),math.log(249.000000,2),math.log(220.500000,2),math.log(248.500000,2),math.log(266.750000,2),math.log(237.062500,2),math.log(189.812500,2),math.log(243.156250,2),math.log(266.171875,2),math.log(289.800781,2),math.log(306.046875,2),math.log(308.782227,2),math.log(388.385254,2),math.log(513.598145,2),math.log(619.599854,2),math.log(1046.763062,2),math.log(1798.932587,2)]
t_98 = [math.log(240.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(262.000000,2),math.log(280.000000,2),math.log(270.000000,2),math.log(289.750000,2),math.log(314.500000,2),math.log(279.187500,2),math.log(276.500000,2),math.log(305.046875,2),math.log(246.976562,2),math.log(275.988281,2),math.log(320.535156,2),math.log(393.453125,2),math.log(532.415039,2),math.log(858.281006,2),math.log(1231.440674,2),math.log(2032.302307,2),math.log(3629.860718,2)]
t_99 = [math.log(272.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(226.000000,2),math.log(217.500000,2),math.log(201.250000,2),math.log(223.750000,2),math.log(259.500000,2),math.log(259.062500,2),math.log(270.093750,2),math.log(308.882812,2),math.log(305.230469,2),math.log(306.130859,2),math.log(329.057617,2),math.log(391.836426,2),math.log(542.268555,2),math.log(937.690063,2),math.log(1710.611511,2),math.log(3259.885803,2)]
t_100 = [math.log(240.000000,2),math.log(232.000000,2),math.log(268.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(248.500000,2),math.log(247.250000,2),math.log(238.000000,2),math.log(241.750000,2),math.log(222.875000,2),math.log(220.765625,2),math.log(245.250000,2),math.log(255.953125,2),math.log(260.656250,2),math.log(266.624023,2),math.log(312.609863,2),math.log(478.201904,2),math.log(663.750732,2),math.log(985.564758,2),math.log(1760.225189,2)]
t_101 = [math.log(240.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(216.000000,2),math.log(256.000000,2),math.log(286.500000,2),math.log(286.500000,2),math.log(272.125000,2),math.log(284.375000,2),math.log(286.875000,2),math.log(270.406250,2),math.log(257.070312,2),math.log(254.191406,2),math.log(258.787109,2),math.log(303.312500,2),math.log(423.776367,2),math.log(605.863281,2),math.log(933.755615,2),math.log(1627.520081,2),math.log(2925.400085,2)]
t_102 = [math.log(240.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(263.000000,2),math.log(272.000000,2),math.log(255.000000,2),math.log(254.500000,2),math.log(261.562500,2),math.log(249.125000,2),math.log(236.265625,2),math.log(296.992188,2),math.log(312.316406,2),math.log(305.738281,2),math.log(323.140625,2),math.log(388.541504,2),math.log(503.821533,2),math.log(787.675903,2),math.log(1383.298462,2),math.log(2461.831238,2)]
t_103 = [math.log(272.000000,2),math.log(296.000000,2),math.log(308.000000,2),math.log(236.000000,2),math.log(229.000000,2),math.log(244.000000,2),math.log(267.000000,2),math.log(289.500000,2),math.log(279.812500,2),math.log(273.812500,2),math.log(249.531250,2),math.log(288.992188,2),math.log(266.890625,2),math.log(296.740234,2),math.log(361.623047,2),math.log(497.930176,2),math.log(700.062256,2),math.log(1302.861938,2),math.log(2300.946045,2),math.log(4423.013123,2)]
t_104 = [math.log(272.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(284.000000,2),math.log(334.000000,2),math.log(282.000000,2),math.log(252.000000,2),math.log(268.000000,2),math.log(244.562500,2),math.log(233.343750,2),math.log(255.625000,2),math.log(225.117188,2),math.log(219.402344,2),math.log(281.021484,2),math.log(352.836914,2),math.log(428.883301,2),math.log(582.053467,2),math.log(866.165405,2),math.log(1482.586121,2),math.log(2615.611359,2)]
t_105 = [math.log(240.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(271.500000,2),math.log(266.750000,2),math.log(247.750000,2),math.log(251.250000,2),math.log(254.687500,2),math.log(246.859375,2),math.log(289.171875,2),math.log(283.476562,2),math.log(255.617188,2),math.log(325.905273,2),math.log(421.285156,2),math.log(576.576416,2),math.log(900.492188,2),math.log(1427.272217,2),math.log(2559.289093,2)]
t_106 = [math.log(224.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(236.000000,2),math.log(265.000000,2),math.log(219.000000,2),math.log(266.000000,2),math.log(251.375000,2),math.log(222.187500,2),math.log(228.687500,2),math.log(248.203125,2),math.log(285.960938,2),math.log(304.531250,2),math.log(404.785156,2),math.log(545.513672,2),math.log(932.910645,2),math.log(1585.236816,2),math.log(2955.722900,2),math.log(5724.390503,2),math.log(11187.407898,2)]
t_107 = [math.log(272.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(236.000000,2),math.log(214.500000,2),math.log(233.500000,2),math.log(259.500000,2),math.log(273.625000,2),math.log(276.250000,2),math.log(241.968750,2),math.log(249.125000,2),math.log(294.871094,2),math.log(302.189453,2),math.log(365.147461,2),math.log(518.607422,2),math.log(752.085205,2),math.log(1271.928711,2),math.log(2212.685913,2),math.log(4197.558838,2)]
t_108 = [math.log(272.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(250.000000,2),math.log(265.500000,2),math.log(284.250000,2),math.log(289.875000,2),math.log(262.937500,2),math.log(253.750000,2),math.log(233.937500,2),math.log(251.960938,2),math.log(323.230469,2),math.log(358.361328,2),math.log(367.994141,2),math.log(543.138184,2),math.log(693.705078,2),math.log(1017.174438,2),math.log(1851.010254,2),math.log(3464.492767,2)]
t_109 = [math.log(272.000000,2),math.log(296.000000,2),math.log(280.000000,2),math.log(254.000000,2),math.log(234.000000,2),math.log(235.000000,2),math.log(237.500000,2),math.log(281.500000,2),math.log(264.375000,2),math.log(247.593750,2),math.log(231.468750,2),math.log(265.632812,2),math.log(323.210938,2),math.log(389.205078,2),math.log(508.164062,2),math.log(768.247559,2),math.log(1156.592529,2),math.log(2009.856323,2),math.log(3810.299377,2),math.log(7271.893982,2)]
t_110 = [math.log(288.000000,2),math.log(296.000000,2),math.log(296.000000,2),math.log(298.000000,2),math.log(246.000000,2),math.log(245.000000,2),math.log(257.750000,2),math.log(266.375000,2),math.log(250.937500,2),math.log(261.437500,2),math.log(237.718750,2),math.log(251.453125,2),math.log(324.625000,2),math.log(355.322266,2),math.log(473.137695,2),math.log(685.236816,2),math.log(1069.492920,2),math.log(1839.162842,2),math.log(3616.687378,2),math.log(7202.853149,2)]
t_111 = [math.log(272.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(274.000000,2),math.log(299.000000,2),math.log(266.000000,2),math.log(239.250000,2),math.log(221.625000,2),math.log(234.500000,2),math.log(268.531250,2),math.log(275.203125,2),math.log(295.789062,2),math.log(323.941406,2),math.log(356.425781,2),math.log(399.498047,2),math.log(516.884766,2),math.log(783.784180,2),math.log(1327.170288,2),math.log(2474.081787,2),math.log(4787.121552,2)]
t_112 = [math.log(224.000000,2),math.log(240.000000,2),math.log(268.000000,2),math.log(232.000000,2),math.log(247.000000,2),math.log(232.500000,2),math.log(247.000000,2),math.log(253.875000,2),math.log(264.562500,2),math.log(247.718750,2),math.log(298.625000,2),math.log(276.367188,2),math.log(257.621094,2),math.log(299.341797,2),math.log(334.528320,2),math.log(381.506348,2),math.log(494.075928,2),math.log(771.128418,2),math.log(1362.307678,2),math.log(2297.101135,2)]
t_113 = [math.log(272.000000,2),math.log(248.000000,2),math.log(308.000000,2),math.log(284.000000,2),math.log(261.000000,2),math.log(257.500000,2),math.log(279.500000,2),math.log(274.000000,2),math.log(284.500000,2),math.log(273.812500,2),math.log(275.359375,2),math.log(283.328125,2),math.log(310.691406,2),math.log(305.619141,2),math.log(350.877930,2),math.log(413.802734,2),math.log(610.544434,2),math.log(917.009277,2),math.log(1572.354065,2),math.log(2725.236816,2)]
t_114 = [math.log(320.000000,2),math.log(280.000000,2),math.log(264.000000,2),math.log(234.000000,2),math.log(250.000000,2),math.log(267.000000,2),math.log(249.250000,2),math.log(255.125000,2),math.log(229.375000,2),math.log(261.593750,2),math.log(265.500000,2),math.log(278.265625,2),math.log(272.394531,2),math.log(273.388672,2),math.log(297.930664,2),math.log(367.100098,2),math.log(532.349121,2),math.log(957.706787,2),math.log(1587.500977,2),math.log(2979.961548,2)]
t_115 = [math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(230.000000,2),math.log(255.000000,2),math.log(218.000000,2),math.log(246.250000,2),math.log(257.750000,2),math.log(270.687500,2),math.log(288.906250,2),math.log(263.953125,2),math.log(254.906250,2),math.log(303.609375,2),math.log(342.894531,2),math.log(403.463867,2),math.log(509.229980,2),math.log(762.211914,2),math.log(1262.629517,2),math.log(2251.356934,2),math.log(4170.161255,2)]
t_116 = [math.log(240.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(262.000000,2),math.log(264.500000,2),math.log(271.000000,2),math.log(277.125000,2),math.log(277.437500,2),math.log(251.531250,2),math.log(285.375000,2),math.log(238.171875,2),math.log(234.648438,2),math.log(276.923828,2),math.log(338.686523,2),math.log(435.251953,2),math.log(628.291016,2),math.log(1007.081299,2),math.log(1767.714478,2),math.log(3408.529938,2)]
t_117 = [math.log(256.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(294.000000,2),math.log(285.000000,2),math.log(286.500000,2),math.log(286.750000,2),math.log(282.875000,2),math.log(253.250000,2),math.log(238.375000,2),math.log(237.671875,2),math.log(266.804688,2),math.log(271.187500,2),math.log(317.269531,2),math.log(387.507812,2),math.log(520.594727,2),math.log(718.660645,2),math.log(1123.458130,2),math.log(1940.038147,2),math.log(3668.607758,2)]
t_118 = [math.log(272.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(262.000000,2),math.log(225.000000,2),math.log(217.000000,2),math.log(247.750000,2),math.log(276.000000,2),math.log(242.312500,2),math.log(230.906250,2),math.log(253.562500,2),math.log(293.945312,2),math.log(309.519531,2),math.log(350.978516,2),math.log(346.931641,2),math.log(489.063477,2),math.log(762.855713,2),math.log(1162.470093,2),math.log(1981.317017,2),math.log(3678.178101,2)]
t_119 = [math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(262.000000,2),math.log(242.000000,2),math.log(245.000000,2),math.log(253.000000,2),math.log(238.625000,2),math.log(234.437500,2),math.log(244.937500,2),math.log(251.937500,2),math.log(243.726562,2),math.log(259.546875,2),math.log(298.726562,2),math.log(378.970703,2),math.log(587.092773,2),math.log(885.679199,2),math.log(1615.018188,2),math.log(2881.041016,2),math.log(5710.791687,2)]
t_120 = [math.log(224.000000,2),math.log(216.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(259.000000,2),math.log(251.500000,2),math.log(229.500000,2),math.log(296.500000,2),math.log(301.187500,2),math.log(289.031250,2),math.log(241.546875,2),math.log(239.148438,2),math.log(244.757812,2),math.log(294.958984,2),math.log(355.646484,2),math.log(489.726074,2),math.log(791.878174,2),math.log(1264.090088,2),math.log(2278.411377,2),math.log(4188.422943,2)]
t_121 = [math.log(224.000000,2),math.log(208.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(251.000000,2),math.log(264.000000,2),math.log(281.750000,2),math.log(286.125000,2),math.log(294.625000,2),math.log(262.937500,2),math.log(277.437500,2),math.log(265.625000,2),math.log(264.687500,2),math.log(261.898438,2),math.log(317.915039,2),math.log(466.381836,2),math.log(749.249023,2),math.log(1383.193848,2),math.log(2473.473877,2),math.log(4564.180542,2)]
t_122 = [math.log(240.000000,2),math.log(248.000000,2),math.log(216.000000,2),math.log(238.000000,2),math.log(234.000000,2),math.log(245.000000,2),math.log(231.000000,2),math.log(236.375000,2),math.log(244.500000,2),math.log(257.781250,2),math.log(306.359375,2),math.log(318.367188,2),math.log(363.707031,2),math.log(513.781250,2),math.log(734.015625,2),math.log(1173.801758,2),math.log(2029.634766,2),math.log(3862.318481,2),math.log(7591.359497,2),math.log(14724.018188,2)]
t_123 = [math.log(256.000000,2),math.log(240.000000,2),math.log(248.000000,2),math.log(250.000000,2),math.log(245.000000,2),math.log(275.500000,2),math.log(273.250000,2),math.log(255.875000,2),math.log(230.750000,2),math.log(262.468750,2),math.log(289.656250,2),math.log(306.210938,2),math.log(334.195312,2),math.log(364.779297,2),math.log(505.136719,2),math.log(647.139648,2),math.log(998.669189,2),math.log(1653.503662,2),math.log(3218.478455,2),math.log(6456.996429,2)]
t_124 = [math.log(272.000000,2),math.log(280.000000,2),math.log(300.000000,2),math.log(242.000000,2),math.log(257.000000,2),math.log(239.500000,2),math.log(242.500000,2),math.log(296.000000,2),math.log(291.875000,2),math.log(329.062500,2),math.log(295.765625,2),math.log(257.968750,2),math.log(263.750000,2),math.log(265.750000,2),math.log(269.667969,2),math.log(379.541016,2),math.log(606.396484,2),math.log(980.608887,2),math.log(1662.569275,2),math.log(3078.739716,2)]
t_125 = [math.log(240.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(246.000000,2),math.log(252.000000,2),math.log(261.500000,2),math.log(259.000000,2),math.log(272.500000,2),math.log(259.187500,2),math.log(270.218750,2),math.log(259.953125,2),math.log(270.617188,2),math.log(312.546875,2),math.log(328.085938,2),math.log(408.850586,2),math.log(584.213867,2),math.log(1033.601807,2),math.log(1759.767578,2),math.log(3513.867249,2),math.log(6874.700745,2)]
t_126 = [math.log(240.000000,2),math.log(232.000000,2),math.log(208.000000,2),math.log(216.000000,2),math.log(257.000000,2),math.log(267.000000,2),math.log(276.250000,2),math.log(275.750000,2),math.log(281.187500,2),math.log(244.656250,2),math.log(225.343750,2),math.log(267.992188,2),math.log(286.277344,2),math.log(374.166016,2),math.log(453.675781,2),math.log(662.555176,2),math.log(1104.729736,2),math.log(2040.927734,2),math.log(3822.685425,2),math.log(7280.723969,2)]
t_127 = [math.log(224.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(272.000000,2),math.log(287.000000,2),math.log(244.000000,2),math.log(258.250000,2),math.log(251.500000,2),math.log(269.375000,2),math.log(281.437500,2),math.log(282.187500,2),math.log(299.164062,2),math.log(349.535156,2),math.log(355.304688,2),math.log(432.463867,2),math.log(651.158203,2),math.log(1130.896729,2),math.log(1918.856567,2),math.log(3567.744324,2),math.log(6795.760590,2)]
t_128 = [math.log(240.000000,2),math.log(240.000000,2),math.log(264.000000,2),math.log(290.000000,2),math.log(267.000000,2),math.log(257.000000,2),math.log(301.500000,2),math.log(248.250000,2),math.log(233.250000,2),math.log(229.375000,2),math.log(225.234375,2),math.log(226.148438,2),math.log(227.441406,2),math.log(258.115234,2),math.log(289.304688,2),math.log(338.833496,2),math.log(445.251465,2),math.log(608.571045,2),math.log(940.674377,2),math.log(1529.010498,2)]
t_129 = [math.log(240.000000,2),math.log(232.000000,2),math.log(260.000000,2),math.log(228.000000,2),math.log(215.000000,2),math.log(204.000000,2),math.log(242.750000,2),math.log(251.625000,2),math.log(258.750000,2),math.log(263.312500,2),math.log(256.203125,2),math.log(262.648438,2),math.log(244.976562,2),math.log(258.730469,2),math.log(292.689453,2),math.log(362.236328,2),math.log(491.802246,2),math.log(704.006592,2),math.log(1086.894104,2),math.log(1909.035431,2)]
t_130 = [math.log(240.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(255.000000,2),math.log(279.000000,2),math.log(272.250000,2),math.log(269.375000,2),math.log(263.312500,2),math.log(264.968750,2),math.log(302.531250,2),math.log(264.460938,2),math.log(273.910156,2),math.log(296.761719,2),math.log(325.029297,2),math.log(344.501953,2),math.log(426.746826,2),math.log(643.511841,2),math.log(1061.471985,2),math.log(1875.283691,2)]
t_131 = [math.log(224.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(264.000000,2),math.log(275.000000,2),math.log(214.000000,2),math.log(225.250000,2),math.log(244.000000,2),math.log(268.562500,2),math.log(263.968750,2),math.log(299.546875,2),math.log(313.796875,2),math.log(291.761719,2),math.log(341.132812,2),math.log(343.825195,2),math.log(437.140137,2),math.log(515.990234,2),math.log(799.345337,2),math.log(1372.642273,2),math.log(2295.328003,2)]
t_132 = [math.log(272.000000,2),math.log(296.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(229.000000,2),math.log(242.000000,2),math.log(232.500000,2),math.log(247.375000,2),math.log(239.250000,2),math.log(243.093750,2),math.log(244.500000,2),math.log(241.734375,2),math.log(268.167969,2),math.log(259.656250,2),math.log(299.523438,2),math.log(302.428711,2),math.log(367.950684,2),math.log(512.604858,2),math.log(859.261169,2),math.log(1573.030579,2)]
t_133 = [math.log(288.000000,2),math.log(296.000000,2),math.log(296.000000,2),math.log(284.000000,2),math.log(260.000000,2),math.log(275.500000,2),math.log(276.250000,2),math.log(270.375000,2),math.log(263.937500,2),math.log(263.250000,2),math.log(256.218750,2),math.log(249.500000,2),math.log(242.054688,2),math.log(273.640625,2),math.log(329.652344,2),math.log(366.570801,2),math.log(546.144043,2),math.log(804.907471,2),math.log(1426.754578,2),math.log(2473.644562,2)]
t_134 = [math.log(256.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(214.000000,2),math.log(224.000000,2),math.log(259.500000,2),math.log(282.500000,2),math.log(278.000000,2),math.log(268.312500,2),math.log(267.062500,2),math.log(273.046875,2),math.log(282.585938,2),math.log(342.062500,2),math.log(310.601562,2),math.log(331.929688,2),math.log(389.689941,2),math.log(563.195557,2),math.log(753.671143,2),math.log(1161.655151,2),math.log(2102.318054,2)]
t_135 = [math.log(240.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(282.000000,2),math.log(275.500000,2),math.log(273.750000,2),math.log(281.125000,2),math.log(272.937500,2),math.log(240.375000,2),math.log(247.234375,2),math.log(272.515625,2),math.log(310.730469,2),math.log(326.072266,2),math.log(354.713867,2),math.log(393.149414,2),math.log(530.997803,2),math.log(856.216553,2),math.log(1477.468811,2),math.log(2617.118958,2)]
t_136 = [math.log(272.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(228.000000,2),math.log(208.000000,2),math.log(228.500000,2),math.log(203.500000,2),math.log(229.875000,2),math.log(255.375000,2),math.log(245.593750,2),math.log(277.031250,2),math.log(275.890625,2),math.log(272.542969,2),math.log(303.960938,2),math.log(334.257812,2),math.log(475.703613,2),math.log(612.317139,2),math.log(1097.321045,2),math.log(1991.055786,2),math.log(3929.992889,2)]
t_137 = [math.log(256.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(244.000000,2),math.log(249.000000,2),math.log(239.500000,2),math.log(244.000000,2),math.log(246.375000,2),math.log(232.875000,2),math.log(232.562500,2),math.log(240.187500,2),math.log(272.289062,2),math.log(298.355469,2),math.log(335.125000,2),math.log(393.782227,2),math.log(498.661133,2),math.log(809.118896,2),math.log(1437.433716,2),math.log(2591.977600,2),math.log(4767.833099,2)]
t_138 = [math.log(272.000000,2),math.log(240.000000,2),math.log(276.000000,2),math.log(256.000000,2),math.log(261.000000,2),math.log(251.000000,2),math.log(269.000000,2),math.log(252.500000,2),math.log(235.000000,2),math.log(244.031250,2),math.log(290.437500,2),math.log(331.296875,2),math.log(299.628906,2),math.log(374.736328,2),math.log(519.006836,2),math.log(884.007812,2),math.log(1578.885498,2),math.log(3022.106079,2),math.log(6182.571228,2),math.log(11892.867706,2)]
t_139 = [math.log(240.000000,2),math.log(256.000000,2),math.log(220.000000,2),math.log(266.000000,2),math.log(277.000000,2),math.log(252.500000,2),math.log(251.500000,2),math.log(268.500000,2),math.log(296.187500,2),math.log(272.062500,2),math.log(249.218750,2),math.log(263.101562,2),math.log(265.621094,2),math.log(334.347656,2),math.log(376.294922,2),math.log(523.962402,2),math.log(833.683350,2),math.log(1507.571777,2),math.log(2613.393738,2),math.log(5009.559723,2)]
t_140 = [math.log(240.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(262.000000,2),math.log(312.000000,2),math.log(271.000000,2),math.log(259.500000,2),math.log(274.250000,2),math.log(270.937500,2),math.log(233.312500,2),math.log(256.921875,2),math.log(260.476562,2),math.log(281.171875,2),math.log(294.478516,2),math.log(298.276367,2),math.log(337.496094,2),math.log(357.885742,2),math.log(547.789551,2),math.log(874.779236,2),math.log(1485.184174,2)]
t_141 = [math.log(240.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(244.000000,2),math.log(264.000000,2),math.log(258.500000,2),math.log(267.750000,2),math.log(247.500000,2),math.log(294.000000,2),math.log(256.312500,2),math.log(275.296875,2),math.log(233.632812,2),math.log(259.941406,2),math.log(294.230469,2),math.log(383.271484,2),math.log(561.125488,2),math.log(784.947998,2),math.log(1292.497559,2),math.log(2423.412476,2),math.log(4550.768829,2)]
t_142 = [math.log(224.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(264.000000,2),math.log(271.500000,2),math.log(300.250000,2),math.log(269.875000,2),math.log(259.000000,2),math.log(258.343750,2),math.log(280.000000,2),math.log(281.250000,2),math.log(311.613281,2),math.log(295.025391,2),math.log(324.582031,2),math.log(462.934082,2),math.log(754.853027,2),math.log(1312.542603,2),math.log(2272.147278,2),math.log(4305.945984,2)]
t_143 = [math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(230.000000,2),math.log(233.000000,2),math.log(240.000000,2),math.log(252.250000,2),math.log(270.125000,2),math.log(246.312500,2),math.log(227.437500,2),math.log(212.671875,2),math.log(204.632812,2),math.log(233.054688,2),math.log(254.791016,2),math.log(315.296875,2),math.log(419.442383,2),math.log(547.050293,2),math.log(779.663818,2),math.log(1405.178345,2),math.log(2572.442993,2)]
t_144 = [math.log(288.000000,2),math.log(336.000000,2),math.log(260.000000,2),math.log(284.000000,2),math.log(262.000000,2),math.log(281.500000,2),math.log(232.750000,2),math.log(270.375000,2),math.log(272.812500,2),math.log(279.750000,2),math.log(246.687500,2),math.log(249.937500,2),math.log(253.152344,2),math.log(244.437500,2),math.log(330.453125,2),math.log(344.292480,2),math.log(387.135254,2),math.log(603.449341,2),math.log(867.213867,2),math.log(1639.354980,2)]
t_145 = [math.log(304.000000,2),math.log(296.000000,2),math.log(260.000000,2),math.log(240.000000,2),math.log(272.000000,2),math.log(262.500000,2),math.log(262.750000,2),math.log(279.750000,2),math.log(304.687500,2),math.log(284.062500,2),math.log(258.843750,2),math.log(297.882812,2),math.log(267.019531,2),math.log(262.201172,2),math.log(301.386719,2),math.log(386.933105,2),math.log(384.208740,2),math.log(585.589600,2),math.log(1050.317566,2),math.log(1782.642365,2)]
t_146 = [math.log(256.000000,2),math.log(248.000000,2),math.log(268.000000,2),math.log(248.000000,2),math.log(274.000000,2),math.log(286.500000,2),math.log(259.500000,2),math.log(235.500000,2),math.log(259.500000,2),math.log(223.812500,2),math.log(263.859375,2),math.log(260.492188,2),math.log(258.832031,2),math.log(294.400391,2),math.log(347.448242,2),math.log(407.110352,2),math.log(592.289551,2),math.log(921.734619,2),math.log(1443.557922,2),math.log(2552.024933,2)]
t_147 = [math.log(256.000000,2),math.log(280.000000,2),math.log(244.000000,2),math.log(212.000000,2),math.log(246.000000,2),math.log(209.000000,2),math.log(227.750000,2),math.log(240.500000,2),math.log(217.000000,2),math.log(250.875000,2),math.log(264.718750,2),math.log(233.226562,2),math.log(277.371094,2),math.log(303.164062,2),math.log(328.845703,2),math.log(387.725586,2),math.log(504.197266,2),math.log(720.787964,2),math.log(1129.955444,2),math.log(2087.200745,2)]
t_148 = [math.log(288.000000,2),math.log(280.000000,2),math.log(244.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(260.500000,2),math.log(268.750000,2),math.log(259.750000,2),math.log(247.375000,2),math.log(270.468750,2),math.log(289.875000,2),math.log(282.046875,2),math.log(274.019531,2),math.log(267.230469,2),math.log(283.535156,2),math.log(363.067871,2),math.log(408.014648,2),math.log(630.044678,2),math.log(1008.712097,2),math.log(1605.293671,2)]
t_149 = [math.log(304.000000,2),math.log(264.000000,2),math.log(288.000000,2),math.log(260.000000,2),math.log(253.000000,2),math.log(222.500000,2),math.log(239.250000,2),math.log(245.125000,2),math.log(260.250000,2),math.log(250.125000,2),math.log(229.562500,2),math.log(299.398438,2),math.log(263.378906,2),math.log(286.058594,2),math.log(311.438477,2),math.log(399.430176,2),math.log(594.862793,2),math.log(815.126099,2),math.log(1393.517639,2),math.log(2513.279755,2)]
t_150 = [math.log(288.000000,2),math.log(264.000000,2),math.log(244.000000,2),math.log(242.000000,2),math.log(223.000000,2),math.log(254.500000,2),math.log(263.000000,2),math.log(236.000000,2),math.log(259.312500,2),math.log(233.593750,2),math.log(268.671875,2),math.log(263.125000,2),math.log(270.328125,2),math.log(303.853516,2),math.log(301.746094,2),math.log(387.318848,2),math.log(517.303711,2),math.log(753.453491,2),math.log(1300.483459,2),math.log(2335.358215,2)]
t_151 = [math.log(272.000000,2),math.log(296.000000,2),math.log(308.000000,2),math.log(288.000000,2),math.log(274.000000,2),math.log(237.500000,2),math.log(264.000000,2),math.log(265.875000,2),math.log(218.875000,2),math.log(234.593750,2),math.log(232.390625,2),math.log(251.328125,2),math.log(249.179688,2),math.log(303.980469,2),math.log(340.657227,2),math.log(376.045410,2),math.log(525.564209,2),math.log(783.758667,2),math.log(1405.916443,2),math.log(2608.079651,2)]
t_152 = [math.log(240.000000,2),math.log(248.000000,2),math.log(292.000000,2),math.log(228.000000,2),math.log(284.000000,2),math.log(295.000000,2),math.log(235.750000,2),math.log(256.500000,2),math.log(247.250000,2),math.log(254.281250,2),math.log(237.703125,2),math.log(247.921875,2),math.log(273.625000,2),math.log(294.144531,2),math.log(344.746094,2),math.log(391.357422,2),math.log(555.281738,2),math.log(755.630371,2),math.log(1314.346497,2),math.log(2444.622437,2)]
t_153 = [math.log(256.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(206.000000,2),math.log(250.000000,2),math.log(259.500000,2),math.log(268.000000,2),math.log(277.625000,2),math.log(266.750000,2),math.log(275.437500,2),math.log(229.437500,2),math.log(242.984375,2),math.log(262.062500,2),math.log(278.732422,2),math.log(374.122070,2),math.log(443.480957,2),math.log(636.798340,2),math.log(1026.568848,2),math.log(1780.002441,2),math.log(3346.983978,2)]
t_154 = [math.log(256.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(266.000000,2),math.log(278.000000,2),math.log(247.000000,2),math.log(308.250000,2),math.log(248.375000,2),math.log(287.875000,2),math.log(292.718750,2),math.log(285.390625,2),math.log(321.148438,2),math.log(359.132812,2),math.log(452.126953,2),math.log(603.406250,2),math.log(884.684082,2),math.log(1446.371338,2),math.log(2595.182251,2),math.log(4840.714783,2),math.log(9676.990631,2)]
t_155 = [math.log(240.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(236.000000,2),math.log(220.000000,2),math.log(248.000000,2),math.log(227.750000,2),math.log(246.625000,2),math.log(263.500000,2),math.log(266.343750,2),math.log(234.890625,2),math.log(249.320312,2),math.log(270.726562,2),math.log(307.863281,2),math.log(368.059570,2),math.log(503.654297,2),math.log(787.677979,2),math.log(1273.602173,2),math.log(2325.135986,2),math.log(4289.254395,2)]
t_156 = [math.log(224.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(238.000000,2),math.log(214.000000,2),math.log(255.000000,2),math.log(246.000000,2),math.log(283.250000,2),math.log(298.437500,2),math.log(256.093750,2),math.log(278.140625,2),math.log(275.679688,2),math.log(252.214844,2),math.log(267.443359,2),math.log(279.360352,2),math.log(376.169922,2),math.log(517.403320,2),math.log(776.659546,2),math.log(1381.352600,2),math.log(2618.589233,2)]
t_157 = [math.log(240.000000,2),math.log(272.000000,2),math.log(236.000000,2),math.log(298.000000,2),math.log(261.000000,2),math.log(224.500000,2),math.log(258.000000,2),math.log(273.000000,2),math.log(245.062500,2),math.log(276.468750,2),math.log(232.890625,2),math.log(253.703125,2),math.log(298.597656,2),math.log(328.296875,2),math.log(383.986328,2),math.log(486.513672,2),math.log(837.843506,2),math.log(1414.655640,2),math.log(2724.489868,2),math.log(5240.620361,2)]
t_158 = [math.log(240.000000,2),math.log(240.000000,2),math.log(244.000000,2),math.log(258.000000,2),math.log(232.000000,2),math.log(234.000000,2),math.log(260.500000,2),math.log(270.125000,2),math.log(268.000000,2),math.log(261.281250,2),math.log(263.406250,2),math.log(277.664062,2),math.log(313.164062,2),math.log(388.224609,2),math.log(461.386719,2),math.log(667.297363,2),math.log(1254.279053,2),math.log(2297.087036,2),math.log(4218.322693,2),math.log(7912.036957,2)]
t_159 = [math.log(256.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(266.000000,2),math.log(256.000000,2),math.log(284.000000,2),math.log(271.750000,2),math.log(276.500000,2),math.log(240.812500,2),math.log(210.531250,2),math.log(238.234375,2),math.log(244.523438,2),math.log(305.361328,2),math.log(305.593750,2),math.log(428.898438,2),math.log(617.557129,2),math.log(1037.103638,2),math.log(1849.773621,2),math.log(3295.019897,2)]
t_160 = [math.log(272.000000,2),math.log(264.000000,2),math.log(264.000000,2),math.log(258.000000,2),math.log(261.000000,2),math.log(239.000000,2),math.log(252.000000,2),math.log(271.125000,2),math.log(248.375000,2),math.log(273.937500,2),math.log(253.750000,2),math.log(261.906250,2),math.log(325.925781,2),math.log(378.210938,2),math.log(401.016602,2),math.log(623.957520,2),math.log(959.576172,2),math.log(1577.635742,2),math.log(2902.919617,2),math.log(5617.325500,2)]
t_161 = [math.log(240.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(212.000000,2),math.log(219.000000,2),math.log(210.500000,2),math.log(244.500000,2),math.log(253.000000,2),math.log(220.500000,2),math.log(238.593750,2),math.log(250.390625,2),math.log(290.671875,2),math.log(281.910156,2),math.log(317.960938,2),math.log(409.344727,2),math.log(602.284180,2),math.log(971.986084,2),math.log(1642.578613,2),math.log(3070.493591,2),math.log(5779.221283,2)]
t_162 = [math.log(224.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(252.000000,2),math.log(256.000000,2),math.log(260.500000,2),math.log(223.500000,2),math.log(238.000000,2),math.log(259.687500,2),math.log(266.968750,2),math.log(315.906250,2),math.log(283.484375,2),math.log(315.039062,2),math.log(371.562500,2),math.log(439.587891,2),math.log(563.006836,2),math.log(826.161377,2),math.log(1374.476074,2),math.log(2403.026428,2),math.log(4469.829620,2)]
t_163 = [math.log(256.000000,2),math.log(224.000000,2),math.log(224.000000,2),math.log(232.000000,2),math.log(212.000000,2),math.log(253.000000,2),math.log(236.750000,2),math.log(209.000000,2),math.log(273.812500,2),math.log(280.937500,2),math.log(300.828125,2),math.log(308.453125,2),math.log(313.476562,2),math.log(364.328125,2),math.log(475.181641,2),math.log(694.086426,2),math.log(1080.291260,2),math.log(1862.211548,2),math.log(3401.326111,2),math.log(6629.247650,2)]
t_164 = [math.log(256.000000,2),math.log(280.000000,2),math.log(252.000000,2),math.log(264.000000,2),math.log(240.000000,2),math.log(250.500000,2),math.log(237.500000,2),math.log(229.875000,2),math.log(205.875000,2),math.log(245.375000,2),math.log(268.437500,2),math.log(245.570312,2),math.log(284.910156,2),math.log(332.875000,2),math.log(393.874023,2),math.log(532.565918,2),math.log(868.443604,2),math.log(1444.798096,2),math.log(2662.146851,2),math.log(5100.693054,2)]
t_165 = [math.log(240.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(266.000000,2),math.log(261.000000,2),math.log(264.250000,2),math.log(234.250000,2),math.log(247.937500,2),math.log(259.812500,2),math.log(238.859375,2),math.log(229.726562,2),math.log(241.761719,2),math.log(275.607422,2),math.log(325.983398,2),math.log(398.081543,2),math.log(533.603760,2),math.log(802.468140,2),math.log(1325.810059,2),math.log(2403.688385,2)]
t_166 = [math.log(272.000000,2),math.log(280.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(253.000000,2),math.log(258.500000,2),math.log(212.000000,2),math.log(214.250000,2),math.log(227.375000,2),math.log(235.562500,2),math.log(249.875000,2),math.log(268.937500,2),math.log(245.179688,2),math.log(339.974609,2),math.log(382.109375,2),math.log(550.968750,2),math.log(774.790527,2),math.log(1321.750610,2),math.log(2474.291138,2),math.log(4552.247559,2)]
t_167 = [math.log(272.000000,2),math.log(256.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(276.000000,2),math.log(267.000000,2),math.log(240.750000,2),math.log(239.500000,2),math.log(259.500000,2),math.log(295.281250,2),math.log(279.937500,2),math.log(313.562500,2),math.log(339.859375,2),math.log(469.136719,2),math.log(583.501953,2),math.log(891.012207,2),math.log(1596.585449,2),math.log(2706.014648,2),math.log(5080.641602,2),math.log(9691.367859,2)]
t_168 = [math.log(288.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(234.000000,2),math.log(245.000000,2),math.log(236.500000,2),math.log(243.750000,2),math.log(234.625000,2),math.log(267.750000,2),math.log(239.125000,2),math.log(255.109375,2),math.log(269.562500,2),math.log(342.632812,2),math.log(348.634766,2),math.log(408.413086,2),math.log(536.993164,2),math.log(808.718018,2),math.log(1365.469482,2),math.log(2244.207336,2),math.log(4403.709930,2)]
t_169 = [math.log(256.000000,2),math.log(272.000000,2),math.log(296.000000,2),math.log(258.000000,2),math.log(260.000000,2),math.log(247.500000,2),math.log(267.250000,2),math.log(261.375000,2),math.log(273.250000,2),math.log(251.031250,2),math.log(241.390625,2),math.log(268.164062,2),math.log(293.417969,2),math.log(328.826172,2),math.log(394.936523,2),math.log(600.644043,2),math.log(924.605469,2),math.log(1590.450195,2),math.log(2901.416626,2),math.log(5780.849945,2)]
t_170 = [math.log(304.000000,2),math.log(296.000000,2),math.log(272.000000,2),math.log(260.000000,2),math.log(256.000000,2),math.log(259.000000,2),math.log(246.000000,2),math.log(217.500000,2),math.log(210.750000,2),math.log(266.375000,2),math.log(297.000000,2),math.log(316.109375,2),math.log(324.664062,2),math.log(426.427734,2),math.log(659.888672,2),math.log(970.879883,2),math.log(1691.297363,2),math.log(3300.986694,2),math.log(6108.951538,2),math.log(11982.156891,2)]
t_171 = [math.log(272.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(235.000000,2),math.log(252.000000,2),math.log(228.250000,2),math.log(247.125000,2),math.log(252.937500,2),math.log(287.281250,2),math.log(272.625000,2),math.log(282.601562,2),math.log(347.503906,2),math.log(405.107422,2),math.log(523.872070,2),math.log(778.362793,2),math.log(1209.710205,2),math.log(2046.599609,2),math.log(3938.543518,2),math.log(7556.346924,2)]
t_172 = [math.log(256.000000,2),math.log(264.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(221.000000,2),math.log(221.000000,2),math.log(203.250000,2),math.log(224.875000,2),math.log(224.687500,2),math.log(193.250000,2),math.log(211.015625,2),math.log(247.367188,2),math.log(279.589844,2),math.log(357.359375,2),math.log(469.617188,2),math.log(643.479980,2),math.log(1088.591553,2),math.log(1982.353271,2),math.log(3757.213501,2),math.log(7260.682526,2)]
t_173 = [math.log(256.000000,2),math.log(272.000000,2),math.log(232.000000,2),math.log(242.000000,2),math.log(262.000000,2),math.log(300.000000,2),math.log(295.750000,2),math.log(275.375000,2),math.log(268.187500,2),math.log(264.718750,2),math.log(283.718750,2),math.log(341.265625,2),math.log(385.687500,2),math.log(515.542969,2),math.log(721.315430,2),math.log(1071.994629,2),math.log(1830.006348,2),math.log(3328.927490,2),math.log(6438.509705,2),math.log(12588.363586,2)]
t_174 = [math.log(256.000000,2),math.log(264.000000,2),math.log(204.000000,2),math.log(218.000000,2),math.log(230.000000,2),math.log(255.500000,2),math.log(246.000000,2),math.log(213.625000,2),math.log(225.000000,2),math.log(222.125000,2),math.log(235.640625,2),math.log(259.570312,2),math.log(357.574219,2),math.log(466.949219,2),math.log(610.685547,2),math.log(899.134277,2),math.log(1467.781738,2),math.log(2664.510254,2),math.log(5033.395813,2),math.log(9875.669250,2)]
t_175 = [math.log(240.000000,2),math.log(304.000000,2),math.log(312.000000,2),math.log(258.000000,2),math.log(248.000000,2),math.log(246.500000,2),math.log(273.750000,2),math.log(275.000000,2),math.log(251.500000,2),math.log(226.906250,2),math.log(241.500000,2),math.log(288.492188,2),math.log(353.925781,2),math.log(344.875000,2),math.log(369.144531,2),math.log(478.551270,2),math.log(756.954346,2),math.log(1273.408813,2),math.log(2221.094910,2),math.log(4164.136078,2)]
t_176 = [math.log(288.000000,2),math.log(256.000000,2),math.log(260.000000,2),math.log(256.000000,2),math.log(298.000000,2),math.log(290.500000,2),math.log(261.750000,2),math.log(234.625000,2),math.log(197.000000,2),math.log(234.062500,2),math.log(275.562500,2),math.log(276.367188,2),math.log(289.078125,2),math.log(272.031250,2),math.log(305.538086,2),math.log(429.111328,2),math.log(596.739746,2),math.log(886.913208,2),math.log(1433.116150,2),math.log(2545.746826,2)]
t_177 = [math.log(256.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(242.500000,2),math.log(269.750000,2),math.log(231.125000,2),math.log(223.500000,2),math.log(279.312500,2),math.log(241.875000,2),math.log(247.875000,2),math.log(287.433594,2),math.log(303.525391,2),math.log(392.829102,2),math.log(514.332031,2),math.log(716.047363,2),math.log(1282.786865,2),math.log(2169.572021,2),math.log(4190.039368,2)]
t_178 = [math.log(256.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(256.000000,2),math.log(213.000000,2),math.log(204.500000,2),math.log(209.250000,2),math.log(217.750000,2),math.log(208.562500,2),math.log(235.406250,2),math.log(235.140625,2),math.log(255.125000,2),math.log(304.156250,2),math.log(291.464844,2),math.log(332.190430,2),math.log(431.545410,2),math.log(634.665527,2),math.log(971.947510,2),math.log(1808.535095,2),math.log(3225.226868,2)]
t_179 = [math.log(224.000000,2),math.log(280.000000,2),math.log(268.000000,2),math.log(254.000000,2),math.log(252.000000,2),math.log(282.000000,2),math.log(273.750000,2),math.log(283.750000,2),math.log(282.687500,2),math.log(253.500000,2),math.log(289.343750,2),math.log(253.984375,2),math.log(249.585938,2),math.log(295.677734,2),math.log(360.595703,2),math.log(484.820312,2),math.log(685.880371,2),math.log(1113.765259,2),math.log(1975.298035,2),math.log(3714.011353,2)]
t_180 = [math.log(240.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(290.000000,2),math.log(279.000000,2),math.log(255.000000,2),math.log(250.250000,2),math.log(234.000000,2),math.log(259.812500,2),math.log(254.000000,2),math.log(262.843750,2),math.log(268.515625,2),math.log(247.710938,2),math.log(308.009766,2),math.log(361.100586,2),math.log(472.528809,2),math.log(668.921387,2),math.log(979.337158,2),math.log(1677.309998,2),math.log(3141.642944,2)]
t_181 = [math.log(240.000000,2),math.log(224.000000,2),math.log(240.000000,2),math.log(226.000000,2),math.log(249.000000,2),math.log(243.000000,2),math.log(257.000000,2),math.log(223.750000,2),math.log(223.187500,2),math.log(230.250000,2),math.log(262.093750,2),math.log(244.320312,2),math.log(280.601562,2),math.log(311.751953,2),math.log(368.403320,2),math.log(496.048340,2),math.log(811.469238,2),math.log(1375.368042,2),math.log(2448.895508,2),math.log(4593.853943,2)]
t_182 = [math.log(224.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(284.000000,2),math.log(258.000000,2),math.log(263.000000,2),math.log(270.750000,2),math.log(267.625000,2),math.log(232.687500,2),math.log(265.562500,2),math.log(247.390625,2),math.log(262.476562,2),math.log(284.867188,2),math.log(303.812500,2),math.log(397.714844,2),math.log(543.692383,2),math.log(813.166748,2),math.log(1334.146362,2),math.log(2353.635559,2),math.log(4571.233887,2)]
t_183 = [math.log(240.000000,2),math.log(232.000000,2),math.log(264.000000,2),math.log(252.000000,2),math.log(251.000000,2),math.log(285.500000,2),math.log(250.750000,2),math.log(227.000000,2),math.log(227.562500,2),math.log(253.843750,2),math.log(292.484375,2),math.log(298.546875,2),math.log(301.730469,2),math.log(318.328125,2),math.log(395.864258,2),math.log(488.070312,2),math.log(739.901367,2),math.log(1285.393066,2),math.log(2290.789001,2),math.log(4702.683411,2)]
t_184 = [math.log(288.000000,2),math.log(264.000000,2),math.log(220.000000,2),math.log(252.000000,2),math.log(212.000000,2),math.log(241.500000,2),math.log(252.500000,2),math.log(206.625000,2),math.log(196.437500,2),math.log(225.062500,2),math.log(219.500000,2),math.log(244.171875,2),math.log(294.265625,2),math.log(340.039062,2),math.log(469.518555,2),math.log(619.182129,2),math.log(958.399902,2),math.log(1680.506958,2),math.log(2992.393555,2),math.log(5441.260437,2)]
t_185 = [math.log(272.000000,2),math.log(256.000000,2),math.log(288.000000,2),math.log(272.000000,2),math.log(271.000000,2),math.log(267.500000,2),math.log(245.500000,2),math.log(227.375000,2),math.log(255.312500,2),math.log(269.843750,2),math.log(288.093750,2),math.log(328.242188,2),math.log(345.042969,2),math.log(426.949219,2),math.log(554.029297,2),math.log(793.787109,2),math.log(1099.097168,2),math.log(2009.550903,2),math.log(4010.529236,2),math.log(7764.115479,2)]
t_186 = [math.log(272.000000,2),math.log(288.000000,2),math.log(264.000000,2),math.log(294.000000,2),math.log(301.000000,2),math.log(265.000000,2),math.log(249.750000,2),math.log(261.125000,2),math.log(255.875000,2),math.log(245.593750,2),math.log(292.625000,2),math.log(320.429688,2),math.log(354.140625,2),math.log(443.992188,2),math.log(631.134766,2),math.log(1014.351074,2),math.log(2002.240967,2),math.log(3790.368042,2),math.log(7357.306152,2),math.log(14360.301270,2)]
t_187 = [math.log(256.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(245.000000,2),math.log(247.000000,2),math.log(250.000000,2),math.log(221.875000,2),math.log(227.062500,2),math.log(247.000000,2),math.log(297.656250,2),math.log(335.328125,2),math.log(328.726562,2),math.log(390.333984,2),math.log(544.601562,2),math.log(793.321777,2),math.log(1301.534912,2),math.log(2448.837280,2),math.log(4380.341125,2),math.log(8378.447205,2)]
t_188 = [math.log(256.000000,2),math.log(272.000000,2),math.log(296.000000,2),math.log(272.000000,2),math.log(258.000000,2),math.log(244.500000,2),math.log(252.250000,2),math.log(234.875000,2),math.log(241.250000,2),math.log(217.875000,2),math.log(237.453125,2),math.log(237.007812,2),math.log(248.808594,2),math.log(282.646484,2),math.log(316.002930,2),math.log(398.375000,2),math.log(730.146484,2),math.log(1089.668945,2),math.log(1788.601013,2),math.log(3467.149902,2)]
t_189 = [math.log(240.000000,2),math.log(224.000000,2),math.log(224.000000,2),math.log(220.000000,2),math.log(212.000000,2),math.log(207.500000,2),math.log(242.500000,2),math.log(247.625000,2),math.log(262.125000,2),math.log(246.718750,2),math.log(254.375000,2),math.log(260.148438,2),math.log(309.664062,2),math.log(347.796875,2),math.log(428.756836,2),math.log(708.537109,2),math.log(1168.057373,2),math.log(2106.860352,2),math.log(4004.243164,2),math.log(7631.550812,2)]
t_190 = [math.log(272.000000,2),math.log(288.000000,2),math.log(256.000000,2),math.log(266.000000,2),math.log(247.000000,2),math.log(270.000000,2),math.log(281.250000,2),math.log(264.750000,2),math.log(256.812500,2),math.log(257.531250,2),math.log(276.062500,2),math.log(237.523438,2),math.log(268.105469,2),math.log(312.482422,2),math.log(453.597656,2),math.log(710.072754,2),math.log(1238.654297,2),math.log(2269.241943,2),math.log(4300.667664,2),math.log(8000.378082,2)]
t_191 = [math.log(240.000000,2),math.log(208.000000,2),math.log(200.000000,2),math.log(220.000000,2),math.log(240.000000,2),math.log(260.500000,2),math.log(245.750000,2),math.log(229.250000,2),math.log(205.062500,2),math.log(232.937500,2),math.log(237.843750,2),math.log(268.179688,2),math.log(298.328125,2),math.log(370.222656,2),math.log(423.529297,2),math.log(524.355957,2),math.log(767.180664,2),math.log(1338.280518,2),math.log(2358.784729,2),math.log(4558.512939,2)]
t_192 = [math.log(240.000000,2),math.log(256.000000,2),math.log(264.000000,2),math.log(230.000000,2),math.log(246.000000,2),math.log(216.000000,2),math.log(215.750000,2),math.log(191.000000,2),math.log(251.062500,2),math.log(254.031250,2),math.log(238.593750,2),math.log(247.523438,2),math.log(271.308594,2),math.log(293.726562,2),math.log(286.190430,2),math.log(391.643555,2),math.log(521.879883,2),math.log(803.594360,2),math.log(1367.450806,2),math.log(2348.435089,2)]
t_193 = [math.log(272.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(246.000000,2),math.log(250.000000,2),math.log(241.000000,2),math.log(246.750000,2),math.log(243.500000,2),math.log(271.312500,2),math.log(273.062500,2),math.log(253.265625,2),math.log(274.789062,2),math.log(269.019531,2),math.log(285.353516,2),math.log(313.893555,2),math.log(340.526367,2),math.log(392.321045,2),math.log(583.955688,2),math.log(994.735107,2),math.log(1742.004120,2)]
t_194 = [math.log(240.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(262.000000,2),math.log(251.000000,2),math.log(250.000000,2),math.log(231.500000,2),math.log(237.000000,2),math.log(218.437500,2),math.log(216.718750,2),math.log(246.578125,2),math.log(244.234375,2),math.log(251.492188,2),math.log(249.728516,2),math.log(245.533203,2),math.log(328.712402,2),math.log(424.506104,2),math.log(602.381836,2),math.log(947.859558,2),math.log(1659.104492,2)]
t_195 = [math.log(336.000000,2),math.log(272.000000,2),math.log(252.000000,2),math.log(262.000000,2),math.log(279.000000,2),math.log(221.000000,2),math.log(219.250000,2),math.log(227.125000,2),math.log(233.312500,2),math.log(268.937500,2),math.log(222.500000,2),math.log(286.703125,2),math.log(276.058594,2),math.log(316.015625,2),math.log(363.354492,2),math.log(457.660156,2),math.log(607.188477,2),math.log(943.734741,2),math.log(1577.066956,2),math.log(3057.984070,2)]
t_196 = [math.log(224.000000,2),math.log(224.000000,2),math.log(216.000000,2),math.log(252.000000,2),math.log(260.000000,2),math.log(221.500000,2),math.log(255.000000,2),math.log(301.250000,2),math.log(275.750000,2),math.log(253.000000,2),math.log(250.796875,2),math.log(234.062500,2),math.log(243.062500,2),math.log(243.992188,2),math.log(291.721680,2),math.log(403.287109,2),math.log(534.786865,2),math.log(806.705078,2),math.log(1267.723267,2),math.log(2062.716492,2)]
t_197 = [math.log(272.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(286.000000,2),math.log(258.000000,2),math.log(260.500000,2),math.log(263.750000,2),math.log(260.000000,2),math.log(241.625000,2),math.log(227.062500,2),math.log(235.343750,2),math.log(249.742188,2),math.log(267.488281,2),math.log(261.445312,2),math.log(285.324219,2),math.log(342.470703,2),math.log(474.523682,2),math.log(741.126343,2),math.log(1283.477051,2),math.log(2404.008575,2)]
t_198 = [math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(242.000000,2),math.log(265.000000,2),math.log(264.000000,2),math.log(236.500000,2),math.log(234.250000,2),math.log(225.062500,2),math.log(215.156250,2),math.log(254.093750,2),math.log(278.789062,2),math.log(261.484375,2),math.log(282.781250,2),math.log(314.142578,2),math.log(416.244629,2),math.log(523.195557,2),math.log(774.037842,2),math.log(1241.793152,2),math.log(2217.450104,2)]
t_199 = [math.log(256.000000,2),math.log(224.000000,2),math.log(236.000000,2),math.log(258.000000,2),math.log(245.000000,2),math.log(265.500000,2),math.log(249.750000,2),math.log(258.250000,2),math.log(230.750000,2),math.log(259.000000,2),math.log(268.984375,2),math.log(301.265625,2),math.log(297.355469,2),math.log(354.361328,2),math.log(383.411133,2),math.log(491.564941,2),math.log(797.129639,2),math.log(1304.567139,2),math.log(2429.506531,2),math.log(4532.140839,2)]
t_200 = [math.log(304.000000,2),math.log(272.000000,2),math.log(248.000000,2),math.log(244.000000,2),math.log(251.000000,2),math.log(277.500000,2),math.log(260.500000,2),math.log(281.375000,2),math.log(303.375000,2),math.log(285.625000,2),math.log(273.437500,2),math.log(301.796875,2),math.log(341.515625,2),math.log(327.517578,2),math.log(314.316406,2),math.log(381.374512,2),math.log(526.137207,2),math.log(767.142578,2),math.log(1220.467773,2),math.log(2212.226715,2)]
t_201 = [math.log(288.000000,2),math.log(248.000000,2),math.log(248.000000,2),math.log(272.000000,2),math.log(281.000000,2),math.log(283.500000,2),math.log(280.000000,2),math.log(271.000000,2),math.log(245.062500,2),math.log(239.375000,2),math.log(271.953125,2),math.log(271.515625,2),math.log(332.796875,2),math.log(288.017578,2),math.log(328.964844,2),math.log(339.809570,2),math.log(477.118652,2),math.log(826.359131,2),math.log(1394.005371,2),math.log(2584.319641,2)]
t_202 = [math.log(288.000000,2),math.log(240.000000,2),math.log(232.000000,2),math.log(230.000000,2),math.log(260.000000,2),math.log(246.500000,2),math.log(274.250000,2),math.log(265.250000,2),math.log(271.937500,2),math.log(260.312500,2),math.log(285.312500,2),math.log(320.976562,2),math.log(382.238281,2),math.log(452.478516,2),math.log(628.586914,2),math.log(1016.956055,2),math.log(1731.702881,2),math.log(3264.062744,2),math.log(6270.809937,2),math.log(12210.726105,2)]
t_203 = [math.log(240.000000,2),math.log(264.000000,2),math.log(256.000000,2),math.log(262.000000,2),math.log(268.000000,2),math.log(312.500000,2),math.log(265.250000,2),math.log(264.875000,2),math.log(287.125000,2),math.log(263.687500,2),math.log(246.484375,2),math.log(268.312500,2),math.log(312.699219,2),math.log(327.746094,2),math.log(389.629883,2),math.log(471.074707,2),math.log(670.482422,2),math.log(1183.290405,2),math.log(2102.251038,2),math.log(3917.102539,2)]
t_204 = [math.log(320.000000,2),math.log(296.000000,2),math.log(348.000000,2),math.log(304.000000,2),math.log(249.000000,2),math.log(258.500000,2),math.log(248.500000,2),math.log(224.375000,2),math.log(266.687500,2),math.log(261.812500,2),math.log(247.546875,2),math.log(255.171875,2),math.log(268.089844,2),math.log(328.375000,2),math.log(333.107422,2),math.log(476.675293,2),math.log(638.818848,2),math.log(1012.448242,2),math.log(1587.021423,2),math.log(2858.043488,2)]
t_205 = [math.log(256.000000,2),math.log(232.000000,2),math.log(280.000000,2),math.log(246.000000,2),math.log(252.000000,2),math.log(231.500000,2),math.log(260.500000,2),math.log(227.500000,2),math.log(239.750000,2),math.log(270.281250,2),math.log(270.171875,2),math.log(290.148438,2),math.log(284.835938,2),math.log(368.376953,2),math.log(480.062500,2),math.log(557.917480,2),math.log(812.247559,2),math.log(1474.737793,2),math.log(2767.102234,2),math.log(5044.320862,2)]
t_206 = [math.log(240.000000,2),math.log(272.000000,2),math.log(264.000000,2),math.log(222.000000,2),math.log(238.000000,2),math.log(230.000000,2),math.log(250.000000,2),math.log(298.875000,2),math.log(274.562500,2),math.log(246.562500,2),math.log(277.984375,2),math.log(283.992188,2),math.log(286.226562,2),math.log(317.203125,2),math.log(361.644531,2),math.log(506.525879,2),math.log(724.247559,2),math.log(1245.275513,2),math.log(2228.817566,2),math.log(4318.614227,2)]
t_207 = [math.log(368.000000,2),math.log(296.000000,2),math.log(280.000000,2),math.log(238.000000,2),math.log(238.000000,2),math.log(187.000000,2),math.log(229.750000,2),math.log(252.500000,2),math.log(238.687500,2),math.log(263.343750,2),math.log(263.984375,2),math.log(302.250000,2),math.log(288.125000,2),math.log(294.101562,2),math.log(339.413086,2),math.log(382.230469,2),math.log(575.448242,2),math.log(988.499878,2),math.log(1743.930786,2),math.log(3430.520599,2)]
t_208 = [math.log(256.000000,2),math.log(256.000000,2),math.log(248.000000,2),math.log(256.000000,2),math.log(265.000000,2),math.log(268.000000,2),math.log(258.500000,2),math.log(273.625000,2),math.log(295.187500,2),math.log(281.218750,2),math.log(260.046875,2),math.log(293.781250,2),math.log(310.160156,2),math.log(329.490234,2),math.log(378.664062,2),math.log(506.040039,2),math.log(769.543945,2),math.log(1219.567627,2),math.log(2223.298218,2),math.log(3995.478638,2)]
t_209 = [math.log(240.000000,2),math.log(248.000000,2),math.log(292.000000,2),math.log(294.000000,2),math.log(272.000000,2),math.log(268.000000,2),math.log(250.250000,2),math.log(249.000000,2),math.log(239.312500,2),math.log(225.375000,2),math.log(243.343750,2),math.log(273.718750,2),math.log(273.125000,2),math.log(305.054688,2),math.log(340.978516,2),math.log(415.079590,2),math.log(497.438232,2),math.log(778.446289,2),math.log(1235.252441,2),math.log(2081.320923,2)]
t_210 = [math.log(288.000000,2),math.log(272.000000,2),math.log(276.000000,2),math.log(248.000000,2),math.log(280.000000,2),math.log(253.000000,2),math.log(251.750000,2),math.log(236.000000,2),math.log(237.187500,2),math.log(221.062500,2),math.log(246.859375,2),math.log(250.882812,2),math.log(258.562500,2),math.log(281.996094,2),math.log(345.596680,2),math.log(405.518555,2),math.log(513.989014,2),math.log(816.346436,2),math.log(1359.758789,2),math.log(2568.587433,2)]
t_211 = [math.log(224.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(250.000000,2),math.log(257.000000,2),math.log(255.500000,2),math.log(300.000000,2),math.log(321.625000,2),math.log(337.937500,2),math.log(248.750000,2),math.log(274.656250,2),math.log(266.757812,2),math.log(246.230469,2),math.log(304.796875,2),math.log(374.375000,2),math.log(553.656738,2),math.log(897.374756,2),math.log(1513.303223,2),math.log(2800.133179,2),math.log(5451.130646,2)]
t_212 = [math.log(240.000000,2),math.log(264.000000,2),math.log(260.000000,2),math.log(254.000000,2),math.log(324.000000,2),math.log(292.000000,2),math.log(257.750000,2),math.log(289.250000,2),math.log(277.562500,2),math.log(257.781250,2),math.log(265.875000,2),math.log(255.625000,2),math.log(243.546875,2),math.log(283.615234,2),math.log(352.751953,2),math.log(485.822266,2),math.log(760.044434,2),math.log(1290.197754,2),math.log(2416.376526,2),math.log(4526.184540,2)]
t_213 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(212.000000,2),math.log(223.000000,2),math.log(246.000000,2),math.log(234.000000,2),math.log(255.250000,2),math.log(273.125000,2),math.log(285.906250,2),math.log(257.953125,2),math.log(260.187500,2),math.log(266.554688,2),math.log(307.945312,2),math.log(367.987305,2),math.log(476.578125,2),math.log(721.371094,2),math.log(1081.691772,2),math.log(1950.868225,2),math.log(3607.900543,2)]
t_214 = [math.log(240.000000,2),math.log(248.000000,2),math.log(264.000000,2),math.log(250.000000,2),math.log(260.000000,2),math.log(280.000000,2),math.log(285.500000,2),math.log(261.000000,2),math.log(254.500000,2),math.log(246.875000,2),math.log(253.875000,2),math.log(300.898438,2),math.log(329.339844,2),math.log(340.097656,2),math.log(415.283203,2),math.log(573.249023,2),math.log(803.269043,2),math.log(1225.448364,2),math.log(2217.294617,2),math.log(4134.860504,2)]
t_215 = [math.log(288.000000,2),math.log(288.000000,2),math.log(300.000000,2),math.log(260.000000,2),math.log(265.000000,2),math.log(296.500000,2),math.log(264.250000,2),math.log(280.750000,2),math.log(259.562500,2),math.log(262.218750,2),math.log(254.906250,2),math.log(261.460938,2),math.log(304.714844,2),math.log(380.144531,2),math.log(537.804688,2),math.log(753.662598,2),math.log(1206.034912,2),math.log(1914.560669,2),math.log(3755.437073,2),math.log(7429.110016,2)]
t_216 = [math.log(240.000000,2),math.log(216.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(257.000000,2),math.log(263.000000,2),math.log(225.000000,2),math.log(235.750000,2),math.log(283.750000,2),math.log(262.718750,2),math.log(253.078125,2),math.log(265.773438,2),math.log(273.445312,2),math.log(299.925781,2),math.log(388.159180,2),math.log(469.714844,2),math.log(630.389404,2),math.log(845.030884,2),math.log(1298.903870,2),math.log(2332.439697,2)]
t_217 = [math.log(272.000000,2),math.log(248.000000,2),math.log(220.000000,2),math.log(240.000000,2),math.log(210.000000,2),math.log(209.000000,2),math.log(226.500000,2),math.log(261.500000,2),math.log(274.187500,2),math.log(234.656250,2),math.log(239.015625,2),math.log(254.929688,2),math.log(260.832031,2),math.log(294.798828,2),math.log(294.138672,2),math.log(411.770996,2),math.log(626.577881,2),math.log(964.480835,2),math.log(1600.454712,2),math.log(2849.451416,2)]
t_218 = [math.log(240.000000,2),math.log(232.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(270.000000,2),math.log(289.000000,2),math.log(260.500000,2),math.log(240.750000,2),math.log(263.312500,2),math.log(256.625000,2),math.log(279.593750,2),math.log(277.867188,2),math.log(288.738281,2),math.log(402.103516,2),math.log(527.182617,2),math.log(764.799805,2),math.log(1377.463379,2),math.log(2531.726807,2),math.log(4891.461914,2),math.log(9489.719666,2)]
t_219 = [math.log(240.000000,2),math.log(224.000000,2),math.log(248.000000,2),math.log(260.000000,2),math.log(285.000000,2),math.log(258.000000,2),math.log(235.750000,2),math.log(225.625000,2),math.log(254.812500,2),math.log(264.125000,2),math.log(282.625000,2),math.log(307.914062,2),math.log(325.550781,2),math.log(332.736328,2),math.log(405.199219,2),math.log(546.740723,2),math.log(870.476807,2),math.log(1491.049438,2),math.log(2774.749573,2),math.log(5197.486603,2)]
t_220 = [math.log(320.000000,2),math.log(320.000000,2),math.log(320.000000,2),math.log(314.000000,2),math.log(284.000000,2),math.log(231.000000,2),math.log(228.250000,2),math.log(247.250000,2),math.log(273.937500,2),math.log(271.031250,2),math.log(253.046875,2),math.log(261.171875,2),math.log(240.679688,2),math.log(285.652344,2),math.log(364.430664,2),math.log(502.416016,2),math.log(820.242188,2),math.log(1365.147461,2),math.log(2400.903259,2),math.log(4545.031372,2)]
t_221 = [math.log(288.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(238.000000,2),math.log(237.000000,2),math.log(271.500000,2),math.log(228.750000,2),math.log(230.875000,2),math.log(273.375000,2),math.log(302.968750,2),math.log(290.421875,2),math.log(265.414062,2),math.log(306.000000,2),math.log(329.910156,2),math.log(398.002930,2),math.log(576.231445,2),math.log(921.848877,2),math.log(1473.862671,2),math.log(2650.479004,2),math.log(5095.896332,2)]
t_222 = [math.log(256.000000,2),math.log(256.000000,2),math.log(236.000000,2),math.log(238.000000,2),math.log(226.000000,2),math.log(235.500000,2),math.log(263.750000,2),math.log(282.375000,2),math.log(300.750000,2),math.log(338.843750,2),math.log(330.968750,2),math.log(312.265625,2),math.log(322.035156,2),math.log(399.794922,2),math.log(454.265625,2),math.log(618.675293,2),math.log(1009.627686,2),math.log(1778.189331,2),math.log(3139.110474,2),math.log(6034.195251,2)]
t_223 = [math.log(256.000000,2),math.log(256.000000,2),math.log(220.000000,2),math.log(254.000000,2),math.log(262.000000,2),math.log(244.500000,2),math.log(235.750000,2),math.log(247.000000,2),math.log(243.937500,2),math.log(277.343750,2),math.log(299.234375,2),math.log(277.351562,2),math.log(268.722656,2),math.log(336.501953,2),math.log(427.319336,2),math.log(530.727051,2),math.log(730.801025,2),math.log(1163.277100,2),math.log(2189.045532,2),math.log(4232.122192,2)]
t_224 = [math.log(240.000000,2),math.log(248.000000,2),math.log(216.000000,2),math.log(248.000000,2),math.log(328.000000,2),math.log(265.500000,2),math.log(252.000000,2),math.log(239.625000,2),math.log(257.437500,2),math.log(283.593750,2),math.log(283.281250,2),math.log(277.140625,2),math.log(275.476562,2),math.log(328.718750,2),math.log(363.162109,2),math.log(479.122559,2),math.log(715.976807,2),math.log(1295.853394,2),math.log(2257.347717,2),math.log(4333.345276,2)]
t_225 = [math.log(272.000000,2),math.log(232.000000,2),math.log(256.000000,2),math.log(274.000000,2),math.log(276.000000,2),math.log(221.500000,2),math.log(251.750000,2),math.log(258.500000,2),math.log(274.812500,2),math.log(228.500000,2),math.log(246.218750,2),math.log(248.617188,2),math.log(290.402344,2),math.log(294.052734,2),math.log(351.851562,2),math.log(482.061035,2),math.log(692.281250,2),math.log(1071.545532,2),math.log(1746.451111,2),math.log(3276.222351,2)]
t_226 = [math.log(256.000000,2),math.log(256.000000,2),math.log(240.000000,2),math.log(240.000000,2),math.log(229.000000,2),math.log(234.000000,2),math.log(254.500000,2),math.log(263.500000,2),math.log(278.750000,2),math.log(303.843750,2),math.log(263.531250,2),math.log(267.351562,2),math.log(302.535156,2),math.log(333.626953,2),math.log(343.302734,2),math.log(449.648926,2),math.log(619.765625,2),math.log(949.547607,2),math.log(1468.785156,2),math.log(2532.076385,2)]
t_227 = [math.log(256.000000,2),math.log(280.000000,2),math.log(296.000000,2),math.log(278.000000,2),math.log(258.000000,2),math.log(291.000000,2),math.log(262.250000,2),math.log(275.125000,2),math.log(283.437500,2),math.log(265.031250,2),math.log(288.453125,2),math.log(281.976562,2),math.log(291.789062,2),math.log(302.677734,2),math.log(365.027344,2),math.log(543.524902,2),math.log(825.347412,2),math.log(1516.006592,2),math.log(2799.236450,2),math.log(5714.157166,2)]
t_228 = [math.log(272.000000,2),math.log(256.000000,2),math.log(224.000000,2),math.log(228.000000,2),math.log(264.000000,2),math.log(225.500000,2),math.log(243.750000,2),math.log(242.250000,2),math.log(240.750000,2),math.log(275.906250,2),math.log(309.093750,2),math.log(293.945312,2),math.log(323.152344,2),math.log(339.945312,2),math.log(388.394531,2),math.log(579.874023,2),math.log(892.659912,2),math.log(1436.723633,2),math.log(2512.391907,2),math.log(4733.396057,2)]
t_229 = [math.log(288.000000,2),math.log(288.000000,2),math.log(264.000000,2),math.log(268.000000,2),math.log(248.000000,2),math.log(246.500000,2),math.log(262.500000,2),math.log(272.625000,2),math.log(256.187500,2),math.log(267.062500,2),math.log(249.281250,2),math.log(259.703125,2),math.log(268.628906,2),math.log(297.462891,2),math.log(364.047852,2),math.log(477.519531,2),math.log(732.721191,2),math.log(1187.771973,2),math.log(2106.167969,2),math.log(3727.853455,2)]
t_230 = [math.log(224.000000,2),math.log(248.000000,2),math.log(284.000000,2),math.log(266.000000,2),math.log(248.000000,2),math.log(291.500000,2),math.log(275.250000,2),math.log(239.375000,2),math.log(287.500000,2),math.log(269.750000,2),math.log(272.140625,2),math.log(272.296875,2),math.log(272.773438,2),math.log(326.398438,2),math.log(404.478516,2),math.log(572.323730,2),math.log(901.449707,2),math.log(1381.859985,2),math.log(2420.385742,2),math.log(4339.032257,2)]
t_231 = [math.log(288.000000,2),math.log(256.000000,2),math.log(276.000000,2),math.log(244.000000,2),math.log(232.000000,2),math.log(259.500000,2),math.log(266.000000,2),math.log(263.000000,2),math.log(261.062500,2),math.log(235.375000,2),math.log(260.937500,2),math.log(285.765625,2),math.log(366.582031,2),math.log(429.771484,2),math.log(453.317383,2),math.log(634.061523,2),math.log(1176.030762,2),math.log(2057.760010,2),math.log(4017.489136,2),math.log(7469.237885,2)]
t_232 = [math.log(256.000000,2),math.log(256.000000,2),math.log(252.000000,2),math.log(242.000000,2),math.log(272.000000,2),math.log(268.500000,2),math.log(275.750000,2),math.log(252.750000,2),math.log(252.500000,2),math.log(266.656250,2),math.log(257.468750,2),math.log(264.750000,2),math.log(278.410156,2),math.log(301.685547,2),math.log(355.460938,2),math.log(430.744629,2),math.log(641.701172,2),math.log(926.227295,2),math.log(1530.318787,2),math.log(2960.322113,2)]
t_233 = [math.log(288.000000,2),math.log(280.000000,2),math.log(256.000000,2),math.log(246.000000,2),math.log(231.000000,2),math.log(242.000000,2),math.log(269.250000,2),math.log(273.875000,2),math.log(250.312500,2),math.log(209.843750,2),math.log(248.125000,2),math.log(246.007812,2),math.log(242.964844,2),math.log(293.398438,2),math.log(376.439453,2),math.log(468.091309,2),math.log(639.336426,2),math.log(1052.983643,2),math.log(1931.583435,2),math.log(3711.090698,2)]
t_234 = [math.log(240.000000,2),math.log(264.000000,2),math.log(228.000000,2),math.log(242.000000,2),math.log(266.000000,2),math.log(251.500000,2),math.log(255.500000,2),math.log(231.375000,2),math.log(253.625000,2),math.log(262.562500,2),math.log(263.218750,2),math.log(341.710938,2),math.log(354.261719,2),math.log(417.875000,2),math.log(581.883789,2),math.log(893.637695,2),math.log(1622.518066,2),math.log(3222.952637,2),math.log(6064.507141,2),math.log(11794.239258,2)]
t_235 = [math.log(256.000000,2),math.log(256.000000,2),math.log(256.000000,2),math.log(262.000000,2),math.log(287.000000,2),math.log(290.000000,2),math.log(277.500000,2),math.log(281.375000,2),math.log(257.187500,2),math.log(279.875000,2),math.log(293.671875,2),math.log(313.953125,2),math.log(303.484375,2),math.log(373.820312,2),math.log(485.549805,2),math.log(668.141113,2),math.log(993.926514,2),math.log(1826.542480,2),math.log(3357.634094,2),math.log(6357.477142,2)]
t_236 = [math.log(256.000000,2),math.log(272.000000,2),math.log(256.000000,2),math.log(262.000000,2),math.log(267.000000,2),math.log(304.000000,2),math.log(250.500000,2),math.log(241.875000,2),math.log(239.875000,2),math.log(242.593750,2),math.log(254.500000,2),math.log(271.609375,2),math.log(262.210938,2),math.log(325.716797,2),math.log(381.216797,2),math.log(531.059570,2),math.log(823.008545,2),math.log(1375.584961,2),math.log(2534.764282,2),math.log(4896.745514,2)]
t_237 = [math.log(256.000000,2),math.log(232.000000,2),math.log(240.000000,2),math.log(238.000000,2),math.log(237.000000,2),math.log(226.000000,2),math.log(209.750000,2),math.log(225.500000,2),math.log(243.937500,2),math.log(255.687500,2),math.log(284.890625,2),math.log(278.132812,2),math.log(303.062500,2),math.log(352.621094,2),math.log(501.832031,2),math.log(720.900879,2),math.log(1068.984131,2),math.log(1760.792114,2),math.log(3273.655090,2),math.log(6428.102692,2)]
t_238 = [math.log(240.000000,2),math.log(216.000000,2),math.log(216.000000,2),math.log(236.000000,2),math.log(239.000000,2),math.log(246.000000,2),math.log(256.250000,2),math.log(253.375000,2),math.log(242.750000,2),math.log(238.218750,2),math.log(284.937500,2),math.log(276.414062,2),math.log(300.695312,2),math.log(352.980469,2),math.log(406.904297,2),math.log(564.453125,2),math.log(874.091064,2),math.log(1542.962280,2),math.log(2829.348389,2),math.log(5289.318878,2)]
t_239 = [math.log(256.000000,2),math.log(280.000000,2),math.log(288.000000,2),math.log(250.000000,2),math.log(230.000000,2),math.log(257.500000,2),math.log(269.000000,2),math.log(254.125000,2),math.log(254.437500,2),math.log(313.656250,2),math.log(307.015625,2),math.log(266.429688,2),math.log(301.605469,2),math.log(322.269531,2),math.log(341.474609,2),math.log(457.291504,2),math.log(718.845459,2),math.log(1219.326416,2),math.log(2198.283752,2),math.log(4270.002625,2)]
t_240 = [math.log(256.000000,2),math.log(248.000000,2),math.log(252.000000,2),math.log(278.000000,2),math.log(260.000000,2),math.log(257.000000,2),math.log(268.000000,2),math.log(255.125000,2),math.log(258.625000,2),math.log(256.187500,2),math.log(266.593750,2),math.log(242.335938,2),math.log(250.285156,2),math.log(318.423828,2),math.log(332.061523,2),math.log(421.304688,2),math.log(562.757812,2),math.log(908.620728,2),math.log(1394.331238,2),math.log(2507.989532,2)]
t_241 = [math.log(240.000000,2),math.log(240.000000,2),math.log(260.000000,2),math.log(264.000000,2),math.log(250.000000,2),math.log(269.000000,2),math.log(303.250000,2),math.log(250.375000,2),math.log(264.437500,2),math.log(226.656250,2),math.log(212.703125,2),math.log(214.328125,2),math.log(220.835938,2),math.log(254.501953,2),math.log(242.655273,2),math.log(307.338867,2),math.log(380.533203,2),math.log(504.440063,2),math.log(767.801147,2),math.log(1332.905487,2)]
t_242 = [math.log(240.000000,2),math.log(272.000000,2),math.log(272.000000,2),math.log(294.000000,2),math.log(268.000000,2),math.log(273.000000,2),math.log(262.750000,2),math.log(241.000000,2),math.log(247.687500,2),math.log(229.031250,2),math.log(222.531250,2),math.log(272.945312,2),math.log(309.343750,2),math.log(322.707031,2),math.log(319.119141,2),math.log(372.056641,2),math.log(394.487793,2),math.log(598.261963,2),math.log(977.413208,2),math.log(1800.387665,2)]
t_243 = [math.log(240.000000,2),math.log(224.000000,2),math.log(200.000000,2),math.log(232.000000,2),math.log(231.000000,2),math.log(225.000000,2),math.log(263.250000,2),math.log(257.250000,2),math.log(241.250000,2),math.log(246.875000,2),math.log(263.656250,2),math.log(293.546875,2),math.log(309.140625,2),math.log(308.193359,2),math.log(336.464844,2),math.log(472.219727,2),math.log(686.434570,2),math.log(1176.141968,2),math.log(2004.928833,2),math.log(3804.061157,2)]
t_244 = [math.log(240.000000,2),math.log(256.000000,2),math.log(232.000000,2),math.log(252.000000,2),math.log(248.000000,2),math.log(232.000000,2),math.log(217.750000,2),math.log(226.625000,2),math.log(211.937500,2),math.log(262.406250,2),math.log(271.078125,2),math.log(249.437500,2),math.log(231.304688,2),math.log(240.810547,2),math.log(296.412109,2),math.log(393.298340,2),math.log(563.142578,2),math.log(930.662720,2),math.log(1454.355103,2),math.log(2641.441010,2)]
t_245 = [math.log(240.000000,2),math.log(216.000000,2),math.log(244.000000,2),math.log(226.000000,2),math.log(233.000000,2),math.log(235.500000,2),math.log(249.250000,2),math.log(275.125000,2),math.log(289.750000,2),math.log(299.531250,2),math.log(283.015625,2),math.log(286.710938,2),math.log(323.320312,2),math.log(311.787109,2),math.log(314.638672,2),math.log(382.597168,2),math.log(485.402344,2),math.log(659.269043,2),math.log(996.664429,2),math.log(1700.985840,2)]
t_246 = [math.log(240.000000,2),math.log(216.000000,2),math.log(236.000000,2),math.log(212.000000,2),math.log(222.000000,2),math.log(236.000000,2),math.log(252.000000,2),math.log(236.750000,2),math.log(253.125000,2),math.log(234.781250,2),math.log(255.359375,2),math.log(284.773438,2),math.log(304.113281,2),math.log(291.306641,2),math.log(337.706055,2),math.log(378.983887,2),math.log(526.241943,2),math.log(782.919800,2),math.log(1219.067688,2),math.log(2314.726379,2)]
t_247 = [math.log(240.000000,2),math.log(248.000000,2),math.log(240.000000,2),math.log(252.000000,2),math.log(261.000000,2),math.log(249.500000,2),math.log(245.750000,2),math.log(294.875000,2),math.log(284.437500,2),math.log(248.937500,2),math.log(256.046875,2),math.log(263.968750,2),math.log(277.343750,2),math.log(331.251953,2),math.log(385.886719,2),math.log(506.554199,2),math.log(718.347412,2),math.log(1094.756226,2),math.log(1787.131470,2),math.log(3189.590759,2)]
t_248 = [math.log(240.000000,2),math.log(248.000000,2),math.log(224.000000,2),math.log(208.000000,2),math.log(234.000000,2),math.log(273.500000,2),math.log(243.000000,2),math.log(236.625000,2),math.log(254.125000,2),math.log(246.937500,2),math.log(278.546875,2),math.log(276.039062,2),math.log(325.796875,2),math.log(332.548828,2),math.log(356.266602,2),math.log(441.993652,2),math.log(619.305664,2),math.log(1138.799194,2),math.log(2001.989319,2),math.log(3746.423065,2)]
t_249 = [math.log(256.000000,2),math.log(232.000000,2),math.log(220.000000,2),math.log(218.000000,2),math.log(250.000000,2),math.log(233.000000,2),math.log(269.250000,2),math.log(311.250000,2),math.log(276.062500,2),math.log(238.656250,2),math.log(247.296875,2),math.log(239.468750,2),math.log(258.839844,2),math.log(323.462891,2),math.log(374.583984,2),math.log(426.752441,2),math.log(561.612061,2),math.log(941.191650,2),math.log(1567.111816,2),math.log(2884.812256,2)]
t_250 = [math.log(272.000000,2),math.log(288.000000,2),math.log(280.000000,2),math.log(280.000000,2),math.log(276.000000,2),math.log(278.000000,2),math.log(229.250000,2),math.log(213.375000,2),math.log(237.375000,2),math.log(245.375000,2),math.log(273.140625,2),math.log(301.164062,2),math.log(335.050781,2),math.log(406.492188,2),math.log(562.574219,2),math.log(875.632324,2),math.log(1577.592041,2),math.log(2902.228027,2),math.log(5662.818481,2),math.log(11235.923035,2)]
t_251 = [math.log(240.000000,2),math.log(232.000000,2),math.log(244.000000,2),math.log(228.000000,2),math.log(231.000000,2),math.log(230.500000,2),math.log(267.000000,2),math.log(235.750000,2),math.log(292.250000,2),math.log(259.843750,2),math.log(235.937500,2),math.log(257.585938,2),math.log(277.000000,2),math.log(285.492188,2),math.log(331.672852,2),math.log(427.292969,2),math.log(647.660400,2),math.log(1067.502808,2),math.log(1974.642334,2),math.log(3680.656647,2)]
t_252 = [math.log(256.000000,2),math.log(264.000000,2),math.log(272.000000,2),math.log(292.000000,2),math.log(239.000000,2),math.log(254.000000,2),math.log(230.500000,2),math.log(268.500000,2),math.log(278.250000,2),math.log(288.531250,2),math.log(256.968750,2),math.log(290.382812,2),math.log(265.421875,2),math.log(286.117188,2),math.log(322.422852,2),math.log(328.073730,2),math.log(496.241211,2),math.log(691.461060,2),math.log(1242.592896,2),math.log(2202.232513,2)]
t_253 = [math.log(256.000000,2),math.log(216.000000,2),math.log(232.000000,2),math.log(236.000000,2),math.log(245.000000,2),math.log(254.500000,2),math.log(225.250000,2),math.log(225.875000,2),math.log(265.625000,2),math.log(237.656250,2),math.log(255.296875,2),math.log(275.367188,2),math.log(290.925781,2),math.log(315.832031,2),math.log(449.968750,2),math.log(586.776367,2),math.log(823.354004,2),math.log(1413.945312,2),math.log(2692.325134,2),math.log(5041.485016,2)]
t_254 = [math.log(272.000000,2),math.log(304.000000,2),math.log(252.000000,2),math.log(252.000000,2),math.log(273.000000,2),math.log(280.500000,2),math.log(254.500000,2),math.log(235.250000,2),math.log(234.562500,2),math.log(222.156250,2),math.log(254.718750,2),math.log(234.554688,2),math.log(259.121094,2),math.log(275.125000,2),math.log(386.370117,2),math.log(510.374512,2),math.log(870.905762,2),math.log(1441.156372,2),math.log(2576.558289,2),math.log(5130.218353,2)]
t_255 = [math.log(272.000000,2),math.log(232.000000,2),math.log(272.000000,2),math.log(246.000000,2),math.log(229.000000,2),math.log(238.500000,2),math.log(266.000000,2),math.log(286.500000,2),math.log(295.875000,2),math.log(305.031250,2),math.log(310.500000,2),math.log(297.882812,2),math.log(321.011719,2),math.log(414.087891,2),math.log(536.256836,2),math.log(805.199707,2),math.log(1334.812256,2),math.log(2288.623901,2),math.log(4342.355225,2),math.log(8381.482056,2)]




#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 255*(1-32/16777216) + 32*0.00025617
sigma_32 = math.sqrt((2.0/255)*(255*(1-32/16777216)+32*0.00025617)**2)


# sample sizeL 64
mu_64 = 255*(1-64/16777216) + 64*0.00025617
sigma_64 = math.sqrt((2.0/255)*(255*(1-64/16777216)+64*0.00025617)**2)


# sample sizeL 128
mu_128 = 255*(1-128/16777216) + 128*0.00025617
sigma_128 = math.sqrt((2.0/255)*(255*(1-128/16777216)+128*0.00025617)**2)


# sample sizeL 256
mu_256 = 255*(1-256/16777216) + 256*0.00025617
sigma_256 = math.sqrt((2.0/255)*(255*(1-256/16777216)+256*0.00025617)**2)


# sample sizeL 512
mu_512 = 255*(1-512/16777216) + 512*0.00025617
sigma_512 = math.sqrt((2.0/255)*(255*(1-512/16777216)+512*0.00025617)**2)


# sample sizeL 1024
mu_1024 = 255*(1-1024/16777216) + 1024*0.00025617
sigma_1024 = math.sqrt((2.0/255)*(255*(1-1024/16777216)+1024*0.00025617)**2)


# sample sizeL 2048
mu_2048 = 255*(1-2048/16777216) + 2048*0.00025617
sigma_2048 = math.sqrt((2.0/255)*(255*(1-2048/16777216)+2048*0.00025617)**2)


# sample sizeL 4096
mu_4096 = 255*(1-4096/16777216) + 4096*0.00025617
sigma_4096 = math.sqrt((2.0/255)*(255*(1-4096/16777216)+4096*0.00025617)**2)


# sample sizeL 8192
mu_8192 = 255*(1-8192/16777216) + 8192*0.00025617
sigma_8192 = math.sqrt((2.0/255)*(255*(1-8192/16777216)+8192*0.00025617)**2)


# sample sizeL 16384
mu_16384 = 255*(1-16384/16777216) + 16384*0.00025617
sigma_16384 = math.sqrt((2.0/255)*(255*(1-16384/16777216)+16384*0.00025617)**2)


# sample sizeL 32768
mu_32768 = 255*(1-32768/16777216) + 32768*0.00025617
sigma_32768 = math.sqrt((2.0/255)*(255*(1-32768/16777216)+32768*0.00025617)**2)


# sample sizeL 65536
mu_65536 = 255*(1-65536/16777216) + 65536*0.00025617
sigma_65536 = math.sqrt((2.0/255)*(255*(1-65536/16777216)+65536*0.00025617)**2)


# sample sizeL 131072
mu_131072 = 255*(1-131072/16777216) + 131072*0.00025617
sigma_131072 = math.sqrt((2.0/255)*(255*(1-131072/16777216)+131072*0.00025617)**2)


# sample sizeL 262144
mu_262144 = 255*(1-262144/16777216) + 262144*0.00025617
sigma_262144 = math.sqrt((2.0/255)*(255*(1-262144/16777216)+262144*0.00025617)**2)


# sample sizeL 524288
mu_524288 = 255*(1-524288/16777216) + 524288*0.00025617
sigma_524288 = math.sqrt((2.0/255)*(255*(1-524288/16777216)+524288*0.00025617)**2)


# sample sizeL 1048576
mu_1048576 = 255*(1-1048576/16777216) + 1048576*0.00025617
sigma_1048576 = math.sqrt((2.0/255)*(255*(1-1048576/16777216)+1048576*0.00025617)**2)


# sample sizeL 2097152
mu_2097152 = 255*(1-2097152/16777216) + 2097152*0.00025617
sigma_2097152 = math.sqrt((2.0/255)*(255*(1-2097152/16777216)+2097152*0.00025617)**2)


# sample sizeL 4194304
mu_4194304 = 255*(1-4194304/16777216) + 4194304*0.00025617
sigma_4194304 = math.sqrt((2.0/255)*(255*(1-4194304/16777216)+4194304*0.00025617)**2)


# sample sizeL 8388608
mu_8388608 = 255*(1-8388608/16777216) + 8388608*0.00025617
sigma_8388608 = math.sqrt((2.0/255)*(255*(1-8388608/16777216)+8388608*0.00025617)**2)


# sample sizeL 16777216
mu_16777216 = 255*(1-16777216/16777216) + 16777216*0.00025617
sigma_16777216 = math.sqrt((2.0/255)*(255*(1-16777216/16777216)+16777216*0.00025617)**2)


#Plotting 5 different lines to present the theoretical distirbution of T

expected_T_a_0 = []
expected_T_a_0.append(math.log(mu_32,2))
expected_T_a_0.append(math.log(mu_64,2))
expected_T_a_0.append(math.log(mu_128,2))
expected_T_a_0.append(math.log(mu_256,2))
expected_T_a_0.append(math.log(mu_512,2))
expected_T_a_0.append(math.log(mu_1024,2))
expected_T_a_0.append(math.log(mu_2048,2))
expected_T_a_0.append(math.log(mu_4096,2))
expected_T_a_0.append(math.log(mu_8192,2))
expected_T_a_0.append(math.log(mu_16384,2))
expected_T_a_0.append(math.log(mu_32768,2))
expected_T_a_0.append(math.log(mu_65536,2))
expected_T_a_0.append(math.log(mu_131072,2))
expected_T_a_0.append(math.log(mu_262144,2))
expected_T_a_0.append(math.log(mu_524288,2))
expected_T_a_0.append(math.log(mu_1048576,2))
expected_T_a_0.append(math.log(mu_2097152,2))
expected_T_a_0.append(math.log(mu_4194304,2))
expected_T_a_0.append(math.log(mu_8388608,2))
expected_T_a_0.append(math.log(mu_16777216,2))
plt.plot(t,expected_T_a_0,linewidth=1, linestyle="-", c="DimGray")

expected_T_a_1 = []
expected_T_a_1.append(math.log(mu_32+sigma_32,2))
expected_T_a_1.append(math.log(mu_64+sigma_64,2))
expected_T_a_1.append(math.log(mu_128+sigma_128,2))
expected_T_a_1.append(math.log(mu_256+sigma_256,2))
expected_T_a_1.append(math.log(mu_512+sigma_512,2))
expected_T_a_1.append(math.log(mu_1024+sigma_1024,2))
expected_T_a_1.append(math.log(mu_2048+sigma_2048,2))
expected_T_a_1.append(math.log(mu_4096+sigma_4096,2))
expected_T_a_1.append(math.log(mu_8192+sigma_8192,2))
expected_T_a_1.append(math.log(mu_16384+sigma_16384,2))
expected_T_a_1.append(math.log(mu_32768+sigma_32768,2))
expected_T_a_1.append(math.log(mu_65536+sigma_65536,2))
expected_T_a_1.append(math.log(mu_131072+sigma_131072,2))
expected_T_a_1.append(math.log(mu_262144+sigma_262144,2))
expected_T_a_1.append(math.log(mu_524288+sigma_524288,2))
expected_T_a_1.append(math.log(mu_1048576+sigma_1048576,2))
expected_T_a_1.append(math.log(mu_2097152+sigma_2097152,2))
expected_T_a_1.append(math.log(mu_4194304+sigma_4194304,2))
expected_T_a_1.append(math.log(mu_8388608+sigma_8388608,2))
expected_T_a_1.append(math.log(mu_16777216+sigma_16777216,2))
plt.plot(t,expected_T_a_1,linewidth=1, linestyle="-", c="DimGray")

expected_T_a_2 = []
expected_T_a_2.append(math.log(mu_32-sigma_32,2))
expected_T_a_2.append(math.log(mu_64-sigma_64,2))
expected_T_a_2.append(math.log(mu_128-sigma_128,2))
expected_T_a_2.append(math.log(mu_256-sigma_256,2))
expected_T_a_2.append(math.log(mu_512-sigma_512,2))
expected_T_a_2.append(math.log(mu_1024-sigma_1024,2))
expected_T_a_2.append(math.log(mu_2048-sigma_2048,2))
expected_T_a_2.append(math.log(mu_4096-sigma_4096,2))
expected_T_a_2.append(math.log(mu_8192-sigma_8192,2))
expected_T_a_2.append(math.log(mu_16384-sigma_16384,2))
expected_T_a_2.append(math.log(mu_32768-sigma_32768,2))
expected_T_a_2.append(math.log(mu_65536-sigma_65536,2))
expected_T_a_2.append(math.log(mu_131072-sigma_131072,2))
expected_T_a_2.append(math.log(mu_262144-sigma_262144,2))
expected_T_a_2.append(math.log(mu_524288-sigma_524288,2))
expected_T_a_2.append(math.log(mu_1048576-sigma_1048576,2))
expected_T_a_2.append(math.log(mu_2097152-sigma_2097152,2))
expected_T_a_2.append(math.log(mu_4194304-sigma_4194304,2))
expected_T_a_2.append(math.log(mu_8388608-sigma_8388608,2))
expected_T_a_2.append(math.log(mu_16777216-sigma_16777216,2))
plt.plot(t,expected_T_a_2,linewidth=1, linestyle="-", c="DimGray")

expected_T_a_3 = []
expected_T_a_3.append(math.log(mu_32+2*sigma_32,2))
expected_T_a_3.append(math.log(mu_64+2*sigma_64,2))
expected_T_a_3.append(math.log(mu_128+2*sigma_128,2))
expected_T_a_3.append(math.log(mu_256+2*sigma_256,2))
expected_T_a_3.append(math.log(mu_512+2*sigma_512,2))
expected_T_a_3.append(math.log(mu_1024+2*sigma_1024,2))
expected_T_a_3.append(math.log(mu_2048+2*sigma_2048,2))
expected_T_a_3.append(math.log(mu_4096+2*sigma_4096,2))
expected_T_a_3.append(math.log(mu_8192+2*sigma_8192,2))
expected_T_a_3.append(math.log(mu_16384+2*sigma_16384,2))
expected_T_a_3.append(math.log(mu_32768+2*sigma_32768,2))
expected_T_a_3.append(math.log(mu_65536+2*sigma_65536,2))
expected_T_a_3.append(math.log(mu_131072+2*sigma_131072,2))
expected_T_a_3.append(math.log(mu_262144+2*sigma_262144,2))
expected_T_a_3.append(math.log(mu_524288+2*sigma_524288,2))
expected_T_a_3.append(math.log(mu_1048576+2*sigma_1048576,2))
expected_T_a_3.append(math.log(mu_2097152+2*sigma_2097152,2))
expected_T_a_3.append(math.log(mu_4194304+2*sigma_4194304,2))
expected_T_a_3.append(math.log(mu_8388608+2*sigma_8388608,2))
expected_T_a_3.append(math.log(mu_16777216+2*sigma_16777216,2))
plt.plot(t,expected_T_a_3,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_4 = []
expected_T_a_4.append(math.log(mu_32-2*sigma_32,2))
expected_T_a_4.append(math.log(mu_64-2*sigma_64,2))
expected_T_a_4.append(math.log(mu_128-2*sigma_128,2))
expected_T_a_4.append(math.log(mu_256-2*sigma_256,2))
expected_T_a_4.append(math.log(mu_512-2*sigma_512,2))
expected_T_a_4.append(math.log(mu_1024-2*sigma_1024,2))
expected_T_a_4.append(math.log(mu_2048-2*sigma_2048,2))
expected_T_a_4.append(math.log(mu_4096-2*sigma_4096,2))
expected_T_a_4.append(math.log(mu_8192-2*sigma_8192,2))
expected_T_a_4.append(math.log(mu_16384-2*sigma_16384,2))
expected_T_a_4.append(math.log(mu_32768-2*sigma_32768,2))
expected_T_a_4.append(math.log(mu_65536-2*sigma_65536,2))
expected_T_a_4.append(math.log(mu_131072-2*sigma_131072,2))
expected_T_a_4.append(math.log(mu_262144-2*sigma_262144,2))
expected_T_a_4.append(math.log(mu_524288-2*sigma_524288,2))
expected_T_a_4.append(math.log(mu_1048576-2*sigma_1048576,2))
expected_T_a_4.append(math.log(mu_2097152-2*sigma_2097152,2))
expected_T_a_4.append(math.log(mu_4194304-2*sigma_4194304,2))
expected_T_a_4.append(math.log(mu_8388608-2*sigma_8388608,2))
expected_T_a_4.append(math.log(mu_16777216-2*sigma_16777216,2))
plt.plot(t,expected_T_a_4,linewidth=.1, linestyle="-", c="DimGray")

#Plotting the experimental linesplt.plot(t, t_0, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_0, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_1, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_2, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_3, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_4, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_5, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_6, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_7, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_8, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_9, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_10, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_11, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_12, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_13, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_14, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_15, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_16, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_17, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_18, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_19, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_20, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_21, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_22, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_23, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_24, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_25, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_26, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_27, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_28, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_29, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_30, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_31, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_32, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_33, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_34, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_35, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_36, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_37, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_38, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_39, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_40, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_41, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_42, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_43, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_44, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_45, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_46, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_47, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_48, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_49, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_50, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_51, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_52, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_53, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_54, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_55, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_56, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_57, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_58, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_59, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_60, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_61, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_62, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_63, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_64, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_65, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_66, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_67, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_68, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_69, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_70, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_71, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_72, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_73, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_74, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_75, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_76, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_77, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_78, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_79, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_80, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_81, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_82, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_83, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_84, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_85, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_86, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_87, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_88, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_89, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_90, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_91, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_92, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_93, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_94, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_95, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_96, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_97, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_98, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_99, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_100, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_101, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_102, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_103, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_104, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_105, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_106, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_107, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_108, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_109, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_110, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_111, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_112, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_113, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_114, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_115, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_116, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_117, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_118, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_119, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_120, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_121, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_122, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_123, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_124, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_125, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_126, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_127, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_128, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_129, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_130, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_131, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_132, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_133, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_134, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_135, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_136, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_137, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_138, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_139, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_140, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_141, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_142, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_143, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_144, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_145, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_146, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_147, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_148, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_149, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_150, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_151, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_152, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_153, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_154, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_155, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_156, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_157, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_158, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_159, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_160, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_161, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_162, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_163, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_164, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_165, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_166, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_167, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_168, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_169, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_170, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_171, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_172, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_173, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_174, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_175, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_176, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_177, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_178, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_179, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_180, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_181, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_182, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_183, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_184, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_185, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_186, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_187, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_188, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_189, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_190, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_191, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_192, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_193, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_194, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_195, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_196, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_197, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_198, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_199, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_200, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_201, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_202, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_203, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_204, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_205, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_206, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_207, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_208, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_209, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_210, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_211, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_212, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_213, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_214, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_215, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_216, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_217, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_218, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_219, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_220, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_221, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_222, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_223, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_224, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_225, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_226, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_227, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_228, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_229, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_230, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_231, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_232, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_233, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_234, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_235, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_236, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_237, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_238, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_239, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_240, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_241, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_242, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_243, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_244, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_245, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_246, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_247, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_248, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_249, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_250, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_251, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_252, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_253, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_254, linewidth=.001, linestyle="-", c="red",alpha = .15)
plt.plot(t, t_255, linewidth=.001, linestyle="-", c="red",alpha = .15)



#Shading the theoretical distribution region
plt.fill_between(t, expected_T_a_1,expected_T_a_2,color='DimGray',alpha=1)
plt.fill_between(t, expected_T_a_1,expected_T_a_3,color='DimGray',alpha=1)
plt.fill_between(t, expected_T_a_2,expected_T_a_4,color='DimGray',alpha=1)


#Formatting the plot
plt.xlabel('$log_2(|\phi|)$')
plt.ylabel('$log_2(T(\phi,a))$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-8 with all zero key upto 6 rounds')
plt.text(8.5,19,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(8.5,18,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
#plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(8.5,17,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([8, 24, 3, 20])
plt.grid(True)
plt.show()
