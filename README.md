# downloaderdude
A simple file-downloader built with the multithreading module.

## What is?
DownloaderDude was a project made for the "Devolopment 2" course at the University of Messina, some time ago.
It was one of my first "serious" Python projects; reading it years later, I can assure you it's not well written. 

**BUT**, trust me: it works. 

## Why multithreading instead of multiprocessing?
Because my teacher asked me to use threads for this project. Maybe I'll start writing a multiprocessing version, one day. Maybe.

## How to use it?
First, we must write our settings. Open the `config.ini` file and modify the parameters accordingly to your needs.
My default settings were this:
```
[TestHost]
;set the hostname to test connection. If hostname is blank (NOT set), the default hostname will be 'google.com'.
hostname = yahoo.com

[Dir]
;set the download directory; If dd_dir is blank (NOT set), the default directory will be 'dd_files'.
dd_dir = test

[Sources]
;set the URLs source file; [REQUIRED] or the script will terminate its operation instantly.
sources = my_sources.txt

[Filters]
;set the file filters for downloading. If filters is blank (NOT set), no filters will be applied on downloader.
;example: filters = .pdf, .deb, .docx, .tar.gz
filters = .pdf, .docx, .deb

[Batch]
;set the number of URLs placed simultaneously in the queue task pool, every iteration.
;If not set, the default number will be equal to the number of URLs in source file w/o filters.
n_batch = 4
```
As you see, you can set:
- The hostname to test connection
- The directory where the downloaded file will be saved
- The name of sources file: it's a simple list of URLs, in txt format.
- The filters: you can exclude some files from downloading, filtering for extension (useful if your sources file is very long... too long to check&edit manually)
- The number of "simultaneously" downloads (performance may vary but, remeber, 'multithreading' it's not 'multiprocessing': the GIL it's a factor to consider)

After a proper setup, you can launch with: `python3 dd_manager.py`

## But... You made a custom logging system instead of using logging package!
Yes, at the time I was asked to add a logging system... made by me. It works decently: check for `log.txt` file inside the script dir. 
