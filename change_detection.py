from osgeo import gdal, osr
# VEGETATION CHANGE DETECTION

file = 'C:/Users/Paige/Box/0_RAM/Projects/USA/USFS_PIBO_Collaborations/Riverscapes_Network_Reach_Scale_Comparison/PIBO/wrk_Data/Drone_Imagery_Sites/GIS/'
inter_file = 'C:/Users/Paige/Desktop/ET-AL/PIBO/Wildhorse_raster_intermediates/'
vb = file + 'valley_bottoms/Wildhorse/valley_bottom.shp'
veg1 = file + 'Sept_2021_Drone/Wildhorse/Geomorphic_Mapping/Wildhorse_GIS/SHP/riparian_21.shp'
veg2 = file + 'June_2023_Drone/Wildhorse/Geomorphic_Mapping/SHP/riparian.shp'
veg3 = 'address'
all_clips = ['Wildhorse_rip21_clip','Wildhorse_up21_clip','Wildhorse_rip23_clip','Wildhorse_up23_clip']
# modify lines 2-9 as needed
## separate veg files into 'riparian' and 'upland' components
veg21 = iface.addVectorLayer(veg1,'veg21','ogr')
layer = iface.activeLayer()
layer.selectByExpression('"type"=\'riparian\'', QgsVectorLayer.SetSelection)
rip = layer.selectedFeatures()
rip_21 = processing.run("native:savefeatures", 
                        {'INPUT':QgsProcessingFeatureSourceDefinition(veg1, 
                          selectedFeaturesOnly=True, 
                          featureLimit=-1, 
                          geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),
                         'OUTPUT':'TEMPORARY_OUTPUT'})
layer.selectByExpression('"type"=\'non\'', QgsVectorLayer.SetSelection)
up = layer.selectedFeatures()
up_21 = processing.run("native:savefeatures", 
                        {'INPUT':QgsProcessingFeatureSourceDefinition(veg1, 
                          selectedFeaturesOnly=True, 
                          featureLimit=-1, 
                          geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),
                         'OUTPUT':'TEMPORARY_OUTPUT'})
QgsProject.instance().removeMapLayers( [veg21.id()] )

veg23 = iface.addVectorLayer(veg2,'veg23','ogr')
layer = iface.activeLayer()
layer.selectByExpression('"type"=\'riparian\'', QgsVectorLayer.SetSelection)
rip = layer.selectedFeatures()
rip_23 = processing.run("native:savefeatures", 
                        {'INPUT':QgsProcessingFeatureSourceDefinition(veg2, 
                          selectedFeaturesOnly=True, 
                          featureLimit=-1, 
                          geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),
                         'OUTPUT':'TEMPORARY_OUTPUT'})
layer.selectByExpression('"type"=\'non\'', QgsVectorLayer.SetSelection)
up = layer.selectedFeatures()
up_23 = processing.run("native:savefeatures", 
                        {'INPUT':QgsProcessingFeatureSourceDefinition(veg2, 
                          selectedFeaturesOnly=True, 
                          featureLimit=-1, 
                          geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),
                         'OUTPUT':'TEMPORARY_OUTPUT'})
QgsProject.instance().removeMapLayers( [veg23.id()] )

all_veg = [rip_21['OUTPUT'], up_21['OUTPUT'],rip_23['OUTPUT'], up_23['OUTPUT']]

# use 'create constant raster tool' with extent calculated by the vb layer
buffer = processing.run("native:buffer", {'INPUT': vb,
                                          'DISTANCE':70,
                                          'SEGMENTS':5,
                                          'END_CAP_STYLE':0,
                                          'JOIN_STYLE':0,
                                          'MITER_LIMIT':2,
                                          'DISSOLVE':False,
                                          'SEPARATE_DISJOINT':False,
                                          'OUTPUT':'TEMPORARY_OUTPUT'})
vb_extent = processing.run("native:polygonfromlayerextent", 
                          {'INPUT': buffer['OUTPUT'],
                           'ROUND_TO':0,
                           'OUTPUT':'TEMPORARY_OUTPUT'})
base = processing.run("native:createconstantrasterlayer", 
                     {'EXTENT':vb_extent['OUTPUT'],
                      'TARGET_CRS':QgsCoordinateReferenceSystem('EPSG:26911'),
                      'PIXEL_SIZE':.05,
                      'NUMBER':1,
                      'OUTPUT_TYPE':5,
                      'OUTPUT': inter_file + 'base.tif'})
# clip raster by mask layer for each polygon
parameters_list = []
for i in range(len(all_clips)):
    x = {'INPUT': base['OUTPUT'],
            'MASK': all_veg[i],
            'ALPHA_BAND': True,
            'CROP_TO_CUTLINE': False,
            'KEEP_RESOLUTION': True,
            'OPTIONS': None,
            'DATA_TYPE': 1,
            'OUTPUT': inter_file+all_clips[i]+'.tif'}
    parameters_list.append(x)
for i in range(len(parameters_list)):
    all_clips2 = processing.run('gdal:cliprasterbymasklayer', parameters_list[i])
# # raster calculations
final = processing.run("native:rastercalc", 
               {'LAYERS':[inter_file + 'base.tif',
                          inter_file + all_clips[0] + '.tif',
                          inter_file + all_clips[1] + '.tif',
                           inter_file + all_clips[2] + '.tif',
                           inter_file + all_clips[3] + '.tif'],
                          'EXPRESSION':'"base@1" + ("Wildhorse_rip21_clip@1"*2) + ("Wildhorse_rip23_clip@1"*6) + ("Wildhorse_up21_clip@1"*-2) + ("Wildhorse_up23_clip@1"*-6)',
                          'EXTENT':None,
                          'CELL_SIZE':None,
                          'CRS':None,
                          'OUTPUT':inter_file + 'veg_final.tif'})
processing.run("native:rasterlayeruniquevaluesreport", 
                            {'INPUT':final['OUTPUT'],'BAND':1,
                             'OUTPUT_HTML_FILE':inter_file + 'final.html'})