from django.shortcuts import render,redirect

# Dashboard View

def card(request):
    return render(request,'dashboard/cards.html')








# Website View
def homepage(request):
    return render(request,'home/home.html')

def footer(request):
    return render(request,'home/footer.html')

def course(request):
    return render(request,'home/course.html')

def abacus(request):
    return render(request,'home/abacus.html')

def achive_photos(request):
    return render(request,'home/achivement-photos.html')

def achive_video(request):
    return render(request,'home/achivement-video.html')

def award(request):
    return render(request,'home/awards.html')

def news(request):
    return render(request,'home/news.html')

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

# Social Media Link View
def whatsapp_chat(request):
    # Construct the WhatsApp chat URL with appropriate parameters
    mobile_no = '7770045402'
    whatsapp_url = f'https://wa.me/{mobile_no}?text=Hello'    
    # Redirect the user to the WhatsApp chat URL
    return redirect(whatsapp_url)

def instagram(request):
    instagram_username = 'your_instagram_username'
    instagram_url = f'https://www.instagram.com/{instagram_username}/'
    # Redirect the user to the WhatsApp chat URL
    return redirect(instagram_url)

def facebook(request):
    facebook_username = 'iginius.abacus'
    facebook_url = f'https://www.facebook.com/{facebook_username}/'
    # Redirect the user to the WhatsApp chat URL
    return redirect(facebook_url)

def youtube(request):
    youtube_username = 'UCi38KUjpRe9RcYHzSyS6RoA'
    youtube_url = f'https://www.youtube.com/channel/{youtube_username}/'
    # Redirect the user to the YouTube channel URL
    return redirect(youtube_url)