from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting, PersistentStoreConnectionSetting


class GloFmn(TethysAppBase):
    """
    Tethys app class for Flood Mitigation Network.
    """

    name = 'Flood Mitigation Network'
    index = 'glo_fmn:home'
    icon = 'glo_fmn/images/logo.jpg'
    package = 'glo_fmn'
    root_url = 'glo-fmn'
    color = '#16a085'
    description = 'Flood Mitigation Network'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='glo-fmn',
                controller='glo_fmn.controllers.home'
            ),
            UrlMap(
                name='popup-info',
                url='glo-fmn/popup-info',
                controller='glo_fmn.controllers_ajax.get_popup_info'
            ),
            UrlMap(
                name='get-meta-file',
                url='glo-fmn/get-meta-file',
                controller='glo_fmn.controllers_ajax.get_meta_file'
            ),
            UrlMap(
                name='add-point',
                url='glo-fmn/add-point',
                controller='glo_fmn.controllers.add_point'
            ),
            UrlMap(
                name='delete-layer',
                url='glo-fmn/delete-layer',
                controller='glo_fmn.controllers.delete_layer'
            ),
            UrlMap(
                name='submit-delete-layer',
                url='glo-fmn/delete-layer/submit',
                controller='glo_fmn.controllers_ajax.layer_delete'
            ),
            UrlMap(
                name='add-point-ajax',
                url='glo-fmn/add-point/submit',
                controller='glo_fmn.controllers_ajax.point_add'
            ),
            UrlMap(
                name='approve-points',
                url='glo-fmn/approve-points',
                controller='glo_fmn.controllers.approve_points'
            ),
            UrlMap(
                name='approve-points_tabulator',
                url='glo-fmn/approve-points/tabulator',
                controller='glo_fmn.controllers_ajax.points_tabulator'
            ),
            UrlMap(
                name='update-points-ajax',
                url='glo-fmn/approve-points/submit',
                controller='glo_fmn.controllers_ajax.point_update'
            ),
            UrlMap(
                name='delete-points-ajax',
                url='glo-fmn/approve-points/delete',
                controller='glo_fmn.controllers_ajax.point_delete'
            ),
            UrlMap(
                name='add-polygon',
                url='glo-fmn/add-polygon',
                controller='glo_fmn.controllers.add_polygon'
            ),
            UrlMap(
                name='add-polygon-ajax',
                url='glo-fmn/add-polygon/submit',
                controller='glo_fmn.controllers_ajax.polygon_add'
            ),
            UrlMap(
                name='approve-polygons',
                url='glo-fmn/approve-polygons',
                controller='glo_fmn.controllers.approve_polygons'
            ),
            UrlMap(
                name='approve-polygons-tabulator',
                url='glo-fmn/approve-polygons/tabulator',
                controller='glo_fmn.controllers_ajax.polygons_tabulator'
            ),
            UrlMap(
                name='update-polygons-ajax',
                url='glo-fmn/approve-polygons/submit',
                controller='glo_fmn.controllers_ajax.polygon_update'
            ),
            UrlMap(
                name='delete-polygons-ajax',
                url='glo-fmn/approve-polygons/delete',
                controller='glo_fmn.controllers_ajax.polygon_delete'
            ),
            UrlMap(
                name='add-new-layer',
                url='glo-fmn/add-new-layer',
                controller='glo_fmn.controllers.add_new_layer'
            ),
            UrlMap(
                name='get-new-layer-attributes',
                url='glo-fmn/add-new-layer/get-attributes',
                controller='glo_fmn.controllers_ajax.get_shp_attributes'
            ),
            UrlMap(
                name='add-new-layer-ajax',
                url='glo-fmn/add-new-layer/submit',
                controller='glo_fmn.controllers_ajax.new_layer_add'
            ),
            UrlMap(
                name='set-layer-style',
                url='glo-fmn/set-layer-style',
                controller='glo_fmn.controllers.set_layer_style'
            ),
            UrlMap(
                name='set-layer-style-ajax',
                url='glo-fmn/set-layer-style/submit',
                controller='glo_fmn.controllers_ajax.layer_style_set'
            ),
            UrlMap(
                name='add-endpoint',
                url='glo-fmn/add-endpoint',
                controller='glo_fmn.controllers.add_endpoint'
            ),
            UrlMap(
                name='add-endpoint-submit',
                url='glo-fmn/add-endpoint/submit',
                controller='glo_fmn.controllers_ajax.endpoint_add'
            ),
            UrlMap(
                name='delete-endpoint',
                url='glo-fmn/delete-endpoint',
                controller='glo_fmn.controllers.delete_endpoint'
            ),
            UrlMap(
                name='delete-endpoint-submit',
                url='glo-fmn/delete-endpoint/submit',
                controller='glo_fmn.controllers_ajax.endpoint_delete'
            ),
            UrlMap(
                name='get-layers-info',
                url='glo-fmn/api/get-layers-info',
                controller='glo_fmn.api.get_layers_info'
            ),
            UrlMap(
                name='get-layers-by-county',
                url='glo-fmn/api/get-layers-by-county',
                controller='glo_fmn.api.get_layers_by_county'
            ),
            UrlMap(
                name='get-points-by-county',
                url='glo-fmn/api/get-points-by-county',
                controller='glo_fmn.api.get_points_by_county'
            ),
            UrlMap(
                name='get-polygons-by-county',
                url='glo-fmn/api/get-polygons-by-county',
                controller='glo_fmn.api.get_polygons_by_county'
            ),
            UrlMap(
                name='get-points-by-layer',
                url='glo-fmn/api/get-points-by-layer',
                controller='glo_fmn.api.get_points_by_layer'
            ),
            UrlMap(
                name='get-polygons-by-layer',
                url='glo-fmn/api/get-polygons-by-layer',
                controller='glo_fmn.api.get_polygons_by_layer'
            ),
            UrlMap(
                name='get-points-by-geometry',
                url='glo-fmn/api/get-points-by-geometry',
                controller='glo_fmn.api.get_points_by_geom'
            ),
            UrlMap(
                name='get-polygons-by-geometry',
                url='glo-fmn/api/get-polygons-by-geometry',
                controller='glo_fmn.api.get_polygons_by_geom'
            ),
            UrlMap(
                name='dowloand-layers',
                url='glo-fmn/download-layers',
                controller='glo_fmn.controllers_ajax.download_layers'
            ),
            UrlMap(
                name='download-interaction',
                url='glo-fmn/download-interaction',
                controller='glo_fmn.controllers_ajax.download_interaction'
            ),
            UrlMap(
                name='download-points-csv',
                url='glo-fmn/api/download-points-csv',
                controller='glo_fmn.api.download_points_csv'
            ),
            UrlMap(
                name='download-polygons-csv',
                url='glo-fmn/api/download-polygons-csv',
                controller='glo_fmn.api.download_polygons_csv'
            ),
            UrlMap(
                name='download-layer-csv',
                url='glo-fmn/api/download-layer-csv',
                controller='glo_fmn.api.download_layer_csv'
            ),
        )

        return url_maps

    def persistent_store_settings(self):
        """
        Define Persistent Store Settings.
        """
        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='layers',
                description='layers database',
                initializer='glo_fmn.model.init_layer_db',
                required=True,
                spatial=True
            ),
        )

        return ps_settings
