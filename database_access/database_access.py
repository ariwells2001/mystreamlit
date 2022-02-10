import streamlit as st
import mysql.connector
import pandas as pd
import mysql.connector
import seaborn as sns
#from influxdb import InfluxDBClient
import numpy as np
from PIL import Image

image = Image.open("ariwells-logo.jpg")
st.sidebar.image(image,width = 200)

#databaseName = ["Select a Database","MySQL","InfluxDB-1.8"]
databaseName = ["Select a Database","MySQL"]
st.sidebar.title("Database Access")
databaseChoice = st.sidebar.selectbox("Database",databaseName)
userID = ""
userPasswrod = ""
selectedDB = ""
hostAddress =""
connectOK=False
#dbCategory = ["Database List"]

if databaseChoice == "MySQL":
    st.title("Access to MySQL")
    userID = st.sidebar.text_input("User Name",value="iotuser")
    userPassword = st.sidebar.text_input("Password",value="iot12345",type="password")
    #selectedDB = st.text_input("Database",value="iot")
    hostAddress = st.sidebar.text_input("Host",value='142.93.75.207')
    connectOK=st.sidebar.button("Connect")
    connection = mysql.connector.connect(host=hostAddress,user=userID,password=userPassword)
    mycursor = connection.cursor()
    mycursor.execute("show databases")
    dbCategory = pd.DataFrame(list(mycursor))
    dbName = st.selectbox("Database", dbCategory)
    mycursor.execute("use {}".format(dbName))
    mycursor.execute("show tables")
    tableList = pd.DataFrame(list(mycursor))
    tableName = st.selectbox("Table List",tableList)
    mycursor.execute("show columns from {}".format(tableName))
    keywordList = pd.DataFrame(list(mycursor))
    keywordName = st.multiselect("Keyword List",keywordList)
    numberofKey=len(keywordName)
    if numberofKey == 1:
        mycursor.execute("select {} from {}".format(keywordName[0],tableName))
        valueList = pd.DataFrame(list(mycursor))
        valueList.columns = [keywordName[0]]
        st.text_area("Query Result",pd.DataFrame.to_string(valueList),height=300)
        st.bar_chart(valueList)
    elif numberofKey == 2:
        mycursor.execute("select {},{} from {}".format(keywordName[0],keywordName[1],tableName))   
        valueList = pd.DataFrame(list(mycursor))
        valueList.columns = [keywordName[0],keywordName[1]]
        st.text_area("Query Result",pd.DataFrame.to_string(valueList),height=300)
        g = sns.PairGrid(valueList,hue=valueList.columns[0])
        g.map_diag(sns.histplot)
        g.map_offdiag(sns.scatterplot)
        g.add_legend()
        g.savefig("output.png")
        st.pyplot(g)
    elif numberofKey == 3:
        mycursor.execute("select {},{},{} from {}".format(keywordName[0],keywordName[1],keywordName[2],tableName))   
        valueList = pd.DataFrame(list(mycursor))
        valueList.columns = [keywordName[0],keywordName[1],keywordName[2]]
        st.text_area("Query Result",pd.DataFrame.to_string(valueList),height=300)
        g = sns.PairGrid(valueList,hue=valueList.columns[0])
        g.map_diag(sns.histplot)
        g.map_offdiag(sns.scatterplot)
        g.add_legend()
        g.savefig("output.png")
        st.pyplot(g)
    elif numberofKey == 4:
        mycursor.execute("select {},{},{},{} from {}".format(keywordName[0],keywordName[1],keywordName[2],keywordName[3],tableName))   
        valueList = pd.DataFrame(list(mycursor))
        valueList.columns = [keywordName[0],keywordName[1],keywordName[2],keywordName[3]]
        st.text_area("Query Result",pd.DataFrame.to_string(valueList),height=300)
        g = sns.PairGrid(valueList,hue=valueList.columns[0])
        g.map_diag(sns.histplot)
        g.map_offdiag(sns.scatterplot)
        g.add_legend()
        g.savefig("output.png")
        st.pyplot(g)
    if numberofKey > 4:
        mycursor.execute("select * from {}".format(tableName))   
        valueList = pd.DataFrame(list(mycursor))
        valueList.columns = keywordName
        st.text_area("Query Result",pd.DataFrame.to_string(valueList),height=300)
        g = sns.PairGrid(valueList,hue=valueList.columns[0])
        g.map_diag(sns.histplot)
        g.map_offdiag(sns.scatterplot)
        g.add_legend()
        g.savefig("output.png")
        st.pyplot(g)
    
    if connectOK or dbName:
        mycursor.execute("use {}".format(dbName)) 
        #result=pd.DataFrame(list(mycursor))
        #connection.commit()
        #mycursor.execute("show tables")
        #result=pd.DataFrame(list(mycursor))
        #connection.commit()
        #st.table(result)
        #result = mycursor.execute("show tables")
        #connection.commit()
        #st.write(pd.DataFrame(result))
        #st.table(dbCategory)



# elif databaseChoice == "InfluxDB-1.8":
#     st.title("Access to InfluxDB-1.8")
#     userID = st.sidebar.text_input("User Name",value="iotuser")
#     userPassword = st.sidebar.text_input("Password",value="iot12345",type="password")
#     #selectedDB = st.text_input("Database",value="iot")
#     hostAddress = st.sidebar.text_input("Host",value='112.157.171.74')
#     port = st.sidebar.text_input("Port", value = "38086")
#     #dbName =st.text_input("Database",value="homeassistant")
#     connectOK=st.sidebar.button("Connect")
#     con = InfluxDBClient(host=hostAddress,port=port,username=userID,password=userPassword)
#     dbCategoryTemp = con.query("show databases")
#     temp = list(dbCategoryTemp.get_points())
#     #st.write(list(temp[2].values()))
#     #st.write(len(temp))
#     dummy = []
#     for i in range(len(temp)):
#         dummy.append(list(temp[i].values()))
#         #st.write(dummy)
#     dummy1 = np.array(dummy)
#     finalList = dummy1.flatten()
#     #dbCategory = pd.DataFrame(list(dbCategoryTemp))
#     #dbName = st.selectbox("Database", dbCategory)
#     dbName = st.selectbox("Database", finalList)
#     con.switch_database(dbName)
#     measureCategoryTemp = con.query("show measurements")
#     temp = list(measureCategoryTemp.get_points())
#     #st.write(list(temp[2].values()))
#     #st.write(len(temp))
#     dummy = []
#     for i in range(len(temp)):
#         dummy.append(list(temp[i].values()))
#         #st.write(dummy)
#     dummy1 = np.array(dummy)
#     finalList = dummy1.flatten()
#     measureName = st.selectbox("Measurements", finalList)
#     sensorValue = con.query('select time,entity_id,value from "{}" order by time desc limit 100'.format(measureName))
#     temp = list(sensorValue.get_points())
#     valueList = pd.DataFrame(temp)
#     st.text_area("Query Result",pd.DataFrame.to_string(valueList),height=300)
    


else:
    st.title("Please select a remote database!!")
    


