import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django 
django.setup()

#Fake Pop Script
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ["Social", "Search", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()  # Pastikan topik disimpan  
    return t  


def populate(N=5):
    for entry in range(N):
        # Dapatkan topik untuk entry
        top = add_topic()
        
        # Buat data palsu untuk entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # Buat entry Webpage baru dengan topik
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Buat entry AccessRecord palsu
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ ==   '__main__':
    print("populating script...") 
    populate(20)
    print("Populating complete!")

