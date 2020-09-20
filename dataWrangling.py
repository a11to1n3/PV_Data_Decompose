import numpy as np
import datetime

def dataWrangling(pv_raw):
  # Weekday arranging initiation
  pv_raw['Mon'] = np.zeros(len(pv_raw))
  pv_raw['Tue'] = np.zeros(len(pv_raw))
  pv_raw['Wed'] = np.zeros(len(pv_raw))
  pv_raw['Thu'] = np.zeros(len(pv_raw))
  pv_raw['Fri'] = np.zeros(len(pv_raw))
  pv_raw['Sat'] = np.zeros(len(pv_raw))
  pv_raw['Sun'] = np.zeros(len(pv_raw))

  # Date arranging initiation
  pv_raw['h00'] = np.zeros(len(pv_raw))
  pv_raw['h01'] = np.zeros(len(pv_raw))
  pv_raw['h02'] = np.zeros(len(pv_raw))
  pv_raw['h03'] = np.zeros(len(pv_raw))
  pv_raw['h04'] = np.zeros(len(pv_raw))
  pv_raw['h05'] = np.zeros(len(pv_raw))
  pv_raw['h06'] = np.zeros(len(pv_raw))
  pv_raw['h07'] = np.zeros(len(pv_raw))
  pv_raw['h08'] = np.zeros(len(pv_raw))
  pv_raw['h09'] = np.zeros(len(pv_raw))
  pv_raw['h10'] = np.zeros(len(pv_raw))
  pv_raw['h11'] = np.zeros(len(pv_raw))
  pv_raw['h12'] = np.zeros(len(pv_raw))
  pv_raw['h13'] = np.zeros(len(pv_raw))
  pv_raw['h14'] = np.zeros(len(pv_raw))
  pv_raw['h15'] = np.zeros(len(pv_raw))
  pv_raw['h16'] = np.zeros(len(pv_raw))
  pv_raw['h17'] = np.zeros(len(pv_raw))
  pv_raw['h18'] = np.zeros(len(pv_raw))
  pv_raw['h19'] = np.zeros(len(pv_raw))
  pv_raw['h20'] = np.zeros(len(pv_raw))
  pv_raw['h21'] = np.zeros(len(pv_raw))
  pv_raw['h22'] = np.zeros(len(pv_raw))
  pv_raw['h23'] = np.zeros(len(pv_raw))

  pv_raw['01'] = np.zeros(len(pv_raw))
  pv_raw['02'] = np.zeros(len(pv_raw))
  pv_raw['03'] = np.zeros(len(pv_raw))
  pv_raw['04'] = np.zeros(len(pv_raw))
  pv_raw['05'] = np.zeros(len(pv_raw))
  pv_raw['06'] = np.zeros(len(pv_raw))
  pv_raw['07'] = np.zeros(len(pv_raw))
  pv_raw['08'] = np.zeros(len(pv_raw))
  pv_raw['09'] = np.zeros(len(pv_raw))
  pv_raw['10'] = np.zeros(len(pv_raw))
  pv_raw['11'] = np.zeros(len(pv_raw))
  pv_raw['12'] = np.zeros(len(pv_raw))
  pv_raw['13'] = np.zeros(len(pv_raw))
  pv_raw['14'] = np.zeros(len(pv_raw))
  pv_raw['15'] = np.zeros(len(pv_raw))
  pv_raw['16'] = np.zeros(len(pv_raw))
  pv_raw['17'] = np.zeros(len(pv_raw))
  pv_raw['18'] = np.zeros(len(pv_raw))
  pv_raw['19'] = np.zeros(len(pv_raw))
  pv_raw['20'] = np.zeros(len(pv_raw))
  pv_raw['21'] = np.zeros(len(pv_raw))
  pv_raw['22'] = np.zeros(len(pv_raw))
  pv_raw['23'] = np.zeros(len(pv_raw))
  pv_raw['24'] = np.zeros(len(pv_raw))
  pv_raw['25'] = np.zeros(len(pv_raw))
  pv_raw['26'] = np.zeros(len(pv_raw))
  pv_raw['27'] = np.zeros(len(pv_raw))
  pv_raw['28'] = np.zeros(len(pv_raw))
  pv_raw['29'] = np.zeros(len(pv_raw))
  pv_raw['30'] = np.zeros(len(pv_raw))
  pv_raw['31'] = np.zeros(len(pv_raw))

  pv_raw['Jan'] = np.zeros(len(pv_raw))
  pv_raw['Feb'] = np.zeros(len(pv_raw))
  pv_raw['Mar'] = np.zeros(len(pv_raw))
  pv_raw['Apr'] = np.zeros(len(pv_raw))
  pv_raw['May'] = np.zeros(len(pv_raw))
  pv_raw['Jun'] = np.zeros(len(pv_raw))
  pv_raw['Jul'] = np.zeros(len(pv_raw))
  pv_raw['Aug'] = np.zeros(len(pv_raw))
  pv_raw['Sep'] = np.zeros(len(pv_raw))
  pv_raw['Oct'] = np.zeros(len(pv_raw))
  pv_raw['Nov'] = np.zeros(len(pv_raw))
  pv_raw['Dec'] = np.zeros(len(pv_raw))

  # Data wrangling
  for i in range(len(pv_raw)):
    if pv_raw.Datetime[i][11:13] == '00':
      pv_raw['h00'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '01':
      pv_raw['h01'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '02':
      pv_raw['h02'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '03':
      pv_raw['h03'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '04':
      pv_raw['h04'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '05':
      pv_raw['h05'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '06':
      pv_raw['h06'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '07':
      pv_raw['h07'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '08':
      pv_raw['h08'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '09':
      pv_raw['h09'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '10':
      pv_raw['h10'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '11':
      pv_raw['h11'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '12':
      pv_raw['h12'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '13':
      pv_raw['h13'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '14':
      pv_raw['h14'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '15':
      pv_raw['h15'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '16':
      pv_raw['h16'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '17':
      pv_raw['h17'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '18':
      pv_raw['h18'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '19':
      pv_raw['h19'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '20':
      pv_raw['h20'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '21':
      pv_raw['h21'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '22':
      pv_raw['h22'][i] = 1
    elif pv_raw.Datetime[i][11:13] == '23':
      pv_raw['h23'][i] = 1

    pv_raw[pv_raw.Datetime[i][:2]][i] = 1

    if pv_raw.Datetime[i][4:5] == '1':
      pv_raw['Jan'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '2':
      pv_raw['Feb'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '3':
      pv_raw['Mar'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '4':
      pv_raw['Apr'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '5':
      pv_raw['May'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '6':
      pv_raw['Jun'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '7':
      pv_raw['Jul'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '8':
      pv_raw['Aug'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '9':
      pv_raw['Sep'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '10':
      pv_raw['Oct'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '11':
      pv_raw['Nov'][i] = 1
    elif pv_raw.Datetime[i][4:5] == '12':
      pv_raw['Dec'][i] = 1

    if pv_raw['Radiation'][i]>0 and pv_raw['Radiation'][i]<=100:
      pv_raw['Radiation Level'] = 0
    elif pv_raw['Radiation'][i]>100 and pv_raw['Radiation'][i]<=200:
      pv_raw['Radiation Level'] = 1
    elif pv_raw['Radiation'][i]>200 and pv_raw['Radiation'][i]<=300:
      pv_raw['Radiation Level'] = 2
    elif pv_raw['Radiation'][i]>300 and pv_raw['Radiation'][i]<=400:
      pv_raw['Radiation Level'] = 3
    elif pv_raw['Radiation'][i]>400 and pv_raw['Radiation'][i]<=500:
      pv_raw['Radiation Level'] = 4
    elif pv_raw['Radiation'][i]>500 and pv_raw['Radiation'][i]<=600:
      pv_raw['Radiation Level'] = 5
    elif pv_raw['Radiation'][i]>600 and pv_raw['Radiation'][i]<=700:
      pv_raw['Radiation Level'] = 6
    elif pv_raw['Radiation'][i]>700 and pv_raw['Radiation'][i]<=800:
      pv_raw['Radiation Level'] = 7
    elif pv_raw['Radiation'][i]>800 and pv_raw['Radiation'][i]<=900:
      pv_raw['Radiation Level'] = 8
    elif pv_raw['Radiation'][i]>900 and pv_raw['Radiation'][i]<=1000:
      pv_raw['Radiation Level'] = 9
    elif pv_raw['Radiation'][i]>1000 and pv_raw['Radiation'][i]<=1100:
      pv_raw['Radiation Level'] = 10
    elif pv_raw['Radiation'][i]>1100 and pv_raw['Radiation'][i]<=1200:
      pv_raw['Radiation Level'] = 11
    elif pv_raw['Radiation'][i]>1200 and pv_raw['Radiation'][i]<=1300:
      pv_raw['Radiation Level'] = 12
    elif pv_raw['Radiation'][i]>1300 and pv_raw['Radiation'][i]<=1400:
      pv_raw['Radiation Level'] = 13
    
    day, month, year = (int(x) for x in pv_raw.Datetime[i][:10].split('/'))
    pv_raw[datetime.date(year, month, day).strftime("%A")[:3]][i] = 1

  return pv_raw
