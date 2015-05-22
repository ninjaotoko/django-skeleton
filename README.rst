Django Skeleton
===============

App para crea la estructura de los templates de django y otros objetos


1) en tu proyecto instala con pip https://github.com/ninjaotoko/django-skeleton

2) en INSTALLED_APPS agrega 'djangoskeleton'

3) en tu template agregá  {% load skeleton_tags %}

4) Ejemplo de un `category_list` que tiene la lista de categorías, lo rendiremos así:

            <h3>Ejemplo generic_object_list</h3>
            {% comment %}
            Así se completa el templatatag, notar que 
            object_list, tag_wrapper='ul', tag_wrapper_attribs='class="no-bullet"', tag_wrapper_element='li', tag_wrapper_element_attribs='', tag_element='', tag_element_attribs=''
            {% endcomment %}

            {% generic_object_list category_list 'div' 'class="row"' 'div' 'class="small-6 columns"' 'h3' as object_list %}
            {{ object_list }}


