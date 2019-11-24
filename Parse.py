import os
import shutil
import random
import string

os.chdir(r'/Users/ryanjoseph/Desktop/NMIL/Dataset/Participant_Data')
print('\nStarting Script!\n')

bool = 0
max_person = 1

for i in os.listdir():
    file_name, file_ext = os.path.splitext(i)
    if file_ext == "":
        text, person_no = file_name.split('_')
        #if max_person <= int(person_no):
            #max_person = person_no

calibration = 0

os.chdir(r'/Users/ryanjoseph/Desktop/NMIL/Dataset/Participant_Data/Participant_'+str(max_person))

for i in os.listdir():
    if i == 'Baseline':
        calibration =1

os.chdir(r'/Users/ryanjoseph/Desktop/NMIL/Dataset/Participant_Data')

if calibration ==0:
    os.makedirs('./Participant_'+str(max_person)+'/Baseline')
    shutil.move('./RawData.csv','./Participant_'+str(max_person)+'/Baseline'+'/RawData')
    shutil.move('./RawData.gdf','./Participant_'+str(max_person)+'/Baseline'+'/RawData.gdf')
    shutil.move('./RawData.edf','./Participant_'+str(max_person)+'/Baseline'+'/RawData.edf')
    for i in os.listdir():
        file_name, file_ext = os.path.splitext(i)
        if file_ext == ".mp4":
            mp4_name=i;
            shutil.move('./'+i,'./Participant_'+str(max_person)+'/Baseline/'+i)
    print('Moved the data to baseline folder.\n')
else:
    video_num = random.randint(0,9)
    f = open('video_record.txt','a+')
    nf = open('video_record.txt','r')
    temp1 = nf.readline()
    temp=[]

    for i in temp1:
        a = int(i)
        temp.append(a)
        #print('temp')

    if len(temp) < 10:
        while video_num in temp:
            video_num = random.randint(0,9)
            #print('while')
    last_video =0
    if temp != []:
        last_video= temp[-1]+1
    if len(temp) <10:
        print('Video to watch: ', video_num+1)
        print('\n')
        f.write(str(video_num))

    print('There are '+ str(10-len(temp))+ ' more video to watch.\n')

    if len(temp) <= 10:
        if len(temp)!=10:
            os.makedirs('./Participant_'+str(max_person)+'/Video_'+str(video_num+1))

        mp4_name= ''

        if last_video:
            shutil.move('./RawData.csv','./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/RawData.csv')
            shutil.move('./RawData.gdf','./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/RawData.gdf')
            shutil.move('./RawData.edf','./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/RawData.edf')
            for i in os.listdir():
                file_name, file_ext = os.path.splitext(i)
                if file_ext == ".mp4":
                    mp4_name=i;
                    shutil.move('./'+i,'./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/'+i)
            os.rename('./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/RawData.csv','./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/Participant_'+str(max_person)+'_Video_'+str(last_video)+'_trial_'+str(len(temp))+'.csv')
            os.rename('./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/RawData.gdf','./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/Participant_'+str(max_person)+'_Video_'+str(last_video)+'_trial_'+str(len(temp))+'.gdf')
            os.rename('./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/RawData.edf','./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/Participant_'+str(max_person)+'_Video_'+str(last_video)+'_trial_'+str(len(temp))+'.edf')
            os.rename('./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/'+mp4_name,'./Participant_'+str(max_person)+'/Video_'+str(last_video)+'/Participant_'+str(max_person)+'_Video_'+str(last_video)+'_trial_'+str(len(temp))+'.mp4')

            print('The data was successfully saved to folder Participant_'+str(max_person)+'/Video_'+str(last_video))
            if len(temp)==10:
                print('\n All videos are watched!!!\n STOP ! \n')
                shutil.move('./video_record.txt','./Participant_'+str(max_person)+'/video_record.txt')

# Taking User Input

quest = input("\nDid the Raw Data Files Save Correctly? (y/n)\n")

if quest == 'y':
    print('\n###############    Completed Script!!    ###############\n')
else:
    print('\nFuck!!\n')
    #print('Last Video: ', last_video)

# Copy Data in those folders

    #os.makedirs('./Participant_'+str(max_person)+'/Junk_Data')
    shutil.move('/Users/ryanjoseph/Desktop/NMIL/Dataset/Participant_Data/Participant_1/Video_2/', './')

# Then Delete Folders







