#!/usr/bin/env python


import os, shutil, fnmatch, random, sys

# Somethins like controller of this script
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

# Creates diractories with randomly selected tracks
def copy_tracks(tracks, output_dir, tracks_per_dir):
    # We have to copy tracksinto empty directory
    if os.listdir(output_dir) != []:
        sys.exit('! Output dir is not empty')

    dir_now = 0
    tracks_copied = tracks_per_dir
    random.shuffle(tracks)

    for track in tracks:
        if int(tracks_copied) < int(tracks_per_dir):
            tracks_copied += 1

            new_track_name = str(tracks_copied) + '.mp3'
            shutil.copyfile(
                track,
                output_dir + '\\' + str(dir_now) + '\\' + new_track_name
            )
        else:
            dir_now += 1
            tracks_copied = 0
            os.mkdir(output_dir + '\\' + str(dir_now))

    return True


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