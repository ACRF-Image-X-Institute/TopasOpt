import sys
from pathlib import Path
sys.path.append(str(Path('../../TopasBayesOpt').resolve()))
from TopasBayesOpt.WaterTankAnalyser import compare_multiple_results

FilesToCompare = ['C:/Users/bwhe3635/Dropbox (Sydney Uni)/Projects/PhaserSims/topas/PhaseSpaceOptimisationTest/Results/WaterTank_itt_95.bin',
                  'C:/Users/bwhe3635/Dropbox (Sydney Uni)/Projects/TopasBayesOpt/examples/SimpleCollimatorExample_TopasFiles/Results/WaterTank.bin']


compare_multiple_results(FilesToCompare, abs_dose=False)






