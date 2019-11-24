import os
import shutil
import random
import string

os.chdir(r'C:\Users\Lab Guest\Desktop\Dataset\Participant_Data')


max_person =1

for i in os.listdir():
    file_name, file_ext = os.path.splitext(i)
    if file_ext == "":
        text, person_no = file_name.split('_')
        if max_person <= int(person_no):
            max_person = person_no

os.makedirs('./Participant_'+str(max_person)+'/Calibration')

 shutil.move('./RawData.csv','./Participant_'+str(max_person)+'/Calibration/RawData.csv')
    shutil.move('./RawData.gdf','./Participant_'+str(max_person)+'/Calibration/RawData.gdf')
    shutil.move('./RawData.edf','./Participant_'+str(max_person)+'/Calibration/RawData.edf')
W
