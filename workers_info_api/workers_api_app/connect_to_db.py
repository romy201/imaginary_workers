import json
import random
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

# lvl1 = '10,000'
# lvl2 = '15,000'
# lvl3 = '20,000'
# lvl4 = '40,000'
#
# sqlformula_workers = 'INSERT INTO workers (first_name, last_name, phone, salary) VALUES (%s, %s, %s, %s)'
#
# workers = [('Bob', 'Espey', '054837363', lvl1),
#            ('Kendal', 'Litwin', '027838494', lvl3),
#            ('Arlie', ' Wedderburn', '09757632', lvl2),
#            ('Emanuel', 'Stratton', '073842647', lvl4),
#            ('Leonarda', 'Jarman', '0541728833', lvl4),
#            ('namefrom', 'namegenerator', '06857734', lvl1),
#            ('Hipolito', 'Hernadez', '047563831', lvl3),
#            ('Calandra', 'Colon', '087563739', lvl1),
#            ('Shawn', 'Eich', '0372648311', lvl1),
#            ('Marva', 'Haack', '012847832', lvl2)
#            ]

# sqlformula_jobs = 'INSERT INTO jobs (name) VALUES (%s)'
#
# jobs = [
#     ('Statistician',),
#     ('Marketing Manager',),
#     ('Artist',),
#     ('Computer Programmer',),
# ]

# workers_id_que = ["SELECT id FROM workers", "SELECT id FROM jobs"]
#
# work_job_ids = {}
# for query in workers_id_que:
#     mycursor.execute(query)
#     my_result = mycursor.fetchall()
#     work_job_ids[query[7:]] = my_result
#
#
# worker_jobs_table = []
# for worker in work_job_ids['id FROM workers']:
#     worker = worker[0]
#     his_jobs = []
#     num_of_jobs_he_has = random.randrange(1, 7)
#     for not_important in range(num_of_jobs_he_has):
#         random_job = work_job_ids['id FROM jobs'][random.randrange(5)][0]
#         if random_job not in his_jobs:
#             his_jobs.append(random_job)
#             worker_jobs_table.append((worker, random_job))
#
#
# worker_jobs_que = "INSERT INTO workers_jobs (worker_id, job_id) VALUES (%s, %s)"
#
# mycursor.executemany(worker_jobs_que, worker_jobs_table)
# mydb.commit()


# paradigms_que = "INSERT INTO paradigm (name) VALUES (%s)"
# paradigms = [
#     ('design stuff',),
#     ('data',),
#     ('reference something silly',)
# ]
# mycursor.executemany(paradigms_que, paradigms)
# mydb.commit()

# jobs_paradigms_que = "INSERT INTO jobs_paradigms (job_id, paradigm_id) VALUES (%s, %s)"
#
# jobs_paradigms_table = [('1', '1'),
#                         ('2', '2'),
#                         ('3', '2'),
#                         ('3', '3'),
#                         ('4', '1'),
#                         ('5', '1'),
#                         ('5', '2'),
#                         ('5', '3')]
# mycursor.executemany(jobs_paradigms_que, jobs_paradigms_table)
# mydb.commit()


# data base creation done.
# -------------------------------------------------------------------------------------------------------------------- #
# now creation of the json file

workers_query = "SELECT * FROM workers"
workers_jobs_que = "SELECT job_id FROM workers_jobs WHERE worker_id = {0}"
specific_job_que = "SELECT name FROM jobs WHERE id = {0}"
mycursor.execute(workers_query)
workers_list_unorganized = mycursor.fetchall()
list_of_workers = []
all_info = {}

for worker in workers_list_unorganized:
    worker_jobs = []
    mycursor.execute(workers_jobs_que.format(worker[0]))
    worker_jobs_ids = mycursor.fetchall()
    for job in worker_jobs_ids:
        mycursor.execute(specific_job_que.format(job[0]))
        job = mycursor.fetchall()
        worker_jobs.append(job[0][0])

    dict_worker = {
        'ID': worker[0],
        'first_name': worker[1],
        'last_name': worker[2],
        'phone': worker[3],
        'salary': worker[4],
        'job_or_jobs': worker_jobs
    }
    list_of_workers.append(dict_worker)

all_info['workers'] = list_of_workers


all_jobs_que = "SELECT * FROM jobs"
jobs_paradigms_que = "SELECT paradigm_id FROM jobs_paradigms WHERE job_id = {0}"
specific_paradigm_que = "SELECT name FROM paradigm WHERE id = {0}"
list_of_jobs = []

mycursor.execute(all_jobs_que)
jobs_list_unorganized = mycursor.fetchall()

for job in jobs_list_unorganized:
    job_paradigms = []
    mycursor.execute(jobs_paradigms_que.format(job[0]))
    jobs_paradigms_ids = mycursor.fetchall()
    for paradigm in jobs_paradigms_ids:
        mycursor.execute(specific_paradigm_que.format(paradigm[0]))
        paradigm = mycursor.fetchall()
        job_paradigms.append(paradigm[0][0])

    dict_job = {
        'name': job[1],
        'paradigm': job_paradigms
    }
    list_of_jobs.append(dict_job)

all_info['jobs'] = list_of_jobs


all_paradigms_que = "SELECT name FROM paradigm"
mycursor.execute(all_paradigms_que)
paradigm_list_unorganized = mycursor.fetchall()

list_of_paradigms = []

for paradigm in paradigm_list_unorganized:
    list_of_paradigms.append(paradigm[0])

all_info['paradigms'] = list_of_paradigms

with open('app_related_data/the_workers_info.json', 'w') as f:
    json.dump(all_info, f, indent=2)

