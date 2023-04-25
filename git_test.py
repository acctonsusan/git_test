from os import system
from time import localtime, strftime


commitText = input('請填寫備註：')
# git push
def create_git_push():
  command_arr = [
    'git pull origin master', # 从远程获取代码并合并本地的版本
    'git add .', # 添加目录到缓存区
    f'git commit -m {commitText}', # 将暂存区内容添加到仓库中
    #'git push -u origin "master"' # push到远程仓库
    'git remote add origin https://github.com/acctonsusan/git_test.git'
    'git push  origin <master> -u'
  ]
  for command in command_arr:
    system(command)

# 時間
nowTime = ''
def get_time():
  nowTime = strftime('%Y-%m-%d %H:%M:%S', localtime())

# 创建文件
#def create_txt():
#  file = open(r'F:\2022\python-auto\gitlog.txt','w')
#  file.write(f'創建：{nowTime} 备注信息：{commitText}')

if __name__ == "__main__":
  get_time()
 # create_txt()
  create_git_push()
