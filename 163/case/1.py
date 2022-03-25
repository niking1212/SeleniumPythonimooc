import os

file_path = os.path.abspath(os.path.dirname(__file__)) + '\\report\\' + 'first_case.html'
file_path2 = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + '\\report\\' + 'first_case.html'
file_path1 = "D:\\pycharm\\imooc\\163\\report\\first_case.html"

print(file_path)
print(file_path1)
print(file_path2)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(base_dir, "report")
log = log_dir + '\\first_case.html'
print(log_dir)
print(base_dir)
print(log)