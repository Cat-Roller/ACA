#task 1
#clean_data = []
#with open('./raw_data.txt','r') as file:
#    for line in file:
#        try:
#            name, age, score = line.split(', ')
#            score = score.strip()
#            age = int(age)
#            score = int(score)
#            clean_data.append({
#                'name': name,
#                'age': age,
#                'score': score
#                })
#        except ValueError:
#            with open('./error.log', 'a') as err:
#                err.write(line)
#print(clean_data)
#========================]

#task2
#prices = {'apple': 1.5, 'milk': 2.5, 'bread': 2.0}
#total_cost = 0
#with open('./list.txt','r') as file:
#    for item in file:
#        try:
#            item = item.strip()
#            total_cost += prices[item]
#        except KeyError:
#            print(f"Item {item} not found\n")
#        finally:
#            print(f'Checked item: {item}\n')
#print(f'Total: {total_cost}')
#============================]

#task3
#IPs = set()
#try:
#    with open('./access.txt','r') as file:
#        for line in file:
#            IP = line.split(maxsplit=1)[0]
#            IPs.add(IP)
#except FileNotFoundError:
#    print('the file with info doesnt exist')
#print(IPs)
#with open('./unique_visitors.txt','a') as file:
#    file.write("\n".join(IPs))
#================================]

#task4
#def read_scores(path):
#    scores = {}
#    with open(f'{path}','r') as file:
#        for line in file:
#            try:
#                if not line:
#                    continue
#                name, score = line.strip().split(', ')
#                score = int(score)
#            except ValueError:
#                score = 0
#            finally:
#                scores[name] = score
#    return scores
#
#math_scores = read_scores('./math_scores.txt')
#science_scores = read_scores('./science_scores.txt')
#all_scores = {}

#for key, score in math_scores.items():
#    if key in science_scores.keys():
#        all_scores[key] = (score, science_scores[key])
#    else:
#        all_scores[key] = (score, 0) 
#
#for key in science_scores.keys():
#    if key not in math_scores.keys():
#        all_scores[key] = (0,science_scores[key])

#print(all_scores)
#=====================================]

#task5
#settings = {}
#with open('./settings.cfg','r') as file:
#    for line in file:
#        if "=" not in line:
#            continue
#        setting, value = line.split(sep='=')
#        setting = setting.strip()
#        value = value.strip()
#        if setting == 'DIFFICULTY' and (value != 'Easy' or value!='Hard'):
#            value='Medium'
#        if setting == 'MAX_PLAYERS' and int(value)>100:
#            #delete raise keyword to run the code
#            raise ValueError('Too many players')
#        settings[setting] = value
#print(settings)