class Show:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def like_show(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()


class Film(Show):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f"Name: {self._name} | Year: {self.year} | Duration: {self.duration}min | Likes: {self._likes}"


class Series(Show):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f"Name: {self._name} | Year: {self.year} | Seasons: {self.seasons} | Likes: {self._likes}"


class Playlist:
    def __init__(self, name, shows):
        self.name = name
        self._shows = shows

    def __getitem__(self, item):
        return self._shows[item]

    @property
    def shows_list(self):
        return self._shows

    def __len__(self):
        return len(self._shows)


avengers = Film("avengers: endgame", 2018, 160)
strangerthings = Series("stranger things", 2016, 4)
breakingbad = Series("breaking bad", 2008, 5)
scream = Film("scream", 1996, 100)
interstellar = Film("interstellar", 2014, 2)
avengers.like_show()
avengers.like_show()
avengers.like_show()
strangerthings.like_show()
breakingbad.like_show()
breakingbad.like_show()
scream.like_show()
scream.like_show()
scream.like_show()
interstellar.like_show()
interstellar.like_show()
interstellar.like_show()
interstellar.like_show()

all_shows = [avengers, strangerthings, breakingbad, scream, interstellar]
my_playlist = Playlist("Playlist number 01", all_shows)

print(f"\n{my_playlist.name}")
print(f"\nTotal shows in the playlist: {len(my_playlist)}")

for show in my_playlist:
    print(f"\n{show}")
