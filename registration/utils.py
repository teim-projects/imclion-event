from django.core.mail import EmailMessage
from django.conf import settings

# ✅ Async Email Sender
def send_email_async(email):
    try:
        email.send(fail_silently=True)
    except Exception as e:
        print("Email Error:", e)


# ✅ Admin Email Function
def create_admin_email(obj):
    email = EmailMessage(
        subject="🎤 New Registration - FULL DETAILS",
        body=f"""
📌 New Registration Received:

👤 Name: {obj.full_name}
📞 Mobile: {obj.mobile}
📱 WhatsApp: {obj.whatsapp}
📧 Email: {obj.email}

🏙️ City: {obj.city}
🎂 Age: {obj.age}

🎶 Category: {obj.category}
🎤 Participation: {obj.participation_type}
⏰ Call Time: {obj.call_time}

💰 Payment Done: {obj.payment_done}

📝 Message:
{obj.message}
        """,
        from_email=settings.EMAIL_HOST_USER,
        to=['IMCPCMC@gmail.com']
    )

    if obj.id_proof:
        email.attach_file(obj.id_proof.path)

    return email


# ✅ User Email Function
def create_user_email(obj):
    return EmailMessage(
        subject="🎉 Registration Confirmed - Singing Event",
        body=f"""
Dear {obj.full_name},

🎉 Congratulations! Your registration has been successfully completed.

We are delighted to have you participate in our Singing Event 🎶

📌 Registered Details:
Category: {obj.category}
Participation: {obj.participation_type}

Our team will contact you shortly with further information.

Thank you for being part of this exciting journey 🌟

Warm Regards,  
IMC Event Team 🎤
        """,
        from_email=settings.EMAIL_HOST_USER,
        to=[obj.email]
    )