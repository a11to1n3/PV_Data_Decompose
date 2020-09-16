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

    
    day, month, year = (int(x) for x in pv_raw.Datetime[i][:10].split('/'))
    pv_raw[datetime.date(year, month, day).strftime("%A")[:3]][i] = 1

  return pv_raw
