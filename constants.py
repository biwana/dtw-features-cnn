def param_selector(dataset):
    if dataset == "50words":
        return 50 #270
    if dataset == "Adiac":
        return 37 #176
    if dataset == "ArrowHead":
        return 3 #251
    if dataset == "Beef":
        return 5 #470
    if dataset == "BeetleFly":
        return 2 #512
    if dataset == "BirdChicken":
        return 2 #512
    if dataset == "Car":
        return 4 #577
    if dataset == "CBF":
        return 3 #128
    if dataset == "ChlorineConcentration":
        return 3 #166
    if dataset == "CinC_ECG_torso":
        return 4 #1639
    if dataset == "Coffee":
        return 2 #286
    if dataset == "Computers":
        return 2 #720
    if dataset == "Cricket_X":
        return 12 #300
    if dataset == "Cricket_Y":
        return 12 #300
    if dataset == "Cricket_Z":
        return 12 #300
    if dataset == "DiatomSizeReduction":
        return 4 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 2 #80
    if dataset == "DistalPhalanxTW":
        return 6 #80
    if dataset == "Earthquakes":
        return 2 #512
    if dataset == "ECG200":
        return 2 #96
    if dataset == "ECG5000":
        return 5 #140
    if dataset == "ECGFiveDays":
        return 2 #136
    if dataset == "ElectricDevices":
        return 7 #96
    if dataset == "FaceAll":
        return 14 # 131
    if dataset == "FaceFour":
        return 4 # 350
    if dataset == "FacesUCR":
        return 14 # 131
    if dataset == "FISH":
        return 7 # 463
    if dataset == "FordA":
        return 2 #500
    if dataset == "FordB":
        return 2 # 500
    if dataset == "Gun_Point":
        return 2 # 150
    if dataset == "Ham":
        return 2 # 431
    if dataset == "HandOutlines":
        return 2 # 2709
    if dataset == "Haptics":
        return 5 # 1092
    if dataset == "Herring":
        return 2 # 512
    if dataset == "InlineSkate":
        return 7 # 1882
    if dataset == "InsectWingbeatSound":
        return 11 # 256
    if dataset == "ItalyPowerDemand":
        return 2 # 24
    if dataset == "LargeKitchenAppliances":
        return 3 # 720
    if dataset == "Lighting2":
        return 2 # 637
    if dataset == "Lighting7":
        return 7 # 319
    if dataset == "MALLAT":
        return 8 # 1024
    if dataset == "Meat":
        return 3 # 448
    if dataset == "MedicalImages":
        return 10 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 2 #80
    if dataset == "MiddlePhalanxTW":
        return 6 #80
    if dataset == "MoteStrain":
        return 2 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 42 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 42 #750
    if dataset == "OliveOil":
        return 4 #570
    if dataset == "OSULeaf":
        return 6 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 2 #80
    if dataset == "Phoneme":
        return 39 #1024
    if dataset == "Plane":
        return 7 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 3 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 2 #80
    if dataset == "ProximalPhalanxTW":
        return 6 #80
    if dataset == "RefrigerationDevices":
        return 3 #720
    if dataset == "ScreenType":
        return 3 #720
    if dataset == "ShapeletSim":
        return 2 #500
    if dataset == "ShapesAll":
        return 60 # 512
    if dataset == "SmallKitchenAppliances":
        return 3 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return 2 #65
    if dataset == "SonyAIBORobotSurface":
        return 2 #70
    if dataset == "StarLightCurves":
        return 3 #1024
    if dataset == "Strawberry":
        return 2 #235
    if dataset == "SwedishLeaf":
        return 15 # 128
    if dataset == "Symbols":
        return 6 #398
    if dataset == "synthetic_control":
        return 6 #60
    if dataset == "ToeSegmentation1":
        return 2 #277
    if dataset == "ToeSegmentation2":
        return 2 #343
    if dataset == "Trace":
        return 4 #275
    if dataset == "TwoLeadECG":
        return 2 #82
    if dataset == "Two_Patterns":
        return 4 #128
    if dataset == "uWaveGestureLibrary_X":
        return 8 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return 8 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return 8 # 315
    if dataset == "UWaveGestureLibraryAll":
        return 8 # 945
    if dataset == "wafer":
        return 2 #152
    if dataset == "Wine":
        return 2 #234
    if dataset == "WordsSynonyms":
        return 25 #270
    if dataset == "Worms":
        return 5 #900
    if dataset == "WormsTwoClass":
        return 2 #900
    if dataset == "yoga":
        return 2 #426
    exit('missing dataset')

