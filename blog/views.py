from django.shortcuts import render

blog_data = [
    {
        "title": "‘বাংলাদেশ বাংলাদেশই, তাদের যেন অস্ট্রেলিয়া, ইংল্যান্ড না ভাবি’",
        "content": "বাংলাদেশ দল যেন সমস্যার অন্য নাম। দারুণ শুরুর পরও মিডল অর্ডারের ধসে বাংলাদেশ গতকাল ভারতের বিপক্ষে তুলেছিল মাত্র ২৫৬ রান। "
                   "এই পুঁজি নিয়ে কী আর ভারতের রোহিত শর্মা-বিরাট কোহলি-শুবমান গিলদের সামলানো যায়!",
        "aythor": "খেলা ডেস্ক",
        "post_datetime": "২০ অক্টোবর ২০২৩, ০৯: ৫৫",
    },
    {
        "title": "এবার মিডল অর্ডার নিয়ে আক্ষেপ নাজমুলের",
        "content": " কখনো টপ অর্ডার, কখনো মিডল অর্ডার— বিশ্বকাপে এবার বাংলাদেশ দলের ব্যাটিং নিয়ে আক্ষেপটা থেকেই যাচ্ছে।",
        "aythor": "খক্রীড়া প্রতিবেদকঢাকা",
        "post_datetime": " অক্টোবর ২০২৩, ২৩: ৩৫",
    }

]


def About(request):
    return render(request, "Blog/about.html", {"title": "Django Blog"})


def homepage(request):
    return render(request, "Blog/home.html", {"blog_data": blog_data})
