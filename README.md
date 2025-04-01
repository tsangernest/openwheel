MISSION: Found F1 data, and sandbox different tech with a lot of data i'm interested in?


TECHNOLOGY Summary (full info in requirements.txt):
* Vuetify
* Pinia
* django REST framework
* postgresql 



TOP TOP priority:
---
* acquire macbook pro, and _obviously_ with _at least_ 64gb of ram,


Next (top down priority):
---
* detailed view
* finish full CRUD operations in UI
* get app in container to reload on command
* search bar with filters
* authentication + authorization


Next After Next (no priority, in no order):
---
Scraping
* probably nice to get betamax setup so i'm not hammering wikipedia eps
* learn to use wikipedia endpoints, to then use spiders to update driver/circuit/update
* scrape images too?


Brainstorm Area:
---
* set up github for ci/cd with test pipeline, is it free, is this possible with no charge?
* setup infra with VM running containers. how to run 1 service per VM/container
* make an exact of project in php, java too i suppose


Known Issues
----------------------------
General:
* should probably rename constructor table to something else, i figured anyone looking at this will know F1

Qualifying Table:
* python time does not support microseconds. datetime does,
* I'm not sure if there's an elegant way to do this since creating a datetime object seems to not like all 0's for year/month/day. seems odd to me that postgres supports 'allballs' for zero datetime. need to do more research on this

