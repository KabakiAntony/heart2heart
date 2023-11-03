import os

from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To
from google.cloud import translate_v2 as translate

from django.shortcuts import render, redirect
from django.contrib import messages


account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


def home(request):
    """ show the home page with the form prompts"""
    return render(request, 'messageHandler/home.html')


def translate_text(target, text):
    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)

    return result


def voice_message(request):
    """ make a voice call to the provided no and read out the message"""
    if request.POST:
        sender_name = request.POST.get('sender_name')
        recipient_name = request.POST.get('recipient_name')
        recipient_phone_no = request.POST.get('recipient_phone_no')
        message = request.POST.get('message')
        language = request.POST.get('language')

        constructed_message = f""" 
            Hello {recipient_name}, we have a heart2heart message 
            from {sender_name}, {message}."""

        result = translate_text(language, constructed_message)

        translated_message = result.get('translatedText')

        client.calls.create(
            twiml=f"""
            <Response>
                <Say voice="Alice">
                    {translated_message}
                </Say>
            </Response>""",
            to=recipient_phone_no,
            from_=os.environ.get('TWILIO_PHONE_NO')
        )

        messages.add_message(request, messages.SUCCESS,
                             "Your message is being passed.")

    return redirect('messageHandler:home')


def email_message(request):
    """ send a dynamic email to the supplied email"""
    if request.POST:
        sender_name = request.POST.get('sender_name')
        recipient_name = request.POST.get('recipient_name')
        recipient_email = request.POST.get('recipient_email')
        message = request.POST.get('message')
        language = request.POST.get('language')

        constructed_message = message + f" ,from {sender_name}"

        result = translate_text(language, constructed_message)

        translated_message = result.get('translatedText')

        sendgrid_send_mail(
            recipientEmail=recipient_email,
            specialMessage=translated_message.capitalize(),
            recipientName=recipient_name,
        )

        messages.add_message(request, messages.SUCCESS,
                             "Your special email has been sent.")

    return redirect('messageHandler:home')


def sendgrid_send_mail(recipientEmail, specialMessage, recipientName):
    mail = Mail()
    mail.from_email = From(
        email=os.environ.get('DEFAULT_FROM_EMAIL'),
        name="heart2heart"
    )
    mail.to = [
        To(
            email=recipientEmail,
            name=recipientName
        )
    ]
    mail.dynamic_template_data = {
        "recipient_name": recipientName,
        "message": specialMessage
    }
    mail.template_id = os.environ.get('TEMPLATE_ID')

    try:
        sg_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg_client.send(mail)
    except Exception as e:
        print(f"Error sending email: {str(e)}")
