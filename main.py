# ราคาที่ลูกค้าจ่าย
customer_payments = {
    'A': 40,
    'B': 50,
    'C': 60
}

# เรทจริงๆ ของร้าน
actual_rate = 36.88

# เรทที่ร้านรับเงิน
received_rate = 36.33

# ค่า fee
fee = 20*actual_rate

additional_payments = {}

# คำนวณค่าเพิ่มที่ลูกค้าต้องจ่าย
for customer, paid_amount in customer_payments.items():
    # คำนวณจำนวนน้ำชาที่ได้จากราคาที่ลูกค้าจ่าย
    amount_of_tea = paid_amount / received_rate

    # คำนวณราคาที่ลูกค้าต้องจ่ายเพิ่ม
    additional_payment = (amount_of_tea * actual_rate) + fee - paid_amount

    additional_payments[customer] = additional_payment

# แสดงผลลัพธ์เพิ่มยอดที่ลูกค้าต้องจ่ายเพิ่มและยอดเดิม
print("ยอดที่ลูกค้าต้องจ่ายเพิ่มและยอดเดิม:")
for customer, paid_amount in customer_payments.items():
    additional_payment = additional_payments[customer]
    total_payment = paid_amount + additional_payment
    print("ลูกค้า {} จ่ายเดิม {:.2f} บาท และต้องจ่ายเพิ่มอีก {:.2f} บาท รวมเป็น {:.2f} บาท".format(customer, paid_amount, additional_payment, total_payment))
