import sys
import numpy as np
from pathlib import Path
from TopasOpt import Optimisers as to

BaseDirectory = 'C:\\Users\\Brendan\\Documents\\temp'
SimulationName = 'development_test'
OptimisationDirectory = Path(__file__).parent

# set up optimisation params for rosen function:
optimisation_params = {}
optimisation_params['ParameterNames'] = ['x', 'y']
optimisation_params['UpperBounds'] = np.array([1, 1])
optimisation_params['LowerBounds'] = np.array([-1, -1])
optimisation_params['start_point'] = np.array([.9, .9])
# Remember true values are  [1.82, 2.5, 27]
optimisation_params['Nitterations'] = 100
# optimisation_params['Suggestions'] # you can suggest points to test if you want - we won't here.
ReadMeText = 'This is an example in which the rosen function is minimised, and demonstrates how this library' \
             'can be tested without actually calling topas'

Optimiser = to.NelderMeadOptimiser(optimisation_params, BaseDirectory, SimulationName, OptimisationDirectory,
                                TopasLocation='testing_mode', ReadMeText=ReadMeText, Overwrite=True, KeepAllResults=False,
                                   NM_StartingSimplexRelativeVal=.4)

Optimiser.RunOptimisation()
