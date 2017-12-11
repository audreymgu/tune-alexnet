import os

# def rename_files(dir):
#   for root, dirs, files in os.walk(dir):
#       mod_root = os.path.basename(root)
#       x = 1
#       for name in files:
#           os.rename(os.path.join(root,name), os.path.join(root, str(mod_root) + str(x) + '.jpg'))
#           x += 1

def list_files(dir):
  r = []
  i = 0
  dir_list = [x[0] for x in os.walk(dir)]
  dir_list = sorted(dir_list, key=str.lower)
  dir_list.pop(0)
  dir_list.pop(0)
  for subdir in dir_list:                                                                                            
    files = os.walk(subdir).next()[2]                                                                             
    if (len(files) > 0):                                                                                          
        for file in files:                                                                                        
            r.append(subdir + '/' + file + ' ' + str(i))
    i += 1
  return r

# # Generate tuples from os.walk
# dir_list = os.walk('data/101_obj')
# 
# # Take directory information
# dir_list = [x[0] for x in dir_list]
# 
# # Sort directories
# dir_list = sorted(dir_list, key=str.lower)
# 
# # Remove root directory
# dir_list.pop(0)

# # Print directory list
# print dir_list

# # Rename files by directory
# for i in dir_list:
#   rename_files(i)

# Create file list
master_list = list_files('data/101_obj')
  
# Print file list
# print master_list

# Create a new text file
text_list = open("list.txt","w+")

# Write in file list
for name in master_list:
  text_list.write('%s\n' % (name))

# Close text file
text_list.close()