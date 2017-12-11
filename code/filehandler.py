import os

def list_files(dir):
  r = []
  i = 0
  dir_list = [x[0] for x in os.walk(dir)]
  dir_list = sorted(dir_list, key=str.lower)
  dir_list.pop(0)
  for subdir in dir_list:
    folder_list = []  
    files = os.walk(subdir).next()[2]                                                                             
    if (len(files) > 0):                                                                                          
        for file in files:                                                                                        
            folder_list.append(subdir + '/' + file + ' ' + str(i))
    i += 1
    r.append(folder_list)
  return r

# Create master file list
master_list = list_files('data/101_obj')

# Create sublists
tr_list = []
va_list = []
te_list = []

for sublist in master_list:
  # Training List
  tr_portion = sublist[:int(len(sublist)*.7)]
  for item in tr_portion:
    tr_list.append(item)
  # Validation List
  va_portion = sublist[int(len(sublist)*.7):int(len(sublist)*.85)]
  for item in va_portion:
    va_list.append(item)
    
for sublist in master_list:
  # Test List
  for item in sublist:
    if not item in tr_list and not item in va_list:
      te_list.append(item)
  
# Print file lists
# print master_list
# print tr_list
# print va_list

# Create a new text file
tr_text = open("@tr_list.txt","w+")
va_text = open("@va_list.txt","w+")
te_text = open("@te_list.txt","w+")

# Write in file list
for item in tr_list:
  tr_text.write('%s\n' % (item))
for item in va_list:
  va_text.write('%s\n' % (item))
for item in te_list:
  te_text.write('%s\n' % (item))
  
# Close text file
tr_text.close()
va_text.close()
te_text.close()