class Song(object):
    def __init__(self, id, duration):
        self.id = id
        self.duration = duration

    def __str__(self):
        return "(id : {}, duration : {})".format(self.id, self.duration)

class CD(object):
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_duration(self):
        result = 0

        for song in self.songs:
            result += song.duration

        return result

    def __str__(self):
        result = "[{0}]"

        s =  ""
        out = "{}"
        for song in self.songs:
            s += out.format(song)

        return result.format(s)

class GreedSolver1(object):
    def solve(self, songs):
        shelf = []

        songs.reverse()

        index = 1
        cd = CD()
        shelf.insert(index, cd)

        while len(songs) > 0:
            song = songs.pop()

            new_duration = song.duration + cd.get_duration()
            out = "CD[{}], Duration: {}, New Duration: {}".format(index, cd.get_duration(), new_duration)
        #     print(out)

            if new_duration > cd.capacity:
                index += 1
                cd = CD()
                shelf.insert(index, cd)
                new_duration = 0

            cd.add_song(song)

        return shelf

if __name__ == '__main__':
    songs = [Song(1, 1), Song(2, 1), Song(3, 2), Song(4, 3), Song(5, 5), Song(6, 5), Song(7, 6), Song(8, 7)]
    solver = GreedSolver1()
    shelf = solver.solve(songs)

    for cd in shelf:
        print(cd)
