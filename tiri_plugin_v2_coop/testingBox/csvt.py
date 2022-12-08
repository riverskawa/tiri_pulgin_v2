import csv

# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  writer.writerow(['姓名', '身高', '體重'])

  # 寫入另外幾列資料
  writer.writerow(['令狐沖', 175, 60])
  writer.writerow(['岳靈珊', 165, 57])