# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from brasil.gov.tiles import _ as _
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from plone.tiles.interfaces import ITileDataManager
from plone.uuid.interfaces import IUUID
from zope import schema
from zope.interface import implements


class IHeaderTile(IPersistentCoverTile):

    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    link_title = schema.TextLine(
        title=_(u'Link title'),
        default=(u''),
        required=False,
    )

    link_text = schema.TextLine(
        title=_(u'Link text'),
        required=False,
    )

    link_url = schema.TextLine(
        title=_(u'Link url'),
        required=False,
    )

    uuid = schema.TextLine(
        title=_(u'UUID'),
        required=False,
        readonly=True,
    )


class HeaderTile(PersistentCoverTile):

    index = ViewPageTemplateFile('templates/header.pt')
    implements(IPersistentCoverTile)
    is_configurable = True
    is_droppable = True
    is_editable = True

    def populate_with_object(self, obj):
        super(HeaderTile, self).populate_with_object(obj)  # check permissions

        title = obj.Title()
        url = obj.absolute_url()
        link_title = url
        link_text = title
        data_mgr = ITileDataManager(self)
        uuid = IUUID(obj)
        data_mgr.set({'title': title,
                      'link_title': link_title,
                      'link_url': url,
                      'link_text': link_text,
                      'uuid': uuid
                      })