def class_modifier_add(dataset):
    if dataset == "50words":
        return -1 #270
    if dataset == "Adiac":
        return -1 #176
    if dataset == "ArrowHead":
        return 0 #251
    if dataset == "Beef":
        return -1 #470
    if dataset == "BeetleFly":
        return -1 #512
    if dataset == "BirdChicken":
        return -1 #512
    if dataset == "Car":
        return -1 #577
    if dataset == "CBF":
        return -1 #128
    if dataset == "ChlorineConcentration":
        return -1 #166
    if dataset == "CinC_ECG_torso":
        return -1 #1639
    if dataset == "Coffee":
        return 0 #286
    if dataset == "Computers":
        return -1 #720
    if dataset == "Cricket_X":
        return -1 #300
    if dataset == "Cricket_Y":
        return -1 #300
    if dataset == "Cricket_Z":
        return -1 #300
    if dataset == "DiatomSizeReduction":
        return -1 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 0 #80
    if dataset == "DistalPhalanxTW":
        return -3 #80
    if dataset == "Earthquakes":
        return 0 #512
    if dataset == "ECG200":
        return 1 #96
    if dataset == "ECG5000":
        return -1 #140
    if dataset == "ECGFiveDays":
        return -1 #136
    if dataset == "ElectricDevices":
        return -1 #96
    if dataset == "FaceAll":
        return -1 # 131
    if dataset == "FaceFour":
        return -1 # 350
    if dataset == "FacesUCR":
        return -1 # 131
    if dataset == "FISH":
        return -1 # 463
    if dataset == "FordA":
        return 1 #500
    if dataset == "FordB":
        return 1 # 500
    if dataset == "Gun_Point":
        return -1 # 150
    if dataset == "Ham":
        return -1 # 431
    if dataset == "HandOutlines":
        return 0 # 2709
    if dataset == "Haptics":
        return -1 # 1092
    if dataset == "Herring":
        return -1 # 512
    if dataset == "InlineSkate":
        return -1 # 1882
    if dataset == "InsectWingbeatSound":
        return -1 # 256
    if dataset == "ItalyPowerDemand":
        return -1 # 24
    if dataset == "LargeKitchenAppliances":
        return -1 # 720
    if dataset == "Lighting2":
        return 1 # 637
    if dataset == "Lighting7":
        return 0 # 319
    if dataset == "MALLAT":
        return -1 # 1024
    if dataset == "Meat":
        return -1 # 448
    if dataset == "MedicalImages":
        return -1 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 0 #80
    if dataset == "MiddlePhalanxTW":
        return -3 #80
    if dataset == "MoteStrain":
        return -1 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return -1 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return -1 #750
    if dataset == "OliveOil":
        return -1 #570
    if dataset == "OSULeaf":
        return -1 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 0 #80
    if dataset == "Phoneme":
        return -1 #1024
    if dataset == "Plane":
        return -1 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return -1 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 0 #80
    if dataset == "ProximalPhalanxTW":
        return -3 #80
    if dataset == "RefrigerationDevices":
        return -1 #720
    if dataset == "ScreenType":
        return -1 #720
    if dataset == "ShapeletSim":
        return 0 #500
    if dataset == "ShapesAll":
        return -1 # 512
    if dataset == "SmallKitchenAppliances":
        return -1 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return -1 #65
    if dataset == "SonyAIBORobotSurface":
        return -1 #70
    if dataset == "StarLightCurves":
        return -1 #1024
    if dataset == "Strawberry":
        return -1 #235
    if dataset == "SwedishLeaf":
        return -1 # 128
    if dataset == "Symbols":
        return -1 #398
    if dataset == "synthetic_control":
        return -1 #60
    if dataset == "ToeSegmentation1":
        return 0 #277
    if dataset == "ToeSegmentation2":
        return 0 #343
    if dataset == "Trace":
        return -1 #275
    if dataset == "TwoLeadECG":
        return -1 #82
    if dataset == "Two_Patterns":
        return -1 #128
    if dataset == "uWaveGestureLibrary_X":
        return -1 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return -1 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return -1 # 315
    if dataset == "UWaveGestureLibraryAll":
        return -1 # 945
    if dataset == "wafer":
        return 1 #152
    if dataset == "Wine":
        return -1 #234
    if dataset == "WordsSynonyms":
        return -1 #270
    if dataset == "Worms":
        return -1 #900
    if dataset == "WormsTwoClass":
        return -1 #900
    if dataset == "yoga":
        return -1 #426
    exit('missing dataset')

