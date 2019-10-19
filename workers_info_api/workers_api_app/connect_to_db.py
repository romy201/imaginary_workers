import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='albert2077',
    database='workers_info'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE workers_info")

# workers_query = "CREATE TABLE workers (id INT AUTO_INCREMENT PRIMARY KEY," \phone's and salary's datatype were changed
# " first_name VARCHAR(255), last_name VARCHAR(255), phone INT, salary INT)"   to a VARCHAR(255) for tiny stupid reasons
#
# jobs_query = "CREATE TABLE jobs (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
#
# workers_jobs_query = "CREATE TABLE workers_jobs (worker_id INT, job_id INT)"
#
# paradigm_query = "CREATE TABLE paradigm (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
#
# jobs_paradigms_query = "CREATE TABLE jobs_paradigms (job_id INT, paradigm_id INT)"

lvl1 = '10,000'
lvl2 = '15,000'
lvl3 = '20,000'
lvl4 = '40,000'

sqlformula_workers = 'INSERT INTO workers (first_name, last_name, phone, salary) VALUES (%s, %s, %s, %s)'

workers = [('Bob', 'Espey', '054837363', lvl1),
           ('Kendal', 'Litwin', '027838494', lvl3),
           ('Arlie', ' Wedderburn', '09757632', lvl2),
           ('Emanuel', 'Stratton', '073842647', lvl4),
           ('Leonarda', 'Jarman', '0541728833', lvl4),
           ('namefrom', 'namegenerator', '06857734', lvl1),
           ('Hipolito', 'Hernadez', '047563831', lvl3),
           ('Calandra', 'Colon', '087563739', lvl1),
           ('Shawn', 'Eich', '0372648311', lvl1),
           ('Marva', 'Haack', '012847832', lvl2)
           ]


mycursor.executemany()

mydb.commit()
