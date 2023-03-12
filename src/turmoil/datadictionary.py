#
#  ███████╗███████╗████████╗██╗   ██╗██████╗ 
#  ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
#  ███████╗█████╗     ██║   ██║   ██║██████╔╝
#  ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
#  ███████║███████╗   ██║   ╚██████╔╝██║     
#  ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
#   
import pandas as pd
import numpy as np
#from numba import jit
#import dask.dataframe as dd
from collections import namedtuple
# 
#  ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
#  ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
#  █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
#  ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
#  ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
#  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
#  

# ========================================= || Enviroment ||
def AdjustDisplay(Dataset):
    pd.options.display.max_rows = Dataset.shape[0]
    pd.options.display.max_columns = Dataset.shape[1]

# ============================================ || Metrics ||
def DatasetViability(Dataset):
  Variables = Dataset.shape[1]
  Filas = Dataset.shape[0]
  # Si es mayor a 2 entonces se procede con el analisis, si no es small data
  np.log10( (Filas - Variables) / Variables )
  return 

# =============================================== || Math ||

# Think Stats: Exploratory Data Analysis in Python pp104
# https://en.wikipedia.org/wiki/Moment_of_inertia
# https://en.wikipedia.org/wiki/Moment_(mathematics)
#
# Statistical Moments
# Source: 
# https://www.analyticsvidhya.com/blog/2022/01/moments-a-must-known-statistical-concept-for-data-science/
# https://uh.edu/~odonnell/econ2370/moment.pdf
# http://yauchunghei.weebly.com/myblog/the-fifth-statistical-moment
# https://online.stat.psu.edu/stat415/lesson/1/1.4
# https://biostatistics.letgen.org/mikes-biostatistics-book/probability-distributions/6-8-moments/
# https://biostatistics.letgen.org/mikes-biostatistics-book/exploring-data/measures-of-central-tendency/

def central_moment(xs, k):
  try:
    mean = np.sum(xs) / xs.size
    cm = np.sum((xs - mean)**k) / xs.size
    return cm
  except FloatingPointError:
    return 0

def arithmetic_mean(data):
    return central_moment(data, 1)

def variance(data):
    return central_moment(data, 2)

def skewness(data):
    return central_moment(data, 3)

def kurtosis(data):
    return central_moment(data, 4)

def tails_assymetry(data): #asymmetry of the tails
    return central_moment(data, 5)

def beta(data):
  Zero = np.std(data)
  if Zero != 0:
    try:
      return 0.3989 / Zero
    except FloatingPointError:
      return 0
  else: return

def interquartile_range(n_std, data):
    md = np.median(data)
    sigma = np.std(data) * n_std
    sigma_min = md - sigma
    sigma_max = md + sigma
    return [sigma_min, sigma_max]

# Uniqueness Ratio
def UniquenessRatio(Dataset,Dta):
  return (Dta['Unique']/Dataset.shape[0]).round(4)*100

# Unique
def Unique(Dataset):
  chng = {i: len(Dataset[i].unique()) for i in Dataset.columns}
  #Dta = pd.DataFrame({'Variable': list(chng.keys()), 'Unique': list(chng.values())})
  return list(chng.values())
# ===================================== || Classification ||

'''
Selecciona el tipo de datos y solo evaluas los numericos
'''

def VariableGrouping(Dataset):
  NumericCols      = [column for column in Dataset.columns if np.issubdtype(Dataset[column].dtype, np.number)]
  NumericData      = Dataset[NumericCols]
  AlphanumericCols = list(set(Dataset.columns)-set(NumericData.columns))
  AlphanumericData = Dataset[ AlphanumericCols ]
  return NumericData, AlphanumericData, NumericCols, AlphanumericCols

def VariableType(Dataset):
  return [x.dtype for x in Dataset]
  
def VariableClass(Dataset):
    '''
    utilizamos el método iterrows() de pandas para iterar sobre las filas del DataFrame. 
    Luego, accedemos a los valores de las columnas utilizando el diccionario row y 
    utilizamos comparaciones booleanas en lugar de convertir a cadena y buscar en la cadena. 
    También hemos eliminado las búsquedas innecesarias en el DataFrame, ya que ahora 
    utilizamos las columnas directamente en la condición. 
    Finalmente, hemos utilizado el método append() para agregar elementos a la lista chng 
    en lugar de una declaración if/else.
    '''
    chng = []
    RangoOrdinal = 20
    n=0
    for i in Dataset.dtypes.values:
      if ( 'int' in str( i ) or 'float' in str( i ) ):
        if len( Dataset[ Dataset.columns.values[n] ].unique() ) < RangoOrdinal:
          chng.append('Ordinal')
        else:
          chng.append('Continual')
      else: chng.append('Category')
      n+=1
    '''
    for i, row in Dataset.iterrows():
      if ( 'int' in str(row.dType) or 'float' in str(row.dType) ):
        if row['Unique'] < RangoOrdinal:
          chng.append('Ordinal')
        else:
          chng.append('Continual')
      else:
        chng.append('Category')'''
    return chng
# =========================================== || Datasets ||

