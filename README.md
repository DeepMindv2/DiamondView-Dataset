# DiamondView-Dataset

This is a dataset we at the Neuro-Machine-Interaction Lab [1] at USF created. This dataset is going to be a EEG dataset set to record Emotion and Personality as it relates to EEG signals. The EEG system we are using is going to be the G-Tec Nautilus (32 Channel). We are going to record various data from participants while they watch a series of emotion envoking videos provided by DiamondView. Participants also take a series of surveys before and after watching the videos. 

Qualtrics Survey: https://usf.az1.qualtrics.com/jfe/form/SV_efzyfh3faHRIn7T 

# Data
The data is going to be saved in 4 formats: CSV, GDF, MP4, and EDF. 
- CSV File = EEG Data
- GDF File = EEG Data
- MP4 File = Frontal Face Camera Data
- EDF File = EEG Data
- ________ = Heart Rate Data
- ________ = Thermal Camera Data

![Image of Participant Repository](https://github.com/DeepMindv2/DiamondView-Dataset/blob/master/Screen%20Shot%202020-01-23%20at%209.17.43%20AM.png) ![Images of Participant Folder](https://github.com/DeepMindv2/DiamondView-Dataset/blob/master/Screen%20Shot%202020-01-23%20at%209.17.53%20AM.png)

# Devices
EEG Device
- G-Tec Nautilus: 32 Channel 
- Sampling Rate: 250 Hz
- Channels: 10-20 System

Thermal Camera 
- Manufacturer: 

Frontal Face Camera
- Manufacturer: Razer Kyo 
- FPS: 1080

Finger Heart Rate Sensor
- Manufacturer: 

# Instructions
Python script curates data acquisition into correct data folder
`<python3 run.py>` 



# Videos 
1.	Volvo Moments – https://youtu.be/pjQt2IEZIXg   (video unavailable)
2.	Gift – https://youtu.be/JMs7dkdO4YY 
3.	Shoulders of Giants – https://youtu.be/Ffp78Q3yHU0 
4.	Duracell: Derrick Coleman – https://youtu.be/d_q0O80KP1c 
5.	Principal: Renovation – https://youtu.be/ONSmv4olOWg 
6.	Scientology: You – https://www.youtube.com/watch?v=wj2JP1BzhfQ 
7.	Thai Life Insurance: Unsung Hero – https://www.youtube.com/watch?v=uaWA2GbcnJU 
8.	Dick’s Sporting Goods: Heart of Gold – https://www.youtube.com/watch?v=SKMICJB3dI0 (not working)
9.	PTSD Social Experiment – https://www.youtube.com/watch?v=yMm1YeSsEWo
10.	Apple: Christmas – https://www.youtube.com/watch?v=v76f6KPSJ2w 


# To Do
- [ ] Find and Order Thermal Camera
- [ ] Find and Order Finger Heart Rate Sensor 
- [ ] Configure the Data acquisition systems for the heart rate sensors 
- [ ] Configure the Data acquisition systems for the Thermal Camera 
- [ ] Verify Python Scripts
- [ ] Verify Qualtrics survey 
- [ ] Complete another test run with all pHD students watching 
- [ ] Work on Visualization for Diamond View 
- [ ] Test fixed G-tec to see if EDF File writer works
- [ ] Get downloaded Diamond View Videos 


# References
[1] https://www.neurosymbiosis.com 
