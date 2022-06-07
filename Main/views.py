from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)


def  contact(request):
    subject = "Contact Laban"
    message = request.POST.get('message')
    name = request.POST.get('name')
    email = request.POST.get('email')
    
    if request.method=='POST':
        message=f'{message}............\nreply to {email}\nBy name {name}'
        send_mail(subject,
                message,
                settings.EMAIL_HOST_USER,
                ['pearljob@gmail.com','pearlvibe@gmail.com'],
                fail_silently = True,
                )
        send_mail(subject,
                f'Dear {name},\n Your message has been recived successfully, We will be contacting You Soon!!!. Have a lovely day',
                settings.EMAIL_HOST_USER,
                [f'{email}'],
                fail_silently = True,
                )
        messages.success(request, f'We have recived your message, You will recive and email confirming it soon, Have a lovely day')
        return redirect('index')
    else:
        messages.success(request, f'Dear {name},\n Sorry But there may be an error in the System, \n Please Contact me on pearljob@gmail.com')
        return redirect('index')
