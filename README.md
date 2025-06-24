MISSION: 
1. Found F1 data,
2. Use as sandbox to tryout different tech


TECHNOLOGY Summary (full info in requirements.txt):
* Vuetify
* Pinia
* django REST framework
* postgresql 


Priority 1:
---
* mbp


Priority 2:
---
* finish full CRUD operations in UI
* search bar with filters
* authentication + authorization


Priority 3 (no priority, in no order):
---
* photo for each driver
  


Brainstorm Area:
---
* set up github for ci/cd with test pipeline, is it free, is this possible with no charge?
* setup infra with VM running containers. how to run 1 service per VM/container
* make an exact of project in php, java too i suppose


Known Issues
----------------------------
Qualifying Table:
* python time does not support microseconds. datetime does,
* I'm not sure if there's an elegant way to do this since creating a datetime object seems to not like all 0's for year/month/day. seems odd to me that postgres supports 'allballs' for zero datetime. need to do more research on this


