# viết chương trình đổi chỗ 2 ký tự đầu tiên của s1 và s2 cho nhau. Sau đó hiển thị ra màn hình chuỗi mới có giá trị s1 + " " + s2.

# Ví dụ:

# Nếu bạn nhập s1 = "sun", s2 = "moon" thì màn hình sẽ hiển thị ra "mon suon"
# Nếu bạn nhập s1 = "apple", s2 = "banana" thì màn hình sẽ hiển thị ra "baple apnana"

s1 = input()
s2 = input()

s3=s1[:2] +s2[2:]
s1 = s2[0:2] + s1[2:]
s2 = s3

print(s1 + " " + s2)    