calculate_tp = lambda tip_percentage,bill_total:(tip_percentage * bill_total) + bill_total
def calculate_tip(my_bill, my_tip=.2):
    return my_bill * my_tip

def get_letter_grade(i):
    if i >= 90:
        return 'A'
    elif i >= 80 and i < 90:
        return 'B'
    elif i >= 70 and i < 80:
        return 'C'
    elif i < 70:
        return 'F'