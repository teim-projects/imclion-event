from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Registration
import threading


# ✅ Background email function (FAST)
def send_email_async(email):
    try:
        email.send(fail_silently=True)
    except Exception as e:
        print("Email Error:", e)


def imc_view(request):
    if request.method == 'POST':
        try:
            payment_done = True if request.POST.get('payment_done') else False

            # ✅ Save data
            obj = Registration.objects.create(
                full_name=request.POST.get('full_name'),
                mobile=request.POST.get('mobile'),
                whatsapp=request.POST.get('whatsapp'),
                email=request.POST.get('email'),
                city=request.POST.get('city'),
                age=request.POST.get('age') or None,
                category=request.POST.get('category'),
                participation_type=request.POST.get('participation_type'),
                call_time=request.POST.get('call_time'),
                message=request.POST.get('message'),
                id_proof=request.FILES.get('id_proof'),
                payment_done=payment_done
            )

            # =========================
            # 📧 ADMIN EMAIL (FULL DETAILS)
            # =========================
            admin_email = EmailMessage(
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
                admin_email.attach_file(obj.id_proof.path)

            # =========================
            # 📧 USER EMAIL (PREMIUM DESIGN)
            # =========================
            user_email = EmailMessage(
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

            # 🚀 SEND EMAILS IN BACKGROUND (FAST)
            threading.Thread(target=send_email_async, args=(admin_email,)).start()
            threading.Thread(target=send_email_async, args=(user_email,)).start()

            return redirect('success')

        except Exception as e:
            print("ERROR:", e)
            return render(request, 'imc.html', {'error': str(e)})

    return render(request, 'imc.html')


def success_view(request):
    return render(request, 'success.html')