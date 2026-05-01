# #task1
# inventory = {}
# with open('./inventory.txt','r') as file:
#     for line in file:
#         try:
#             item, quantity = line.split(':')
#             quantity = int(quantity.strip())
#             if item.upper() in inventory.keys():
#                 inventory[item.upper()] += quantity
#         except ValueError:
#             with open('./audit_error.log', 'a') as err:
#                 err.write(line)
# print(inventory)

# #task2
# all_logins = [
#     "192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", 
#     "10.0.0.5", "192.168.1.10", "172.16.0.1", "8.8.8.8", 
#     "192.168.1.1", "10.0.0.9", "192.168.1.10", "10.0.0.5"
# ]
# blacklisted_ips = {"172.16.0.1", "8.8.8.8", "200.50.10.1"}

# Secure_IPs = set(all_logins)

# for banned_ip in blacklisted_ips:
#     if banned_ip in Secure_IPs:
#         Secure_IPs.remove(banned_ip)

# safe_ips = tuple(Secure_IPs)

# with open('authorized_logins.txt','a') as file:
#     for ip in safe_ips:
#         file.write(f'{ip}\n')

# #task3
# transaction_amount = 0
# while True:
#     try:
#         transaction_amount = input('Enter transaction value \n')

#         if transaction_amount == 'exit':
#             break

#         transaction_amount = int(transaction_amount)

#         if transaction_amount > 5000:
#             raise ValueError('High values over 5000 require approval')
        
#         elif transaction_amount <= 0:
#             raise ValueError('Invalid amount') 
        
#     except ValueError as e:
#             if 'High values over 5000 require approval' in e.args or 'Invalid amount' in e.args:
#                 print(e)
#             else:
#                  print('Invalid Input Type')

#     finally:
#         print('System: Monitoring active')

# #task4
# semester_1 = {
#     "Alice": [85, 90], "Bob": [70, 65], "Charlie": [100], 
#     "David": [88], "Eve": [92, 91]
# }
# semester_2 = {
#     "Alice": [95, 88], "Frank": [78, 80], "Bob": [72], 
#     "Grace": [99], "Charlie": [90, 85], "Heidi": [75]
# }

# names1 = set(semester_1.keys())
# names2 = set(semester_2.keys())
# names = names1.union(names2)

# all_grades = {}
# for name in names:
#     if name in semester_1 and name in semester_2:
#         all_grades[name] = semester_1[name] + semester_2[name]
#     elif name in semester_1:
#         all_grades[name] = semester_1[name]
#     else:
#         all_grades[name] = semester_2[name]
# print(all_grades)
