## 1. Introduction ##

import csv
f = open("top100.csv","r")
music = list(csv.reader(f))

artists = []
for row in music[1:]:
    artists.append(row[1])
    
print(artists)    

## 2. Extract the Artists using a List Comprehension ##

artists = []
for row in music[1:]:
    artists.append(row[1])
    
artists_lc = [row[1] for row in music[1:]]    

## 3. Getting the Artist Count using a function ##

def counter(artists):
    artist_dict = dict()
    for values in artists:
        if values in artist_dict.keys():
            artist_dict[values] += 1
        else:
            artist_dict[values] = 1         
    return artist_dict

counts = counter(artists)
print(counts)
                
            
            

## 4. Getting the artist count using Counter() ##

from collections import Counter
artist_counts = Counter(artists)

## 7. Sorting our list of lists to extract the top value ##

artist_counts.sort()
top_artist = artist_counts[0]

## 8. Specifying a key when sorting our list ##

def by_count(artists):
    return artists[1]

artist_counts_list.sort(key=by_count, reverse=True)
top_artist = artist_counts_list[0]
print(top_artist)
    

## 9. Creating a function using lambda ##

f = open("top100.csv","r")
music = list(csv.reader(f))
artists = []
for row in music[1:]:
    artists.append(row[1])
from collections import Counter
artist_dict = Counter(artists)
artist_counts_lol = [[key,value] for key,value in artist_dict.items()]
artist_counts_lol.sort(key = lambda  x: x[1], reverse=True)
lambda_top_artist = artist_counts_lol[0:1]
print(lambda_top_artist)

## 10. Creating a Pipeline using Modularization ##

# Add your functions here
def read_data(filename):
    f = open(filename,"r")
    music = list(csv.reader(f)) 
    return music

def clean_data(music_list):
    artists = [row[1] for row in music_list[1:]]
    artist_dict = Counter(artists)
    artist_counts_list = [[key,value] for key,value in artist_dict.items()]
    artist_counts_list.sort(key = lambda x: x[1], reverse=True)
    return artist_counts_list
    
def  top_artist(list_of_lists):
    return list_of_lists[0]

# Uncomment when ready
music_as_list = read_data("top100.csv")
sorted_lol = clean_data(music_as_list)
most_popular_artist = top_artist(sorted_lol)

## 11. How to deal with errors ##

cleaned_list= []
for row in music_sample[1:]:
    try:
        cleaned_list.append([row[0],row[1],float(row[-1])])
    except:
        "Pass"

## 12. Passing new data into our pipeline ##

f = open("top100.csv","r")
music_all = list(csv.reader(f))

from collections import Counter

def extract_artist(music):
    return [row[1] for row in music[1:]]

def get_count(artists):
    artist_dict = Counter(artists)
    return [[key,value] for key,value in artist_dict.items()]

def sort_by_streams(artist_counts):
    artist_counts.sort(key=lambda x: x[1], reverse=True)
    return artist_counts

# Add your code here
artists = extract_artist(music_all)
artist_counts = get_count(artists)
top = sort_by_streams(artist_counts)