import sqlite3
from dsdcalls import DSDCalls
import os


calldir = 'Z:/Recordings/Radio/DSDBPD/Record'

conn = sqlite3.connect('bpdcalls.db')

c = conn.cursor()

try:
    c.execute("""CREATE TABLE bpdcalls (
                date text,
                time text,
                duration integer,
                type text,
                cc integer,
                slot text,
                calltype text,
                grp text,
                rid text,
                src text,
                unique(src)
                )""")
    print("Database created!")
except:
    print("Database already exists.")


def insert_call(bpdcall):
    with conn:
        c.execute("INSERT INTO bpdcalls VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (bpdcall.date,
        bpdcall.time, bpdcall.dur, bpdcall.type, bpdcall.cc, bpdcall.slot, bpdcall.calltype, bpdcall.group, bpdcall.rid,
        bpdcall.src))

def get_calls():
    c.execute("SELECT * FROM bpdcalls WHERE type='DMR'")
    print(c.fetchall())


os.chdir(calldir) # change dir to record dir
dirs = [d for d in os.listdir('.') if os.path.isdir(d)] # lists all in dir and only dirs
newestdir = sorted(dirs, key=lambda x: os.path.getctime(x), reverse=True)[:1] # gets newest folders
os.chdir(newestdir[0]) # change current dir to newest dir
calls = [d for d in os.listdir('.') if os.path.isfile(d)] # list all files in dir and only files
newestcall = sorted(calls, key=lambda x: os.path.getctime(x), reverse=True)[:1] # gets newest file
newcallpath = calldir + '/' + newestdir[0] + '/' + newestcall[0] # creates full path for newest file
newcallpath = newcallpath.replace('/','\\')
print(newcallpath)
newestcall = newestcall[0]
newestcall = newestcall.replace(".wav","")
calldetails = newestcall.split("_")
del calldetails[3]
calldetails.insert(0, newestdir[0])
calldetails.insert(9, newcallpath)

print(calldetails)

print(str(calldetails[9]))

curbpdcall = DSDCalls(calldetails[0], calldetails[1], calldetails[2], calldetails[3], calldetails[4], calldetails[5], calldetails[6], calldetails[7], calldetails[8], str(calldetails[9]))

try:
    insert_call(curbpdcall)
except sqlite3.IntegrityError:
    print("UNIQUE constraint; file already in DB")

get_calls()

conn.close()