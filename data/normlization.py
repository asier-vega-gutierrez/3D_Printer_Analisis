import pandas as pd
from datetime import datetime
rutas = [
    "four_towers_original/arm_failure.json", 
    "four_towers_original/bowden.json", 
    "four_towers_original/plastic.json", 
    "four_towers_original/proper.json", 
    "four_towers_original/retraction.json",
    "four_towers_original/unstick.json"]
rutas2 = [
    "four_towers_original/arm_failure_machine.csv", 
    "four_towers_original/bowden_machine.csv", 
    "four_towers_original/plastic_machine.csv", 
    "four_towers_original/proper_machine.csv", 
    "four_towers_original/retraction_machine.csv",
    "four_towers_original/unstick_machine.csv"]
rutastxt = [
    "four_towers_original/arm_failure.txt", 
    "four_towers_original/bowden.txt", 
    "four_towers_original/plastic.txt", 
    "four_towers_original/proper.txt", 
    "four_towers_original/retraction.txt",
    "four_towers_original/unstick.txt"]
rutas2txt = [
    "four_towers_original/arm_failure_external.csv", 
    "four_towers_original/bowden_external.csv", 
    "four_towers_original/plastic_external.csv", 
    "four_towers_original/proper_external.csv", 
    "four_towers_original/retraction_external.csv",
    "four_towers_original/unstick_external.csv"]


#PARA LOS JSON
from pandas.io.json import json_normalize
df = pd.read_json(rutas[5], lines=True, convert_dates = False)
df['time2'] = pd.to_datetime(df['timestamp'], unit='ms')
df = pd.json_normalize(df.to_dict('records'))


df['coords.extr'] = df['coords.extr'].astype(str).str.strip('[]')
df['coords.xyz'] = df['coords.xyz'].astype(str).str.strip('[]')
df['coords.axesHomed'] = df['coords.axesHomed'].astype(str).str.strip('[]')
df['params.extrFactors'] = df['params.extrFactors'].astype(str).str.strip('[]')
df['temps.current'] = df['temps.current'].astype(str).str.strip('[]')
df['temps.heads.current'] = df['temps.heads.current'].astype(str).str.strip('[]')
df['temps.heads.active'] = df['temps.heads.active'].astype(str).str.strip('[]').str.strip('[]')
df['temps.tools.active'] = df['temps.heads.active'].astype(str).str.strip('[]').str.strip('[]')
df['temps.heads.standby'] = df['temps.heads.standby'].astype(str).str.strip('[]')
df['temps.heads.state'] = df['temps.heads.state'].astype(str).str.strip('[]')
df['temps.tools.standby'] = df['temps.tools.standby'].astype(str).str.strip('[]')
#df['extrRaw'] = df['extrRaw'].astype(str).str.strip('[]')

df['temps.extra'] = df['temps.extra'].astype(str).str.strip('[]')
df['temps.extra'] = df['temps.extra'].astype(str).str.strip('{}')
df[['temps.extra.name','temps.extra.temp']] = df['temps.extra'].str.split(',', expand=True)
df = df.drop('temps.extra', axis=1)
df['temps.extra.name'] = df['temps.extra.name'].str.slice(start=9)
df['temps.extra.name'] = df['temps.extra.name'].str.slice(stop=-1)
df['temps.extra.temp'] = df['temps.extra.temp'].str.slice(start=9)

print(df['temps.heads.active'])
df.to_csv(rutas2[5])



#PARA LOS TXT
#df = pd.read_csv(rutastxt[5], names=['data_id', 'accel0X', 'accel0Y', 'accel0Z', 'accel1X', 'accel1Y', 'accel1Z', 'tension', 'timestamp'], low_memory=False)
#df['time'] = pd.to_datetime(df['timestamp'], unit='ms')
#df.to_csv(rutas2txt[5])


