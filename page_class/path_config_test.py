import os

# 设置文件路径的可配置
# os.path.realpath(__file__)  # 查看当前文件绝对路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试报告路径
test_report_path = os.path.join(project_path, 'report_test', 'test_result.html')
# 截图存放路径
test_screen_path = os.path.join(project_path, 'report_test', 'screen_2')

# 配置日志文件路径
test_log_path = os.path.join(project_path, 'report_test',  'logs_1', 'test_log.txt')


if __name__ == '__main__':
    print(test_log_path)