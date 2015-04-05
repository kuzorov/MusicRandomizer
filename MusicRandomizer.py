#!/usr/bin/env python


import os, shutil, fnmatch, random, sys


# Something like controller of this script
def randomize(library_dir, output_dir, tracks_per_dir=25):
    tracks = get_tracks(library_dir)
    if len(tracks) > 0:
        copy_tracks(tracks, output_dir, tracks_per_dir)
    else:
        print('! There is no tracks in library dir')

    return True


# Gets list of tracks from specified dir
def get_tracks(library_dir):
    tracks = []
    for root, dirnames, filenames in os.walk(library_dir):
        for filename in fnmatch.filter(filenames, '*.mp3'):
            tracks.append(os.path.join(root, filename))

    return tracks


# Creates directories with randomly selected tracks
def copy_tracks(tracks, output_dir, tracks_per_dir):
    # We have to copy tracks into empty directory
    dir_now = 0
    tracks_copied = tracks_per_dir
    random.shuffle(tracks)
    tracks_amount = len(tracks)
    current_track = 0

    for track in tracks:
        if int(tracks_copied) >= int(tracks_per_dir):
            dir_now += 1
            tracks_copied = 0
            os.mkdir(os.path.join(output_dir, str(dir_now)))

        tracks_copied += 1

        new_track_name = str(tracks_copied) + '.mp3'
        shutil.copyfile(
            track,
            os.path.join(output_dir, str(dir_now), new_track_name)
        )
        
        current_track += 1
        render_progressbar(current_track, tracks_amount)

    return True


# Renders progressbar on console
def render_progressbar(current, total, bar_length=20):
    percent = float(current) / total
    hashes = '#' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rProgress: [{0}] {1}%\r".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()


if __name__ == '__main__':
    if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
        library_dir = sys.argv[1]
        output_dir = sys.argv[2]
        # Default value
        traks_per_dir = 25

        if len(sys.argv) >= 5 and sys.argv[3] == '-n':
            traks_per_dir = sys.argv[4]

        randomize(library_dir, output_dir, traks_per_dir)

    else:
        print('! Something wrong, check your paths')