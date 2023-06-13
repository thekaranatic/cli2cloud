# import os
# print(dir(os))
# help(os.error)

# from fileformats import dict_file_formats as ext
# print(dir(ext))

# import appwrite.client
# print(dir(appwrite.client.storage))
# print("https://cloud.appwrite.io/v1")

# import random as rnd
# print(dir(rnd.ran))

# import string
# import secrets

# BUCKET_RAND = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(0,20))
# BUCKET_ID = "C2CBUCK" + BUCKET_RAND

# FILE_ID = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(0,20))  
# print(BUCKET_ID)

# result = {
#     '$id': 'QWJ2g9eSsjhh4AXHU4qr', 
#     '$createdAt': '2023-06-07T11:43:42.137+00:00', 
#     '$updatedAt': '2023-06-07T11:43:42.137+00:00', 
#     '$permissions': [], 
#     'fileSecurity': False, 
#     'name': 'bucket-1', 
#     'enabled': True, 
#     'maximumFileSize': 3000000000, 
#     'allowedFileExtensions': [], 
#     'compression': 'none', 
#     'encryption': True, 
#     'antivirus': True
# }

# bucket_id = result['$id']
# bucket_name = result['name']
# bucket_created_dt = result['$createdAt']

# index_of_T = bucket_created_dt.find('T')
# index_of_period = bucket_created_dt.index('.')

# bucket_created_date = bucket_created_dt[:index_of_T]
# bucket_created_time = bucket_created_dt[index_of_T+1:index_of_period-3]

# print("Bucket '{}' created at {} on {}".format(bucket_name, bucket_created_time, bucket_created_date))

buckets = []
fr = open("./data/buckets.txt","r")
data = fr.readlines()

for id in data:
    bucket_ids = id.split("\n")
    buckets.append(bucket_ids[0])

print(buckets)


timestamp = '2023-06-09T12:49:42.910+00:00'

# Convert the timestamp to a datetime object
datetime_obj = datetime.datetime.fromisoformat(timestamp[:-6])

# Get the user's local time zone
user_timezone = pytz.timezone(datetime.datetime.now(pytz.timezone('UTC')).astimezone().tzinfo.zone)

# Convert the datetime object to the user's local time zone
localized_datetime = datetime_obj.astimezone(user_timezone)

# Format the localized datetime in a user-friendly format
user_friendly_format = localized_datetime.strftime('%Y-%m-%d %H:%M:%S')

print(user_friendly_format)

