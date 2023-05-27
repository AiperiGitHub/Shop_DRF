from celery import shared_task
from django.core.mail import send_mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from apps.cart.models import Order, Inventory


@shared_task
def create_order(order_id):
    order = Order.objects.get(id=order_id)
    order.create_order()
    order.save()
    return order


@shared_task
def update_inventory(inventory_id):
    inventory = Inventory.objects.get(id=inventory_id)
    inventory.update_inventory()
    inventory.save()
    return inventory


@shared_task
def process_order(order_id):
    try:
        # Получаем заказ из базы данных
        order = Order.objects.get(id=order_id)

        # Выполняем необходимую обработку заказа
        # Например, вычисляем общую стоимость, обновляем инвентарь и т.д.
        order.calculate_total_price()

        # Обновляем инвентарь на основе заказа
        order.update_inventory()

        # Отправляем уведомление покупателю
        send_order_notification.delay(order_id)

        # Устанавливаем статус заказа как обработанный
        order.status = 'обработан'
        order.save()

        return True

    except Order.DoesNotExist:
        return False


@shared_task
def send_order_notification(order_id):
    order = Order.objects.get(id=order_id)

    recipient_email = order.email
    message = "Уважаемый покупатель, ваш заказ успешно оформлен."

    # Создание сообщения
    msg = MIMEMultipart()
    msg["From"] = "edilbekova_aiperi@mail.ru"
    msg["To"] = "urmatovnaa05@mail.ru"
    msg["Subject"] = "Уведомление о заказе"

    # Добавление текста сообщения
    msg.attach(MIMEText(message, "plain"))

    # Отправка сообщения по электронной почте
    send_mail




























# from celery import shared_task
# from apps.cart.models import Order, Inventory
# from notifications import send_order_notification
#
#
# @shared_task
# def create_order(order_id):
#     order = Order.objects.get(id=order_id)
#     order.create_order()
#     order.save()
#     return order
#
#
# @shared_task
# def update_inventory(inventory_id):
#     inventory = Inventory.objects.get(id=inventory_id)
#     inventory.update_inventory()
#     inventory.save()
#     return inventory
#
#
# class Order:
#     def __init__(self, order_details):
#         self.order_details = order_details
#
#     def send_order_notification(self):
#         # Логика отправки уведомления покупателю
#         # Здесь вы можете использовать различные методы отправки уведомлений,
#         # такие как отправка электронной почты, SMS и т.д.
#         # Ниже приведен пример отправки уведомления по электронной почте:
#
#         recipient_email = self.order_details['email']
#         message = "Уважаемый покупатель, ваш заказ успешно оформлен."
#         # Код для отправки уведомления по электронной почте
#
#         # Пример кода для отправки уведомления через SMTP (почтовый сервер)
#         import smtplib
#         from email.mime.text import MIMEText
#         from email.mime.multipart import MIMEMultipart
#
#         sender_email = "your_email@example.com"
#         smtp_server = "smtp.example.com"
#         smtp_port = 587
#         username = "your_username"
#         password = "your_password"
#
#         # Создание сообщения
#         msg = MIMEMultipart()
#         msg["From"] = sender_email
#         msg["To"] = recipient_email
#         msg["Subject"] = "Уведомление о заказе"
#
#         # Добавление текста сообщения
#         msg.attach(MIMEText(message, "plain"))
#
#         # Отправка сообщения через SMTP
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.starttls()
#             server.login(username, password)
#             server.send_message(msg)
#
#         print("Уведомление успешно отправлено.")
# @shared_task
# def process_order(order_id):
#     try:
#         # Получаем заказ из базы данных
#         order = Order.objects.get(id=order_id)
#
#         # Выполняем необходимую обработку заказа
#         # Например, вычисляем общую стоимость, обновляем инвентарь и т.д.
#         order.calculate_total_price()
#
#         # Обновляем инвентарь на основе заказа
#         order.update_inventory()
#
#         # Отправляем уведомление покупателю
#         send_order_notification(order)
#
#         # Устанавливаем статус заказа как обработанный
#         order.status = 'обработан'
#         order.save()
#
#         return True
#
#     except Order.DoesNotExist:
#         return False
#
#
