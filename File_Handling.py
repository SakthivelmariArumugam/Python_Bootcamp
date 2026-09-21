f=open("About",'r')
#Read Function will print whole file
print(f.read())
#Readline Function will print Every Iniditual line
print(f.readline())
print(f.readline())
#print Particular number of characters in the line
print(f.readline(4),end="$")

#File write operation
f1=open("Story",'w')
f1.write("Cloud Firestore — NoSQL database, commonly used for web/mobile apps.Cloud SQL — Managed relational databases like MySQL,PostgreSQL, and SQL Server.Cloud Spanner — Globally distributed relational database, designed for large-scale systems.BigQuery — Data warehouse for analytics and very large datasets.Firebase Realtime Database — NoSQL database with real-time data synchronization.")
#File contend append operation
f1=open("Story",'w')
f1.write("There isn't a simple fixed limit like maximum 100 users. Firebase's limits are mainly based on usage.")

#copy the data one file to another file
for data in f:
  f1.write(data)

#if you want to read any image using mode 'rb'


