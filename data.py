d={
    'id':[1,2,3,5,4,6,7,9,8,5,2],
    "hiredate":['01-jun-2000','8-sep-2000','01-dec-2000','28-sep-2000','8-jan-2001','8-jan-2002','8-jan-2002','18-feb-2002','12-feb-2002','28-sep-2000','8-sep-2000'],
    "sal":[5000,4000,2000,3000,4000,10000,2000,7000,9000,3000,'4000'],
    "comm":[0,400,None,100,200,100,250,300,100,100,400],
    "job":['manager','analyst','salesman','clerk',None,'president','salesman','Developer','Data scientist','clerk','analyst'],
    "record_year":[2000,2000,2000,2000,2001,2002,None,2002,2002,2000,'2000']
}

import pandas as pd
df = pd.DataFrame(d)
df.to_excel('employeee.xlsx',index=False)
