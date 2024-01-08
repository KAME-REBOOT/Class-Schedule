import re
import streamlit as st
import csv
import pandas as pd
with open(r"Class Schedule.txt", 'r') as file:
    s = file.read()

add = st.button('Add Time Table')
if add:
    schd = ''
    schd = st.text_area('Time Table')
    if schd!='':
        with open(r"Class Schedule.txt", 'w') as file:
            file.write(schd)
        with open(r"Class Schedule.txt", 'r') as file:
            s = file.read()
print(s)
if s:
    def split_string_at_elements(input_string, split_elements):
        pattern = '|'.join(re.escape(element) for element in split_elements)
        result = re.split(pattern, input_string)
        result = [item for item in result if item]

        return result

    #s = input()

    dps_ = split_string_at_elements(s, ['\n'])#' ', '\t'])
    dps = []
    for x in dps_:
        dps.append(split_string_at_elements(x, [' ', '\t']))

    for x in dps[::2]:
        locals()[x[0]]={}
        #print(x[0])
    for x in dps:
        if x[0]!='LAB':
            locals()[x[0]][x[1]]=x[2:]
        else:
            locals()[y][x[0]]=x[1:]
        y=x[0]

    #------------------------------------------------------------------------------------------------------------------------------#
    #------------------------------------------------------------------------------------------------------------------------------#

    day = st.selectbox('Day', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
    if day:
        day = day.upper()
        daytt = locals()[day]

        tslots = {0:'8:00', 1:'8:55', 2:'9:50', 3:'10:45', 4:'11:40', 5:'12:35', 6:'2:00', 7:'2:55', 8:'3:50', 9:'4:45', 10:'5:40', 11:'6:35'}
        lslots = {0:'8:00', 1:'8:50', 2:'9:50', 3:'10:45', 4:'11:40', 5:'12:30', 6:'2:00', 7:'2:50', 8:'3:50', 9:'4:40', 10:'5:40', 11:'6:30'}

        theory = []
        lab = []
        for y, x in enumerate(daytt['THEORY']):
            sl = x.split('-')
            if len(sl)>2:
                time = tslots[y]
                #print(time)
                sub = sl[1]
                #print(sub)
                venue = '-'.join(sl[3:5])
                #print(venue)
                theory.append([time, sub, venue])
        for y, x in enumerate(daytt['LAB']):
            sl = x.split('-')
            if len(sl)>2:
                time = lslots[y-1]
                #print(time)
                sub = sl[1]
                #print(sub)
                venue = '-'.join(sl[3:5])
                #print(venue)
                lab.append([time, sub, venue])

        st.write('Theory')
        file = open("theory.csv", "w", encoding = 'utf-8')
        Writer = csv.writer(file)
        Writer.writerow(['Time', 'Subject', 'Venue'])
        for row in theory :
            Writer.writerow(row)
        file.close()
        file = open("theory.csv", "r", encoding = 'utf-8')
        c = file.read
        df = pd.read_csv("theory.csv", encoding = 'utf-8')
        st.dataframe(df) 
        
        st.write('Lab')
        file = open("lab.csv", "w", encoding = 'utf-8')
        Writer = csv.writer(file)
        Writer.writerow(['Time', 'Subject', 'Venue'])
        for row in lab :
            Writer.writerow(row)
        file.close()
        file = open("lab.csv", "r", encoding = 'utf-8')
        c = file.read
        df = pd.read_csv("lab.csv", encoding = 'utf-8')
        st.dataframe(df) 
