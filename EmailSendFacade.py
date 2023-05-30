# Subsystem 1: EmailService
class EmailService:
    def send_email(self, recipient, subject, content):
        print(f"Mengirim email ke {recipient}:\nSubjek: {subject}\nKonten: {content}")


# Subsystem 2: SMSNotificationService
class SMSNotificationService:
    def send_sms(self, recipient, message):
        print(f"Mengirim SMS ke {recipient}:\nIsi Pesan: {message}")


# Facade
class NotificationFacade:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSNotificationService()

    def send_notification(self, recipient, subject, content, sms_message):
        self.email_service.send_email(recipient, subject, content)
        self.sms_service.send_sms(recipient, sms_message)


# Client
def main():
    facade = NotificationFacade()

    recipient = "kampusmerdeka@gmail.com"
    subject = "REGISTER"
    email_content = "Ini adalah email percobaan."
    sms_message = "Notifikasi melalui SMS."

    facade.send_notification(recipient, subject, email_content, sms_message)


if __name__ == '__main__':
    main()
