# vacation-khatam-hui

### Appologies for stating the work very late, Working from home is never easy for me for I am lost in Peace but back to work now.


#### After starting work I found this project gets complexed when we have many number of users as then we have to take care of these things (possibly more that are unoticed), A simple breakdown:
* User SignUp
* Admin Panel for user views
* User will login, their own db to keep count for playbacks of different media and downloads performed by them
* User can playback media, download a media, view stats of downloads and playbacks on basis of day and monthly.
* Permission classes for admin and user
* playback and download details have to be updated for media or user

Update1:
Date- 2/2/2020, Time- 21:53

Endpoint for searching media (stuck with how to get playback count incremented when ShowMedia(playback) api is called)
-- It includes adding media (generic CreateAPIView)
-- Viewing Media (api that will support playback increment)
-- One click play for user
-- Download media

Keeping proper authentication and making a suffice database are major challenges here.
Will update it after refactoring the workflow, old ways won't make it.
Sorry but I won't be able to discuss on call in night for 2 days.

and Thanks for your help Abhishek.

-------------------------------------------------------------------------------