def class_modifier_multi(dataset):
    if dataset == "50words":
        return 1 #270
    if dataset == "Adiac":
        return 1 #176
    if dataset == "ArrowHead":
        return 1 #251
    if dataset == "Beef":
        return 1 #470
    if dataset == "BeetleFly":
        return 1 #512
    if dataset == "BirdChicken":
        return 1 #512
    if dataset == "Car":
        return 1 #577
    if dataset == "CBF":
        return 1 #128
    if dataset == "ChlorineConcentration":
        return 1 #166
    if dataset == "CinC_ECG_torso":
        return 1 #1639
    if dataset == "Coffee":
        return 1 #286
    if dataset == "Computers":
        return 1 #720
    if dataset == "Cricket_X":
        return 1 #300
    if dataset == "Cricket_Y":
        return 1 #300
    if dataset == "Cricket_Z":
        return 1 #300
    if dataset == "DiatomSizeReduction":
        return 1 #345
    if dataset == "DistalPhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "DistalPhalanxOutlineCorrect":
        return 1 #80
    if dataset == "DistalPhalanxTW":
        return 1 #80
    if dataset == "Earthquakes":
        return 1 #512
    if dataset == "ECG200":
        return 0.5 #96
    if dataset == "ECG5000":
        return 1 #140
    if dataset == "ECGFiveDays":
        return 1 #136
    if dataset == "ElectricDevices":
        return 1 #96
    if dataset == "FaceAll":
        return 1 # 131
    if dataset == "FaceFour":
        return 1 # 350
    if dataset == "FacesUCR":
        return 1 # 131
    if dataset == "FISH":
        return 1 # 463
    if dataset == "FordA":
        return 0.5 #500
    if dataset == "FordB":
        return 0.5 # 500
    if dataset == "Gun_Point":
        return 1 # 150
    if dataset == "Ham":
        return 1 # 431
    if dataset == "HandOutlines":
        return 1 # 2709
    if dataset == "Haptics":
        return 1 # 1092
    if dataset == "Herring":
        return 1 # 512
    if dataset == "InlineSkate":
        return 1 # 1882
    if dataset == "InsectWingbeatSound":
        return 1 # 256
    if dataset == "ItalyPowerDemand":
        return 1 # 24
    if dataset == "LargeKitchenAppliances":
        return 1 # 720
    if dataset == "Lighting2":
        return 0.5 # 637
    if dataset == "Lighting7":
        return 1 # 319
    if dataset == "MALLAT":
        return 1 # 1024
    if dataset == "Meat":
        return 1 # 448
    if dataset == "MedicalImages":
        return 1 # 99
    if dataset == "MiddlePhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "MiddlePhalanxOutlineCorrect":
        return 1 #80
    if dataset == "MiddlePhalanxTW":
        return 1 #80
    if dataset == "MoteStrain":
        return 1 #84
    if dataset == "NonInvasiveFatalECG_Thorax1":
        return 1 #750
    if dataset == "NonInvasiveFatalECG_Thorax2":
        return 1 #750
    if dataset == "OliveOil":
        return 1 #570
    if dataset == "OSULeaf":
        return 1 #427
    if dataset == "PhalangesOutlinesCorrect":
        return 1 #80
    if dataset == "Phoneme":
        return 1 #1024
    if dataset == "Plane":
        return 1 #144
    if dataset == "ProximalPhalanxOutlineAgeGroup":
        return 1 #80
    if dataset == "ProximalPhalanxOutlineCorrect":
        return 1 #80
    if dataset == "ProximalPhalanxTW":
        return 1 #80
    if dataset == "RefrigerationDevices":
        return 1 #720
    if dataset == "ScreenType":
        return 1 #720
    if dataset == "ShapeletSim":
        return 1 #500
    if dataset == "ShapesAll":
        return 1 # 512
    if dataset == "SmallKitchenAppliances":
        return 1 #720
    if dataset == "SonyAIBORobotSurfaceII":
        return 1 #65
    if dataset == "SonyAIBORobotSurface":
        return 1 #70
    if dataset == "StarLightCurves":
        return 1 #1024
    if dataset == "Strawberry":
        return 1 #235
    if dataset == "SwedishLeaf":
        return 1 # 128
    if dataset == "Symbols":
        return 1 #398
    if dataset == "synthetic_control":
        return 1 #60
    if dataset == "ToeSegmentation1":
        return 1 #277
    if dataset == "ToeSegmentation2":
        return 1 #343
    if dataset == "Trace":
        return 1 #275
    if dataset == "TwoLeadECG":
        return 1 #82
    if dataset == "Two_Patterns":
        return 1 #128
    if dataset == "uWaveGestureLibrary_X":
        return 1 # 315
    if dataset == "uWaveGestureLibrary_Y":
        return 1 # 315
    if dataset == "uWaveGestureLibrary_Z":
        return 1 # 315
    if dataset == "UWaveGestureLibraryAll":
        return 1 # 945
    if dataset == "wafer":
        return 0.5 #152
    if dataset == "Wine":
        return 1 #234
    if dataset == "WordsSynonyms":
        return 1 #270
    if dataset == "Worms":
        return 1 #900
    if dataset == "WormsTwoClass":
        return 1 #900
    if dataset == "yoga":
        return 1 #426
    exit('missing dataset')
