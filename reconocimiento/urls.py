from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('procesar_imagen/', views.procesar_imagen, name='procesar_imagen'),
    path('contratista/', views.contratista, name='contratista'),
    path('entrevista/', views.entrevista, name='entrevista'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('apoderado/', views.apoderado, name='apoderado'),
    path('agregar_empresa/', views.agregar_empresa, name='agregar_empresa'),
    path('guardar/', views.guardar, name='guardar'),
    path('datos/', views.datos, name='datos'),
    path('procesar_post_contratista/', views.procesar_post_contratista, name='procesar_post_contratista'),
    path('procesar_post_colaborador/', views.procesar_post_colaborador, name='procesar_post_colaborador'),
    path('procesar_post_ubicacion/', views.procesar_post_ubicacion, name='procesar_post_ubicacion'),
    path('guardar_visita/', views.guardar_visita, name='guardar_visita'),
    path('registro_salida/', views.registro_salida, name='registro_salida'),
    path('reporte_personalizado/', views.reporte_personalizado, name='reporte_personalizado'),
    path('filtrar_informe/', views.formulario_filtros, name='formulario_filtros'),
    path('reporte_filtrado/', views.reporte, name='reporte'),
    path('reporte/', views.reporte_total, name='reporte_total'),
    path('reporte_visitas_activas/', views.reporte_visitas_activas, name='reporte_visitas_activas'),
    path('exportar_a_excel/', views.exportar_a_excel, name='exportar_a_excel'),
    path('finalizar_visita_manual/', views.finalizar_visita_manual, name='finalizar_visita_manual'),
    path('otras_visitas/', views.otras_visitas, name='otras_visitas'),
    

]

urlpatterns += staticfiles_urlpatterns()


