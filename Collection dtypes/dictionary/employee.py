
employee={"name":"hari","dept":"r&d","salary":50000,"combo_offer":1000,"extra_working_day":3}

# print all key value
for k,v in employee.items():

    print(k,v)

# chk extra working days present
if("extra_working_day") in employee:

    print("present")

else:

    print("absent")

#print employee net_pay
if "extra_working_day" in employee:

    sal=employee.get("combo_offer")*employee.get("extra_working_day")

    net_pay=employee.get("salary")+sal

    print(net_pay)

else:

    net_pay=employee.get("salary")

    print(net_pay)

