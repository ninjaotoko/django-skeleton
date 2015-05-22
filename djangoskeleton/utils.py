# -*- coding:utf-8 -*-

from django.template import Context, Template


class Skeleton:
    """
    {% load skeleton %}
    <!doctype html>
    <html class="no-js" {% skeleton_get_html_attributes %}>
        <head>
            <title>{% block title %}Título de la página{% endblock %}</title>

            <!-- meta -->
            {% skeleton_get_meta %}

            <!-- stylesheet, javascript y otros -->
            {% skeleton_get_style %}
            {% skeleton_get_head_scripts %}
        </head>

        <body {% skeleton_get_body_attributes %}>
            <!-- header -->
            {% skeleton_get_header %}

            <!-- main content -->
            {% block main %}
            <main>    
                ...
            </main>
            {% endblock %}

            <!-- footer -->
            {% skeleton_get_footer %}

            <!-- scripts -->
            {% skeleton_get_scripts %}
        </body>
    </html>
    """

    html_attributes = {}
    head = {
        'meta': [],
        'style': [],
        'head_scripts': []
    }
    body_attributes = {}
    body = {
        'header': [],
        'footer': []
    }

    def __init__(self, *args, **kwargs):
        pass

    def add_to(self, part, tag, *args, **kwargs):
        pass

    def remove_from(self, part, tag, *args, **kwargs):
        pass
    
    def prepend_to(self, part, tag, *args, **kwargs):
        pass

    def add_to_header(self, name, object, *args, **kwargs):
        pass

    def remove_from_header(self, name, *args, **kwargs):
        pass

    def prepend_to_header(self, name, object, *args, **kwargs):
        pass

    def add_to_footer(self, name, object, *args, **kwargs):
        pass

    def remove_from_footer(self, name, *args, **kwargs):
        pass

    def prepend_to_footer(self, name, object, *args, **kwargs):
        pass

    def add_to_main(self, name, object, *args, **kwargs):
        pass

    def remove_from_main(self, name, *args, **kwargs):
        pass

    def prepend_to_main(self, name, object, *args, **kwargs):
        pass

    def set_html_attributes(self, attribs, *args, **kwargs):
        self.html_attributes.update(attribs)

    def get_html_attributes(self, *args, **kwargs):
        """
        Configura los atributos para el tag `<html>`
        """
        return self.dict_to_attribs(self.html_attributes)

    def get_meta(self, *args, **kwargs):
        """
        Crea los tags `<meta>`
        """
        return self.head.get('meta')

    def get_style(self, *args, **kwargs):
        """
        Crea los tags `<style>`
        """

        pass

    def get_head_script(self, *args, **kwargs):
        """
        Crea los `<scripts>` asociados del head
        """

        pass

    def set_body_attributes(self, attribs, *args, **kwargs):
        self.body_attributes.update(attribs)

    def get_body_attributes(self, *args, **kwargs):
        """
        Configura los atributos para el tag `<body>`
        """
        return self.dict_to_attribs(self.body_attributes)

    def get_header(self, *args, **kwargs):
        """
        Incluye todo el bloque del tag `<header>`
        """

        pass

    def get_footer(self, *args, **kwargs):
        """
        Incluye todo el bloque del tag `<footer>`
        """

        pass

    def get_scripts(self, *args, **kwargs):
        """
        Incluye los `<scripts>` asociados
        """

        pass


    def dict_to_attribs(self, options):
        """
        Transforma un `dict` en atributos del estilo key="val" y devuelve un string
        """

        return " ".join([
            "%s=\"%s\"" % (key, val) 
            for key, val in options.iteritems()
            ])



class RendereableObjectList:
    """
    Acepta una lista de objetos o QuerySet y devuelve una lista de objetos en HTML

    Toma como Template el campo `template` o si no existe busca el template por 
    nombre y por defecto usa `templates/default_rendereable_object_list.html`

    """

    def get_object_list(self, *args, **kwargs):
        """
        Devuelve un lista de objetos para construir un contexto

        """

        raise Exception("%s.get_object_list Not implemented" % self.__class__.__name__)


    def get_queryset(self, *args, **kwargs):
        """
        Devuelve un QuerySet para construir un contexto
        
        """
        
        raise Exception("%s.get_queryset Not implemented" % self.__class__.__name__)

    
    def get_template(self, *args, **kwargs):
        """
        Devuelve una instancia de Template

        """
        
        raise Exception("%s.get_template Not implemented" % self.__class__.__name__)

    
    def get_context(self, *args, **kwargs):
        """
        Deveulve una contexto para ser utilizado en el render

        """

        object_list = self.get_object_list(*args, **kwargs) or \
                self.get_queryset(*args, **kwargs)

        return Context({'object_list': object_list})


    def render(self, *args, **kwargs):
        """
        Render

        """

        context = self.get_context(*args, **kwargs)
        template = self.get_template(*args, **kwargs)

        return template.render(context)
