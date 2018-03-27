# PhotoDownloader
This project is created for downloading all photos for exactly user from VK

FIrstly you should create "messages", "links" and "photos" directories manually. After that run each file step by step:
GetAllChats -> Messages Downloader -> PrepareLinks -> PhotoDownloader.

**GettAllChats** grabs all chats of current user and put it into temp file chats.pickle, where next structe is used:
[{'type': type, 'id': id}, ..., {'type': type, 'id': id}]. Type can be "chat" and "dialog", id is id of chat or user accordingly.

**MessagesDownloader** grabs all messages history from providing file with list of chats. Each dialog is put into single file in "messages" directory.

**PrepareLinks** looks for best quality images among all messages history, creates file with links to images for each bunch of messages (dialog), stores it in "links" directory

**PhotoDownloader** downloads all photos via provided links, stores them in separate folders for each dialog in root "photos" directory