def AdvancedMathProcessing(Dataset,reduction=True):
  if reduction == True:
    data = Dataset[ VariableGrouping(Dataset)[2] ].apply( lambda x: x.to_numpy().astype('float16') )
  else:
    data = Dataset[ VariableGrouping(Dataset)[2] ].apply( lambda x: x.to_numpy().astype('float64') )

  stats = {
        'mean':     data.apply( lambda x: arithmetic_mean(x) ).values,
        'variance': data.apply( lambda x: variance(x) ).values,
        'skewness': data.apply( lambda x: skewness(x) ).values,
        'kurtosis': data.apply( lambda x: kurtosis(x) ).values,
        'tails_assymetry':data.apply( lambda x: tails_assymetry(x) ).values,
        'beta':     data.apply( lambda x: beta(x) ).values,
    }
  return pd.DataFrame.from_dict(data=stats, orient='index', columns=VariableGrouping(Dataset)[2] ).T.round(4).reset_index().rename(columns={"index": "Name"})

def move_columns(df: pd.DataFrame, cols_to_move: list, new_index: int) -> pd.DataFrame:
    """
    This method re-arranges the columns in a dataframe to place the desired columns at the desired index.
    ex Usage: df = move_columns(df, ['Rev'], 2)   
    :param df:
    :param cols_to_move: The names of the columns to move. They must be a list
    :param new_index: The 0-based location to place the columns.
    :return: Return a dataframe with the columns re-arranged
    """
    other = [c for c in df if c not in cols_to_move]
    start = other[0:new_index]
    end = other[new_index:]
    return df[start + cols_to_move + end]

def BasicMathProcessing(Dataset):
  # obtener estadísticas descriptivas básicas
  Metrics = Dataset.describe(include='all').T

  # seleccionar las columnas necesarias
  Metrics = Metrics[['min', '25%', '50%', '75%', 'max']].round(4)
  Metrics['Unique'] = Unique(Dataset)
  Metrics['Ratio'] = UniquenessRatio(Dataset, Metrics)
  Metrics = Metrics[['Unique','Ratio','min', '25%', '50%', '75%', 'max']].reset_index().rename(columns={"index": "Name"})
  Metrics.sort_values(by=['Ratio'], ascending=True, inplace=True)
  #]
  
  return Metrics

def VariableDescription(Dataset):
  Description           = pd.DataFrame()
  Description['Name']   = Dataset.columns.values
  Description['Type']   = Dataset.dtypes.values
  Description['Class']= VariableClass(Dataset)
  Description['Nulls']  = Dataset.apply(lambda x: x.isnull().sum()).values
  Description['Count']  = Dataset.apply(lambda x: x.isnull().count()).values
  Description['len']= Description['Count'] - Description['Nulls']
  Description.pop( 'Count' )

  return Description
  

# 
#  ██████╗  █████╗ ████████╗ █████╗     ██████╗ ██╗ ██████╗████████╗
#  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔══██╗██║██╔════╝╚══██╔══╝
#  ██║  ██║███████║   ██║   ███████║    ██║  ██║██║██║        ██║   
#  ██║  ██║██╔══██║   ██║   ██╔══██║    ██║  ██║██║██║        ██║   
#  ██████╔╝██║  ██║   ██║   ██║  ██║    ██████╔╝██║╚██████╗   ██║   
#  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═════╝ ╚═╝ ╚═════╝   ╚═╝   
#  
def GetDataDictionary(Dataset,reduction):
# Advanced Metrics Dataset
  AdvancedMetrics = AdvancedMathProcessing(Dataset,reduction=reduction)
  AdvancedMetrics2=AdvancedMetrics.copy()
  AdvancedMetrics2.sort_values(by=['variance'], ascending=True, inplace=True)
  AdvancedMetrics2.set_index('Name', inplace=True)
# Basics Metrics Dataset
  BasicMetrics    = BasicMathProcessing(Dataset)
# Variable Description
  Description= VariableDescription(Dataset)
  Description2 = pd.merge(Description,BasicMetrics, how='left')
  Description2.sort_values(by=['Ratio'], ascending=True, inplace=True)
  Description2.set_index('Name', inplace=True)
# Master
  Master = pd.merge(Description,BasicMetrics, how='left')
  Master = pd.merge(Master,AdvancedMetrics, how='left')
  Master.sort_values(by=['Ratio'], ascending=True, inplace=True)
  Master.set_index('Name', inplace=True)
  #return AdvancedMetrics, BasicMetrics, Description, Master

# define artifact
# from collections import namedtuple
  MetaData = namedtuple('DataDictionary', 'Propierties Advanced DataDictionary')
  MetaData = MetaData(Description2, AdvancedMetrics2, Master)

  return MetaData

'''
Rules

Metrics to consider data [dta] as:

SI dta == texto: Categorico, revisar manual
SI-NO:
    SI Skewness dta > | 1 | Y unicos > 20:
        dta = log10(dta);
    SI-NO: none
    ---
    SI 3σ^4 < 1 Y  unicos > 20:
        SI log10( (Filas - unicos) / unicos ) > 2:
            dta == continuo
        SI-NO: 
            dta == rango //Nota: para eda se toma como ordinal, tratar de hacer bins y volver ordinal
    SI-NO:
        dta == ordinal
'''