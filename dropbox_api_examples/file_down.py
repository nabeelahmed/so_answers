"""

"""


import dropbox
import time

ACCESS_TOKEN = 'GfheDQ9SCcEAAAAAAAAx-qU64N5Tnp2mQ9-CQ6pdoSJHnboz21ylu6FSiw9L2J-v '

dbx = dropbox.Dropbox(ACCESS_TOKEN)
acc_info = dbx.users_get_current_account()
print acc_info, "putting to sleep ....."
time.sleep(10)
with open("test.txt", "w") as f:
	metadata, res = dbx.files_download(path="/tmp.txt")
   	f.write(res.content)

