# 
#  ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
#  ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
#  █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
#  ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
#  ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
#  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
#  
from numpy import log10
import pandas as pd
from IPython.display import display, HTML

# ========================================= || Enviroment ||
def AdjustDisplay(Dataset):
    pd.options.display.max_rows = Dataset.shape[0]
    pd.options.display.max_columns = Dataset.shape[1]

# ============================================ || Metrics ||

def DatasetViability(Dataset):
  Variables = Dataset.shape[1]
  Filas = Dataset.shape[0]
  # Si es mayor a 2 entonces se procede con el analisis, si no es small data
  Viability = log10( (Filas - Variables) / Variables )
  return Viability

# =============================================== || Math ||

# Think Stats: Exploratory Data Analysis in Python pp104
# https://en.wikipedia.org/wiki/Moment_of_inertia
# https://en.wikipedia.org/wiki/Moment_(mathematics)
#
def RawMoment(xs, k):
    return sum(x**k for x in xs) / len(xs)

def CentralMoment(xs, k):
    Mean = RawMoment(xs, 1)
    Cm = sum((x - Mean)**k for x in xs) / len(xs)
    return Cm

def σ(nStd,Data):
    md = Data.median()
    σmin = md - ( Data.std() * nStd )
    σmax = md - ( Data.std() * nStd )
    return [σmin,σmax]

# display(HTML(Data.to_html())), print('\n',Data)

