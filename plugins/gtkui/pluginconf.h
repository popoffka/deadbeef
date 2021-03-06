/*
    DeaDBeeF - ultimate music player for GNU/Linux systems with X11
    Copyright (C) 2009-2013 Alexey Yakovenko <waker@users.sourceforge.net>

    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
*/
#ifndef __PLUGINCONF_H
#define __PLUGINCONF_H

int
gtkui_run_dialog (GtkWidget *parentwin, ddb_dialog_t *conf, uint32_t buttons, int (*callback)(int button, void *ctx), void *ctx);

int
gtkui_run_dialog_root (ddb_dialog_t *conf, uint32_t buttons, int (*callback)(int button, void *ctx), void *ctx);

#endif
