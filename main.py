# تعريف الدوال للعمليات الحسابية
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطأ: لا يمكن القسمة على صفر!"
    return x / y

print("--- آلة حاسبة بسيطة ---")
print("اختر العملية:")
print("1. جمع (+)")
print("2. طرح (-)")
print("3. ضرب (*)")
print("4. قسمة (/)")

# حلقة تكرار للسماح بإجراء عمليات متعددة
while True:
    # أخذ خيار المستخدم
    choice = input("\nأدخل رقم العملية (1 أو 2 أو 3 أو 4): ")

    # التحقق من أن الخيار صالح
    if choice in ('1', '2', '3', '4'):
        try:
            # طلب الأرقام من المستخدم
            num1 = float(input("أدخل الرقم الأول: "))
            num2 = float(input("أدخل الرقم الثاني: "))
        except ValueError:
            print("إدخال غير صالح! الرجاء إدخال أرقام فقط.")
            continue

        # تنفيذ العملية بناءً على اختيار المستخدم
        if choice == '1':
            print(f"النتيجة: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"النتيجة: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"النتيجة: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"النتيجة: {num1} / {num2} = {divide(num1, num2)}")

        # سؤال المستخدم إذا كان يريد الاستمرار
        next_calculation = input("\nهل تريد القيام بعملية أخرى؟ (نعم/لا): ")
        if next_calculation.lower() not in ('نعم', 'yes', 'y'):
            print("شكراً لاستخدامك الآلة الحاسبة. وداعاً!")
            break
    else:
        print("إدخال غير صالح! الرجاء اختيار رقم من 1 إلى 4.")
