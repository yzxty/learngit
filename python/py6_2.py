import unittest
import json


def convert_file_format(input_file_path: str, output_file_path: str, input_format: str = 'csv', output_format: str = 'json'):
    fo = open(input_file_path, "r", encoding='UTF-8')  # 打开csv文件
    ls=[]
    for line in fo:
        line=line.replace("\n","")  #将换行换成空
        ls.append(line.split(","))  #以，为分隔符
    fo.close()  #关闭文件流
    fw=open(output_file_path,"w",encoding='UTF-8')  #打开json文件
    for i in range(1,len(ls)):  #遍历文件的每一行内容，除了列名
        ls[i]=dict(zip(ls[0],ls[i]))  #ls[0]为列名，所以为key,ls[i]为value,
        #zip()是一个内置函数，将两个长度相同的列表组合成一个关系对
    json.dump(ls[1:],fw,sort_keys=True,indent=4,ensure_ascii=False)
    fw.close()

class StudentIOTest(unittest.TestCase):
    def test_convert_file_format(self):
        convert_file_format('./student.csv', './student.json', 'csv', 'json')

        with open('./student.json', 'r', encoding='utf8') as f:
            students = json.load(f)
        print(students[0])
        self.assertDictEqual(students[0], {
            'age': '18' ,'class': '高三三班','gender': '男','name': '张三',  'score': '98'
        })


if __name__ == '__main__':
    unittest.main()
