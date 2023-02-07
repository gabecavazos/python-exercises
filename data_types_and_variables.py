
#5
movies = ['The Little Mermaid', 'Brother Bear', 'Hercules']
rental_days = [3, 5, 1]
rental_dict = {'The Little Mermaid' : 3, 'Brother Bear' : 5, 'Hercules' : 1}
amount_owed = [n * 3 for n in rental_days]
print(sum(amount_owed))

#6
company = ['Google', 'Amazon', 'Facebook']
company_hourly_rates = [400, 380, 350]
company_hours = [6, 4, 10]
pay_for_week = []
company_dict = {'Google' : 400, 'Amazon' : 380, 'Facebook' : 350}
print((company_dict['Google'] * 6) + (company_dict['Amazon'] * 4) + (company_dict['Facebook'] * 10))

#7
class_full = False
schedule_conflicts = True 

student_can_enroll = schedule_conflicts and not class_full
print(student_can_enroll)

#8 
items_bought = 3
offer_not_expired = True
premium_member = True
product_offer = items_bought > 2 and offer_not_expired or premium_member
print(product_offer)

#9
username = 'codeup'
password = 'notastrongpassword'

password_length = bool(len(password) >= 5)
username_length = bool(len(username) <= 20)
combo_check = password == username

proper_combo = password_length and username_length and username == username.strip() and not combo_check
print(proper_combo)