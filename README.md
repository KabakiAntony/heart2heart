# heart2heart

## what is heart2heart

    heart2heart is messaging service where you send short messages as voice and email, the beauty of it is you get to choose the language the recipient will recipient will receive the message in, breaking down barriers of communication.

The service utilizes

- [Twilio Programmable Voice](https://www.twilio.com/docs/voice)
- [Twilio SendGrid](https://sendgrid.com/)
- [Google Cloud Translation API](https://cloud.google.com/translate/docs/reference/rest)

You will need to signup to the various services in order to get the respective API keys.

## Setup and installation
[get it here](https://www.postgresql.org/download/)

   Clone this repo and **cd** into it only then you can start working following the steps below.

1. Set up virtualenv

   ```bash
        virtualenv venv
   ```

2. Activate virtualenv

   ```bash
      LINUX/MAC

      . venv/bin/activate

      WINDOWS

      . venv/scripts/activate
      
   ```

3. Install dependencies

   ```bash
        pip install -r requirements.txt
   ```

4. .env file example

    Create the **env** file in the root of your project and place the following settings in the file and others that you might want to add to the file.

   ```bash
        SENDGRID_API_KEY='your sendgrid api key'
        DEFAULT_FROM_EMAIL='some email'
        TWILIO_ACCOUNT_SID=
        TWILIO_AUTH_TOKEN=
        TWILIO_PHONE_NO=
        TEMPLATE_ID=
   ```

5. Start the server

   ```bash
      python manage.py runserver
   ```

<details open>

Incase of a bug or anything else use any on the below channels to reach me

[Find me on twitter](https://twitter.com/kabakikiarie) OR  drop me an email at <kabaki.antony@gmail.com>.
