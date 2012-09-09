# -*- coding: UTF-8 -*-
#/*
# *      Copyright (C) 2011 Libor Zoubek
# *
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# */

import re,os,urllib,urllib2
import xbmcaddon,xbmc,xbmcgui,xbmcplugin

__scriptid__   = 'plugin.video.online-files'
__scriptname__ = 'Soubory Online'
__addon__      = xbmcaddon.Addon(id=__scriptid__)
__language__   = __addon__.getLocalizedString
__settings__   = __addon__.getSetting

import util,search

import xbmcutil
import bezvadata,hellspy,ulozto
import xbmcprovider

	

def search_cb(what):
	for key in providers.keys():
		p = providers[key]
		result = p.provider.search(what)
		for item in result:
			item['title'] = '[%s] %s' % (p.provider.name,item['title'])
		p.list(result)
	return xbmcplugin.endOfDirectory(int(sys.argv[1]))

def bezvadata_filter(item):
	ext_filter = __settings__('bezvadata_ext-filter').split(',')
	ext_filter =  ['.'+f.strip() for f in ext_filter]
	extension = os.path.splitext(item['title'])[1]
	if extension in ext_filter:
		return False
	elif '18+' in item.keys() and __settings__('bezvadata_18+content') != 'true':
		return False
	return True


settings = {
	'downloads':__settings__('downloads'),
	'download-notify':__settings__('download-notify'),
	'download-notify-every':__settings__('download-notify-every'),
}

providers = {}

if __settings__('bezvadata_enabled') == 'true':
	p = bezvadata.BezvadataContentProvider(filter=bezvadata_filter)
	extra = {
			'keep-searches':__settings__('bezvadata_keep-searches')
	}
	extra.update(settings)
	providers[p.name] = xbmcprovider.XBMContentProvider(p,extra,__addon__)
if __settings__('ulozto_enabled') == 'true':
	p = ulozto.UloztoContentProvider(__settings__('ulozto_user'),__settings__('ulozto_pass'))
	extra = {
			'vip':__settings__('ulozto_usevip'),
			'keep-searches':__settings__('ulozto_keep-searches')
	}
	extra.update(settings)
	providers[p.name] = xbmcprovider.XBMCLoginOptionalContentProvider(p,extra,__addon__)
if __settings__('hellspy_enabled') == 'true':
	p = hellspy.HellspyContentProvider(__settings__('hellspy_user'),__settings__('hellspy_pass'))
	extra = {
			'keep-searches':__settings__('hellspy_keep-searches')
	}
	extra.update(settings)
	providers[p.name] = xbmcprovider.XBMCLoginRequiredContentProvider(p,extra,__addon__)


def root():
	search.item()
	xbmcutil.add_local_dir(xbmcutil.__lang__(30006),settings['downloads'],xbmcutil.icon('download.png'))
	for provider in providers.keys():
		xbmcutil.add_dir(provider,{'cp':provider})
	return xbmcplugin.endOfDirectory(int(sys.argv[1]))

params = util.params()
if params=={}:
	xbmc.executebuiltin('RunPlugin(plugin://script.usage.tracker/?do=reg&cond=31000&id=%s)' % __scriptid__)
	root()
elif 'cp' in params.keys():
	cp = params['cp']
	if cp in providers.keys():
		providers[cp].run(params)
else:
	search.main(__addon__,'search_history',params,search_cb)
