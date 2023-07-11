import pandas as pd
rutas = [
    "four_towers/arm_failure/head_arm_failure.txt", 
    "four_towers/bowden/bowden_accel.txt", 
    "four_towers/plastic/accel_plastic.txt", 
    "four_towers/proper/accel.txt", 
    "four_towers/retraction/retraction_05.txt",
    "four_towers/unstick/accel_unstick.txt"]

nombre = ["arm_failure","bowden","plastic","proper","retraction","unstick" ]

#serie = pd.Series(["arm_failure"], index=all)


df = [pd.DataFrame,pd.DataFrame,pd.DataFrame,pd.DataFrame,pd.DataFrame,pd.DataFrame]
for i, ruta in enumerate(rutas):
    dftemp = pd.read_csv(ruta, names=['data_id', 'accel0X', 'accel0Y', 'accel0Z', 'accel1X', 'accel1Y', 'accel1Z', 'tension', 'timestamp'], low_memory=False)
    dftemp['quality'] = nombre[i]
    dftemp['time'] = pd.to_datetime(dftemp['timestamp'], unit='ms')
    df[i] = dftemp
    
    
dfmerge = pd.concat([df[0],df[1],df[2],df[3],df[4],df[5]])
dfmerge.insert(0, 'new_id', range(0, len(dfmerge)))
dfmerge.to_csv('out.csv', index=False)

print(df[0])
print(df[1])
print(df[2])
print(df[3])
print(df[4])
print(df[5])


