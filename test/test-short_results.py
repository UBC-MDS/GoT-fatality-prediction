import pandas as pd
import numpy as np
import pytest
from short_results import short_results


test_cv_results = 

{'mean_fit_time': np.array([0.04341373, 0.0871592 , 0.05320287, 0.06795144, 0.04012394,
        0.0673275 , 0.04910107, 0.03742876, 0.05182781, 0.05294995,
        0.04125571, 0.0485518 , 0.04777231, 0.05064015, 0.05722361,
        0.03482137, 0.03153071, 0.05437212, 0.06835508, 0.03854537,
        0.05077662, 0.03987393, 0.05327034, 0.05985718, 0.05860553,
        0.04381585, 0.0551909 , 0.03816347, 0.06754956, 0.03680229,
        0.04358974, 0.04443216, 0.06407309, 0.06038713, 0.04140167,
        0.08301644, 0.06599646, 0.06279626, 0.043748  , 0.04749103]),
 'std_fit_time': np.array([0.00743457, 0.02449238, 0.01027834, 0.01521616, 0.00876377,
        0.02237169, 0.00868665, 0.00616654, 0.00582787, 0.00583982,
        0.0061633 , 0.0036747 , 0.00517343, 0.00816859, 0.0086693 ,
        0.00361784, 0.00456505, 0.00384919, 0.00760293, 0.00342388,
        0.00275718, 0.00568968, 0.00875321, 0.00617557, 0.00579132,
        0.0045253 , 0.00867295, 0.00930604, 0.01359608, 0.00418338,
        0.0109304 , 0.01060685, 0.0279114 , 0.0098487 , 0.00237394,
        0.01556313, 0.00818594, 0.01033682, 0.00293247, 0.00163448]),
 'mean_score_time': np.array([0.02024517, 0.02423892, 0.0222126 , 0.02028604, 0.0228189 ,
        0.02200456, 0.01855497, 0.02061849, 0.01951175, 0.01859059,
        0.0156548 , 0.01893802, 0.01564894, 0.02444854, 0.01872263,
        0.01805892, 0.01679406, 0.02071915, 0.01877856, 0.02015529,
        0.02026625, 0.02001081, 0.0187562 , 0.02390742, 0.02208457,
        0.02261171, 0.0251111 , 0.01827364, 0.0224443 , 0.01902347,
        0.01947212, 0.01723318, 0.02476449, 0.02414694, 0.01882477,
        0.02484822, 0.02094326, 0.01873689, 0.01352029, 0.01113462]),
 'std_score_time': np.array([0.00270593, 0.00378849, 0.00636774, 0.00584687, 0.00548322,
        0.0038598 , 0.00378569, 0.00353722, 0.00270615, 0.00482542,
        0.0012641 , 0.00462236, 0.00168662, 0.0101116 , 0.0033738 ,
        0.00216589, 0.00271471, 0.00226679, 0.00356705, 0.00495883,
        0.00404306, 0.00779843, 0.00262348, 0.00611888, 0.00424386,
        0.0049908 , 0.01019118, 0.00131746, 0.00308899, 0.00217264,
        0.00132766, 0.00243882, 0.00396573, 0.00906554, 0.00150983,
        0.00517913, 0.00159248, 0.00297468, 0.00441409, 0.00308778]),
 'param_logisticregression__max_iter': np.masked_array(data=[100, 1000, 1000, 2000, 2000, 2000, 2000, 1500, 1000,
                    1500, 1000, 100, 1000, 2000, 1500, 500, 2000, 1500,
                    500, 100, 1000, 1500, 500, 100, 1500, 1000, 100, 500,
                    2000, 1000, 2000, 1500, 1500, 2000, 100, 1500, 2000,
                    2000, 100, 100],
              mask=[False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False],
        fill_value='?',
             dtype=object),
 'param_logisticregression__class_weight': np.masked_array(data=[None, 'balanced', 'balanced', 'balanced', 'balanced',
                    None, 'balanced', None, None, 'balanced', None,
                    'balanced', None, 'balanced', 'balanced', None, None,
                    'balanced', None, None, None, 'balanced', 'balanced',
                    None, 'balanced', None, None, 'balanced', None, None,
                    'balanced', None, None, 'balanced', 'balanced', None,
                    None, 'balanced', 'balanced', None],
              mask=[False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False],
        fill_value='?',
             dtype=object),
 'param_logisticregression__C': np.masked_array(data=[0.0001438449888287663, 3.792690190732246,
                    7.847599703514607e-06, 69.51927961775591,
                    4.281332398719396e-07, 0.20691380811147903,
                    5455.594781168515, 0.0001438449888287663,
                    1274.2749857031322, 297.6351441631313,
                    0.011288378916846883, 23357.21469090121,
                    23357.21469090121, 23357.21469090121,
                    0.20691380811147903, 7.847599703514607e-06, 1e-07,
                    5455.594781168515, 3.792690190732246,
                    1.8329807108324375e-06, 5455.594781168515,
                    0.011288378916846883, 1274.2749857031322,
                    5455.594781168515, 3.792690190732246,
                    0.0026366508987303553, 23357.21469090121,
                    1.8329807108324375e-06, 69.51927961775591,
                    0.0001438449888287663, 0.0026366508987303553,
                    0.04832930238571752, 23357.21469090121,
                    0.8858667904100814, 0.011288378916846883,
                    16.237767391887175, 23357.21469090121,
                    16.237767391887175, 0.04832930238571752,
                    69.51927961775591],
              mask=[False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False,
                    False, False, False, False, False, False, False, False],
        fill_value='?',
             dtype=object),
 'params': [{'logisticregression__max_iter': 100,
   'logisticregression__class_weight': None,
   'logisticregression__C': 0.0001438449888287663},
  {'logisticregression__max_iter': 1000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 3.792690190732246},
  {'logisticregression__max_iter': 1000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 7.847599703514607e-06},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 69.51927961775591},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 4.281332398719396e-07},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 0.20691380811147903},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 5455.594781168515},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': None,
   'logisticregression__C': 0.0001438449888287663},
  {'logisticregression__max_iter': 1000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 1274.2749857031322},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 297.6351441631313},
  {'logisticregression__max_iter': 1000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 0.011288378916846883},
  {'logisticregression__max_iter': 100,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 23357.21469090121},
  {'logisticregression__max_iter': 1000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 23357.21469090121},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 23357.21469090121},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 0.20691380811147903},
  {'logisticregression__max_iter': 500,
   'logisticregression__class_weight': None,
   'logisticregression__C': 7.847599703514607e-06},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 1e-07},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 5455.594781168515},
  {'logisticregression__max_iter': 500,
   'logisticregression__class_weight': None,
   'logisticregression__C': 3.792690190732246},
  {'logisticregression__max_iter': 100,
   'logisticregression__class_weight': None,
   'logisticregression__C': 1.8329807108324375e-06},
  {'logisticregression__max_iter': 1000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 5455.594781168515},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 0.011288378916846883},
  {'logisticregression__max_iter': 500,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 1274.2749857031322},
  {'logisticregression__max_iter': 100,
   'logisticregression__class_weight': None,
   'logisticregression__C': 5455.594781168515},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 3.792690190732246},
  {'logisticregression__max_iter': 1000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 0.0026366508987303553},
  {'logisticregression__max_iter': 100,
   'logisticregression__class_weight': None,
   'logisticregression__C': 23357.21469090121},
  {'logisticregression__max_iter': 500,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 1.8329807108324375e-06},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 69.51927961775591},
  {'logisticregression__max_iter': 1000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 0.0001438449888287663},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 0.0026366508987303553},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': None,
   'logisticregression__C': 0.04832930238571752},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': None,
   'logisticregression__C': 23357.21469090121},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 0.8858667904100814},
  {'logisticregression__max_iter': 100,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 0.011288378916846883},
  {'logisticregression__max_iter': 1500,
   'logisticregression__class_weight': None,
   'logisticregression__C': 16.237767391887175},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': None,
   'logisticregression__C': 23357.21469090121},
  {'logisticregression__max_iter': 2000,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 16.237767391887175},
  {'logisticregression__max_iter': 100,
   'logisticregression__class_weight': 'balanced',
   'logisticregression__C': 0.04832930238571752},
  {'logisticregression__max_iter': 100,
   'logisticregression__class_weight': None,
   'logisticregression__C': 69.51927961775591}],
 'split0_test_score': np.array([0.        , 0.55924171, 0.32692308, 0.57276995, 0.58515284,
        0.1978022 , 0.57009346, 0.        , 0.20408163, 0.57009346,
        0.13793103, 0.57009346, 0.20408163, 0.57009346, 0.53953488,
        0.        , 0.        , 0.57009346, 0.20408163, 0.        ,
        0.20408163, 0.54081633, 0.57009346, 0.20408163, 0.55924171,
        0.0952381 , 0.20408163, 0.58515284, 0.20408163, 0.        ,
        0.49180328, 0.17977528, 0.20408163, 0.55238095, 0.54081633,
        0.20408163, 0.20408163, 0.57276995, 0.53456221, 0.20408163]),
 'split1_test_score': np.array([0.        , 0.51141553, 0.27184466, 0.51376147, 0.5093633 ,
        0.26262626, 0.51376147, 0.        , 0.28846154, 0.51376147,
        0.15217391, 0.51376147, 0.28846154, 0.51376147, 0.50909091,
        0.        , 0.        , 0.51376147, 0.28571429, 0.        ,
        0.28846154, 0.51643192, 0.51376147, 0.28846154, 0.51141553,
        0.07058824, 0.28846154, 0.5112782 , 0.28846154, 0.        ,
        0.50273224, 0.22916667, 0.28846154, 0.51376147, 0.51643192,
        0.28846154, 0.28846154, 0.51376147, 0.51612903, 0.28846154]),
 'split2_test_score': np.array([0.        , 0.50458716, 0.48826291, 0.49769585, 0.49302326,
        0.28828829, 0.49769585, 0.        , 0.32478632, 0.49769585,
        0.13333333, 0.49769585, 0.32478632, 0.49769585, 0.51376147,
        0.        , 0.        , 0.49769585, 0.32758621, 0.        ,
        0.32478632, 0.49038462, 0.49769585, 0.32478632, 0.50458716,
        0.07058824, 0.32478632, 0.49302326, 0.32478632, 0.        ,
        0.45833333, 0.22680412, 0.32478632, 0.50458716, 0.49038462,
        0.32478632, 0.32478632, 0.50458716, 0.49074074, 0.32478632]),
 'split3_test_score': np.array([0.        , 0.50485437, 0.48333333, 0.50485437, 0.58163265,
        0.46956522, 0.50485437, 0.        , 0.47457627, 0.50485437,
        0.32989691, 0.50485437, 0.47457627, 0.50485437, 0.5       ,
        0.        , 0.        , 0.50485437, 0.47457627, 0.        ,
        0.47457627, 0.48314607, 0.50485437, 0.47457627, 0.50485437,
        0.18181818, 0.47457627, 0.58461538, 0.47457627, 0.        ,
        0.51798561, 0.41121495, 0.47457627, 0.49514563, 0.48314607,
        0.47457627, 0.47457627, 0.50485437, 0.50746269, 0.47457627]),
 'split4_test_score': np.array([0.        , 0.50731707, 0.25242718, 0.50246305, 0.51674641,
        0.2244898 , 0.50246305, 0.        , 0.32432432, 0.50246305,
        0.15384615, 0.50246305, 0.32432432, 0.50246305, 0.50980392,
        0.        , 0.        , 0.50246305, 0.32432432, 0.        ,
        0.32432432, 0.52849741, 0.50246305, 0.32432432, 0.50731707,
        0.11494253, 0.32432432, 0.51674641, 0.32432432, 0.        ,
        0.48554913, 0.19148936, 0.32432432, 0.51231527, 0.52849741,
        0.32432432, 0.32432432, 0.50246305, 0.51231527, 0.32432432]),
 'mean_test_score': np.array([0.        , 0.51748317, 0.36455823, 0.51830894, 0.53718369,
        0.28855435, 0.51777364, 0.        , 0.32324602, 0.51777364,
        0.18143627, 0.51777364, 0.32324602, 0.51777364, 0.51443824,
        0.        , 0.        , 0.51777364, 0.32325654, 0.        ,
        0.32324602, 0.51185527, 0.51777364, 0.32324602, 0.51748317,
        0.10663506, 0.32324602, 0.53816322, 0.32324602, 0.        ,
        0.49128072, 0.24769008, 0.32324602, 0.5156381 , 0.51185527,
        0.32324602, 0.32324602, 0.5196872 , 0.51224199, 0.32324602]),
 'std_test_score': np.array([0.        , 0.02102254, 0.10197642, 0.02772616, 0.03851896,
        0.09568437, 0.02667546, 0.        , 0.08753798, 0.02667546,
        0.07465207, 0.02667546, 0.08753798, 0.02667546, 0.01333292,
        0.        , 0.        , 0.02667546, 0.0877834 , 0.        ,
        0.08753798, 0.02200844, 0.02667546, 0.08753798, 0.02102254,
        0.04110998, 0.08753798, 0.0389485 , 0.08753798, 0.        ,
        0.01981385, 0.0840127 , 0.08753798, 0.01952775, 0.02200844,
        0.08753798, 0.08753798, 0.02682383, 0.01413119, 0.08753798]),
 'rank_test_score': np.array([35, 11, 19,  4,  2, 31,  5, 35, 21,  5, 33,  5, 21,  5, 14, 35, 35,
         5, 20, 35, 21, 16,  5, 21, 11, 34, 21,  1, 21, 35, 18, 32, 21, 13,
        16, 21, 21,  3, 15, 21]),
 'split0_train_score': np.array([0.        , 0.52205006, 0.31408776, 0.52205006, 0.50371945,
        0.26      , 0.52205006, 0.        , 0.29879518, 0.52205006,
        0.14044944, 0.52205006, 0.29879518, 0.52205006, 0.49942987,
        0.        , 0.        , 0.52205006, 0.29468599, 0.        ,
        0.29879518, 0.51074589, 0.52205006, 0.29879518, 0.52205006,
        0.06567164, 0.29879518, 0.50479233, 0.29807692, 0.        ,
        0.50730412, 0.21108179, 0.29879518, 0.51294118, 0.51074589,
        0.29807692, 0.29879518, 0.52205006, 0.49374289, 0.29807692]),
 'split1_train_score': np.array([0.        , 0.52668213, 0.30331754, 0.52619325, 0.51792829,
        0.27722772, 0.5255814 , 0.        , 0.33486239, 0.5255814 ,
        0.15934066, 0.5255814 , 0.33486239, 0.5255814 , 0.52073733,
        0.        , 0.        , 0.5255814 , 0.3287037 , 0.        ,
        0.33486239, 0.51174289, 0.5255814 , 0.33486239, 0.52668213,
        0.09912536, 0.33486239, 0.51896208, 0.33486239, 0.        ,
        0.51468531, 0.22047244, 0.33486239, 0.52607184, 0.51174289,
        0.32794457, 0.33486239, 0.52447552, 0.52307692, 0.33486239]),
 'split2_train_score': np.array([0.        , 0.52386496, 0.53284672, 0.52790698, 0.53510896,
        0.28780488, 0.52790698, 0.        , 0.36734694, 0.52790698,
        0.15686275, 0.52790698, 0.36734694, 0.52790698, 0.52508751,
        0.        , 0.        , 0.52790698, 0.35023041, 0.        ,
        0.36734694, 0.53020962, 0.52790698, 0.36734694, 0.52386496,
        0.08308605, 0.36734694, 0.53510896, 0.36734694, 0.        ,
        0.50338295, 0.19892473, 0.36734694, 0.52193995, 0.53020962,
        0.36818182, 0.36734694, 0.52447552, 0.53504673, 0.36734694]),
 'split3_train_score': np.array([0.        , 0.54669704, 0.39035088, 0.54669704, 0.53893696,
        0.43693694, 0.54669704, 0.        , 0.47133758, 0.54669704,
        0.32820513, 0.54669704, 0.47133758, 0.54669704, 0.54842474,
        0.        , 0.        , 0.54669704, 0.46908316, 0.        ,
        0.47133758, 0.54545455, 0.54669704, 0.47133758, 0.54669704,
        0.19101124, 0.47133758, 0.5375    , 0.47133758, 0.        ,
        0.52951096, 0.38942308, 0.47133758, 0.54732041, 0.54545455,
        0.47133758, 0.47133758, 0.54669704, 0.55099648, 0.47133758]),
 'split4_train_score': np.array([0.        , 0.52729384, 0.29928741, 0.52607184, 0.52455357,
        0.28009828, 0.52607184, 0.        , 0.33860045, 0.52607184,
        0.15083799, 0.52607184, 0.33860045, 0.52607184, 0.52852154,
        0.        , 0.        , 0.52607184, 0.33783784, 0.        ,
        0.33860045, 0.52605459, 0.52607184, 0.33860045, 0.52729384,
        0.07121662, 0.33860045, 0.52455357, 0.33860045, 0.        ,
        0.50688705, 0.21750663, 0.33860045, 0.52838934, 0.52605459,
        0.33860045, 0.33860045, 0.52838934, 0.53474676, 0.33860045]),
 'mean_train_score': np.array([0.        , 0.52931761, 0.36797806, 0.52978383, 0.52404944,
        0.30841356, 0.52966146, 0.        , 0.36218851, 0.52966146,
        0.18713919, 0.52966146, 0.36218851, 0.52966146, 0.5244402 ,
        0.        , 0.        , 0.52966146, 0.35610822, 0.        ,
        0.36218851, 0.52484151, 0.52966146, 0.36218851, 0.52931761,
        0.10202218, 0.36218851, 0.52418339, 0.36204486, 0.        ,
        0.51235408, 0.24748173, 0.36218851, 0.52733254, 0.52484151,
        0.36082827, 0.36218851, 0.5292175 , 0.52752196, 0.36204486]),
 'std_train_score': np.array([0.        , 0.00889533, 0.08886593, 0.0086725 , 0.01260938,
        0.06490171, 0.00872645, 0.        , 0.05875705, 0.00872645,
        0.07083323, 0.00872645, 0.05875705, 0.00872645, 0.01569434,
        0.        , 0.        , 0.00872645, 0.05942287, 0.        ,
        0.05875705, 0.0128487 , 0.00872645, 0.05875705, 0.00889533,
        0.04594859, 0.05875705, 0.01183311, 0.05891254, 0.        ,
        0.00933451, 0.07135558, 0.05875705, 0.01129967, 0.0128487 ,
        0.05963141, 0.05875705, 0.0089729 , 0.01908223, 0.05891254])}


def test_input_correct_type():
    assert # check that runnning short_results on a list returns an error

def test_short_results_returns_dataframe():
    banana = short_results(test_cv_results)
    assert isinstance(banana, pd.DataFrame)

def test_short_results_correct_size():
    banana = short_results(test_cv_results)
    assert banana.shape == (4,6)

def test_short_results_scores():
    banana = short_results(test_cv_results)
    assert 0<banana.iloc[5,0]<1