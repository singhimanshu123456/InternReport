import os

os.system('git init')

os.system('git remote add origin https://github.com/singhimanshu123456/InternReport.git')
os.system('git config --global user.name "{}"'.format("hilnu"))
os.system('git config --global user.email "{}"'.format("t-hilnu@expediagroup.com"))

os.system("git add .")

os.system('git commit -m "{}"'.format("ADD UPDATED DOCS"))

os.system("git push origin master")
