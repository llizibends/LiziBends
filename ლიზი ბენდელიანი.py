# 1.    x=int(input ())
# except ValueError:
#     print('თქვენ არ შეგიტანიათ რიცხვი')
#     x=0
# try:
#     y=int(input())
# except ValueError:
#     print("თქვენ არ შეგიტანიათ რიცხვი")
#     y=0
# else:
#     print("ყველაფერი სწორია")
# finally:
#     print("პროგრამა 100%-ით წარმატებულად მუშაობს")
# try:
#     res=x/y
# except ZeroDivisionError:
#     print ("თქვენ შეიტანეთ 0")
#     res=0
# print(res)

# 2.# with open('test.txt', 'wt', encoding='utf-8') as inFile:
# #     num=int(input())
# #     line=str('7 / '+str(num)+'='+str(7/num))
# #     print(line)
# #     inFile.write(line)


# 3. username=('Lizi','Nino','Teo','Nini')
# looper1=username.__iter__()
# print(looper1.__next__())
# print(looper1.__next__())
# print(looper1.__next__())
# print(looper1.__next__())
# print(looper1.__next__())

# 4.პითონში %d და %s არის ფორმატირების კოდები, 
# რომლებიც გამოიყენება სტრიქონების ფორმატირების ძველ მეთოდებში. 
# ისინი მოქმედებენ როგორც ჩანაცვლების დამფუძნებლები სტრიქონის ლიტერალში,
# რომლებიც შეიცვლება ფაქტობრივი მნიშვნელობებით პროგრამის შესრულების დროს.

# 5.city={1:'Kutaisi','კუთხე':'imereti', 'ღირსშანიშნაობა':['ბაგრატი']}
# del city['კუთხე']
# print(city)

# 6. try:
#     for i in range(20):
#         print(i)
#         if i == 5:
#             raise StopIteration("Stopping the iteration at", i)
# except StopIteration as e:
#     print("Iteration stopped:", e)


# 8. my_list = [("ვაშლი", 3), ("ბანანი", 6), ("ფორთოხალი", 4)]
# for fruit, quantity in my_list:
#     print(f"მე მაქვს {quantity} {fruit}")