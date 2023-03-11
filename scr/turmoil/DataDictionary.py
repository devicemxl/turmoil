# 
#  ██████╗  █████╗ ████████╗ █████╗     ██████╗ ██╗ ██████╗████████╗
#  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔══██╗██║██╔════╝╚══██╔══╝
#  ██║  ██║███████║   ██║   ███████║    ██║  ██║██║██║        ██║   
#  ██║  ██║██╔══██║   ██║   ██╔══██║    ██║  ██║██║██║        ██║   
#  ██████╔╝██║  ██║   ██║   ██║  ██║    ██████╔╝██║╚██████╗   ██║   
#  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═════╝ ╚═╝ ╚═════╝   ╚═╝   
#                   
from numpy import percentile
import pandas as pd
import operations as op
from IPython.display import display, HTML
#
def CreateDataDictionary(Dataset):
  # ============================ Variables and unique values
  chng={}
  for i in Dataset.columns:
    chng[i]= len(Dataset[i].unique())
  #
  Dta=pd.DataFrame.from_dict( data=chng,orient='index' ).reset_index()
  Dta.columns=['Variable','Unique']
  chng=[]
  # ============================================== Data Type
  for i in Dataset.columns:
    chng.append(Dataset[i].dtype)
  Dta['Type'] = chng
  # ========================================= Variable Class
  chng=[]
  RangoOrdinal=20
  for i in Dta.index:
    j = Dta[Dta.Type.index == i].Type
    if 'float' in str(j) or 'int' in str(j):
      Dx = Dta[Dta.Type.index == i]
      if Dx.Unique.to_list()[0] < RangoOrdinal:
        chng.append( 'Ordinal' )
      else:chng.append('Continuous')
    else:chng.append('Categorical')
  chng
  Dta['Class'] = chng
  # ======================================= Uniqueness Ratio
  Dta['Ratio'] = (Dta['Unique']/Dataset.shape[0]).round(4)*100
  # ========================================= Basic Measures
  chng =[]
  for i in Dta['Variable']:
    try:
      chng.append(Dataset[i].min().round(4) )
    except:
      chng.append( None )
  Dta['Min'] = chng
  #
  chng =[]
  for i in Dta['Variable']:
    try:
      chng.append( percentile(Dataset[i], 25).round(4) )
    except:
      chng.append( None )
  Dta['q25'] = chng
  #
  chng =[]
  for i in Dta['Variable']:
    try:
      chng.append( percentile(Dataset[i], 50).round(4) )
    except:
      chng.append( None )
  Dta['q50'] = chng
  #
  chng =[]
  for i in Dta['Variable']:
    try:
      chng.append( percentile(Dataset[i], 75).round(4) )
    except:
      chng.append( None )
  Dta['q75'] = chng
  #
  chng =[]
  for i in Dta['Variable']:
    try:
      chng.append(Dataset[i].max().round(4) )
    except:
      chng.append( None )
  Dta['Max'] = chng
  #
  Dta.sort_values(by='Unique',ascending=True,inplace=True)
  Dta.sort_values(by='Class',ascending=False,inplace=True)
  #
  # Convertir en Clase el diccionario para poder tener resultado de variables:
  #     Categoricas
  #     Numericas
  # ademas de poder agregar por separado:
  #     Medidas basicas
  #     Momentos Matematicos
  #     Propiedades basicas del dataset como tipo, etc
  #
  # Dta[ Dta['Class']=='Categorical' ]
  # Dta[ Dta['Class']!='Categorical' ]
  #
  
  return Dta

def GetDataDictionary(Dataset):
    Dta=CreateDataDictionary(Dataset)
    display(HTML(Dta.to_html()))
    return Dta
