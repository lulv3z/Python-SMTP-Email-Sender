import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = "test@gmail.com"
password = "IhrAppPasswort"  # oder Ihr reguläres Passwort, wenn 2FA deaktiviert ist

# Erstellen Sie eine MIMEMultipart-Nachricht
message = MIMEMultipart()
message['From'] = my_email
message['To'] = "rennuxbot@gmail.com"
message['Subject'] = "Test-E-Mail"
body = "Hello World!"
message.attach(MIMEText(body, 'plain'))

try:
    # Verbindung zum SMTP-Server herstellen
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()

    # Anmeldung am E-Mail-Konto
    connection.login(user=my_email, password=password)

    # E-Mail senden
    connection.sendmail(from_addr=my_email, to_addrs="rennuxbot@gmail.com", msg=message.as_string())

    print("E-Mail erfolgreich gesendet!")

except Exception as e:
    print(f"Fehler beim Senden der E-Mail: {str(e)}")

finally:
    # Verbindung trennen
    connection.quit()
