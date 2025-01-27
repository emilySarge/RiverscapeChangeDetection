# LandcoverChangeDetection
### Study site:
Wildhorse Creek is a floodplain setting with a primary channel width generally between 10 and 15 meters. The 720-meter gravel-bedded stream reach is embedded in a glacial valley in the Sawtooth Mountains is approximately 2300 meters above sea level with a slope of 0.021 and sinuosity of 1.16 and flows through Paleoproterozoic gneissic rocks. The reach lies on a footwall just upstream of a low angle normal fault and is flanked to the south by a complex of normal and thrust faults. The creek is located in the Idaho Batholith level III ecoregion which is characterized as a western cordillera with conifer forests composed of Douglas-fir, Engelmann spruce, and subalpine fir. Common land uses in this region include logging, grazing, recreation and mining.

### Data:
#### Landcover Classes
###### Vegetation: 
Portions of the valley bottom that are riparian or non-riparian were delineated as a polygon using imagery. The combined extents of active channel, riparian and upland equate to the total extent of the valley bottom. This data collected at the scale of the valley bottom provides critical insight into riverscape health, such as the ratio of riparian area to valley bottom area. 

###### Active Channel: 
The active channel is the area that is currently being reworked by scouring and depositional stream processes. It includes backwaters (e.g. ponds), free-flowing sections, unvegetated bars, and dry channel bed areas that are below the bankfull elevation and was digitized using drone imagery and QGIS spatial software.  

### Analysis:
We used QGIS area calculations to quantify the proportion of valley bottom that is occupied by the active channel at low and higher flows. The difference between the flows was visualized and quantified by a rasterized polygon overlay workflow, highlighting areas of channel expansion and narrowing. This same raster overlay was used to quantify shifts in the vegetation cover classes. 

Although we did not expect significant riparian expansion or upland encroachment within the two-year time frame analyzed here, the proportion of the valley bottom occupied by riparian vegetation offers insight into longer-term riverscape connectivity. We used QGIS area calculations to quantify the proportion of valley bottom that is occupied by riparian and upland vegetation at low and higher flows. The difference between the flows was visualized and quantified by a rasterized polygon overlay workflow, highlighting areas of channel expansion – where riparian areas convert to part of the stream channel, riparian encroachment where stream channel area converts to riparian habitat, riparian expansion – where the riparian forest expands into upland areas, and upland encroachment – where upland vegetation overtakes riparian areas. 

### Results:
![landcover_change](https://github.com/user-attachments/assets/7e018d14-d7cb-4e28-9c6e-5da8174f25ff)
![landcoverchange_table](https://github.com/user-attachments/assets/a4b23e61-fbf3-4273-a5a1-0d325d5fd67b)


