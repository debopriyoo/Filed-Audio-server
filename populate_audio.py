import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'audio_project.settings')

import django
django.setup()

from audio.models import Song,Podcast,Audiobook
from faker import Faker

fakegen = Faker()

def populate(N):

    fake_participants=''

    for entry in range(N):

        fake_song_name_list=["Difficult Nobody","The Resilient Best Day","Its Draws Without Gangsta","We Get Outs Nobody","Bowl Beyond the Periodical","The Mistake Teach","Overcoming Romance","Organise Revolution","Blue Woe","Fly","Discord","Under The Brilliant Forever","Lie Forgets At a Contaminates","Height For Tracker","The Radical Apology","The Matter of Faith","The Screams Party","Angels Rain Trait","Discord Chattering","From Its Poetry","Playing Yearnings","Far"]
        fake_audiobook_name_list=["Such a Fun Age","Where the Crawdads Sing Deluxe Edition ","Becoming ","The Body","Bad Blood","Wow, No Thank You","Untamed","Little Fires Everywhere","The Dutch House: A Novel Ann Patchett ","The Adventures of Tom Sawyer","Me Talk Pretty One Day","Educated","Elizabeth II: Life of a Monarch","Librivox","Lit2Go","Loyal Books","Mind Webs","Open Culture","Libby","Podiobooks","Project Gutenberg"]
        fake_podcast_name_list=["The Download","The Downlow Download","The 411","Excellent Episodes","Syndicated Speakers","Podcast Of Characters","Pod Behavior","Mod Pod","Your Daily","Spirit Podcast ","Like Content ","Better Broadcast ","Realpodcast ","Excellent Episodes ","Morning Muse ","Night Talk ","My Favorite Murder ","Uhh Yeah Dude ","ID10T (Formerly The Nerdist) ","Stuff You Should Know ","The Joe Rogan Experience ","The Tech Guy-This Week in Tech ","Too Beautiful to Live ","Keith and The Girl"]

        fake_song_name = random.choice(fake_song_name_list)
        fake_duration_song =  random.choice(range(100,400))

        fake_podcast_name = random.choice(fake_podcast_name_list)
        fake_duration_podcast =  random.choice(range(100,500))
        fake_host = fakegen.name()
        lenth=random.choice(range(1,10))
        for item in range(lenth):
            fake_nm = fakegen.name()+','
            fake_participants = fake_participants + fake_nm

        fake_audiobook_name = random.choice(fake_podcast_name_list)
        fake_author = fakegen.name()
        fake_duration_audiobook = random.choice(range(200,800))
        fake_narrator = fakegen.name()

        sng = Song.objects.get_or_create(song_name=fake_song_name,duration=fake_duration_song)[0]
        pdcst = Podcast.objects.get_or_create(podcast_name=fake_podcast_name,duration=fake_duration_podcast,host=fake_host,participants=fake_participants[:-1])[0]
        adiobok = Audiobook.objects.get_or_create(audiobook_name=fake_audiobook_name,duration=fake_duration_audiobook,author=fake_author,narrator=fake_narrator)[0]



if __name__ == '__main__':
    print('populating script')
    populate(5)
    print('populating complete')
