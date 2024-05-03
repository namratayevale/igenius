from django.shortcuts import render,redirect

# Create your views here.

# def demo(request):
#     return render(request,'home/index.html')

def homepage(request):
    return render(request,'home/home.html')

def footer(request):
    return render(request,'home/footer.html')

def course(request):
    return render(request,'home/course.html')

def achive_photos(request):
    return render(request,'home/achivement-photos.html')

def achive_video(request):
    return render(request,'home/achivement-video.html')

def career(request):
    return render(request,'home/career.html')

def contact_us(request):
    return render(request,'home/contact-us.html')

def about_us(request):
    return render(request,'home/about-us.html')

def franchise(request):
    return render(request,'home/franchise.html')

def blog(request):
    return render(request,'home/blog.html')

def find_us(request):
    return render(request,'home/find-us.html')

def our_team(request):
    return render(request,'home/our-team.html')

# def whatsapp_chat(request):
#     # Construct the WhatsApp chat URL with appropriate parameters
#     mobile_no = '9022645448'
#     whatsapp_url = f'https://wa.me/{mobile_no}?text=Hello'    
#     # Redirect the user to the WhatsApp chat URL
#     return redirect(whatsapp_url)