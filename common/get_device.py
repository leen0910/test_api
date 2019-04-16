# -*- coding:utf-8 -*-
import csv

class GetDevices:
    def test_readdevices(self):
        """读取设备信息"""
        filename = 'C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\test_device.csv'
        data = []
        try:
            with open(filename,'rt',encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader)
                data = [row for row in reader]
        except csv.Error as e:
            print("Error reading CSV file at line %s: %s"%(reader.line_num, e))
        return data

    def tearDown(self):
        pass

if __name__ == "__main__":
    t=GetDevices()
    t.test_readdevices()
