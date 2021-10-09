import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def auto_generate_mail(subject, email, input_message, name="", phone="", url=""):
    message = Mail(
                from_email= 'hei@{{ cookiecutter.project_name }}.no',
                to_emails= 'hei@{{ cookiecutter.project_name }}.no',
                subject='New inquiry | ' + subject,
                html_content= """<div>
                                <p>Hi,</p>
                                <br>
                                <p>There’s been a new inquiry at {{ cookiecutter.project_name }}.no.</p>
                                <br>
                                <p>Subject: """ + subject + """</p>
                                <p>Email: """ + email + """</p>
                                <p>Phone: """ + phone + """</p>
                                <p>Url: """ + url + """</p>
                                <br>
                                <p>Message: """ + input_message + """</p>
                                <br>
                                <p>Sincerely,</p>
                                <p>Your webapp</p>
                            </div>"""
        )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)